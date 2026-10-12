#!/usr/bin/env python3
"""Men's hero banners: built for distance. Burnout ends here at the top and as large as the width allows, the nervous system
figure as the image, the pain headline beside it, all key copy above the 54 in line. Two color treatments.
Run: python3 build/make_men_hero.py"""
from svgkit import *
from svgkit import head as head_

W, H = 3300, 8100
HEADLINE = ["Who feels it", "when you’re", "stressed?"]
TURN = ["It isn’t a character flaw.", "It’s a stress response,", "and you can learn to", "work with it."]
WHAT_WE_DO = ["Soma-Q is a nervous system alignment", "practice. We train high-performing", "leaders to notice stress sooner, shift", "in the moment and recover faster."]

def hero(name, title, scheme, tag="burnout"):
    dark = scheme == "dark"
    p = head_(f"{title}, 32 x 80 in", 33, 81, "Retractable banner 32 x 80 in trim, file 33 x 81 in (0.5 in bleed). Men's hero banner built for distance: logo, Burnout ends here, the figure and the headline all sit above the 54 in line; the lower Linen area is close-range only. CONFIRM the vendor template.")
    p += f'<rect width="{W}" height="{H}" fill="{'#FFFFFF' if dark and tag == 'shift' else LINEN}"/>\n'
    top = 5500 if dark else 2720
    p += f'<rect width="{W}" height="{top}" fill="{DEEP}"/>\n'
    if not dark:
        p += f'<rect y="{top}" width="{W}" height="{5500-top}" fill="{LIGHT}"/>\n'
    p += logo(250, 200, 1150, True)
    l1, l2 = ("Burnout ends", "here.") if tag == "burnout" else ("Shift", "Happens")
    tm = '<tspan font-size="170" dy="-170" dx="14">™</tspan>'
    p += (f'<text x="250" y="1290" font-family="DM Serif Display" font-size="430" fill="{WHITE}">{l1}</text>'
          f'<text x="250" y="1690" font-family="DM Serif Display" font-size="430" fill="{WHITE}">{l2}{tm}</text>\n')
    p += label(250, 1900, "", "WHAT WE DO", 64).replace(f'fill="{DEEP}"', f'fill="{LIGHT}"')
    p += lines(250, 2070, WHAT_WE_DO, 128, 160, LIGHT if dark else WHITE, weight="500")
    p += placed(f"{{{{FIGURE:{scheme}}}}}", 200, 2800, 1.4)
    fg, tx, pr = (WHITE, PALE, LIGHT) if dark else (DEEP, INK, DEEP)
    p += lines(1750, 3010, HEADLINE, 200, 225, fg, family="DM Serif Display")
    hc = LIGHT if dark else DEEP
    bold = lambda x, y, rows: "".join(f'<text x="{x}" y="{y+i*170}" font-family="DM Serif Display" font-size="150" fill="{hc}" stroke="{hc}" stroke-width="7" stroke-linejoin="round">{t}</text>' for i, t in enumerate(rows)) + "\n"
    p += bold(1750, 3800, ["What do you", "do next?"])
    p += lines(1750, 4230, TURN, 104, 142, WHITE if dark else DEEP, weight="700")
    p += bold(1750, 4970, ["Show up the way", "you want to."])
    p += lines(250, 5800, ["Book a free", "discovery call."], 150, 170, DEEP, family="DM Serif Display")
    p += lines(250, 6200, ["An honest conversation about what pressure", "is costing you. No obligation."], 66, 90, INK, weight="500")
    p += f'<rect x="2330" y="5640" width="720" height="720" rx="40" fill="#FFFFFF" stroke="{DEEP}" stroke-width="10"/><svg x="2400" y="5710" width="580" height="580">{{{{QR_CALL}}}}</svg>'
    p += lines(250, 6500, ["SOMA-Q.COM"], 80, 0, DEEP, weight="700", ls="10")
    p += TAIL
    (SRC / f"{name}.html").write_text(p)

hero("banner_men_hero_dark", "Men's hero banner, dark", "dark")
hero("banner_men_hero_light", "Men's hero banner, light band", "light")
hero("banner_men_hero_dark_shift", "Hero banner, dark, Shift happens", "dark", "shift")
hero("banner_men_hero_light_shift", "Hero banner, light band, Shift happens", "light", "shift")
print("ok hero")
