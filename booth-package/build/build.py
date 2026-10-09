#!/usr/bin/env python3
"""Render the booth art, the strategy packet and the order guide to PDF (and PNG previews).

Usage (from booth-package/):   python3 build/build.py [piece ...]
Needs: pip install segno ; Chromium (Playwright's copy is auto-detected) ; poppler-utils for previews.
"""
import base64, glob, math, os, pathlib, re, shutil, subprocess, sys
import segno
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import art

ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "build"))
import config as C

SRC, OUT = ROOT / "src", ROOT / "output"
OUT.mkdir(exist_ok=True)

PIECE_TAG = {"banner_men_story": "men-banner-story", "banner_men_proof": "men-banner-proof", "backdrop_men": "men-backdrop", "banner_story": "banner-story", "banner_proof": "banner-proof", "leavebehind": "leavebehind",
             "poster_progress": "poster-progress", "poster_capacity": "poster-capacity", "handout_measurement": "handout-measure",
             "poster_loop": "poster-loop", "poster_shift": "poster-shift", "poster_outcomes": "poster-outcomes", "poster_where": "poster-where",
             "banner_retractable": "banner", "backdrop": "backdrop", "counter_sign": "sign", "card_individual": "card",
             "sheet_organizations": "orgsheet", "business_card": "bizcard", "strategy_packet": "packet",
             "order_guide": "guide", "table_front": "table"}
URL_LOG = []
RENDERED = []


# ---------- shared SVG pieces for the explainer posters and cards ----------
DEEP, LIGHT, PALE, LINEN, WHITE, INK = "#103C41", "#9BC4BD", "#E4F2F2", "#EEEADD", "#FEFCF8", "#24211D"

def arrow(x1, y1, x2, y2, color, width=14, head=62):
    ang = math.atan2(y2 - y1, x2 - x1)
    bx, by = x2 - head * math.cos(ang), y2 - head * math.sin(ang)
    lx, ly = bx + head * 0.55 * math.sin(ang), by - head * 0.55 * math.cos(ang)
    rx, ry = bx - head * 0.55 * math.sin(ang), by + head * 0.55 * math.cos(ang)
    return (f'<line x1="{x1}" y1="{y1}" x2="{bx:.0f}" y2="{by:.0f}" stroke="{color}" stroke-width="{width}" stroke-linecap="round"/>'
            f'<polygon points="{x2},{y2} {lx:.0f},{ly:.0f} {rx:.0f},{ry:.0f}" fill="{color}"/>')

def footer(scheme, qr_svg, caption="Scan for the free|Burnout Signal Check"):
    dark = scheme == "dark"
    logo = b64img(C.LOGO_ON_DARK if dark else C.LOGO_ON_LIGHT) or ""
    txt, sub = (WHITE, PALE) if dark else (DEEP, INK)
    c1, c2 = caption.split("|")
    o = f'<image href="{logo}" x="175" y="3200" width="560" height="208" preserveAspectRatio="xMinYMid meet"/>'
    o += f'<text x="190" y="3466" font-family="DM Sans" font-weight="500" font-size="48" letter-spacing="7" fill="{sub}">SOMA-Q.COM</text>'
    o += f'<text x="1700" y="3300" text-anchor="end" font-family="DM Sans" font-weight="700" font-size="48" fill="{txt}">{c1}</text>'
    o += f'<text x="1700" y="3362" text-anchor="end" font-family="DM Sans" font-weight="700" font-size="48" fill="{txt}">{c2}</text>'
    o += f'<rect x="1770" y="3110" width="380" height="380" rx="26" fill="#FFFFFF"/>'
    o += f'<svg x="1795" y="3135" width="330" height="330">{qr_svg}</svg>'
    return o

def chrome():
    for p in [shutil.which("chromium"), shutil.which("google-chrome"), *glob.glob("/opt/pw-browsers/chromium-*/chrome-linux/chrome")]:
        if p and os.path.exists(p):
            return p
    sys.exit("No Chromium found.")

def target(kind, tag):
    if C.QR_MODE == "go":
        return f"{C.SITE}/go/{kind}?c={C.CAMPAIGN}&p={tag}"
    base = C.DIRECT[kind]
    if base.startswith("[") or "as.me" in base or "zoom.us" in base:
        return base                       # external or unset links take no tracking parameters
    sep = "&" if "?" in base else "?"
    return f"{base}{sep}utm_source=event&utm_medium=print&utm_campaign={C.CAMPAIGN}&utm_content={tag}"

def qr_svg(url):
    if url.startswith("["):
        return '<div style="line-height:1.2;font-size:8pt;text-align:center;padding:.5em">[QR: set URL in config.py]</div>'
    return segno.make(url, error="m").svg_inline(dark="#103C41", light="#FFFFFF", border=1, scale=10, omitsize=True)

def b64img(path):
    p = ROOT / path
    if not p.exists():
        return None
    mime = "image/jpeg" if p.suffix.lower() in (".jpg", ".jpeg") else "image/png"
    return f"data:{mime};base64," + base64.b64encode(p.read_bytes()).decode()

def logo(path, fallback):
    d = b64img(path)
    return f'<img class="logo" alt="Soma-Q" src="{d}">' if d else f'<div class="logo logo-missing">[LOGO: place {fallback} in assets/]</div>'

def photo_block(show):
    if not show:
        return ""
    d = b64img(C.PHOTO_PATH)
    inner = f'<img alt="Megan McDonald" src="{d}">' if d else '<div class="photo-missing">[PHOTO: place assets/megan-headshot.jpg]</div>'
    return f'<div class="photo">{inner}</div>'

def render(name, variant=None):
    src = (SRC / f"{name}.html").read_text()
    tag = PIECE_TAG.get(name, name)
    subs = {
        "{{LOGO_DARK}}": logo(C.LOGO_ON_DARK, "soma-q-logo-teal-reversed.png"),
        "{{LOGO_LIGHT}}": logo(C.LOGO_ON_LIGHT, "soma-q-logo-teal.png"),
        "{{POPL_QR}}": (f'<img alt="POPL QR" src="{b64img(C.POPL_QR_IMAGE)}">' if b64img(C.POPL_QR_IMAGE) else "[POPL QR: add assets/popl-qr.png]"),
        "{{PHOTO}}": photo_block(variant == "photo"),
        "{{VARIANT_CLASS}}": f"v-{variant or 'plain'}",
        "{{EVENT_NAME}}": C.EVENT_NAME, "{{EVENT_DATES}}": C.EVENT_DATES, "{{EVENT_VENUE}}": C.EVENT_VENUE,
        "{{BOOTH_NUMBER}}": C.BOOTH_NUMBER, "{{BOOTH_SIZE}}": C.BOOTH_SIZE, "{{CAMPAIGN}}": C.CAMPAIGN,
        "{{CARD_NAME}}": C.CARD_NAME, "{{CARD_TITLE}}": C.CARD_TITLE, "{{CARD_EMAIL}}": C.CARD_EMAIL,
        "{{CARD_WEB}}": C.CARD_WEB, "{{CARD_PHONE}}": C.CARD_PHONE,
    }
    for kind in ("quiz", "ebook", "reset", "call", "org", "overview"):
        key = "{{QR_%s}}" % kind.upper()
        if key in src:
            u = target(kind, tag)
            subs[key] = qr_svg(u)
            URL_LOG.append(f"{name}{'/' + variant if variant else ''} [{kind}]: {u}")
    subs["{{LOGO_DARK_URI}}"] = b64img(C.LOGO_ON_DARK) or ""
    subs["{{LOGO_LIGHT_URI}}"] = b64img(C.LOGO_ON_LIGHT) or ""
    html = src
    keep_photo = variant == "photo"
    html = re.sub(r"<!--PHOTO-->(.*?)<!--/PHOTO-->", (lambda m: m.group(1)) if keep_photo else "", html, flags=re.S)
    html = re.sub(r"<!--NOPHOTO-->(.*?)<!--/NOPHOTO-->", "" if keep_photo else (lambda m: m.group(1)), html, flags=re.S)
    subs["{{PHOTO_URI}}"] = b64img(C.PHOTO_PATH) or ""
    def _sub_art(m):
        kind, scheme, opt, var = m.group(1), m.group(2), m.group(3) or "", m.group(4) or ""
        if kind == "LOOP":
            return art.loop(scheme, opt != "nogloss", art.MEN_LOOP if var == "men" else None)[0]
        if kind == "OUTCOMES":
            return art.outcomes(scheme, art.MEN_OUTCOMES if opt == "men" else None)[0]
        return art.bodymap(scheme)[0]
    html = re.sub(r"\{\{(LOOP|OUTCOMES|BODYMAP):(light|dark)(?::(\w+))?(?::(\w+))?\}\}", _sub_art, html)
    CAPS = {"quiz": "Scan for the free|Burnout Signal Check", "call": "Scan to book a|free discovery call",
            "overview": "Scan to request the|full Measurement Overview"}
    for m in re.finditer(r"\{\{FOOTER:(light|dark)(?::(\w+))?\}\}", src):
        kind = m.group(2) or "quiz"
        qr_u = target(kind, tag)
        URL_LOG.append(f"{name} [{kind}]: {qr_u}")
        html = html.replace(m.group(0), footer(m.group(1), qr_svg(qr_u), CAPS[kind]))
    for k, v in subs.items():
        html = html.replace(k, v)
    out_name = f"{name}_{variant}" if variant else name
    tmp = SRC / f"_{out_name}.rendered.html"
    tmp.write_text(html)
    pdf = OUT / f"{out_name}.pdf"
    subprocess.run([chrome(), "--headless=new", "--no-sandbox", "--disable-gpu", "--allow-file-access-from-files",
                    "--virtual-time-budget=15000", "--no-pdf-header-footer", f"--print-to-pdf={pdf}", tmp.as_uri()],
                   check=True, capture_output=True)
    if os.environ.get('QA'):
        RENDERED.append((out_name, tmp))
    else:
        tmp.unlink()
    make_previews(pdf, out_name)
    print("built", pdf.name)

def make_previews(pdf, out_name):
    """One PNG per page in output/preview/, long side about 3000 px, so every piece can be viewed inline."""
    PREV = OUT / "preview"
    PREV.mkdir(exist_ok=True)
    for old in PREV.glob(f"{out_name}-*.png"):
        old.unlink()
    info = subprocess.run(["pdfinfo", str(pdf)], capture_output=True, text=True).stdout
    m = re.search(r"Page size:\s+([\d.]+) x ([\d.]+) pts", info)
    long_pts = max(float(m.group(1)), float(m.group(2))) if m else 792
    dpi = max(20, min(300, round(3000 / (long_pts / 72))))
    subprocess.run(["pdftoppm", "-png", "-r", str(dpi), str(pdf), str(PREV / out_name)], check=False)

def write_gallery():
    PREV = OUT / "preview"
    items = sorted(PREV.glob("*.png"))
    md = ["# Preview gallery", "", "Every page of every piece as an image. Rebuild with `python3 build/build.py`.", ""]
    html = ["<!doctype html><meta charset=utf-8><title>Soma-Q booth package: preview</title><style>body{font-family:sans-serif;margin:24px;background:#EEEADD;color:#24211D}h1{color:#103C41}figure{margin:0 0 32px}img{max-width:100%;height:auto;border:1px solid #9BC4BD;background:#fff}figcaption{font-weight:700;margin:6px 0}</style><h1>Soma-Q booth package: preview</h1>"]
    for f in items:
        md += [f"## {f.stem}", f"![{f.stem}](preview/{f.name})", ""]
        html.append(f'<figure><figcaption>{f.stem}</figcaption><img src="preview/{f.name}" loading="lazy"></figure>')
    (OUT / "PREVIEW.md").write_text("\n".join(md))
    (OUT / "preview.html").write_text("\n".join(html))

def write_redirects():
    rows = "\n".join(f"| /go/{k} | {v} |" for k, v in C.GO_TARGETS.items())
    (OUT / "redirects_for_designer.md").write_text(f"""# Redirects needed on soma-q.com before the print files go out

Printed QR codes point to /go/ addresses so the destination can be changed after printing.
Each request arrives as /go/<name>?c=<campaign>&p=<piece>. Please:

1. Redirect (HTTP 302) each address below to its destination.
2. Keep the c and p parameters when passing through, and append them as utm_campaign and utm_content on the
   destination if it is a soma-q.com page, so the scans can be told apart.
3. Log each hit (date, name, c, p) so scans per printed piece can be counted even when the destination is external.
4. Test every address on a phone on cell data.

| Address | Destination |
| --- | --- |
{rows}

Current campaign: {C.CAMPAIGN}. Destinations in [BRACKETS] still need to be supplied by Megan.
""")

if __name__ == "__main__":
    plan = [("banner_story", None), ("banner_proof", None), ("banner_proof", "photo"), ("backdrop", None), ("backdrop", "photo"),
            ("banner_men_story", None), ("banner_men_proof", None), ("banner_men_proof", "photo"), ("backdrop_men", None), ("backdrop_men", "photo"),
            ("table_front", None), ("counter_sign", None), ("card_individual", None), ("business_card", None),
            ("leavebehind", None), ("poster_loop", None), ("poster_shift", None), ("poster_outcomes", None),
            ("poster_where", None), ("poster_progress", None), ("poster_capacity", None), ("handout_measurement", None), ("strategy_packet", None), ("order_guide", None)]
    wanted = sys.argv[1:]
    for name, variant in plan:
        if wanted and name not in wanted:
            continue
        if (SRC / f"{name}.html").exists():
            render(name, variant)
        else:
            print("skip (no source yet):", name)
    (OUT / "qr_urls.txt").write_text("Scan-test every URL on a phone, on cell data, from the printed proof.\n\n" + "\n".join(URL_LOG) + "\n")
    write_redirects()
    write_gallery()
    if os.environ.get('QA'):
        import qa
        qa.run(RENDERED)
        for _, p in RENDERED:
            p.unlink()
