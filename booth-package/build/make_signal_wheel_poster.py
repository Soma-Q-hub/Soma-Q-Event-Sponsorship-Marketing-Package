#!/usr/bin/env python3
"""Booth poster, 24 x 36 in: the NeuroSoma Axis node signal WHEEL (circular). Source: NeuroSoma_Axis_Node_Signal_Map.csv.
Seven node cards around a center circle, clockwise from the top (I at the top). Each card: one mind signal and one body signal per state
(client-facing state names), verbatim from the CSV. Clinical-sounding signals left out of this public version."""
import math
from svgkit import *
from svgkit import head as head_
from measure import widths

N = [
 ("I", "Foundation", "SQ", ["Feels safe and settled", "Deep, restorative sleep"], ["Hypervigilance", "Easy to startle"], ["Chronic insecurity", "Heavy fatigue"]),
 ("II", "Creativity", "SQ", ["Creative flow and play", "Fluid hips and pelvis"], ["Emotional overwhelm", "Hip flexor (psoas) tension"], ["Feeling stuck or flat", "Stiff hips, low flexibility"]),
 ("III", "Confidence", "SQ", ["Clear boundaries", "Steady, efficient digestion"], ["Irritability", "Stomach knots, indigestion"], ["Helplessness", "Chronic fatigue"]),
 ("IV", "Compassion", "EQ", ["Empathy without absorbing", "Open chest and shoulders"], ["Absorbing others&#8217; pain", "Chest tightness"], ["Social withdrawal", "Shallow breathing"]),
 ("V", "Expression", "EQ", ["Speaks clearly and truthfully", "Relaxed jaw, tongue, and neck"], ["Interrupting, talking over others", "Tight throat"], ["Fear of speaking up", "Weak or small voice"]),
 ("VI", "Clarity", "IQ", ["Sees situations as they are", "Relaxed eyes and brow"], ["Rumination, looping thoughts", "Eye strain"], ["Low focus and concentration", "Tired, heavy eyes"]),
 ("VII", "Purpose", "IQ", ["Clear sense of purpose", "Thinking stays online under pressure"], ["Overanalyzing", "Racing mind at night"], ["Loss of meaning", "Brain fog"]),
]
FS, LH = 36, 42
TW = 540
def prefixes(t):
    ws = t.split(); return {" ".join(ws[i:j]) for i in range(len(ws)) for j in range(i+1, len(ws)+1)}
cands = set()
for n in N:
    for c in n[3:6]:
        for e in c: cands |= prefixes(e.replace("&#8217;", "’"))
cands = sorted(cands)
wm = dict(zip(cands, widths([(t, "DM Sans", FS, "500") for t in cands])))
def wrap(t):
    t = t.replace("&#8217;", "’"); cur, out = "", []
    for w in t.split():
        c = (cur + " " + w).strip()
        if wm[c] <= TW: cur = c
        else: out.append(cur); cur = w
    out.append(cur); return [o.replace("’", "&#8217;") for o in out]

p = head_("Poster: NeuroSoma Axis node signal wheel, 24 x 36 in", 24.25, 36.25, "Booth poster, 24 x 36 in trim + 0.125 in bleed. Brand palette only. Educational framework, not diagnostic.")
p += f'<rect width="2425" height="3625" fill="{WHITE}"/>\n'
p += f'<rect width="2425" height="540" fill="{DEEP}"/>\n'
p += logo(150, 70, 400, True)
p += f'<text x="150" y="365" font-family="DM Serif Display" font-size="170" fill="{WHITE}">The NeuroSoma Axis</text>'
p += lines(150, 465, ["What each node sounds like when you are aligned, heightened, or needing support."], 56, 0, LIGHT, weight="500")
CX, CY = 1212, 1910
CARD_W = 620
pos = [(1212, 910), (1860, 1287), (1960, 2132), (1540, 2801), (884, 2801), (464, 2132), (564, 1287)]
# spokes and rings first (under the cards)
p += f'<circle cx="{CX}" cy="{CY}" r="760" fill="none" stroke="{LIGHT}" stroke-width="6" stroke-opacity=".6" stroke-dasharray="4 18" stroke-linecap="round"/>\n'
for (x, y) in pos:
    p += f'<line x1="{CX}" y1="{CY}" x2="{x}" y2="{y}" stroke="{LIGHT}" stroke-width="10" stroke-opacity=".8"/>\n'
chips = [("ALIGNED", LIGHT, DEEP, None, 150), ("HEIGHTENED", DEEP, WHITE, None, 205), ("NEEDING SUPPORT", PALE, DEEP, DEEP, 300)]
for n, (x, y) in zip(N, pos):
    rows = []
    for cell in n[3:6]:
        rows.append([wrap(e) for e in cell])
    hh = 120 + sum(36 + 18 + sum(len(w) for w in r) * LH + 14 + 20 for r in rows)
    x0, y0 = x - CARD_W / 2, y - hh / 2
    p += f'<rect x="{x0}" y="{y0}" width="{CARD_W}" height="{hh}" rx="34" fill="{LINEN}"/>\n'
    p += f'<text x="{x0+34}" y="{y0+84}" font-family="DM Serif Display" font-size="64" fill="{DEEP}">{n[0]}. {n[1]}</text>'
    p += f'<text x="{x0+CARD_W-34}" y="{y0+76}" text-anchor="end" font-family="DM Sans" font-weight="700" font-size="30" letter-spacing="4" fill="{DEEP}" fill-opacity=".6">{n[2]}</text>\n'
    yy = y0 + 118
    for (lab, bg, fg, st, cw), r in zip(chips, rows):
        p += f'<rect x="{x0+34}" y="{yy}" width="{cw}" height="38" rx="19" fill="{bg}"' + (f' stroke="{st}" stroke-width="3"' if st else "") + '/>'
        p += f'<text x="{x0+34+cw/2}" y="{yy+27}" text-anchor="middle" font-family="DM Sans" font-weight="700" font-size="22" letter-spacing="3" fill="{fg}">{lab}</text>\n'
        ty = yy + 38 + 18 + 28
        for w in r:
            p += lines(x0 + 34, ty, w, FS, LH, INK, weight="500"); ty += LH * len(w)
        yy = ty - 28 + 14 + 20 - 18 + 18
# center
p += f'<circle cx="{CX}" cy="{CY}" r="330" fill="{DEEP}"/><circle cx="{CX}" cy="{CY}" r="352" fill="none" stroke="{LIGHT}" stroke-width="8"/>\n'
p += logo(CX - 190, CY - 215, 380, True, center=True)
p += lines(CX, CY + 95, ["Seven nodes."], 64, 0, WHITE, family="DM Serif Display", anchor="middle")
p += lines(CX, CY + 175, ["One axis."], 64, 0, LIGHT, family="DM Serif Display", anchor="middle")
FY = 3200
p += f'<rect y="{FY}" width="2425" height="{3625-FY}" fill="{DEEP}"/>\n'
p += lines(150, FY + 100, ["An educational framework to help you notice", "what your system is telling you. It is not a", "diagnostic or medical tool."], 54, 76, WHITE, weight="500")
p += lines(150, FY + 345, ["SOMA-Q.COM"], 62, 0, LIGHT, weight="700", ls="10")
p += f'<rect x="1470" y="{FY+50}" width="300" height="300" rx="22" fill="#FFFFFF"/><svg x="1495" y="{FY+75}" width="250" height="250">{{{{QR_QUIZ}}}}</svg>'
p += lines(1830, FY + 125, ["Take the free", "Burnout Signal", "Check."], 62, 78, WHITE, family="DM Serif Display")
p += TAIL
(SRC / "poster_signal_wheel.html").write_text(p)
print("ok wheel poster")
