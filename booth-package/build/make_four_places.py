#!/usr/bin/env python3
"""Optional banner built around the outcomes line. 32 x 80 in. Three band colors (Linen, Light Teal, White) behind the four places, with the nervous system figure.
Plain structure (Oct 13): 1 What you get (headline) / 2 Where (four places + figure) / 3 What to do (the free check + Pressure happens, Burnout doesn't have to) / 4 What this is (Shift Happens, education and training)."""
from svgkit import *
from svgkit import head as head_

W, H = 3300, 8100
ROWS = [("Health", ["Sleep that doesn’t restore you,", "and a body that has been running", "on alarm for too long."]),
        ("Wealth", ["Money and business decisions", "made from pressure", "instead of clarity."]),
        ("Relationships", ["Less patience for the people", "you love than you give", "everyone else."]),
        ("Career", ["Leading well on the outside", "while running on empty", "on the inside."])]

def banner(name, band, cta_bg, tag, scheme, dark=False):
    p = head_(f"Banner: Discover how to reclaim your energy, clarity, and joy in four places ({tag}), 32 x 80 in", 33, 81, f"OPTIONAL banner built around the outcomes line, {tag} band behind the four places, with the nervous system figure. 32 x 80 in trim, file 33 x 81 in (0.5 in bleed). The four places use the website descriptors. CONFIRM the vendor template.")
    p += f'<rect width="{W}" height="{H}" fill="{"#FFFFFF" if dark else DEEP}"/>\n'
    p += logo(250, 200, 1000, not dark)
    hl = ["Discover how", "to reclaim your", "energy, clarity,", "and joy:"] if dark else ["Discover how", "to reclaim your", "energy, clarity,", "and joy in", "four places:"]
    p += lines(250, 1000 + (120 if dark else 0), hl, 330, 365, DEEP if dark else WHITE, family="DM Serif Display")
    y0 = 2700
    p += f'<rect y="{y0}" width="{W}" height="2640" fill="{band}"/>\n'
    for i, (nm, d) in enumerate(ROWS):
        t = y0 - 38 + i * 660
        if i:
            p += f'<rect x="250" y="{t}" width="1800" height="6" fill="{LIGHT if dark else DEEP}" fill-opacity="{.5 if dark else .25}"/>\n'
        p += lines(250, t + 290, [nm], 230, 0, WHITE if dark else DEEP, family="DM Serif Display")
        p += lines(250, t + 430, d, 82 if dark else 74, 98 if dark else 92, PALE if dark else INK, weight="500")
    p += placed("{{FIGURE:%s}}" % scheme, 2180, 3130, 1.0)
    if dark:
        cta(p_list := [p], cta_bg)
        return
    # white (or linen) section: the call to action, with the core line above it
    p += f'<rect y="5340" width="{W}" height="1780" fill="{cta_bg}"/>\n'
    p += lines(W / 2, 5660, ["Pressure happens.", "Burnout doesn’t have to."], 150, 175, DEEP, family="DM Serif Display", anchor="middle")
    p += lines(W / 2, 6015, ["Take the free Burnout Signal Check."], 100, 0, "#3E807A", family="DM Serif Display", anchor="middle")
    p += f'<rect x="{W/2-320}" y="6095" width="640" height="640" rx="36" fill="#FFFFFF" stroke="{DEEP}" stroke-width="10"/><svg x="{W/2-320+50}" y="{6095+50}" width="540" height="540">{{{{QR_QUIZ}}}}</svg>'
    p += lines(W / 2, 6904, ["SOMA-Q.COM"], 84, 0, DEEP, weight="700", anchor="middle", ls="12")
    # base: what this is
    p += f'<rect y="7120" width="{W}" height="{H-7120}" fill="{DEEP}"/>\n'
    p += (f'<text x="{W/2}" y="7550" text-anchor="middle" font-family="DM Serif Display" font-size="130"><tspan fill="{LIGHT}">Shift </tspan><tspan fill="{WHITE}">Happens</tspan><tspan fill="{WHITE}" font-size="36" dy="-54">™</tspan></text>\n')
    p += lines(W / 2, 7770, ["NERVOUS SYSTEM ALIGNMENT EDUCATION AND TRAINING", "TO CHANGE YOUR RESPONSE TO STRESS"], 54, 78, LIGHT, weight="700", anchor="middle", ls="5")
    p += TAIL
    (SRC / f"{name}.html").write_text(p)

def cta(pl, cta_bg):
    p = pl[0]
    p += f'<rect y="5340" width="{W}" height="1400" fill="{cta_bg}"/>\n'
    p += lines(W / 2, 5540, ["Pressure happens.", "Burnout doesn’t have to."], 150, 175, DEEP, family="DM Serif Display", anchor="middle")
    p += f'<rect x="{W/2-320}" y="5830" width="640" height="640" rx="36" fill="#FFFFFF" stroke="{DEEP}" stroke-width="10"/><svg x="{W/2-320+50}" y="{5830+50}" width="540" height="540">{{{{QR_QUIZ}}}}</svg>'
    p += lines(W / 2, 6665, ["Take the free Burnout Signal Check."], 100, 0, "#3E807A", family="DM Serif Display", anchor="middle")
    p += f'<rect y="6740" width="{W}" height="{H-6740}" fill="{DEEP}"/>\n'
    p += (f'<text x="{W/2}" y="7090" text-anchor="middle" font-family="DM Serif Display" font-size="130"><tspan fill="{LIGHT}">Shift </tspan><tspan fill="{WHITE}">Happens</tspan><tspan fill="{WHITE}" font-size="36" dy="-54">™</tspan></text>\n')
    p += lines(W / 2, 7330, ["SOMA-Q IS A NERVOUS SYSTEM ALIGNMENT PRACTICE.", "WE TRAIN HIGH-PERFORMING LEADERS TO NOTICE STRESS", "SOONER, SHIFT IN THE MOMENT, AND RECOVER FASTER."], 68, 100, WHITE, weight="500", anchor="middle", ls="3")
    p += lines(W / 2, 7900, ["SOMA-Q.COM"], 84, 0, WHITE, weight="700", anchor="middle", ls="12")
    p += TAIL
    (SRC / "banner_four_places_dark.html").write_text(p)

banner("banner_four_places", LINEN, "#FFFFFF", "Linen", "light")
banner("banner_four_places_light", LIGHT, "#FFFFFF", "Light Teal", "light")
banner("banner_four_places_white", "#FFFFFF", LINEN, "White", "light")
banner("banner_four_places_dark", DEEP, LINEN, "Dark Teal", "dark", True)
print("ok four places")
