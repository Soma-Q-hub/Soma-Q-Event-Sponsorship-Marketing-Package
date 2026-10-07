#!/usr/bin/env python3
"""Render the booth art, the strategy packet and the order guide to PDF (and PNG previews).

Usage (from booth-package/):   python3 build/build.py [piece ...]
Needs: pip install segno ; Chromium (Playwright's copy is auto-detected) ; poppler-utils for previews.
"""
import base64, glob, os, pathlib, shutil, subprocess, sys
import segno

ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "build"))
import config as C

SRC, OUT = ROOT / "src", ROOT / "output"
OUT.mkdir(exist_ok=True)

PIECE_TAG = {"banner_retractable": "banner", "backdrop": "backdrop", "counter_sign": "sign", "card_individual": "card",
             "sheet_organizations": "orgsheet", "business_card": "bizcard", "strategy_packet": "packet",
             "order_guide": "guide", "table_front": "table"}
URL_LOG = []

def chrome():
    for p in [shutil.which("chromium"), shutil.which("google-chrome"), *glob.glob("/opt/pw-browsers/chromium-*/chrome-linux/chrome")]:
        if p and os.path.exists(p):
            return p
    sys.exit("No Chromium found.")

def target(kind, tag):
    if C.QR_MODE == "go":
        return f"{C.SITE}/go/{kind}?c={C.CAMPAIGN}&p={tag}"
    base = C.DIRECT[kind]
    if base.startswith("[") or "as.me" in base:
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
    for kind in ("quiz", "ebook", "reset", "call", "org"):
        key = "{{QR_%s}}" % kind.upper()
        if key in src:
            u = target(kind, tag)
            subs[key] = qr_svg(u)
            URL_LOG.append(f"{name}{'/' + variant if variant else ''} [{kind}]: {u}")
    html = src
    for k, v in subs.items():
        html = html.replace(k, v)
    out_name = f"{name}_{variant}" if variant else name
    tmp = SRC / f"_{out_name}.rendered.html"
    tmp.write_text(html)
    pdf = OUT / f"{out_name}.pdf"
    subprocess.run([chrome(), "--headless=new", "--no-sandbox", "--disable-gpu", "--allow-file-access-from-files",
                    "--virtual-time-budget=15000", "--no-pdf-header-footer", f"--print-to-pdf={pdf}", tmp.as_uri()],
                   check=True, capture_output=True)
    tmp.unlink()
    big = name in ("banner_retractable", "table_front", "backdrop")
    subprocess.run(["pdftoppm", "-png", "-r", "30" if name == "backdrop" else ("50" if big else "80"), "-f", "1", "-l", "3",
                    str(pdf), str(OUT / f"preview_{out_name}")], check=False)
    print("built", pdf.name)

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
    plan = [("banner_retractable", None), ("banner_retractable", "photo"), ("backdrop", None), ("backdrop", "photo"),
            ("table_front", None), ("counter_sign", None), ("card_individual", None), ("business_card", None),
            ("sheet_organizations", None), ("strategy_packet", None), ("order_guide", None)]
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
