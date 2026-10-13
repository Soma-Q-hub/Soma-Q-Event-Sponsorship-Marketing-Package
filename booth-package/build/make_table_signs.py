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
# the faint light triangle from the social post, bottom right, bleeding off the page (original size and position)
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
    p += f'<circle cx="{70+22}" cy="{cy}" r="22" fill="{LINEN}"/>\n'
    p += f'<text x="{70+22}" y="{cy+8}" text-anchor="middle" font-family="DM Sans" font-weight="700" font-size="22" fill="{DEEP}">{i+1}</text>\n'
    p += f'<text x="{70+64}" y="{cy+8}" font-family="DM Sans" font-size="23" fill="{PALE}"><tspan font-weight="700" fill="{LINEN}">{b}</tspan>{rest}</text>\n'
# closing line, bottom left
p += lines(70, 925, ["Not whether you showed up."], 20, 0, PALE, weight="500")
p += lines(70, 978, ["Whether you changed", "under pressure."], 40, 48, LINEN, family="DM Serif Display")
p += lines(70, 1062, ["SOMA-Q.COM"], 15, 0, LIGHT, weight="700", ls="3")
# QR inside the triangle, centered on its axis (x = 650) and clear of both sloping sides, on a linen plate
TX = 650
qs = 112
qx, qy = TX - qs / 2, 922
p += f'<rect x="{qx-9}" y="{qy-9}" width="{qs+18}" height="{qs+18}" rx="12" fill="{LINEN}"/>\n'
p += f'<rect x="{qx}" y="{qy}" width="{qs}" height="{qs}" rx="7" fill="#FFFFFF"/><svg x="{qx+7}" y="{qy+7}" width="{qs-14}" height="{qs-14}">{{{{QR_OVERVIEW}}}}</svg>'
p += lines(TX, 1062, ["Scan for the free measurement overview"], 13, 0, WHITE, weight="700", anchor="middle")
p += TAIL
(SRC / "table_sign_signs.html").write_text(p)
print("ok table sign")

# ---------------------------------------------------------------- LINEN OPTION (Oct 13): same content, plays the whole palette
W, H = 875, 1125
p = head_("Table sign OPTION, Linen: Five signs your nervous system is changing, 8.5 x 11 in", 8.75, 11.25, "OPTION on Linen: Deep Teal header band and bottom band, Linen field, Deep Teal discs, mid-teal accents, light teal triangle, QR to the measurement overview (/go/overview, destination to confirm). 8.5 x 11 in trim, 0.125 in bleed.")
p += f'<rect width="{W}" height="{H}" fill="{LINEN}"/>\n'
p += f'<polygon points="650,790 1010,1330 290,1330" fill="none" stroke="#3E807A" stroke-opacity=".38" stroke-width="4"/>\n'
p += f'<rect width="{W}" height="340" fill="{DEEP}"/>\n'
p += logo(70, 58, 170, True)
p += lines(70, 150, ["MEASURED EVERY WEEK"], 14, 0, LIGHT, weight="700", ls="3.5")
p += lines(70, 228, ["Five signs your nervous", "system is changing."], 56, 66, WHITE, family="DM Serif Display")
y0 = 380
RH = 74
for i in range(6):
    p += f'<rect x="70" y="{y0 + i*RH}" width="{W-140}" height="1.4" fill="{DEEP}" fill-opacity=".28"/>\n'
for i, (b, rest) in enumerate(SIGNS):
    cy = y0 + i * RH + RH / 2
    p += f'<circle cx="{70+22}" cy="{cy}" r="22" fill="{DEEP}"/>\n'
    p += f'<text x="{70+22}" y="{cy+8}" text-anchor="middle" font-family="DM Sans" font-weight="700" font-size="22" fill="{LINEN}">{i+1}</text>\n'
    p += f'<text x="{70+64}" y="{cy+8}" font-family="DM Sans" font-size="23" fill="{DEEP}"><tspan font-weight="700" fill="#3E807A">{b}</tspan>{rest}</text>\n'
p += lines(70, 925, ["Not whether you showed up."], 20, 0, INK, weight="500")
p += lines(70, 978, ["Whether you changed", "under pressure."], 40, 48, DEEP, family="DM Serif Display")
TX = 650; qs = 112; qx, qy = TX - qs / 2, 922
p += f'<rect x="{qx-9}" y="{qy-9}" width="{qs+18}" height="{qs+18}" rx="12" fill="{DEEP}"/>\n'
p += f'<rect x="{qx}" y="{qy}" width="{qs}" height="{qs}" rx="7" fill="#FFFFFF"/><svg x="{qx+7}" y="{qy+7}" width="{qs-14}" height="{qs-14}">{{{{QR_OVERVIEW}}}}</svg>'
p += lines(TX, 1062, ["Scan for the free measurement overview"], 13, 0, DEEP, weight="700", anchor="middle")
p += f'<rect y="1074" width="{W}" height="{H-1074}" fill="{DEEP}"/>\n'
p += lines(70, 1098, ["SOMA-Q.COM"], 13, 0, LIGHT, weight="700", ls="3")
p += TAIL
(SRC / "table_sign_signs_linen.html").write_text(p)
