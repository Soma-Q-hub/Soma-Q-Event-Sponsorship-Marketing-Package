"""SVG building blocks shared by posters, banners, backdrop and cards.
Each function returns (svg_inner, width, height) in local units (0.01 in at poster scale); callers place it with a
transform and set the viewBox. Colors come from the six-color Soma-Q palette only."""
import math

DEEP, LIGHT, PALE, LINEN, WHITE, INK = "#103C41", "#9BC4BD", "#E4F2F2", "#EEEADD", "#FEFCF8", "#24211D"
MUTED = "#5C5A53"

def _arrow(x1, y1, x2, y2, color, width=14, head=62):
    ang = math.atan2(y2 - y1, x2 - x1)
    bx, by = x2 - head * math.cos(ang), y2 - head * math.sin(ang)
    lx, ly = bx + head * 0.55 * math.sin(ang), by - head * 0.55 * math.cos(ang)
    rx, ry = bx - head * 0.55 * math.sin(ang), by + head * 0.55 * math.cos(ang)
    return (f'<line x1="{x1}" y1="{y1}" x2="{bx:.0f}" y2="{by:.0f}" stroke="{color}" stroke-width="{width}" stroke-linecap="round"/>'
            f'<polygon points="{x2},{y2} {lx:.0f},{ly:.0f} {rx:.0f},{ry:.0f}" fill="{color}"/>')

def loop(scheme="light", gloss=True):
    """The Pressure Loop, reading top to bottom: Something happens, then the three-step loop, with the interrupt point
    on the arrow between the trigger and the loop. Local box 2075 wide."""
    dark = scheme == "dark"
    nfill, ntxt, nsub = (WHITE, DEEP, INK) if dark else (DEEP, WHITE, PALE)
    arr = LIGHT if dark else DEEP
    pfill, pstroke, ptxt = ("none", LIGHT, WHITE) if dark else (WHITE, DEEP, DEEP)
    mid = PALE if dark else DEEP
    h = 400 if gloss else 300
    T = 540                       # top node y
    B = 1300 if gloss else 1180   # bottom nodes y
    def node(x, y, title, l1, l2):
        g = f'<rect x="{x}" y="{y}" width="825" height="{h}" rx="40" fill="{nfill}"/>'
        g += f'<text x="{x+412}" y="{y+(155 if gloss else 185)}" text-anchor="middle" font-family="DM Serif Display" font-size="88" fill="{ntxt}">{title}</text>'
        if gloss:
            g += f'<text x="{x+412}" y="{y+255}" text-anchor="middle" font-family="DM Sans" font-size="48" fill="{nsub}">{l1}</text>'
            g += f'<text x="{x+412}" y="{y+321}" text-anchor="middle" font-family="DM Sans" font-size="48" fill="{nsub}">{l2}</text>'
        return g
    o = ""
    # 1 Something happens (start), arrow, interrupt badge
    o += f'<rect x="562" y="0" width="900" height="190" rx="95" fill="{pfill}" stroke="{pstroke}" stroke-width="10"/>'
    o += f'<text x="1012" y="127" text-anchor="middle" font-family="DM Serif Display" font-size="72" fill="{ptxt}">Something happens</text>'
    o += _arrow(1012, 200, 1012, T - 12, arr)
    o += f'<line x1="1075" y1="{(190+T)//2}" x2="1250" y2="{(190+T)//2}" stroke="{LIGHT if dark else DEEP}" stroke-width="10" stroke-dasharray="26 20"/>'
    o += f'<rect x="1250" y="215" width="825" height="290" rx="40" fill="{LIGHT}"/>'
    o += f'<text x="1662" y="335" text-anchor="middle" font-family="DM Sans" font-weight="700" font-size="60" letter-spacing="5" fill="{DEEP}">INTERRUPT HERE</text>'
    o += f'<text x="1662" y="410" text-anchor="middle" font-family="DM Sans" font-size="46" fill="{DEEP}">Notice the tension,</text>'
    o += f'<text x="1662" y="465" text-anchor="middle" font-family="DM Sans" font-size="46" fill="{DEEP}">then choose</text>'
    # 2 the loop: Body tightens -> Mind speeds up -> You react -> back to Body tightens
    o += node(600, T, "Body tightens", "Jaw, shoulders, breath.", "Bracing without noticing")
    o += node(1250, B, "Mind speeds up", "Replaying, rehearsing,", "analyzing")
    o += node(0, B, "You react", "Words, tone,", "body language")
    o += _arrow(1370, T + h + 12, 1650, B - 14, arr)
    o += _arrow(1240, B + h // 2, 850, B + h // 2, arr)
    o += _arrow(380, B - 14, 650, T + h + 14, arr)
    cy = (T + h + B) // 2
    for i, t in enumerate(["Reaction feeds", "the tension that", "produced it."]):
        o += f'<text x="1012" y="{cy-40+i*64}" text-anchor="middle" font-family="DM Serif Display" font-style="italic" font-size="54" fill="{mid}">{t}</text>'
    return o, 2075, B + h

def outcomes(scheme="light"):
    """Three outcome circles inside the Soma-Q triangle, with a Q emblem at the center."""
    tri_stroke = LIGHT if scheme == "dark" else DEEP
    o = f'<polygon points="1000,0 2000,1732 0,1732" fill="none" stroke="{tri_stroke}" stroke-width="14" stroke-linejoin="round"/>'
    cx = {"t": (1000, 855), "l": (740, 1305), "r": (1260, 1305)}
    o += f'<circle cx="{cx["t"][0]}" cy="{cx["t"][1]}" r="330" fill="{DEEP}" fill-opacity=".95"/>'
    o += f'<circle cx="{cx["l"][0]}" cy="{cx["l"][1]}" r="330" fill="{LIGHT}" fill-opacity=".93"/>'
    o += f'<circle cx="{cx["r"][0]}" cy="{cx["r"][1]}" r="330" fill="{WHITE}" fill-opacity=".95" stroke="{DEEP}" stroke-width="8"/>'
    o += f'<text x="1000" y="735" text-anchor="middle" font-family="DM Serif Display" font-size="82" fill="{WHITE}">Restored</text><text x="1000" y="820" text-anchor="middle" font-family="DM Serif Display" font-size="82" fill="{WHITE}">energy</text>'
    o += f'<text x="715" y="1440" text-anchor="middle" font-family="DM Serif Display" font-size="76" fill="{DEEP}">Focused</text><text x="715" y="1520" text-anchor="middle" font-family="DM Serif Display" font-size="76" fill="{DEEP}">clarity</text>'
    o += f'<text x="1285" y="1440" text-anchor="middle" font-family="DM Serif Display" font-size="76" fill="{DEEP}">Joy and</text><text x="1285" y="1520" text-anchor="middle" font-family="DM Serif Display" font-size="76" fill="{DEEP}">fulfillment</text>'
    # center emblem: the Soma-Q triangle with a Q
    o += f'<polygon points="1000,985 1135,1215 865,1215" fill="{DEEP}" stroke="{WHITE}" stroke-width="10" stroke-linejoin="round"/>'
    o += f'<text x="1000" y="1190" text-anchor="middle" font-family="DM Serif Display" font-size="120" fill="{WHITE}">Q</text>'
    return o, 2000, 1732

def bodymap(scheme="light", labels=True, zones=True):
    """Front-view body outline with the six places pressure shows up first. Local box 2075 x 1850."""
    fill = WHITE
    o = f'<g fill="{fill}" stroke="{DEEP}" stroke-width="10" stroke-linejoin="round" transform="translate(-170,-1280)">'
    o += '<circle cx="1212" cy="1420" r="140"/><rect x="1152" y="1540" width="120" height="180" rx="40"/>'
    o += '<path d="M1010 1690 C890 1705 800 1740 800 1860 L800 2330 Q800 2410 880 2410 L1544 2410 Q1624 2410 1624 2330 L1624 1860 C1624 1740 1534 1705 1414 1690 Z"/>'
    o += '<rect x="670" y="1790" width="115" height="640" rx="57"/><rect x="1640" y="1790" width="115" height="640" rx="57"/>'
    o += '<rect x="895" y="2400" width="285" height="660" rx="60"/><rect x="1244" y="2400" width="285" height="660" rx="60"/></g>'
    if zones:
        zs = [(1212, 1475), (1212, 1670), (935, 1815), (1489, 1815), (1212, 2000), (1212, 2250), (1040, 2760), (1384, 2760)]
        for x, y in zs:
            o += f'<circle cx="{x-170}" cy="{y-1280}" r="76" fill="{LIGHT}" fill-opacity=".35" stroke="{DEEP}" stroke-width="7" stroke-dasharray="20 14"/>'
    if labels:
        L = [("left", 5, 1475, "Jaw", 1140, 1475), ("right", 2080, 1670, "Throat", 1290, 1670), ("left", 5, 1815, "Shoulders", 859, 1815),
             ("left", 5, 2000, "Chest", 1136, 2000), ("right", 2080, 2250, "Belly", 1288, 2250), ("right", 2080, 2760, "Legs", 1460, 2760)]
        for side, lx, ly, name, zx, zy in L:
            w = len(name) * 50 + 40
            x1 = lx + w if side == "left" else lx - w
            o += f'<line x1="{x1}" y1="{ly-1280-24}" x2="{zx-170}" y2="{zy-1280}" stroke="{DEEP}" stroke-width="5"/>'
            o += f'<text x="{lx}" y="{ly-1280}" text-anchor="{"start" if side == "left" else "end"}" font-family="DM Serif Display" font-size="88" fill="{DEEP}">{name}</text>'
    return o, 2075, 1790
