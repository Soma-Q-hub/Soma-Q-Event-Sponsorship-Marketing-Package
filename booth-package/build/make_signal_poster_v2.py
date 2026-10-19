#!/usr/bin/env python3
"""NeuroSoma Axis node signal map, center-aligned (every entry, label and question centered in its cell, and each block centered top to bottom in its row; no bullets).
Writes two sources: poster_signal_map_c (24 x 36 in, brand colors) and signal_map_bw_letter (8.5 x 11 in, black and white, outlines only, for a home printer low on ink).
Signals are the same word-for-word CSV picks as the grid poster."""
import io, contextlib
with contextlib.redirect_stdout(io.StringIO()):
    import make_signal_poster as base
from svgkit import *
from svgkit import head as head_
from measure import widths
NODES = base.NODES
def subs(t):
    ws = t.split(); return {" ".join(ws[i:j]) for i in range(len(ws)) for j in range(i+1, len(ws)+1)}
allt = set()
for n in NODES:
    allt |= subs(n[2].replace("&#8217;", "’"))
    for c in n[3:6]:
        for e in c: allt |= subs(e.replace("&#8217;", "’"))
allt = sorted(allt)
SIZES = [(39, "500"), (34, "500"), (11.5, "500"), (9.5, "500")]
items = [(t, "DM Sans", s, w) for (s, w) in SIZES for t in allt]
W_ = {(t, s): r for (t, f, s, w), r in zip(items, widths(items))}
def wrap(text, maxw, size):
    text = text.replace("&#8217;", "’"); cur, out = "", []
    for w in text.split():
        c = (cur + " " + w).strip()
        if W_[(c, size)] <= maxw: cur = c
        else: out.append(cur); cur = w
    out.append(cur); return [o.replace("’", "&#8217;") for o in out]
def ctext(cx, y, rows, size, lh, fill, weight="500", family="DM Sans"):
    return lines(cx, y, rows, size, lh, fill, family=family, weight=weight, anchor="middle")

# ---------------------------------------------------------------- 24 x 36 in, brand colors, centered
p = head_("Poster: NeuroSoma Axis node signal map, centered, 24 x 36 in", 24.25, 36.25, "Booth poster, 24 x 36 in trim + 0.125 in bleed. Brand palette only. Everything centered. Educational framework, not diagnostic.")
p += f'<rect width="2425" height="3625" fill="{WHITE}"/><rect width="2425" height="560" fill="{DEEP}"/>\n'
p += logo(150, 70, 420, True)
p += f'<text x="150" y="390" font-family="DM Serif Display" font-size="170" fill="{WHITE}">The NeuroSoma Axis</text>'
p += lines(150, 480, ["Seven places your body and mind report in, and what each one sounds like."], 60, 0, LIGHT, weight="500")
X0, CW, GAP = 590, 550, 15
hy = 610
heads = [("ALIGNED", LIGHT, DEEP, None), ("HEIGHTENED", DEEP, WHITE, None), ("NEEDING SUPPORT", PALE, DEEP, DEEP)]
for i, (t, bg, fg, st) in enumerate(heads):
    x = X0 + i * (CW + GAP)
    p += f'<rect x="{x}" y="{hy}" width="{CW}" height="100" rx="20" fill="{bg}"' + (f' stroke="{st}" stroke-width="5"' if st else "") + '/>'
    p += f'<text x="{x+CW/2}" y="{hy+68}" text-anchor="middle" font-family="DM Sans" font-weight="700" font-size="44" letter-spacing="3" fill="{fg}">{t}</text>\n'
RH, y0 = 345, 750
FS, LH, GP = 39, 46, 26
LCX = 340   # center of the label column
for r, n in enumerate(NODES):
    y = y0 + r * RH
    top, hgt = y - 10, RH - 10
    cy = top + hgt / 2
    if r % 2 == 0: p += f'<rect x="100" y="{top}" width="2225" height="{hgt}" rx="26" fill="{LINEN}"/>\n'
    ql = wrap(n[2], 400, 34)
    bh = 80 + 12 + len(ql) * 42
    by = cy - bh / 2
    p += f'<text x="{LCX}" y="{by+62}" text-anchor="middle" font-family="DM Serif Display" font-size="64"><tspan fill="{LIGHT}">{n[0]}.</tspan><tspan fill="{DEEP}" dx="12">{n[1]}</tspan></text>'
    p += ctext(LCX, by + 62 + 12 + 34 + 4, ql, 34, 42, INK)
    for i, cell in enumerate(n[3:6]):
        cx = X0 + i * (CW + GAP) + CW / 2
        blocks = [wrap(e, CW - 60, FS) for e in cell]
        h = sum(len(b) * LH for b in blocks) + GP * (len(blocks) - 1)
        yy = cy - h / 2 + FS * 0.8
        for b in blocks:
            p += ctext(cx, yy, b, FS, LH, INK); yy += len(b) * LH + GP
FY = 3200
p += f'<rect y="{FY}" width="2425" height="{3625-FY}" fill="{DEEP}"/>\n'
p += lines(150, FY + 100, ["An educational framework to help you notice", "what your system is telling you. It is not a", "diagnostic or medical tool."], 54, 76, WHITE, weight="500")
p += lines(150, FY + 345, ["SOMA-Q.COM"], 62, 0, LIGHT, weight="700", ls="10")
p += f'<rect x="1470" y="{FY+50}" width="300" height="300" rx="22" fill="#FFFFFF"/><svg x="1495" y="{FY+75}" width="250" height="250">{{{{QR_QUIZ}}}}</svg>'
p += lines(1830, FY + 125, ["Take the free", "Burnout Signal", "Check."], 62, 78, WHITE, family="DM Serif Display")
p += TAIL
(SRC / "poster_signal_map_c.html").write_text(p)

# ---------------------------------------------------------------- 8.5 x 11 in, black and white, no fills (low ink), centered
K = "#000000"
p = head_("NeuroSoma Axis node signal map, black and white, 8.5 x 11 in", 8.5, 11, "Letter size, black and white, outlines only, no bleed. Keep 0.4 in margins for a home printer. Everything centered. Educational framework, not diagnostic.")
p += '<rect width="850" height="1100" fill="#FFFFFF"/>\n'
p += f'<text x="425" y="76" text-anchor="middle" font-family="DM Serif Display" font-size="38" fill="{K}">The NeuroSoma Axis</text>'
p += lines(425, 100, ["Seven places your body and mind report in, and what each one sounds like."], 12, 0, K, weight="500", anchor="middle")
p += lines(425, 46, ["SOMA-Q"], 10, 0, K, weight="700", anchor="middle", ls="4")
LX0, LX1 = 45, 200
CX0, CW, CG = 205, 198, 6
hy, hh = 122, 28
for i, t in enumerate(["ALIGNED", "HEIGHTENED", "NEEDING SUPPORT"]):
    x = CX0 + i * (CW + CG)
    p += f'<rect x="{x}" y="{hy}" width="{CW}" height="{hh}" rx="5" fill="none" stroke="{K}" stroke-width="1.6"/>'
    p += f'<text x="{x+CW/2}" y="{hy+18.5}" text-anchor="middle" font-family="DM Sans" font-weight="700" font-size="10.5" letter-spacing="1.4" fill="{K}">{t}</text>\n'
RY0, RHH = 160, 117
FSL, LHL, GPL = 11.5, 13.5, 7
for r, n in enumerate(NODES):
    top = RY0 + r * RHH
    cy = top + RHH / 2
    p += f'<rect x="{LX0}" y="{top+RHH-1}" width="{CX0+3*CW+2*CG-LX0}" height="0.8" fill="{K}"/>\n'
    lcx = (LX0 + LX1) / 2 - 2
    ql = wrap(n[2], 140, 9.5)
    bh = 20 + 8 + len(ql) * 11.5
    by = cy - bh / 2
    p += f'<text x="{lcx}" y="{by+17}" text-anchor="middle" font-family="DM Serif Display" font-size="19" fill="{K}">{n[0]}. {n[1]}</text>'
    p += ctext(lcx, by + 17 + 8 + 9, ql, 9.5, 11.5, K)
    for i, cell in enumerate(n[3:6]):
        cx = CX0 + i * (CW + CG) + CW / 2
        blocks = [wrap(e, CW - 16, FSL) for e in cell]
        h = sum(len(b) * LHL for b in blocks) + GPL * (len(blocks) - 1)
        yy = cy - h / 2 + FSL * 0.8
        for b in blocks:
            p += ctext(cx, yy, b, FSL, LHL, K); yy += len(b) * LHL + GPL
FY = RY0 + 7 * RHH + 18
p += lines(45, FY + 14, ["An educational framework to help you notice what your system is telling you.", "It is not a diagnostic or medical tool."], 10, 14, K, weight="500")
p += lines(45, FY + 52, ["SOMA-Q.COM"], 10, 0, K, weight="700", ls="3")
p += f'<rect x="716" y="{FY-6}" width="90" height="90" fill="#FFFFFF" stroke="{K}" stroke-width="1"/><svg x="722" y="{FY}" width="78" height="78">{{{{QR_QUIZ}}}}</svg>'
p += lines(706, FY + 22, ["Take the free", "Burnout Signal", "Check."], 12, 15, K, family="DM Serif Display", anchor="end")
p += TAIL
(SRC / "signal_map_bw_letter.html").write_text(p)
print("ok v2", FY + 90)
