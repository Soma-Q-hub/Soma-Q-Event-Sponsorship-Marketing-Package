#!/usr/bin/env python3
"""Generate the large-format pieces (two retractable banners, backdrop, table cover) as SVG pages.
Helpers live in svgkit.py. Run: python3 build/make_large_pieces.py"""
from svgkit import *

# ============================ BANNER 1: the story ============================
W, H = 3300, 8100
p = head("Banner 1: the story, 32 x 80 in", 33, 81, "Retractable banner 32 x 80 in trim, file 33 x 81 in (0.5 in bleed). The bottom ~12 in sits in the stand base, and a 30 in table hides the lower part once the banner stands behind it, so the story sits in the upper 54 in. CONFIRM the vendor template.")
p += f'<rect width="{W}" height="{H}" fill="{LINEN}"/>\n'
p += f'<rect width="{W}" height="900" fill="{DEEP}"/>\n' + logo(250, 235, 1200, True)
p += lines(3050, 530, ["Nervous system alignment", "for high-performing leaders"], 76, 100, LIGHT, weight="700", anchor="end", ls="3")
p += lines(250, 1290, ["What if you", "could train", "your response", "to stress?"], 350, 332, DEEP, family="DM Serif Display")
p += f'<rect x="250" y="2480" width="2800" height="720" rx="50" fill="{WHITE}" stroke="{DEEP}" stroke-width="10"/>\n'
p += lines(340, 2640, ["WHAT WE DO"], 60, 0, DEEP, weight="700", ls="8")
p += lines(340, 2790, ["Soma-Q is a nervous system alignment practice. We train", "high-performing leaders and their teams to restore energy,", "focused clarity, and joy under pressure."], 98, 124, INK)
p += label(250, 3470, "1", "PRESSURE RUNS IN A LOOP", 66)
p += hair(250, 3050, 3540)
p += placed("{{LOOP:light:nogloss}}", 280, 3700, 1.32)
p += lines(250, 6330, ["Burnout ends here.™"], 250, 0, DEEP, family="DM Serif Display")
p += lines(250, 6490, ["The free first steps are on the table. Scan one to start."], 88, 0, INK, weight="500")
p += lines(250, 6760, ["SOMA-Q.COM"], 80, 0, DEEP, weight="700", ls="10")
p += TAIL
(SRC / "banner_story.html").write_text(p)

# ============================ BANNER 2: the proof ============================
p = head("Banner 2: the proof, 32 x 80 in", 33, 81, "Retractable banner 32 x 80 in trim, file 33 x 81 in (0.5 in bleed). Pairs with banner 1. Same safe-zone notes apply: headline, outcomes and the person sit in the upper 54 in; the numbers panel is secondary.")
p += f'<rect width="{W}" height="{H}" fill="{LINEN}"/>\n'
p += f'<rect width="{W}" height="900" fill="{DEEP}"/>\n' + logo(250, 235, 1200, True)
p += lines(3050, 530, ["Nervous system alignment", "for high-performing leaders"], 76, 100, LIGHT, weight="700", anchor="end", ls="3")
p += lines(250, 1290, ["Built to restore", "your energy,", "clarity and joy", "under pressure."], 300, 322, DEEP, family="DM Serif Display")
p += placed("{{OUTCOMES:light}}", 500, 2380, 1.15)
# who is behind it
p += hair(250, 3050, 4640)
p += "<!--PHOTO-->" + photo_circle(660, 5130, 360) + lines(1220, 5060, ["Megan McDonald, Founder"], 96, 0, DEEP, family="DM Serif Display") + lines(1220, 5190, ["13 years as a healthcare technology", "executive. RYT-500. Certified and accredited", "through SOMA Breath."], 62, 78, INK) + "<!--/PHOTO-->"
p += "<!--NOPHOTO-->" + lines(250, 5030, ["Megan McDonald, Founder"], 110, 0, DEEP, family="DM Serif Display") + lines(250, 5200, ["13 years as a healthcare technology executive.", "RYT-500. Certified and accredited through SOMA Breath", "as a trauma-informed breathwork practitioner."], 66, 84, INK) + "<!--/NOPHOTO-->"
# proof panel (secondary, sits lower)
p += f'<rect x="250" y="5700" width="2800" height="900" rx="40" fill="{WHITE}" stroke="{DEEP}" stroke-width="10"/>\n'
p += lines(340, 5830, ["WATCH IT IN YOUR OWN NUMBERS"], 54, 0, DEEP, weight="700", ls="6")
rows = [("Regulation", 7, 3), ("Clarity", 6, 4), ("Fulfillment", 8, 5)]
for i, (n, v, b0) in enumerate(rows):
    y = 5960 + i * 150
    p += f'<text x="340" y="{y+38}" font-family="DM Sans" font-size="70" fill="{INK}">{n}</text>'
    p += f'<rect x="1250" y="{y-12}" width="{v*130}" height="64" rx="8" fill="{LIGHT}"/><circle cx="{1250+b0*130}" cy="{y+20}" r="22" fill="{WHITE}" stroke="{DEEP}" stroke-width="9"/>'
p += lines(340, 6500, ["Week 1 (ring) to Week 10 (bar). Example, not client data."], 54, 0, "#5C5A53")
p += lines(250, 7330, ["Burnout ends here.™"], 200, 0, DEEP, family="DM Serif Display")
p += lines(250, 7560, ["SOMA-Q.COM"], 80, 0, DEEP, weight="700", ls="10")
p += TAIL
(SRC / "banner_proof.html").write_text(p)

# ============================ BACKDROP ============================
BW, BH = 12100, 9100
p = head("Backdrop 120 x 90 in", 121, 91, "PLACEHOLDER trim 120 x 90 in, file 121 x 91 in (0.5 in bleed). Pop-up and fabric backdrops each have their own template, curve and frame lines: CONFIRM first. A 30 in table hides the lowest ~30 in when set against the backdrop, so everything that must be read sits in the top 60 in; the lower band is only the sign-off.")
p += f'<rect width="{BW}" height="{BH}" fill="{LINEN}"/>\n'
p += f'<rect width="{BW}" height="560" fill="{DEEP}"/>\n' + logo(600, 66, 1150, True)
p += lines(11500, 340, ["Nervous system alignment for high-performing leaders"], 105, 0, LIGHT, weight="700", anchor="end", ls="4")
# left column: the question, then what we do, then who
p += lines(600, 1660, ["What if you", "could train", "your response", "to stress?"], 640, 600, DEEP, family="DM Serif Display")
p += hair(600, 4700, 4000)
p += lines(600, 4260, ["WHAT WE DO"], 90, 0, DEEP, weight="700", ls="10")
p += lines(600, 4520, ["Soma-Q is a nervous system alignment practice. We train", "high-performing leaders and their teams to restore", "energy, focused clarity, and joy under pressure."], 150, 200, INK)
p += "<!--PHOTO-->" + photo_circle(1080, 5640, 440, cid="phb") + lines(1800, 5560, ["Megan McDonald, Founder"], 200, 0, DEEP, family="DM Serif Display") + lines(1800, 5760, ["13 years as a healthcare technology", "executive. RYT-500."], 120, 160, INK) + "<!--/PHOTO-->"
p += "<!--NOPHOTO-->" + lines(600, 5560, ["Megan McDonald, Founder"], 200, 0, DEEP, family="DM Serif Display") + lines(600, 5760, ["13 years as a healthcare technology executive. RYT-500."], 120, 0, INK) + "<!--/NOPHOTO-->"
# right: the loop, large, with the outcomes beneath it
p += vhair(5150, 900, 6500)
CX = 8350
p += label(CX, 900, "1", "PRESSURE RUNS IN A LOOP", 100, "middle")
p += placed("{{LOOP:light:gloss}}", CX - int(2075*1.95/2), 1060, 1.95)
p += label(CX, 4650, "2", "BUILT TO RESTORE", 100, "middle")
p += placed("{{OUTCOMES:light}}", CX - 1120, 4790, 1.12)
# sign-off band
p += f'<rect x="0" y="6850" width="{BW}" height="2250" fill="{LIGHT}" fill-opacity=".5"/>\n'
p += lines(600, 8100, ["Burnout ends here.™"], 560, 0, DEEP, family="DM Serif Display")
p += lines(11500, 7750, ["The free first steps are on the table."], 130, 0, DEEP, weight="500", anchor="end")
p += lines(11500, 8250, ["SOMA-Q.COM"], 300, 0, DEEP, weight="700", anchor="end", ls="20")
p += TAIL
(SRC / "backdrop.html").write_text(p)

# ============================ TABLE COVER FRONT ============================
TW, TH = 7300, 3100
p = head("Table cover front 72 x 30 in", 73, 31, "Placeholder trim 72 x 30 in (front of a 6 ft throw), file 73 x 31 in (0.5 in bleed). Vendor templates have seams and folds: CONFIRM before export.")
p += f'<rect width="{TW}" height="{TH}" fill="{LIGHT}"/>\n'
p += f'<rect x="300" y="300" width="1900" height="2500" rx="60" fill="{LINEN}"/>\n' + logo(420, 1050, 1660, False)
p += lines(2700, 1300, ["Burnout ends here.™"], 480, 0, DEEP, family="DM Serif Display")
p += lines(2700, 1800, ["Nervous system training for high-performing", "leaders and teams, built to restore energy,", "focused clarity, and joy under pressure."], 140, 190, DEEP, weight="500")
p += lines(2700, 2560, ["SOMA-Q.COM"], 140, 0, DEEP, weight="700", ls="16")
p += TAIL
(SRC / "table_front.html").write_text(p)
print("ok")
