#!/usr/bin/env python3
"""Re-size the two FINAL business card sources from 0.125 in bleed (3.75 x 2.25 in) to 0.25 in bleed (4 x 2.5 in).
The trim stays 3.5 x 2 in and every element keeps its place relative to the trim. Full-bleed shapes are stretched out to the new edge."""
import re, pathlib
SRC = pathlib.Path(__file__).resolve().parent.parent / "src"
W, H, E = 375, 225, 12.5
def widen(html, newname):
    html = html.replace("3.75in 2.25in", "4in 2.5in").replace("width: 3.75in", "width: 4in").replace("height: 2.25in", "height: 2.5in")
    html = re.sub(r'viewBox="0 0 375 225"', f'viewBox="{-E} {-E} {W+2*E} {H+2*E}"', html)
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
    html = html.replace("0.125 in bleed", "0.25 in bleed").replace("file 3.75 x 2.25", "file 4 x 2.5")
    (SRC / f"{newname}.html").write_text(html)
for a, b in (("bizcard2_front_allwhite_serif", "bizcard2_front_allwhite_serif_b25"), ("bizcard2_back_d", "bizcard2_back_d_b25")):
    widen((SRC / f"{a}.html").read_text(), b)
print("ok b25")
