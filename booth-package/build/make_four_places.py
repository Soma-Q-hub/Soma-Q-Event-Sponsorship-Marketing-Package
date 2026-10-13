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

def banner(name, band, cta_bg, tag, scheme, dark=False, flip=False):
    p = head_(f"Banner: Discover how to reclaim your energy, clarity, and joy in four places ({tag}), 32 x 80 in", 33, 81, f"OPTIONAL banner built around the outcomes line, {tag} band behind the four places, with the nervous system figure. 32 x 80 in trim, file 33 x 81 in (0.5 in bleed). The four places use the website descriptors. CONFIRM the vendor template.")
    p += f'<rect width="{W}" height="{H}" fill="{"#FFFFFF" if dark else DEEP}"/>\n'
    p += logo(250, 200, 1000, not dark)
    hl = ["Discover how", "to reclaim your", "energy, clarity,", "and joy:"] if dark else ["Discover how", "to reclaim your", "energy, clarity,", "and joy in", "four places:"]
    p += lines(250, 1000 + (120 if dark and not flip else 0), hl, 330, 365, DEEP if dark else WHITE, family="DM Serif Display")
    y0 = 2330 if flip else 2700          # flipped version: shorter white top, taller dark places band
    RH = 740 if flip else 660
    p += f'<rect y="{y0}" width="{W}" height="{4*RH if flip else 2640}" fill="{band}"/>\n'
    for i, (nm, d) in enumerate(ROWS):
        t = y0 - 38 + i * RH
        if i:
            p += f'<rect x="250" y="{t}" width="1800" height="6" fill="{LIGHT if dark else DEEP}" fill-opacity="{.5 if dark else .25}"/>\n'
        hs, ds = (250, 88) if flip else (230, 82 if dark else 74)
        p += lines(250, t + (320 if flip else 290), [nm], hs, 0, WHITE if dark else DEEP, family="DM Serif Display")
        p += lines(250, t + (470 if flip else 430), d, ds, ds * 1.2 if dark else 92, PALE if dark else INK, weight="500")
    if flip:
        p += placed("{{FIGURE:%s}}" % scheme, 2074, 2802, 1.12)
    else:
        p += placed("{{FIGURE:%s}}" % scheme, 2180, 3130, 1.0)
    if dark:
        cta([p], cta_bg, flip)
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

def cta(pl, cta_bg, flip=False):
    p = pl[0]
    G = 150  # equal gap above and below the paragraph, measured cap-top to baseline
    def about_block(S, p, lt=False):
        B1 = S + 30 + G + 59
        B3 = B1 + 240
        C = B3 + G + 59
        sh, hp, tx = ("#3E807A", DEEP, DEEP) if lt else (LIGHT, WHITE, WHITE)
        p += (f'<text x="{W/2}" y="{S}" text-anchor="middle" font-family="DM Serif Display" font-size="130"><tspan fill="{sh}">Shift </tspan><tspan fill="{hp}">Happens</tspan><tspan fill="{hp}" font-size="36" dy="-54">™</tspan></text>\n')
        p += lines(W / 2, B1, ["SOMA-Q IS A NERVOUS SYSTEM ALIGNMENT PRACTICE.", "WE TRAIN HIGH-PERFORMING LEADERS TO NOTICE STRESS", "SOONER, SHIFT IN THE MOMENT, AND RECOVER FASTER."], 84, 120, tx, weight="500", anchor="middle", ls="3")
        p += lines(W / 2, C, ["SOMA-Q.COM"], 84, 0, tx, weight="700", anchor="middle", ls="12")
        return p, C
    def qr_block(y, p, bg, dark_bg):
        fg, cap, edge = (WHITE, PALE, LIGHT) if dark_bg else (DEEP, "#3E807A", DEEP)
        p += f'<rect y="{y}" width="{W}" height="{H-y}" fill="{bg}"/>\n'
        p += lines(W / 2, y + 260, ["Pressure happens.", "Burnout doesn’t have to."], 150, 175, fg, family="DM Serif Display", anchor="middle")
        qy = y + 560
        p += f'<rect x="{W/2-320}" y="{qy}" width="640" height="640" rx="36" fill="#FFFFFF" stroke="{edge}" stroke-width="10"/><svg x="{W/2-320+50}" y="{qy+50}" width="540" height="540">{{{{QR_QUIZ}}}}</svg>'
        p += lines(W / 2, qy + 785, ["Take the free Burnout Signal Check."], 100, 0, cap, family="DM Serif Display", anchor="middle")
        return p
    if not flip:
        p = qr_block(5340, p, cta_bg, False)
        p += f'<rect y="6780" width="{W}" height="{H-6780}" fill="{DEEP}"/>\n'
        p, C = about_block(7130, p)
        name = "banner_four_places_dark"
    else:
        # flipped: one continuous Linen section after the taller dark places band
        BAND_END = 2330 + 4 * 740
        p += f'<rect y="{BAND_END}" width="{W}" height="{H-BAND_END}" fill="{LINEN}"/>\n'
        S = BAND_END + 260
        B1 = S + 30 + G + 59
        B3 = B1 + 240
        C = B3 + G + 59
        p += (f'<text x="{W/2}" y="{S}" text-anchor="middle" font-family="DM Serif Display" font-size="150"><tspan fill="#3E807A">Shift </tspan><tspan fill="{DEEP}">Happens</tspan><tspan fill="{DEEP}" font-size="42" dy="-62">™</tspan></text>\n')
        p += lines(W / 2, B1, ["SOMA-Q IS A NERVOUS SYSTEM ALIGNMENT PRACTICE.", "WE TRAIN HIGH-PERFORMING LEADERS TO NOTICE STRESS", "SOONER, SHIFT IN THE MOMENT, AND RECOVER FASTER."], 84, 120, DEEP, weight="500", anchor="middle", ls="3")
        p += lines(W / 2, C, ["SOMA-Q.COM"], 84, 0, DEEP, weight="700", anchor="middle", ls="12")
        qs = 760; qy = C + 260
        p += f'<rect x="{W/2-qs/2}" y="{qy}" width="{qs}" height="{qs}" rx="42" fill="#FFFFFF" stroke="{DEEP}" stroke-width="10"/><svg x="{W/2-qs/2+60}" y="{qy+60}" width="{qs-120}" height="{qs-120}">{{{{QR_QUIZ}}}}</svg>'
        p += lines(W / 2, qy + qs + 270, ["Pressure happens."], 150, 0, DEEP, family="DM Serif Display", anchor="middle")
        p += lines(W / 2, qy + qs + 440, ["Take the free Burnout Signal Check."], 100, 0, "#3E807A", family="DM Serif Display", anchor="middle")
        name = "banner_four_places_dark_flip"
    p += TAIL
    (SRC / f"{name}.html").write_text(p)

banner("banner_four_places", LINEN, "#FFFFFF", "Linen", "light")
banner("banner_four_places_light", LIGHT, "#FFFFFF", "Light Teal", "light")
banner("banner_four_places_white", "#FFFFFF", LINEN, "White", "light")
banner("banner_four_places_dark", DEEP, LINEN, "Dark Teal", "dark", True)
banner("banner_four_places_dark_flip", DEEP, LINEN, "Dark Teal, flipped", "dark", True, True)
print("ok four places")
