#!/usr/bin/env python3
"""Tabletop stand sign resized for the Yomdug magnetic acrylic QR stand (listing: panel about 11.8 x 5.9 in).
Trim 11.5 x 5.5 in (a little under the panel so the corner magnets sit on the border), plus 0.25 in bleed on every side: file 12 x 6 in.
The existing 12 x 6 layout is scaled to 91.7 percent (uniform, so QR codes stay square) and centered; full-width bands are stretched into the bleed.
CONFIRM the exact insert size from the product listing or the holder itself before printing."""
import re, pathlib
SRC = pathlib.Path(__file__).resolve().parent.parent / "src"
U = 5.5 / 600           # inches per drawing unit (old design was 600 units tall = 6 in at 0.01 in/unit)
BL = 0.25 / U           # bleed in units
TRIM_W = 11.5 / U       # trim width in units
OFF = (TRIM_W - 1200) / 2
L = OFF + BL; T = BL
VW, VH = 12 / U, 6 / U
html = (SRC / "stand_sign.html").read_text()
html = re.sub(r'viewBox="0 0 1200 600"', f'viewBox="{-L:.2f} {-T:.2f} {VW:.2f} {VH:.2f}"', html)
def fix(m):
    t = m.group(0)
    def g(k):
        r = re.search(rf'\b{k}="([-\d.]+)"', t); return float(r.group(1)) if r else None
    x, y, w, h = g("x") or 0.0, g("y") or 0.0, g("width"), g("height")
    if w is None or h is None: return t
    nx, ny, nw, nh = x, y, w, h
    if x <= 0: nx, nw = -L, nw + L
    if x + w >= 1200: nw += L
    if y <= 0: ny, nh = -T, nh + T
    if y + h >= 600: nh += T
    if (nx, ny, nw, nh) == (x, y, w, h): return t
    t = re.sub(r'\b(x|y)="[-\d.]+"', "", t, count=2)
    t = re.sub(r'\bwidth="[-\d.]+"', f'width="{nw:.2f}"', t, count=1)
    t = re.sub(r'\bheight="[-\d.]+"', f'height="{nh:.2f}"', t, count=1)
    return t.replace("<rect", f'<rect x="{nx:.2f}" y="{ny:.2f}"', 1)
html = re.sub(r"<rect[^>]*>", fix, html)
(SRC / "stand_sign_fit.html").write_text(html)
print("ok stand fit", round(L, 2), round(VW, 2), round(VH, 2))
