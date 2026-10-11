#!/usr/bin/env python3
"""Men's hero banners: built for distance. Burnout ends here at the top and as large as the width allows, the nervous system
figure as the image, the pain headline beside it, all key copy above the 54 in line. Two color treatments.
Run: python3 build/make_men_hero.py"""
from svgkit import *
from svgkit import head as head_

W, H = 3300, 8100
HEADLINE = ["Everyone", "around you", "can feel", "your stress.", "Can you?"]
TURN = ["It isn’t a character flaw.", "It’s a stress response,", "and you can learn to", "work with it."]
PLAIN = ["Soma-Q teaches you to notice and settle your", "body’s stress response, so you can think clearly", "and be present with the people who matter."]

def hero(name, title, scheme):
    dark = scheme == "dark"
    p = head_(f"{title}, 32 x 80 in", 33, 81, "Retractable banner 32 x 80 in trim, file 33 x 81 in (0.5 in bleed). Men's hero banner built for distance: logo, Burnout ends here, the figure and the headline all sit above the 54 in line; the lower Linen area is close-range only. CONFIRM the vendor template.")
    p += f'<rect width="{W}" height="{H}" fill="{LINEN}"/>\n'
    top = 5500 if dark else 2300
    p += f'<rect width="{W}" height="{top}" fill="{DEEP}"/>\n'
    if not dark:
        p += f'<rect y="{top}" width="{W}" height="{5500-top}" fill="{LIGHT}"/>\n'
    p += logo(250, 200, 1150, True)
    p += lines(250, 1290, ["Burnout ends", "here.™"], 430, 400, WHITE, family="DM Serif Display")
    p += lines(250, 1990, ["NERVOUS SYSTEM ALIGNMENT", "FOR HIGH-PERFORMING LEADERS"], 150, 190, LIGHT, weight="700", ls="6")
    p += placed(f"{{{{FIGURE:{scheme}}}}}", 200, 2620, 1.4)
    fg, tx, pr = (WHITE, PALE, LIGHT) if dark else (DEEP, INK, DEEP)
    p += lines(1750, 2800, HEADLINE, 200, 225, fg, family="DM Serif Display")
    p += lines(1750, 4020, TURN, 100, 136, tx, weight="500")
    p += lines(1750, 4960, ["Show up the way", "you mean to."], 150, 170, pr, family="DM Serif Display")
    p += label(250, 5950, "", "WHAT WE DO", 60)
    p += lines(250, 6090, PLAIN, 98, 124, INK)
    p += lines(250, 6560, ["The free first steps are on the table. Scan one to start."], 88, 0, INK, weight="500")
    p += lines(250, 6830, ["SOMA-Q.COM"], 80, 0, DEEP, weight="700", ls="10")
    p += TAIL
    (SRC / f"{name}.html").write_text(p)

hero("banner_men_hero_dark", "Men's hero banner, dark", "dark")
hero("banner_men_hero_light", "Men's hero banner, light band", "light")
print("ok hero")
