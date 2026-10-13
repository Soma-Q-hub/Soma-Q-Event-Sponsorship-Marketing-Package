#!/usr/bin/env python3
"""Optional banner built around the outcomes line: Discover how to reclaim your energy, clarity, and joy in four places. 32 x 80 in.
Three background versions for the four places: Linen, Light Teal, White. Headline set in the same type as 'Leadership does not happen from the neck up.'"""
from svgkit import *
from svgkit import head as head_

W, H = 3300, 8100
ROWS = [("Health", ["Sleep that doesn’t restore you, and a body that has", "been running on alarm for too long."]),
        ("Wealth", ["Money and business decisions made from pressure", "instead of clarity."]),
        ("Relationships", ["Less patience for the people you love than you", "give everyone else."]),
        ("Career", ["Leading well on the outside while running on empty", "on the inside."])]

def banner(name, band, cta_bg, tag):
    p = head_(f"Banner: Discover how to reclaim your energy, clarity, and joy in four places ({tag}), 32 x 80 in", 33, 81, f"OPTIONAL banner built around the outcomes line, {tag} band behind the four places. 32 x 80 in trim, file 33 x 81 in (0.5 in bleed). The four places use the website descriptors. CONFIRM the vendor template.")
    p += f'<rect width="{W}" height="{H}" fill="{DEEP}"/>\n'
    p += logo(250, 200, 1000, True)
    p += lines(250, 1000, ["Discover how", "to reclaim your", "energy, clarity,", "and joy in", "four places:"], 330, 365, WHITE, family="DM Serif Display")
    y0 = 2800
    p += f'<rect y="{y0}" width="{W}" height="2800" fill="{band}"/>\n'
    for i, (nm, d) in enumerate(ROWS):
        t = y0 + i * 700
        if i:
            p += f'<rect x="250" y="{t}" width="2800" height="6" fill="{DEEP}" fill-opacity=".25"/>\n'
        p += lines(250, t + 300, [nm], 230, 0, DEEP, family="DM Serif Display")
        p += lines(250, t + 470, d, 84, 110, INK, weight="500")
    p += f'<rect y="5600" width="{W}" height="1400" fill="{cta_bg}"/>\n'
    p += lines(W / 2, 5852, ["Take the free Burnout Signal Check."], 120, 0, DEEP, family="DM Serif Display", anchor="middle")
    p += f'<rect x="{W/2-350}" y="5952" width="700" height="700" rx="40" fill="#FFFFFF" stroke="{DEEP}" stroke-width="10"/><svg x="{W/2-350+54}" y="{5952+54}" width="592" height="592">{{{{QR_QUIZ}}}}</svg>'
    p += lines(W / 2, 6831, ["SOMA-Q.COM"], 84, 0, DEEP, weight="700", anchor="middle", ls="12")
    p += f'<rect y="7000" width="{W}" height="{H-7000}" fill="{DEEP}"/>\n'
    p += lines(W / 2, 7330, ["Pressure happens.", "Burnout doesn’t have to."], 150, 175, WHITE, family="DM Serif Display", anchor="middle")
    p += (f'<text x="{W/2}" y="7720" text-anchor="middle" font-family="DM Serif Display" font-size="104"><tspan fill="{LIGHT}">Shift </tspan><tspan fill="{WHITE}">Happens</tspan><tspan fill="{WHITE}" font-size="30" dy="-44">™</tspan></text>\n')
    p += lines(W / 2, 7910, ["EDUCATION AND TRAINING TO CHANGE YOUR RESPONSE TO STRESS"], 56, 0, LIGHT, weight="700", anchor="middle", ls="6")
    p += TAIL
    (SRC / f"{name}.html").write_text(p)

banner("banner_four_places", LINEN, "#FFFFFF", "Linen")
banner("banner_four_places_light", LIGHT, "#FFFFFF", "Light Teal")
banner("banner_four_places_white", "#FFFFFF", LINEN, "White")
print("ok four places")
