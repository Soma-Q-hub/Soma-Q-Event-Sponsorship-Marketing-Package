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
# Linen border, inset about 0.2 in inside trim
p += f'<rect x="35" y="35" width="{W-70}" height="{H-70}" rx="18" fill="none" stroke="{LINEN}" stroke-opacity=".85" stroke-width="2.5"/>\n'
# faint light triangle, centered on the page, with the QR in the middle of it (bleeds off the bottom)
CX = W / 2
p += f'<polygon points="{CX},770 {CX+300},1062 {CX-300},1062" fill="none" stroke="{LIGHT}" stroke-opacity=".3" stroke-width="3.5" stroke-linejoin="round"/>\n'
p += logo(70, 58, 150, True)
p += lines(70, 142, ["MEASURED EVERY WEEK"], 14, 0, LIGHT, weight="700", ls="3.5")
p += lines(70, 208, ["Five signs your nervous", "system is changing."], 56, 62, WHITE, family="DM Serif Display")
y0 = 300
RH = 68
for i in range(6):
    p += f'<rect x="70" y="{y0 + i*RH}" width="{W-140}" height="1.2" fill="{LIGHT}" fill-opacity=".35"/>\n'
for i, (b, rest) in enumerate(SIGNS):
    cy = y0 + i * RH + RH / 2
    p += f'<circle cx="{70+20}" cy="{cy}" r="20" fill="{LINEN}"/>\n'
    p += f'<text x="{70+20}" y="{cy+7.5}" text-anchor="middle" font-family="DM Sans" font-weight="700" font-size="21" fill="{DEEP}">{i+1}</text>\n'
    p += f'<text x="{70+60}" y="{cy+8}" font-family="DM Sans" font-size="23" fill="{PALE}"><tspan font-weight="700" fill="{LINEN}">{b}</tspan>{rest}</text>\n'
# closing line, centered under the list
p += lines(CX, 690, ["Not whether you showed up."], 19, 0, PALE, weight="500", anchor="middle")
p += lines(CX, 732, ["Whether you changed under pressure."], 36, 0, LINEN, family="DM Serif Display", anchor="middle")
# QR centered in the triangle, on a linen plate
qs = 140
qx, qy = CX - qs / 2, 870
p += f'<rect x="{qx-9}" y="{qy-9}" width="{qs+18}" height="{qs+18}" rx="14" fill="{LINEN}"/>\n'
p += f'<rect x="{qx}" y="{qy}" width="{qs}" height="{qs}" rx="8" fill="#FFFFFF"/><svg x="{qx+8}" y="{qy+8}" width="{qs-16}" height="{qs-16}">{{{{QR_OVERVIEW}}}}</svg>'
p += lines(CX, qy + qs + 33, ["Scan for the free measurement overview"], 15, 0, WHITE, weight="700", anchor="middle")
p += TAIL
(SRC / "table_sign_signs.html").write_text(p)
print("ok table sign")
