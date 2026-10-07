#!/usr/bin/env python3
"""Generate the large-format pieces (two retractable banners, backdrop, table cover) as SVG pages.
Light fields with Deep Teal type and Light Teal accents: easier to read under venue lighting and on large prints than a
solid Deep Teal field. Units are 0.01 in. Run: python3 build/make_large_pieces.py"""
import pathlib
SRC = pathlib.Path(__file__).resolve().parent.parent / "src"
DEEP, LIGHT, PALE, LINEN, WHITE, INK = "#103C41", "#9BC4BD", "#E4F2F2", "#EEEADD", "#FEFCF8", "#24211D"

def head(title, w_in, h_in, note):
    return f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><title>{title}</title>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;700&family=DM+Serif+Display:ital@0;1&display=swap">
<style>
/* {note} */
@page {{ size: {w_in}in {h_in}in; margin: 0; }}
html, body {{ margin: 0; padding: 0; width: {w_in}in; height: {h_in}in; overflow: hidden; -webkit-print-color-adjust: exact; print-color-adjust: exact; }}
svg.page {{ display: block; width: {w_in}in; height: {h_in}in; }}
</style></head><body>
<svg class="page" viewBox="0 0 {int(w_in*100)} {int(h_in*100)}" xmlns="http://www.w3.org/2000/svg">
'''
TAIL = '</svg></body></html>\n'

def lines(x, y, rows, size, lh, fill, family="DM Sans", weight="400", anchor="start", style="", ls=""):
    o = ""
    for i, t in enumerate(rows):
        o += (f'<text x="{x}" y="{y+i*lh}" text-anchor="{anchor}" font-family="{family}" font-weight="{weight}" font-size="{size}" '
              f'fill="{fill}"{(" font-style=" + chr(34) + style + chr(34)) if style else ""}{(" letter-spacing=" + chr(34) + str(ls) + chr(34)) if ls else ""}>{t}</text>')
    return o + "\n"

def tri(x, y, w, color, op=1):
    return f'<polygon points="{x},{y+w*0.866:.0f} {x+w/2:.0f},{y} {x+w},{y+w*0.866:.0f}" fill="{color}" fill-opacity="{op}"/>\n'

def logo(x, y, w, dark):
    uri = "{{LOGO_DARK_URI}}" if dark else "{{LOGO_LIGHT_URI}}"
    return f'<image href="{uri}" x="{x}" y="{y}" width="{w}" height="{w*512/1378:.0f}" preserveAspectRatio="xMinYMid meet"/>\n'

def placed(inner_token, x, y, scale):
    return f'<g transform="translate({x},{y}) scale({scale})">{inner_token}</g>\n'

# ============================ BANNER 1: the story ============================
W, H = 3300, 8100
p = head("Banner 1: the story, 32 x 80 in", 33, 81, "Retractable banner 32 x 80 in trim, file 33 x 81 in (0.5 in bleed). The bottom ~12 in sits in the stand base, and a 30 in table hides the lower part once the banner stands behind it, so the story sits in the upper 54 in. CONFIRM the vendor template.")
p += f'<rect width="{W}" height="{H}" fill="{LINEN}"/>\n'
p += tri(1500, 5700, 2300, LIGHT, .30)
p += f'<rect width="{W}" height="900" fill="{DEEP}"/>\n' + logo(250, 235, 1200, True)
p += lines(3050, 530, ["Nervous system alignment", "for high-performing leaders"], 76, 100, LIGHT, weight="700", anchor="end", ls="3")
p += lines(250, 1290, ["What if you", "could train", "your response", "to stress?"], 350, 332, DEEP, family="DM Serif Display")
p += f'<rect x="250" y="2480" width="2800" height="720" rx="50" fill="{WHITE}" stroke="{DEEP}" stroke-width="10"/>\n'
p += lines(340, 2640, ["WHAT WE DO"], 60, 0, DEEP, weight="700", ls="8")
p += lines(340, 2790, ["Soma-Q is a nervous system alignment practice. We train", "high-performing leaders and their teams to restore energy,", "focused clarity, and joy under pressure."], 98, 124, INK)
p += lines(250, 3470, ["PRESSURE RUNS IN A LOOP"], 66, 0, DEEP, weight="700", ls="9")
p += f'<polygon points="250,3870 284,3810 318,3870" fill="{DEEP}" transform="translate(0,0)" opacity="0"/>\n'
p += placed("{{LOOP:light:nogloss}}", 400, 3600, 1.30)
p += lines(250, 6130, ["Burnout ends here.™"], 250, 0, DEEP, family="DM Serif Display")
p += lines(250, 6290, ["The free first steps are on the table. Scan one to start."], 88, 0, INK, weight="500")
p += lines(250, 6560, ["SOMA-Q.COM"], 80, 0, DEEP, weight="700", ls="10")
p += TAIL
(SRC / "banner_story.html").write_text(p)

# ============================ BANNER 2: the proof ============================
p = head("Banner 2: the proof, 32 x 80 in", 33, 81, "Retractable banner 32 x 80 in trim, file 33 x 81 in (0.5 in bleed). Pairs with banner 1. Same safe-zone notes apply.")
p += f'<rect width="{W}" height="{H}" fill="{LINEN}"/>\n'
p += tri(300, 5900, 2200, LIGHT, .30)
p += f'<rect width="{W}" height="900" fill="{DEEP}"/>\n' + logo(250, 235, 1200, True)
p += lines(3050, 530, ["Nervous system alignment", "for high-performing leaders"], 76, 100, LIGHT, weight="700", anchor="end", ls="3")
p += lines(250, 1330, ["Built to restore", "your energy,", "clarity and joy", "under pressure."], 330, 352, DEEP, family="DM Serif Display")
p += placed("{{OUTCOMES:light}}", 480, 2650, 1.17)
p += f'<rect x="250" y="4900" width="2800" height="900" rx="40" fill="{WHITE}" stroke="{DEEP}" stroke-width="10"/>\n'
p += lines(340, 5030, ["WATCH IT IN YOUR OWN NUMBERS"], 54, 0, DEEP, weight="700", ls="6")
rows = [("Regulation", 7, 3), ("Clarity", 6, 4), ("Fulfillment", 8, 5)]
for i, (n, v, b0) in enumerate(rows):
    y = 5160 + i * 150
    p += f'<text x="340" y="{y+38}" font-family="DM Sans" font-size="70" fill="{INK}">{n}</text>'
    p += f'<rect x="1250" y="{y-12}" width="{v*130}" height="64" rx="8" fill="{LIGHT}"/><circle cx="{1250+b0*130}" cy="{y+20}" r="22" fill="{WHITE}" stroke="{DEEP}" stroke-width="9"/>'
p += lines(340, 5700, ["Week 1 (ring) to Week 10 (bar). Example, not client data."], 54, 0, "#5C5A53")
p += "<!--PHOTO-->" + '<clipPath id="ph"><circle cx="760" cy="6560" r="330"/></clipPath><image href="{{PHOTO_URI}}" x="430" y="6130" width="660" height="825" preserveAspectRatio="xMidYMin slice" clip-path="url(#ph)"/><circle cx="760" cy="6560" r="330" fill="none" stroke="#9BC4BD" stroke-width="16"/>' + "<!--/PHOTO-->"
p += "<!--PHOTO-->" + lines(1250, 6450, ["Megan McDonald, Founder", ], 92, 0, DEEP, family="DM Serif Display") + lines(1250, 6570, ["13 years as a healthcare technology", "executive. RYT-500. Certified and accredited", "through SOMA Breath."], 62, 78, INK) + "<!--/PHOTO-->"
p += "<!--NOPHOTO-->" + lines(250, 6200, ["Megan McDonald, Founder"], 100, 0, DEEP, family="DM Serif Display") + lines(250, 6350, ["13 years as a healthcare technology executive.", "RYT-500. Certified and accredited through SOMA Breath", "as a trauma-informed breathwork practitioner."], 66, 84, INK) + "<!--/NOPHOTO-->"
p += lines(250, 7050, ["Burnout ends here.™"], 150, 0, DEEP, family="DM Serif Display") if False else ""
p += TAIL
(SRC / "banner_proof.html").write_text(p)

# ============================ BACKDROP ============================
BW, BH = 12100, 9100
p = head("Backdrop 120 x 90 in", 121, 91, "PLACEHOLDER trim 120 x 90 in, file 121 x 91 in (0.5 in bleed). Pop-up and fabric backdrops each have their own template, curve and frame lines: CONFIRM first. A table and people hide the lowest ~45 in, so everything that must be read sits in the top 45 in.")
p += f'<rect width="{BW}" height="{BH}" fill="{LINEN}"/>\n'
p += f'<rect width="{BW}" height="560" fill="{DEEP}"/>\n' + logo(600, 110, 1500, True)
p += lines(11500, 330, ["Nervous system alignment for high-performing leaders"], 110, 0, LIGHT, weight="700", anchor="end", ls="4")
p += lines(600, 1650, ["What if you", "could train", "your response", "to stress?"], 560, 520, DEEP, family="DM Serif Display")
p += lines(600, 3990, ["Soma-Q is a nervous system alignment practice. We train", "high-performing leaders and their teams to restore", "energy, focused clarity, and joy under pressure."], 138, 175, INK)
p += lines(4700, 1010, ["PRESSURE RUNS IN A LOOP"], 100, 0, DEEP, weight="700", ls="11")
p += placed("{{LOOP:light:gloss}}", 4700, 1200, 1.60)
p += lines(8450, 1010, ["BUILT TO RESTORE"], 100, 0, DEEP, weight="700", ls="11")
p += placed("{{OUTCOMES:light}}", 8450, 1200, 1.55)
p += f'<rect x="0" y="5200" width="{BW}" height="3900" fill="{LIGHT}" fill-opacity=".45"/>\n' + tri(7600, 5300, 3500, WHITE, .35)
p += "<!--PHOTO-->" + '<clipPath id="ph"><circle cx="1500" cy="6600" r="900"/></clipPath><image href="{{PHOTO_URI}}" x="600" y="5700" width="1800" height="2250" preserveAspectRatio="xMidYMin slice" clip-path="url(#ph)"/><circle cx="1500" cy="6600" r="900" fill="none" stroke="#103C41" stroke-width="30"/>' + lines(2800, 6450, ["Megan McDonald, Founder"], 230, 0, DEEP, family="DM Serif Display") + lines(2800, 6780, ["13 years as a healthcare technology executive. RYT-500."], 130, 0, INK) + "<!--/PHOTO-->"
p += "<!--NOPHOTO-->" + lines(600, 6350, ["Megan McDonald, Founder"], 230, 0, DEEP, family="DM Serif Display") + lines(600, 6680, ["13 years as a healthcare technology executive. RYT-500."], 130, 0, INK) + "<!--/NOPHOTO-->"
p += lines(600, 8300, ["Burnout ends here.™"], 520, 0, DEEP, family="DM Serif Display")
p += lines(7400, 8700, ["SOMA-Q.COM"], 230, 0, DEEP, weight="700", ls="20")
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
