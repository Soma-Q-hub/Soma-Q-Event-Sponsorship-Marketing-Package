#!/usr/bin/env python3
"""Re-size the two FINAL postcard sources from 0.125 in bleed (6.25 x 4.25 in) to 0.25 in bleed (6.5 x 4.5 in).
The trim stays 6 x 4 in and every element keeps its place relative to the trim. Full-bleed shapes are stretched out to the new edge."""
import re, pathlib
SRC = pathlib.Path(__file__).resolve().parent.parent / "src"
W, H, E = 625, 425, 12.5
def widen(html, newname):
    html = html.replace("6.25in 4.25in", "6.5in 4.5in").replace("width: 6.25in", "width: 6.5in").replace("height: 4.25in", "height: 4.5in")
    html = re.sub(r'viewBox="0 0 625 425"', f'viewBox="{-E} {-E} {W+2*E} {H+2*E}"', html)
    def fix(m):
        t = m.group(0)
        g = lambda k: (float(re.search(rf'\b{k}="([-\d.]+)"', t).group(1)) if re.search(rf'\b{k}="([-\d.]+)"', t) else None)
        x, y, w, h = g("x"), g("y"), g("width"), g("height")
        x = 0.0 if x is None else x; y = 0.0 if y is None else y
        if w is None or h is None: return t
        nx, ny, nw, nh = x, y, w, h
        if x <= 0: nx, nw = -E, nw + E
        if y <= 0: ny, nh = -E, nh + E
        if x + w >= W: nw = nw + E
        if y + h >= H: nh = nh + E
        if (nx, ny, nw, nh) == (x, y, w, h): return t
        t = re.sub(r'\bx="[-\d.]+"', "", t, count=1)
        t = re.sub(r'\by="[-\d.]+"', "", t, count=1)
        t = re.sub(r'\bwidth="[-\d.]+"', f'width="{nw:g}"', t, count=1)
        t = re.sub(r'\bheight="[-\d.]+"', f'height="{nh:g}"', t, count=1)
        return t.replace("<rect", f'<rect x="{nx:g}" y="{ny:g}"', 1)
    html = re.sub(r"<rect[^>]*>", fix, html)
    html = html.replace("0.125 in bleed", "0.25 in bleed").replace("file 6.25 x 4.25", "file 6.5 x 4.5")
    (SRC / f"{newname}.html").write_text(html)
for a, b in (("postcard_front_l", "postcard_front_l_b25"), ("postcard_back_w", "postcard_back_w_b25")):
    widen((SRC / f"{a}.html").read_text(), b)
print("ok b25")
