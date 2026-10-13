#!/usr/bin/env python3
"""Optional banner: "You do hard things." In-your-face leadership message. 32 x 80 in. Run: python3 build/make_hard_things.py"""
from svgkit import *
from svgkit import head as head_

W, H = 3300, 8100
p = head_("Banner: You do hard things, 32 x 80 in", 33, 81, "OPTIONAL banner, 32 x 80 in trim, file 33 x 81 in (0.5 in bleed). In-your-face leadership message: You do hard things, who is running the show, leadership does not happen from the neck up. Key lines sit above the 54 in line. CONFIRM the vendor template.")
p += f'<rect width="{W}" height="{H}" fill="{DEEP}"/>\n'
# ---- teal top: the hard things
p += logo(250, 200, 1000, True)
p += lines(250, 1290, ["You do"], 500, 0, WHITE, family="DM Serif Display")
p += lines(250, 1790, ["hard things."], 500, 0, WHITE, family="DM Serif Display")
p += lines(250, 2250, ["To get more done,", "learn to slow down."], 150, 190, LIGHT, weight="700")
# ---- linen: who is running the show
p += f'<rect y="2750" width="{W}" height="1300" fill="{LINEN}"/>\n'
p += lines(250, 3270, ["Who is running", "the show?"], 330, 360, DEEP, family="DM Serif Display")
p += lines(250, 3800, ["You already do the right things: the workouts, the meditation, and the time off.", "Still, burnout can keep coming back."], 70, 100, INK, weight="500")
# ---- teal: neck up
p += lines(250, 4650, ["Leadership", "does not happen", "from the neck up."], 330, 365, WHITE, family="DM Serif Display")
p += lines(250, 5760, ["Notice the signal. Locate what is happening. Choose your next response."], 68, 0, LIGHT, weight="700")
# ---- white: outcomes + quiz
p += f'<rect y="5930" width="{W}" height="1380" fill="#FFFFFF"/>\n'
p += lines(W / 2, 6180, ["Lead from energy, clarity, and joy,", "so you can keep doing hard things."], 112, 140, DEEP, family="DM Serif Display", anchor="middle")
p += lines(W / 2, 6490, ["Take the free Burnout Signal Check."], 92, 0, "#3E807A", family="DM Serif Display", anchor="middle")
p += f'<rect x="{W/2-330}" y="6560" width="660" height="660" rx="38" fill="#FFFFFF" stroke="{DEEP}" stroke-width="10"/><svg x="{W/2-330+52}" y="{6560+52}" width="556" height="556">{{{{QR_QUIZ}}}}</svg>'
# ---- base
p += f'<rect y="7310" width="{W}" height="{H-7310}" fill="{DEEP}"/>\n'
p += lines(W / 2, 7620, ["EDUCATION AND TRAINING TO CHANGE YOUR RESPONSE TO STRESS"], 62, 0, WHITE, weight="700", anchor="middle", ls="6")
p += lines(W / 2, 7840, ["SOMA-Q.COM"], 84, 0, LIGHT, weight="700", anchor="middle", ls="12")
p += TAIL
(SRC / "banner_hard_things.html").write_text(p)
print("ok hard things")
