#!/usr/bin/env python3
"""Men's track large-format pieces: same brand system, palette and mechanism as the main set, different front door.
Headlines lead with showing up the way you intend; the loop names the fixing pattern; the triangle carries the same
three outcomes in plain words. Copy rules: soma-q-brand-docs (outcome first, no hype, no em dashes, no client data).
Run: python3 build/make_men_pieces.py"""
from svgkit import *

W, H = 3300, 8100
SUB = ["Stay steady under pressure, think clearly when it counts,", "and be fully present with the people who matter."]
CARD = ["Soma-Q is a nervous system alignment practice. We train", "high-performing leaders to stay steady, think clearly,", "and be fully present at work and at home."]

# ============================ MEN BANNER 1: the story ============================
p = head("Men's track, Banner 1: the story, 32 x 80 in", 33, 81, "Retractable banner 32 x 80 in trim, file 33 x 81 in (0.5 in bleed). Men's track. The bottom ~12 in sits in the stand base and a 30 in table hides the lower part, so the story sits in the upper 54 in. CONFIRM the vendor template.")
p += f'<rect width="{W}" height="{H}" fill="{LINEN}"/>\n'
p += f'<rect width="{W}" height="900" fill="{DEEP}"/>\n' + logo(250, 235, 1200, True)
p += lines(3050, 530, ["Nervous system alignment", "for high-performing leaders"], 76, 100, LIGHT, weight="700", anchor="end", ls="3")
p += lines(250, 1330, ["Show up the", "way you", "mean to."], 380, 360, DEEP, family="DM Serif Display")
p += lines(250, 2380, SUB, 90, 120, INK, weight="500")
p += f'<rect x="250" y="2680" width="2800" height="720" rx="50" fill="{WHITE}" stroke="{DEEP}" stroke-width="10"/>\n'
p += lines(340, 2840, ["WHAT WE DO"], 60, 0, DEEP, weight="700", ls="8")
p += lines(340, 2990, CARD, 98, 124, INK)
p += label(250, 3670, "1", "THE LOOP PROBLEM-SOLVERS GET CAUGHT IN", 62)
p += hair(250, 3050, 3740)
p += placed("{{LOOP:light:nogloss:men}}", 280, 3890, 1.32)
p += lines(250, 6440, ["Burnout ends here.™"], 250, 0, DEEP, family="DM Serif Display")
p += lines(250, 6600, ["The free first steps are on the table. Scan one to start."], 88, 0, INK, weight="500")
p += lines(250, 6870, ["SOMA-Q.COM"], 80, 0, DEEP, weight="700", ls="10")
p += TAIL
(SRC / "banner_men_story.html").write_text(p)

# ============================ MEN BANNER 2: the proof ============================
p = head("Men's track, Banner 2: the proof, 32 x 80 in", 33, 81, "Retractable banner 32 x 80 in trim, file 33 x 81 in (0.5 in bleed). Men's track. Headline, outcomes and the person sit in the upper 54 in; the numbers panel is secondary.")
p += f'<rect width="{W}" height="{H}" fill="{LINEN}"/>\n'
p += f'<rect width="{W}" height="900" fill="{DEEP}"/>\n' + logo(250, 235, 1200, True)
p += lines(3050, 530, ["Nervous system alignment", "for high-performing leaders"], 76, 100, LIGHT, weight="700", anchor="end", ls="3")
p += lines(250, 1290, ["Built to help", "you stay steady,", "think clearly,", "and be present."], 300, 322, DEEP, family="DM Serif Display")
p += placed("{{OUTCOMES:light:men}}", 500, 2380, 1.15)
p += hair(250, 3050, 4640)
p += "<!--PHOTO-->" + photo_circle(660, 5130, 360) + lines(1220, 5020, ["Megan McDonald, Founder"], 96, 0, DEEP, family="DM Serif Display") + lines(1220, 5150, ["13 years as a healthcare technology executive,", "responsible for both profit and patient outcomes.", "RYT-500. Certified and accredited through SOMA Breath."], 58, 76, INK) + "<!--/PHOTO-->"
p += "<!--NOPHOTO-->" + lines(250, 5030, ["Megan McDonald, Founder"], 110, 0, DEEP, family="DM Serif Display") + lines(250, 5200, ["13 years as a healthcare technology executive,", "responsible for both profit and patient outcomes.", "RYT-500. Certified and accredited through SOMA Breath", "as a trauma-informed breathwork practitioner."], 66, 84, INK) + "<!--/NOPHOTO-->"
p += f'<rect x="250" y="5700" width="2800" height="900" rx="40" fill="{WHITE}" stroke="{DEEP}" stroke-width="10"/>\n'
p += lines(340, 5830, ["TRACK IT LIKE YOU TRACK EVERYTHING ELSE"], 54, 0, DEEP, weight="700", ls="5")
rows = [("Regulation", 7, 3), ("Clarity", 6, 4), ("Response/Reactivity", 6, 3)]
for i, (n, v, b0) in enumerate(rows):
    y = 5960 + i * 150
    p += f'<text x="340" y="{y+38}" font-family="DM Sans" font-size="{70 if len(n) < 12 else 58}" fill="{INK}">{n}</text>'
    p += f'<rect x="1250" y="{y-12}" width="{v*130}" height="64" rx="8" fill="{LIGHT}"/><circle cx="{1250+b0*130}" cy="{y+20}" r="22" fill="{WHITE}" stroke="{DEEP}" stroke-width="9"/>'
p += lines(340, 6500, ["Week 1 (ring) to Week 10 (bar). Example, not client data."], 54, 0, "#5C5A53")
p += lines(250, 7330, ["Burnout ends here.™"], 200, 0, DEEP, family="DM Serif Display")
p += lines(250, 7560, ["SOMA-Q.COM"], 80, 0, DEEP, weight="700", ls="10")
p += TAIL
(SRC / "banner_men_proof.html").write_text(p)

# ============================ MEN BACKDROP ============================
BW, BH = 12100, 9100
p = head("Men's track backdrop 120 x 90 in", 121, 91, "PLACEHOLDER trim 120 x 90 in, file 121 x 91 in (0.5 in bleed). Men's track. Confirm the vendor template first. A 30 in table hides the lowest ~30 in against the backdrop, so everything that must be read sits in the top 60 in.")
p += f'<rect width="{BW}" height="{BH}" fill="{LINEN}"/>\n'
p += f'<rect width="{BW}" height="560" fill="{DEEP}"/>\n' + logo(600, 66, 1150, True)
p += lines(11500, 340, ["Nervous system alignment for high-performing leaders"], 105, 0, LIGHT, weight="700", anchor="end", ls="4")
p += lines(600, 1780, ["Show up the", "way you", "mean to."], 780, 740, DEEP, family="DM Serif Display")
p += hair(600, 4700, 4080)
p += lines(600, 4330, ["WHAT WE DO"], 90, 0, DEEP, weight="700", ls="10")
p += lines(600, 4590, CARD, 150, 200, INK)
p += "<!--PHOTO-->" + photo_circle(1080, 5700, 440, cid="phb") + lines(1800, 5620, ["Megan McDonald, Founder"], 200, 0, DEEP, family="DM Serif Display") + lines(1800, 5820, ["13 years as a healthcare technology", "executive. RYT-500."], 120, 160, INK) + "<!--/PHOTO-->"
p += "<!--NOPHOTO-->" + lines(600, 5620, ["Megan McDonald, Founder"], 200, 0, DEEP, family="DM Serif Display") + lines(600, 5820, ["13 years as a healthcare technology executive. RYT-500."], 120, 0, INK) + "<!--/NOPHOTO-->"
p += vhair(5150, 900, 6500)
CX = 8350
p += label(CX, 900, "1", "THE LOOP PROBLEM-SOLVERS GET CAUGHT IN", 100, "middle")
p += placed("{{LOOP:light:gloss:men}}", CX - int(2075*1.95/2), 1060, 1.95)
p += label(CX, 4650, "2", "BUILT TO RESTORE", 100, "middle")
p += placed("{{OUTCOMES:light:men}}", CX - 1120, 4790, 1.12)
p += f'<rect x="0" y="6850" width="{BW}" height="2250" fill="{LIGHT}" fill-opacity=".5"/>\n'
p += lines(600, 8100, ["Burnout ends here.™"], 560, 0, DEEP, family="DM Serif Display")
p += lines(11500, 7750, ["The free first steps are on the table."], 130, 0, DEEP, weight="500", anchor="end")
p += lines(11500, 8250, ["SOMA-Q.COM"], 300, 0, DEEP, weight="700", anchor="end", ls="20")
p += TAIL
(SRC / "backdrop_men.html").write_text(p)
print("ok")
