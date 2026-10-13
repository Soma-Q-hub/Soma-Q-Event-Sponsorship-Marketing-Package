#!/usr/bin/env python3
"""Optional banner built around the outcomes line: Discover how to reclaim your energy, clarity, and joy in four places. 32 x 80 in."""
from svgkit import *
from svgkit import head as head_

W, H = 3300, 8100
ROWS = [("Health", ["Sleep that doesn’t restore you, and a body that has", "been running on alarm for too long."]),
        ("Wealth", ["Money and business decisions made from pressure", "instead of clarity."]),
        ("Relationships", ["Less patience for the people you love than you", "give everyone else."]),
        ("Career", ["Leading well on the outside while running on empty", "on the inside."])]
p = head_("Banner: Discover how to reclaim your energy, clarity, and joy in four places, 32 x 80 in", 33, 81, "OPTIONAL banner built around the outcomes line. 32 x 80 in trim, file 33 x 81 in (0.5 in bleed). The four places use the website descriptors. CONFIRM the vendor template.")
p += f'<rect width="{W}" height="{H}" fill="{DEEP}"/>\n'
p += logo(250, 200, 1000, True)
p += lines(250, 1150, ["Discover how to reclaim", "your energy, clarity,", "and joy in four places:"], 250, 290, WHITE, family="DM Serif Display")
# linen: the four places
y0 = 2150
p += f'<rect y="{y0}" width="{W}" height="3200" fill="{LINEN}"/>\n'
for i, (nm, d) in enumerate(ROWS):
    t = y0 + i * 800
    if i:
        p += f'<rect x="250" y="{t}" width="2800" height="6" fill="{DEEP}" fill-opacity=".25"/>\n'
    p += lines(250, t + 330, [nm], 250, 0, DEEP, family="DM Serif Display")
    p += lines(250, t + 510, d, 88, 116, INK, weight="500")
# white: call to action
p += f'<rect y="5350" width="{W}" height="1400" fill="#FFFFFF"/>\n'
p += lines(W / 2, 5602, ["Take the free Burnout Signal Check."], 120, 0, DEEP, family="DM Serif Display", anchor="middle")
p += f'<rect x="{W/2-350}" y="5702" width="700" height="700" rx="40" fill="#FFFFFF" stroke="{DEEP}" stroke-width="10"/><svg x="{W/2-350+54}" y="{5702+54}" width="592" height="592">{{{{QR_QUIZ}}}}</svg>'
p += lines(W / 2, 6581, ["SOMA-Q.COM"], 84, 0, DEEP, weight="700", anchor="middle", ls="12")
# base
p += f'<rect y="6750" width="{W}" height="{H-6750}" fill="{DEEP}"/>\n'
p += lines(W / 2, 7260, ["Pressure happens.", "Burnout doesn’t have to."], 170, 200, WHITE, family="DM Serif Display", anchor="middle")
p += lines(W / 2, 7740, ["EDUCATION AND TRAINING TO CHANGE YOUR RESPONSE TO STRESS"], 62, 0, LIGHT, weight="700", anchor="middle", ls="6")
p += TAIL
(SRC / "banner_four_places.html").write_text(p)
print("ok four places")
