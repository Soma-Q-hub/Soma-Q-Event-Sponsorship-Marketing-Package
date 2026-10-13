#!/usr/bin/env python3
"""Table sign, 8.5 x 11 in portrait (file 8.75 x 11.25 in, 0.125 in bleed). Five signs your nervous system is changing, built from the FiveSigns social post
(numbered discs, hairlines, faint light triangle). QR goes to the free measurement overview (/go/overview, destination to be confirmed)."""
from svgkit import *
from svgkit import head as head_

W, H = 875, 1125
SIGNS = [("How readily", " you return to steady after stress"),
         ("How early", " you notice your body’s signals of pressure"),
         ("How steady", " you stay under the week’s emotional weight"),
         ("How consistently", " you practice when no one is watching"),
         ("How often", " you find moments of meaning and joy")]
p = head_("Table sign: Five signs your nervous system is changing, 8.5 x 11 in", 8.75, 11.25, "Table sign, 8.5 x 11 in trim, file 8.75 x 11.25 in (0.125 in bleed). Five signs your nervous system is changing, measured every week, with the QR to the free measurement overview. Text sits at least 0.5 in inside trim.")
p += f'<rect width="{W}" height="{H}" fill="{DEEP}"/>\n'
# faint light triangle, as on the social post (behind everything, bleeds off the bottom right)
p += f'<polygon points="650,790 1010,1330 290,1330" fill="none" stroke="{LIGHT}" stroke-opacity=".16" stroke-width="4"/>\n'
p += logo(70, 62, 170, True)
p += lines(70, 165, ["MEASURED EVERY WEEK"], 14, 0, LIGHT, weight="700", ls="3.5")
p += lines(70, 248, ["Five signs your nervous", "system is changing."], 60, 72, WHITE, family="DM Serif Display")
y0 = 365
RH = 86
for i in range(6):
    p += f'<rect x="70" y="{y0 + i*RH}" width="{W-140}" height="1.2" fill="{LIGHT}" fill-opacity=".35"/>\n'
for i, (b, rest) in enumerate(SIGNS):
    cy = y0 + i * RH + RH / 2
    p += f'<circle cx="{70+22}" cy="{cy}" r="22" fill="{LIGHT}"/>\n'
    p += f'<text x="{70+22}" y="{cy+8}" text-anchor="middle" font-family="DM Sans" font-weight="500" font-size="22" fill="{DEEP}">{i+1}</text>\n'
    p += f'<text x="{70+64}" y="{cy+8}" font-family="DM Sans" font-size="23" fill="{PALE}"><tspan font-weight="700" fill="{LIGHT}">{b}</tspan>{rest}</text>\n'
# bottom: closing line left, QR right
p += lines(70, 925, ["Not whether you showed up."], 20, 0, PALE, weight="500")
p += lines(70, 978, ["Whether you changed", "under pressure."], 40, 48, WHITE, family="DM Serif Display")
p += lines(70, 1062, ["SOMA-Q.COM"], 15, 0, LIGHT, weight="700", ls="3")
qx, qy, qs = 640, 850, 150
p += f'<rect x="{qx}" y="{qy}" width="{qs}" height="{qs}" rx="10" fill="#FFFFFF"/><svg x="{qx+10}" y="{qy+10}" width="{qs-20}" height="{qs-20}">{{{{QR_OVERVIEW}}}}</svg>'
p += lines(qx + qs / 2, qy + qs + 30, ["Scan for the free", "measurement overview"], 15, 20, WHITE, weight="700", anchor="middle")
p += TAIL
(SRC / "table_sign_signs.html").write_text(p)
print("ok table sign")
