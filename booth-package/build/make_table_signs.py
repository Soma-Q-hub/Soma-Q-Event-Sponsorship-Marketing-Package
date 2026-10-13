#!/usr/bin/env python3
"""Table sign, 8.5 x 11 in portrait (file 8.75 x 11.25 in, 0.125 in bleed). Five signs your nervous system is changing (from the social post FiveSigns), with the quiz QR."""
from svgkit import *
from svgkit import head as head_

W, H = 875, 1125
SIGNS = ["How readily you return to steady after stress",
         "How early you notice your body’s signals of pressure",
         "How steady you stay under the week’s emotional weight",
         "How consistently you practice when no one is watching",
         "How often you find moments of meaning and joy"]
p = head_("Table sign: Five signs your nervous system is changing, 8.5 x 11 in", 8.75, 11.25, "Table sign, 8.5 x 11 in trim, file 8.75 x 11.25 in (0.125 in bleed). Five signs your nervous system is changing, measured every week, with the free Burnout Signal Check QR. Text sits at least 0.5 in inside trim.")
p += f'<rect width="{W}" height="{H}" fill="{DEEP}"/>\n'
p += logo(70, 62, 170, True)
p += lines(70, 165, ["MEASURED EVERY WEEK"], 14, 0, LIGHT, weight="700", ls="3.5")
p += lines(70, 238, ["Five signs your", "nervous system", "is changing."], 64, 72, WHITE, family="DM Serif Display")
y0 = 478
for i, t in enumerate(SIGNS):
    y = y0 + i * 66
    p += f'<rect x="70" y="{y-38}" width="{W-140}" height="1.2" fill="{LIGHT}" fill-opacity=".35"/>\n' if i else ""
    p += lines(70, y + 12, [str(i + 1)], 40, 0, LIGHT, family="DM Serif Display")
    p += lines(140, y + 8, [t], 22.5, 0, WHITE, weight="500")
p += lines(70, 828, ["Not whether you showed up.", "Whether you changed."], 31, 40, LIGHT, family="DM Serif Display")
# linen strip with the quiz QR
p += f'<rect y="925" width="{W}" height="{H-925}" fill="{LINEN}"/>\n'
p += f'<rect x="70" y="950" width="132" height="132" rx="10" fill="#FFFFFF" stroke="{DEEP}" stroke-width="2.5"/><svg x="{70+10}" y="{950+10}" width="112" height="112">{{{{QR_QUIZ}}}}</svg>'
p += lines(235, 1000, ["Take the free", "Burnout Signal Check."], 33, 40, DEEP, family="DM Serif Display")
p += lines(235, 1068, ["SOMA-Q.COM"], 17, 0, "#3E807A", weight="700", ls="3.5")
p += TAIL
(SRC / "table_sign_signs.html").write_text(p)
print("ok table sign")
