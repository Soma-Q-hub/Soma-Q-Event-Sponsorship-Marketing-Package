#!/usr/bin/env python3
"""Hat artwork: Soma-Q logo + SHIFT HAPPENS, flat and outlined (no gradients, no live fonts) so it can be embroidered,
screen printed or heat transferred. The logo is traced from the flat reversed logo in assets/ (alpha mask), the lettering is
DM Sans Bold converted to outlines. Outputs go to booth-package/hat/.
Needs: pip install potracer fonttools brotli pillow numpy ; Chromium for the PNG exports.
Run: python3 build/make_hat.py"""
import pathlib, subprocess, sys, urllib.request, re, tempfile
import numpy as np
from PIL import Image
import potrace
from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen

ROOT = pathlib.Path(__file__).resolve().parent.parent
OUT = ROOT / "hat"
OUT.mkdir(exist_ok=True)
DEEP, LIGHT, WHITE, LINEN = "#103C41", "#9BC4BD", "#FEFCF8", "#EEEADD"
FONT_URL = "https://fonts.gstatic.com/s/dmsans/v17/rP2tp2ywxg089UriI5-g4vlH9VoD8CmcqZG40F9JadbnoEwARZtRSW32.woff2"   # DM Sans 700, latin
FONT = pathlib.Path(tempfile.gettempdir()) / "dmsans700.woff2"


def trace_logo():
    """Alpha mask of the flat reversed logo -> one compound SVG path. Returns (d, width, height) in logo pixels."""
    im = Image.open(ROOT / "assets" / "soma-q-logo-teal-reversed.png").convert("RGBA")
    a = im.getchannel("A")
    bbox = a.getbbox()
    a = a.crop(bbox)
    S = 3
    a = a.resize((a.width * S, a.height * S), Image.LANCZOS)
    bm = potrace.Bitmap(np.array(a) <= 127)
    plist = bm.trace(turdsize=30, alphamax=1.0, opttolerance=0.4)
    d = []
    for c in plist:
        sp = c.start_point
        d.append(f"M{sp.x/S:.2f},{sp.y/S:.2f}")
        for seg in c.segments:
            if seg.is_corner:
                d.append(f"L{seg.c.x/S:.2f},{seg.c.y/S:.2f}L{seg.end_point.x/S:.2f},{seg.end_point.y/S:.2f}")
            else:
                d.append(f"C{seg.c1.x/S:.2f},{seg.c1.y/S:.2f} {seg.c2.x/S:.2f},{seg.c2.y/S:.2f} {seg.end_point.x/S:.2f},{seg.end_point.y/S:.2f}")
        d.append("Z")
    return "".join(d), a.width / S, a.height / S


def text_outline(txt, size, tracking=0.14):
    """Lettering as an SVG path (outlined). Origin at left baseline, y down. Returns (d, advance_width, cap_height)."""
    if not FONT.exists():
        urllib.request.urlretrieve(FONT_URL, FONT)
    f = TTFont(str(FONT))
    gs, cmap, hmtx = f.getGlyphSet(), f.getBestCmap(), f["hmtx"]
    upm = f["head"].unitsPerEm
    k = size / upm
    x = 0.0
    parts = []
    for ch in txt:
        g = cmap[ord(ch)]
        pen = SVGPathPen(gs)
        gs[g].draw(TransformPen(pen, (k, 0, 0, -k, x, 0)))
        parts.append(pen.getCommands())
        x += hmtx[g][0] * k + tracking * size
    cap = f["OS/2"].sCapHeight * k
    return " ".join(parts), x - tracking * size, cap


def art(logo_fill, word_fill, word_w=400.0, logo_w=400.0, with_logo=True):
    """Stacked art, units = 0.01 in. Returns (svg_inner, width, height)."""
    ld, lw, lh = trace_logo()
    sc = logo_w / lw
    # size the lettering so its width equals word_w
    d0, w0, cap0 = text_outline("SHIFT HAPPENS", 100)
    size = 100 * word_w / w0
    d, w, cap = text_outline("SHIFT HAPPENS", size)
    gap = 34
    inner, y = "", 0
    if with_logo:
        inner += f'<path transform="scale({sc:.5f})" d="{ld}" fill="{logo_fill}" fill-rule="evenodd"/>'
        y = lh * sc + gap
    inner += f'<g transform="translate({(logo_w - w)/2:.2f},{y + cap:.2f})"><path d="{d}" fill="{word_fill}"/></g>'
    return inner, max(logo_w, w), y + cap


def svg_doc(inner, w, h, bg=None, pad=0):
    r = f'<rect x="{-pad}" y="{-pad}" width="{w+2*pad}" height="{h+2*pad}" fill="{bg}"/>' if bg else ""
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{(w+2*pad)/100:.3f}in" height="{(h+2*pad)/100:.3f}in" '
            f'viewBox="{-pad} {-pad} {w+2*pad} {h+2*pad}">{r}{inner}</svg>\n')


def chrome():
    sys.path.insert(0, str(ROOT / "build"))
    import build
    return build.chrome()


def png(svg_path, png_path, w_in, h_in, dpi=300, transparent=True):
    W, H = int(w_in * dpi), int(h_in * dpi)
    html = svg_path.with_suffix(".tmp.html")
    html.write_text(f'<!doctype html><meta charset="utf-8"><style>html,body{{margin:0;background:transparent}}img{{display:block;width:{W}px;height:{H}px}}</style><img src="{svg_path.name}">')
    cmd = [chrome(), "--headless=new", "--no-sandbox", "--disable-gpu", "--allow-file-access-from-files", "--hide-scrollbars",
           f"--window-size={W},{H}", f"--screenshot={png_path}"]
    if transparent:
        cmd.append("--default-background-color=00000000")
    subprocess.run(cmd + [html.as_uri()], check=True, capture_output=True)
    html.unlink()


def hat_mock(inner, w, h, hat, name):
    """Plain front-view cap illustration with the art placed on the crown. Not to scale, only for judging contrast."""
    s = 3.0 / w * 100 / 100        # art width ~ 3 in on a 6.4 in wide cap
    body = (f'<svg xmlns="http://www.w3.org/2000/svg" width="1000" height="760" viewBox="0 0 1000 760"><rect width="1000" height="760" fill="#F3F1EA"/>'
            f'<ellipse cx="500" cy="660" rx="330" ry="36" fill="#000" fill-opacity=".10"/>'
            f'<path d="M150,470 C150,170 330,70 500,70 C670,70 850,170 850,470 C700,500 300,500 150,470 Z" fill="{hat}"/>'
            f'<path d="M110,520 C250,600 750,600 890,520 C860,440 690,470 500,470 C310,470 140,440 110,520 Z" fill="{hat}" stroke="#000" stroke-opacity=".18" stroke-width="3"/>'
            f'<circle cx="500" cy="84" r="16" fill="{hat}" stroke="#000" stroke-opacity=".18" stroke-width="3"/>'
            f'<g transform="translate({500 - w*0.8/2},{250}) scale(0.8)">{inner}</g>'
            f'<text x="500" y="730" text-anchor="middle" font-family="DM Sans, sans-serif" font-size="20" fill="#5C5A53">Illustration only, not to scale</text></svg>\n')
    p = OUT / name
    p.write_text(body)
    return p


if __name__ == "__main__":
    # colorway A: Deep Teal cap, Light Teal logo + white lettering (two thread colors)
    # colorway B: Linen or white cap, everything Deep Teal (one thread color)
    ways = {"A_on-deep-teal-cap_light-teal-and-white": (LIGHT, WHITE, DEEP),
            "B_on-linen-cap_deep-teal-one-color": (DEEP, DEEP, LINEN)}
    for key, (lf, wf, hat) in ways.items():
        inner, w, h = art(lf, wf)
        p = OUT / f"SomaQ_Hat_ShiftHappens_front_{key}.svg"
        p.write_text(svg_doc(inner, w, h))
        png(p, p.with_suffix(".png"), w / 100, h / 100)
        mock = hat_mock(inner, w, h, hat, f"SomaQ_Hat_mockup_{key}.svg")
        png(mock, mock.with_suffix(".png"), 10, 7.6, dpi=100, transparent=False)
        mock.unlink()
        # lettering only, for a side or back panel
        inner2, w2, h2 = art(lf, wf, with_logo=False, word_w=300.0)
        p2 = OUT / f"SomaQ_Hat_ShiftHappens_wordmark-only_{key}.svg"
        p2.write_text(svg_doc(inner2, w2, h2))
        png(p2, p2.with_suffix(".png"), w2 / 100, h2 / 100)
        print("ok", key, f"front art {w/100:.2f} x {h/100:.2f} in")
