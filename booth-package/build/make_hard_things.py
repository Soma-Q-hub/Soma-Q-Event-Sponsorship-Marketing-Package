#!/usr/bin/env python3
"""Optional banner: Leadership does not happen from the neck up. / You do hard things. 32 x 80 in. Run: python3 build/make_hard_things.py"""
from svgkit import *
from svgkit import head as head_

W, H = 3300, 8100
p = head_("Banner: Leadership does not happen from the neck up, 32 x 80 in", 33, 81, "OPTIONAL banner, 32 x 80 in trim, file 33 x 81 in (0.5 in bleed). In-your-face leadership message: Leadership does not happen from the neck up, You do hard things, the nervous system figure, outcomes and the quiz QR. Key lines sit above the 54 in line. CONFIRM the vendor template.")
p += f'<rect width="{W}" height="{H}" fill="{DEEP}"/>\n'
# ---- teal top: the headline people see first
p += logo(250, 200, 1000, True)
p += lines(250, 1180, ["Leadership", "does not happen", "from the neck up."], 330, 365, WHITE, family="DM Serif Display")
p += lines(250, 2420, ["You do hard things."], 250, 0, LIGHT, family="DM Serif Display")
p += lines(250, 2760, ["To get more done, learn to slow down."], 100, 0, PALE, weight="700")
# ---- linen: the figure and the three beats
p += f'<rect y="3050" width="{W}" height="2550" fill="{LINEN}"/>\n'
p += placed("{{FIGURE:light}}", 300, 3288, 1.2)
p += lines(1560, 3778, ["Notice the", "signal."], 150, 175, DEEP, family="DM Serif Display")
p += lines(1560, 4318, ["Locate what", "is happening."], 150, 175, DEEP, family="DM Serif Display")
p += lines(1560, 4858, ["Choose your", "next response."], 150, 175, "#3E807A", family="DM Serif Display")
# ---- white: outcomes + quiz
p += f'<rect y="5600" width="{W}" height="1630" fill="#FFFFFF"/>\n'
p += lines(W / 2, 5905, ["Lead from energy, clarity, and joy,", "so you can keep doing hard things."], 112, 140, DEEP, family="DM Serif Display", anchor="middle")
p += lines(W / 2, 6265, ["Take the free Burnout Signal Check."], 92, 0, "#3E807A", family="DM Serif Display", anchor="middle")
p += f'<rect x="{W/2-330}" y="6345" width="660" height="660" rx="38" fill="#FFFFFF" stroke="{DEEP}" stroke-width="10"/><svg x="{W/2-330+52}" y="{6345+52}" width="556" height="556">{{{{QR_QUIZ}}}}</svg>'
# ---- base
p += f'<rect y="7230" width="{W}" height="{H-7230}" fill="{DEEP}"/>\n'
p += lines(W / 2, 7590, ["EDUCATION AND TRAINING TO CHANGE YOUR RESPONSE TO STRESS"], 62, 0, WHITE, weight="700", anchor="middle", ls="6")
p += lines(W / 2, 7810, ["SOMA-Q.COM"], 84, 0, LIGHT, weight="700", anchor="middle", ls="12")
p += TAIL
(SRC / "banner_hard_things.html").write_text(p)
print("ok hard things")
