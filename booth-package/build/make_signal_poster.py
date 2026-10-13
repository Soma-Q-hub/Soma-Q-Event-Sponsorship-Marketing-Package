#!/usr/bin/env python3
"""Booth poster, 24 x 36 in: the NeuroSoma Axis node signal map, readable version. Source: NeuroSoma_Axis_Node_Signal_Map.csv (Drive, Sept 23).
Seven nodes, three states (client-facing names), three signals per cell (two mind, one body), picked from the CSV rows verbatim.
Clinical-sounding signals (chest pain, blood pressure, panic, depression, hopelessness) are left out of this public version."""
from svgkit import *
from svgkit import head as head_
from measure import widths

NODES = [
 ("I", "Foundation", "Is there something underneath me?", ["Feels safe and settled", "Steady under pressure", "Deep, restorative sleep"], ["Hypervigilance", "Fear of change", "Easy to startle"], ["Feeling ungrounded or not present", "Chronic insecurity", "Heavy fatigue"]),
 ("II", "Creativity", "Can I move, receive, and feel?", ["Emotions move and resolve", "Creative flow and play", "Fluid hips and pelvis"], ["Emotional overwhelm", "Swept up in moods", "Hip flexor (psoas) tension"], ["Numbness", "Feeling stuck or flat", "Stiff hips, low flexibility"]),
 ("III", "Confidence", "Is this mine to carry or mine to witness?", ["Clear boundaries", "Decisive, reliable follow-through", "Steady, efficient digestion"], ["Irritability", "Need to control or be right", "Stomach knots, indigestion"], ["Helplessness", "Easily overridden by others", "Chronic fatigue"]),
 ("IV", "Compassion", "Can I stay connected without losing myself?", ["Empathy without absorbing", "Secure, warm connection", "Open chest and shoulders"], ["People-pleasing, over-giving", "Absorbing others&#8217; pain", "Chest tightness"], ["Social withdrawal", "Loneliness", "Shallow breathing"]),
 ("V", "Expression", "Can what is true inside come out?", ["Speaks clearly and truthfully", "Listens fully", "Relaxed jaw, tongue, and neck"], ["Interrupting, talking over others", "Over-explaining as a defense", "Tight throat"], ["Fear of speaking up", "Difficulty putting feelings into words", "Weak or small voice"]),
 ("VI", "Clarity", "Am I seeing what is here or what I predict?", ["Sees situations as they are", "Focused attention", "Relaxed eyes and brow"], ["Rumination, looping thoughts", "Scattered attention", "Eye strain"], ["Low focus and concentration", "Seeing only one right way", "Tired, heavy eyes"]),
 ("VII", "Purpose", "Is the system organized as one thing?", ["Clear sense of purpose", "Sees the bigger picture", "Thinking stays online under pressure"], ["Overanalyzing", "Living in the head", "Racing mind at night"], ["Loss of meaning", "Cynicism", "Brain fog"]),
]
QW = ["Is there something underneath me?"]

def wrap(text, maxw, wmap, size):
    words, lines_, cur = text.split(), [], ""
    for w in words:
        t = (cur + " " + w).strip()
        if wmap[(t, size)] <= maxw: cur = t
        else: lines_.append(cur); cur = w
    lines_.append(cur); return lines_

texts = set()
for n in NODES:
    for c in n[3:6]:
        for e in c: texts.add(e)
fs, qs = 39, 34
allt = set()
def prefixes(t):
    ws = t.split(); return {" ".join(ws[:i]) for i in range(1, len(ws)+1)} | {" ".join(ws[i:j]) for i in range(len(ws)) for j in range(i+1, len(ws)+1)}
cands = set()
for t in texts: cands |= prefixes(t.replace("&#8217;", "’"))
qc = set()
for n in NODES: qc |= prefixes(n[2])
items = [(t, "DM Sans", fs, "500") for t in sorted(cands)] + [(t, "DM Sans", qs, "500") for t in sorted(qc)]
res = widths(items)
wmap = {}
for (t, f, s, w), r in zip(items, res): wmap[(t, s)] = r

p = head_("Poster: NeuroSoma Axis node signal map, 24 x 36 in", 24.25, 36.25, "Booth poster, 24 x 36 in trim + 0.125 in bleed. Brand palette only. Educational framework, not diagnostic.")
p += f'<rect width="2425" height="3625" fill="{WHITE}"/>\n'
p += f'<rect width="2425" height="560" fill="{DEEP}"/>\n'
p += logo(150, 70, 420, True)
p += f'<text x="150" y="390" font-family="DM Serif Display" font-size="170" fill="{WHITE}">The NeuroSoma Axis</text>'
p += f'<text x="1730" y="300" font-family="DM Serif Display" font-size="44" fill="{LIGHT}">&#8482;</text>' if False else ""
p += lines(150, 480, ["Seven places your body and mind report in, and what each one sounds like."], 60, 0, LIGHT, weight="500")
# column headers
X0, CW, GAP = 590, 550, 15
hy = 610
heads = [("ALIGNED", LIGHT, DEEP, None), ("HEIGHTENED", DEEP, WHITE, None), ("NEEDING SUPPORT", PALE, DEEP, DEEP)]
for i, (t, bg, fg, st) in enumerate(heads):
    x = X0 + i * (CW + GAP)
    p += f'<rect x="{x}" y="{hy}" width="{CW}" height="100" rx="20" fill="{bg}"' + (f' stroke="{st}" stroke-width="5"' if st else "") + '/>'
    p += f'<text x="{x+CW/2}" y="{hy+68}" text-anchor="middle" font-family="DM Sans" font-weight="700" font-size="44" letter-spacing="3" fill="{fg}">{t}</text>\n'
RH, y0 = 345, 750
for r, n in enumerate(NODES):
    y = y0 + r * RH
    if r % 2 == 0:
        p += f'<rect x="100" y="{y-10}" width="2225" height="{RH-10}" rx="26" fill="{LINEN}"/>\n'
    p += f'<text x="150" y="{y+95}" font-family="DM Serif Display" font-size="76" fill="{LIGHT}">{n[0]}.</text>'
    p += f'<text x="150" y="{y+185}" font-family="DM Serif Display" font-size="80" fill="{DEEP}">{n[1]}</text>\n'
    ql = wrap(n[2], 400, wmap, qs)
    p += lines(150, y + 245, ql, qs, 44, INK, weight="500")
    for i, cell in enumerate(n[3:6]):
        x = X0 + i * (CW + GAP)
        yy = y + 58
        for e in cell:
            e = e.replace("&#8217;", "’")
            ls_ = wrap(e, CW - 76, wmap, fs)
            p += f'<polygon points="{x+14},{yy+2} {x+30},{yy-26} {x+46},{yy+2}" fill="{DEEP}"/>'
            p += lines(x + 62, yy, [l.replace("’", "&#8217;") for l in ls_], fs, 46, INK, weight="500")
            yy += 46 * len(ls_) + 20
# footer
FY = 3200
p += f'<rect y="{FY}" width="2425" height="{3625-FY}" fill="{DEEP}"/>\n'
p += lines(150, FY + 100, ["An educational framework to help you notice", "what your system is telling you. It is not a", "diagnostic or medical tool."], 54, 76, WHITE, weight="500")
p += lines(150, FY + 345, ["SOMA-Q.COM"], 62, 0, LIGHT, weight="700", ls="10")
p += f'<rect x="1470" y="{FY+50}" width="300" height="300" rx="22" fill="#FFFFFF"/><svg x="1495" y="{FY+75}" width="250" height="250">{{{{QR_QUIZ}}}}</svg>'
p += lines(1830, FY + 125, ["Take the free", "Burnout Signal", "Check."], 62, 78, WHITE, family="DM Serif Display")
p += TAIL
(SRC / "poster_signal_map.html").write_text(p)
print("ok signal poster")
