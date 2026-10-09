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

MEN_LOOP = {
    "top": "Something happens",
    "badge": ("INTERRUPT HERE", "Locate it in your body,", "then choose"),
    "n1": ("Body tightens", "Jaw, chest, gut.", "Bracing without noticing"),
    "n2": ("Mind goes to work", "Analyzing, fixing,", "comparing"),
    "n3": ("React or go quiet", "Short fuse,", "or silence"),
    "center": ["Trying to fix it", "feeds the loop", "that produced it."],
}
DEFAULT_LOOP = {
    "top": "Something happens",
    "badge": ("INTERRUPT HERE", "Notice the tension,", "then choose"),
    "n1": ("Body tightens", "Jaw, shoulders, breath.", "Bracing without noticing"),
    "n2": ("Mind speeds up", "Replaying, rehearsing,", "analyzing"),
    "n3": ("You react", "Words, tone,", "body language"),
    "center": ["Reaction feeds", "the tension that", "produced it."],
}
DEFAULT_OUTCOMES = [("Restored", "energy", 82), ("Focused", "clarity", 76), ("Joy and", "fulfillment", 76)]
MEN_OUTCOMES = [("Steady under", "pressure", 82), ("Clear when", "it counts", 76), ("Present at home", "and at work", 62)]

def loop(scheme="light", gloss=True, words=None):
    """The Pressure Loop, reading top to bottom: Something happens, then the three-step loop, with the interrupt point
    on the arrow between the trigger and the loop. Local box 2075 wide."""
    W = words or DEFAULT_LOOP
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
    o += f'<text x="1012" y="127" text-anchor="middle" font-family="DM Serif Display" font-size="72" fill="{ptxt}">{W["top"]}</text>'
    o += _arrow(1012, 200, 1012, T - 12, arr)
    o += f'<line x1="1075" y1="{(190+T)//2}" x2="1250" y2="{(190+T)//2}" stroke="{LIGHT if dark else DEEP}" stroke-width="10" stroke-dasharray="26 20"/>'
    o += f'<rect x="1250" y="215" width="825" height="290" rx="40" fill="{LIGHT}"/>'
    o += f'<text x="1662" y="335" text-anchor="middle" font-family="DM Sans" font-weight="700" font-size="60" letter-spacing="5" fill="{DEEP}">{W["badge"][0]}</text>'
    o += f'<text x="1662" y="410" text-anchor="middle" font-family="DM Sans" font-size="46" fill="{DEEP}">{W["badge"][1]}</text>'
    o += f'<text x="1662" y="465" text-anchor="middle" font-family="DM Sans" font-size="46" fill="{DEEP}">{W["badge"][2]}</text>'
    # 2 the loop: Body tightens -> Mind speeds up -> You react -> back to Body tightens
    o += node(600, T, *W["n1"])
    o += node(1250, B, *W["n2"])
    o += node(0, B, *W["n3"])
    o += _arrow(1370, T + h + 12, 1650, B - 14, arr)
    o += _arrow(1240, B + h // 2, 850, B + h // 2, arr)
    o += _arrow(380, B - 14, 650, T + h + 14, arr)
    cy = (T + h + B) // 2
    for i, t in enumerate(W["center"]):
        o += f'<text x="1012" y="{cy-40+i*64}" text-anchor="middle" font-family="DM Serif Display" font-style="italic" font-size="54" fill="{mid}">{t}</text>'
    return o, 2075, B + h

def outcomes(scheme="light", labels=None):
    """Three outcome circles inside the Soma-Q triangle, with a Q emblem at the center."""
    tri_stroke = LIGHT if scheme == "dark" else DEEP
    o = f'<polygon points="1000,0 2000,1732 0,1732" fill="none" stroke="{tri_stroke}" stroke-width="14" stroke-linejoin="round"/>'
    cx = {"t": (1000, 855), "l": (740, 1305), "r": (1260, 1305)}
    o += f'<circle cx="{cx["t"][0]}" cy="{cx["t"][1]}" r="330" fill="{DEEP}" fill-opacity=".95"/>'
    o += f'<circle cx="{cx["l"][0]}" cy="{cx["l"][1]}" r="330" fill="{LIGHT}" fill-opacity=".93"/>'
    o += f'<circle cx="{cx["r"][0]}" cy="{cx["r"][1]}" r="330" fill="{WHITE}" fill-opacity=".95" stroke="{DEEP}" stroke-width="8"/>'
    L = labels or DEFAULT_OUTCOMES
    def lab(x, y, pair, fill, size):
        return "".join(f'<text x="{x}" y="{y+k*(size+6)}" text-anchor="middle" font-family="DM Serif Display" font-size="{size}" fill="{fill}">{t}</text>' for k, t in enumerate(pair))
    o += lab(1000, 735, L[0][:2], WHITE, L[0][2])
    o += lab(715, 1440, L[1][:2], DEEP, L[1][2])
    o += lab(1285, 1440, L[2][:2], DEEP, L[2][2])
    # center emblem: the solid Soma-Q triangle from the logo, no letter (the Q is already in the logo; a letter did not
    # scale inside a triangle this small)
    o += f'<polygon points="1000,990 1150,1240 850,1240" fill="{DEEP}" stroke="{WHITE}" stroke-width="12" stroke-linejoin="round"/>\n'
    return o, 2000, 1732

def _mirror_path(right, cx):
    """right = [start, (c1, c2, p), ...] describing the right-hand outer contour from the crown down to the crotch
    (dx offsets from the centerline). Returns one closed SVG path: right side down, mirrored left side back up."""
    def X(dx, s=1): return cx + s * dx
    start, segs = right[0], right[1:]
    d = f"M{X(start[0])},{start[1]}"
    for c1, c2, p in segs:
        d += f" C{X(c1[0])},{c1[1]} {X(c2[0])},{c2[1]} {X(p[0])},{p[1]}"
    anchors = [start] + [s[2] for s in segs]
    for k in range(len(segs) - 1, -1, -1):
        c1, c2, _ = segs[k]
        prev = anchors[k]
        d += f" C{X(c2[0], -1)},{c2[1]} {X(c1[0], -1)},{c1[1]} {X(prev[0], -1)},{prev[1]}"
    return d + " Z"

def bodymap(scheme="light", labels=True, zones=True):
    """Front-view neutral human figure with the nervous system drawn through it (brain, spinal cord, nerves to the arms
    and legs), plus the places pressure shows up first. Original drawing in the Soma-Q palette; sized for a 3/4 in
    sticker. Local box 2075 x 1790."""
    cx = 1212
    R = [(0, 1280),
         ((52, 1280), (96, 1322), (96, 1385)), ((96, 1432), (82, 1458), (66, 1478)), ((56, 1490), (48, 1500), (46, 1515)),
         ((46, 1560), (48, 1588), (62, 1600)), ((110, 1612), (170, 1618), (205, 1640)), ((232, 1655), (250, 1690), (252, 1735)),
         ((262, 1800), (290, 1900), (330, 2010)), ((345, 2050), (365, 2100), (385, 2160)), ((398, 2200), (412, 2250), (425, 2290)),
         ((432, 2310), (440, 2335), (436, 2352)), ((428, 2372), (410, 2368), (404, 2350)),
         ((392, 2310), (372, 2260), (348, 2210)), ((330, 2170), (306, 2120), (286, 2070)), ((262, 2010), (220, 1920), (190, 1840)),
         ((178, 1815), (172, 1800), (168, 1790)),
         ((160, 1850), (150, 1930), (146, 2000)), ((146, 2050), (156, 2100), (166, 2150)),
         ((176, 2200), (180, 2250), (176, 2300)), ((172, 2400), (164, 2480), (148, 2560)), ((136, 2630), (128, 2680), (126, 2720)),
         ((130, 2790), (134, 2850), (120, 2920)), ((110, 2960), (100, 2985), (94, 3005)), ((96, 3030), (130, 3040), (150, 3054)),
         ((152, 3068), (44, 3068), (36, 3050)), ((30, 3020), (34, 2990), (38, 2960)), ((44, 2900), (40, 2840), (34, 2780)),
         ((30, 2730), (34, 2680), (36, 2640)), ((36, 2520), (20, 2380), (8, 2260)), ((4, 2230), (2, 2210), (0, 2200))]
    body = _mirror_path(R, cx)
    glow = f'fill="none" stroke="{LIGHT}" stroke-opacity=".55" stroke-linecap="round" stroke-linejoin="round"'
    nerve = f'fill="none" stroke="{DEEP}" stroke-opacity=".85" stroke-linecap="round" stroke-linejoin="round"'
    # one side of the peripheral nerves (drawn at +dx, mirrored for the other side)
    arm = f"M{cx+30},1650 C{cx+120},1655 {cx+200},1690 {cx+250},1790 C{cx+275},1880 {cx+290},1950 {cx+305},2010 C{cx+330},2090 {cx+370},2200 {cx+408},2310"
    arm_b = [f"M{cx+408},2310 L{cx+428},2346", f"M{cx+408},2310 L{cx+414},2350", f"M{cx+395},2290 L{cx+396},2335"]
    leg = f"M{cx+8},2100 C{cx+50},2150 {cx+82},2230 {cx+92},2400 C{cx+100},2540 {cx+96},2700 {cx+94},2860 C{cx+92},2940 {cx+86},2990 {cx+78},3030"
    leg_b = [f"M{cx+84},3000 L{cx+120},3046", f"M{cx+84},3000 L{cx+96},3052", f"M{cx+84},3000 L{cx+62},3050"]
    side = "".join(f'<path d="{d}" {glow} stroke-width="16"/>' for d in [arm, leg]) + "".join(f'<path d="{d}" {nerve} stroke-width="5"/>' for d in [arm, leg]) + "".join(f'<path d="{d}" {nerve} stroke-width="3.5" stroke-opacity=".6"/>' for d in arm_b + leg_b)
    for y in range(1680, 2100, 46):      # intercostal branches following the ribs
        wd = 128 - (y - 1680) * 0.045
        side += f'<path d="M{cx+14},{y} C{cx+66},{y-4} {cx+104},{y+10} {cx+wd:.0f},{y+44}" {nerve} stroke-width="3.5" stroke-opacity=".38"/>'
    o = f'<defs><radialGradient id="zg" cx="50%" cy="50%" r="50%"><stop offset="0" stop-color="{LIGHT}" stop-opacity=".95"/><stop offset="1" stop-color="{LIGHT}" stop-opacity=".30"/></radialGradient></defs>'
    o += '<g transform="translate(-170,-1280)">'
    o += f'<path d="{body}" fill="{WHITE}" fill-opacity=".72" stroke="{DEEP}" stroke-width="7" stroke-linejoin="round"/>'
    o += f'<path d="M{cx+66},1472 C{cx+54},1500 {cx+26},1522 {cx},1524 C{cx-26},1522 {cx-54},1500 {cx-66},1472" fill="none" stroke="{DEEP}" stroke-opacity=".3" stroke-width="5" stroke-linecap="round"/>'
    # brain
    o += f'<path d="M{cx},1300 C{cx+58},1296 {cx+86},1334 {cx+80},1376 C{cx+74},1414 {cx+34},1428 {cx},1426 C{cx-34},1428 {cx-74},1414 {cx-80},1376 C{cx-86},1334 {cx-58},1296 {cx},1300 Z" fill="{LIGHT}" fill-opacity=".6" stroke="{DEEP}" stroke-width="5"/>'
    o += f'<path d="M{cx},1304 L{cx},1424 M{cx-56},1340 C{cx-36},1352 {cx-30},1372 {cx-48},1392 M{cx+56},1340 C{cx+36},1352 {cx+30},1372 {cx+48},1392 M{cx-70},1372 C{cx-50},1378 {cx-40},1396 {cx-44},1416 M{cx+70},1372 C{cx+50},1378 {cx+40},1396 {cx+44},1416" {nerve} stroke-width="3.5" stroke-opacity=".55"/>'
    # spinal cord with vertebral segments
    o += f'<path d="M{cx},1424 L{cx},2110" {glow} stroke-width="22"/><path d="M{cx},1424 L{cx},2110" {nerve} stroke-width="7"/>'
    for y in range(1560, 2100, 36):
        o += f'<rect x="{cx-17}" y="{y}" width="34" height="13" rx="6" fill="{WHITE}" stroke="{DEEP}" stroke-opacity=".8" stroke-width="3"/>'
    o += f'<g>{side}</g><g transform="translate({2*cx},0) scale(-1,1)">{side}</g>'
    if zones:
        zs = [(cx, 1482, 50), (cx, 1592, 50), (cx - 135, 1700, 66), (cx + 135, 1700, 66), (cx, 1820, 68), (cx, 2050, 70), (cx - 82, 2420, 70), (cx + 82, 2420, 70)]
        for x, y, r in zs:
            o += f'<circle cx="{x}" cy="{y}" r="{r}" fill="url(#zg)" stroke="{DEEP}" stroke-width="5"/><circle cx="{x}" cy="{y}" r="9" fill="{DEEP}"/>'
    if labels:
        L = [("l", cx, 1482, 50, "Jaw"), ("l", cx - 135, 1700, 66, "Shoulders"), ("l", cx, 2050, 70, "Belly"),
             ("r", cx, 1592, 50, "Throat"), ("r", cx, 1820, 68, "Chest"), ("r", cx + 82, 2420, 70, "Legs")]
        for side_, zx, zy, zr, name in L:
            lx = cx - 480 if side_ == "l" else cx + 480
            ex = zx - zr if side_ == "l" else zx + zr
            o += f'<line x1="{lx + (12 if side_ == "l" else -12)}" y1="{zy}" x2="{ex}" y2="{zy}" stroke="{DEEP}" stroke-width="5"/>'
            o += f'<text x="{lx}" y="{zy+30}" text-anchor="{"end" if side_ == "l" else "start"}" font-family="DM Serif Display" font-size="88" fill="{DEEP}">{name}</text>'
    o += '</g>'
    return o, 2075, 1790
