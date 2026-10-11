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


_FIG_R = [(0, 1280),
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

def nervous_figure_old(scheme="dark"):
    """The neutral figure with the nervous system drawn through it, no zone markers or labels: a hero image.
    scheme 'dark' = Light Teal lines for a Deep Teal field; 'light' = Deep Teal lines for a light field. Local box 880 x 1790."""
    cx = 440 + 0
    if scheme == "dark":
        fill, fill_op, stroke, nerve, glow, glow_op, brain, vert_fill = WHITE, ".07", LIGHT, LIGHT, PALE, ".28", LIGHT, DEEP
    else:
        fill, fill_op, stroke, nerve, glow, glow_op, brain, vert_fill = WHITE, ".72", DEEP, DEEP, LIGHT, ".55", LIGHT, WHITE
    cxr = 1212   # figure is drawn around x = 1212 in its source coordinates
    body = _mirror_path(_FIG_R, cxr)
    g = f'fill="none" stroke="{glow}" stroke-opacity="{glow_op}" stroke-linecap="round" stroke-linejoin="round"'
    n = f'fill="none" stroke="{nerve}" stroke-opacity=".95" stroke-linecap="round" stroke-linejoin="round"'
    arm = f"M{cxr+30},1650 C{cxr+120},1655 {cxr+200},1690 {cxr+250},1790 C{cxr+275},1880 {cxr+290},1950 {cxr+305},2010 C{cxr+330},2090 {cxr+370},2200 {cxr+408},2310"
    arm_b = [f"M{cxr+408},2310 L{cxr+428},2346", f"M{cxr+408},2310 L{cxr+414},2350", f"M{cxr+395},2290 L{cxr+396},2335"]
    leg = f"M{cxr+8},2100 C{cxr+50},2150 {cxr+82},2230 {cxr+92},2400 C{cxr+100},2540 {cxr+96},2700 {cxr+94},2860 C{cxr+92},2940 {cxr+86},2990 {cxr+78},3030"
    leg_b = [f"M{cxr+84},3000 L{cxr+120},3046", f"M{cxr+84},3000 L{cxr+96},3052", f"M{cxr+84},3000 L{cxr+62},3050"]
    side = "".join(f'<path d="{d}" {g} stroke-width="20"/>' for d in [arm, leg]) + "".join(f'<path d="{d}" {n} stroke-width="7"/>' for d in [arm, leg]) + "".join(f'<path d="{d}" {n} stroke-width="5" stroke-opacity=".7"/>' for d in arm_b + leg_b)
    for y in range(1680, 2100, 46):
        wd = 128 - (y - 1680) * 0.045
        side += f'<path d="M{cxr+14},{y} C{cxr+66},{y-4} {cxr+104},{y+10} {cxr+wd:.0f},{y+44}" {n} stroke-width="5" stroke-opacity=".5"/>'
    o = '<g transform="translate(-772,-1280)">'
    o += f'<path d="{body}" fill="{fill}" fill-opacity="{fill_op}" stroke="{stroke}" stroke-width="9" stroke-linejoin="round"/>'
    o += (f'<path d="M{cxr},1300 C{cxr+58},1296 {cxr+86},1334 {cxr+80},1376 C{cxr+74},1414 {cxr+34},1428 {cxr},1426 C{cxr-34},1428 {cxr-74},1414 {cxr-80},1376 '
          f'C{cxr-86},1334 {cxr-58},1296 {cxr},1300 Z" fill="{brain}" fill-opacity=".45" stroke="{nerve}" stroke-width="7"/>')
    o += f'<path d="M{cxr},1304 L{cxr},1424 M{cxr-56},1340 C{cxr-36},1352 {cxr-30},1372 {cxr-48},1392 M{cxr+56},1340 C{cxr+36},1352 {cxr+30},1372 {cxr+48},1392" {n} stroke-width="5" stroke-opacity=".6"/>'
    o += f'<path d="M{cxr},1424 L{cxr},2110" {g} stroke-width="30"/><path d="M{cxr},1424 L{cxr},2110" {n} stroke-width="10"/>'
    for y in range(1560, 2100, 36):
        o += f'<rect x="{cxr-17}" y="{y}" width="34" height="13" rx="6" fill="{vert_fill}" stroke="{nerve}" stroke-width="4"/>'
    o += f'<g>{side}</g><g transform="translate({2*cxr},0) scale(-1,1)">{side}</g></g>'
    return o, 880, 1790


def nervous_figure(scheme="dark"):
    """Neutral, androgynous figure (near-straight torso, same shoulder and hip width) with the nervous system lit from inside:
    brain, spinal cord, vagus, brachial and lumbar plexus, branching peripheral nerves, soft white glow. Local box 880 x 1790."""
    dark = scheme == "dark"
    if dark:
        edge, body, core, halo, halo2, node = LIGHT, "#17474D", WHITE, PALE, LIGHT, WHITE
    else:
        edge, body, core, halo, halo2, node = DEEP, "#FBFAF6", DEEP, LIGHT, LIGHT, DEEP
    cx = 440
    def mir(d_fn):
        return d_fn(1) + d_fn(-1)
    # ---- silhouette: all outlines first, then all fills, so limbs merge into one shape ----
    parts = []   # (kind, attrs)
    limbs = []
    limbs.append(f'<path d="M{cx-232},390 C{cx-232},325 {cx-140},296 {cx-44},292 L{cx+44},292 C{cx+140},296 {cx+232},325 {cx+232},390 C{cx+222},560 {cx+206},640 {cx+200},720 C{cx+198},850 {cx+206},930 {cx+206},1010 L{cx-206},1010 C{cx-206},930 {cx-198},850 {cx-200},720 C{cx-206},640 {cx-222},560 {cx-232},390 Z"')
    limbs.append(f'<rect x="{cx-44}" y="190" width="88" height="130"')
    limbs.append(f'<ellipse cx="{cx}" cy="112" rx="82" ry="106"')
    for sg in (1, -1):
        limbs.append(f'<path d="M{cx+sg*215},355 L{cx+sg*300},1050" fill="none" stroke-width="96" stroke-linecap="round"')
        limbs.append(f'<ellipse cx="{cx+sg*316}" cy="1130" rx="42" ry="74"')
        limbs.append(f'<path d="M{cx+sg*105},980 L{cx+sg*105},1700" fill="none" stroke-width="164" stroke-linecap="round"')
        limbs.append(f'<ellipse cx="{cx+sg*112}" cy="1738" rx="96" ry="44"')
    o = ""
    for l in limbs:   # outline pass
        w = "" if "stroke-width" in l else ' fill="none"'
        if "stroke-width" in l:
            import re as _re
            wd = int(_re.search(r'stroke-width="(\d+)"', l).group(1)) + 20
            o += _re.sub(r'stroke-width="\d+"', f'stroke-width="{wd}"', l) + f' stroke="{edge}" stroke-linejoin="round"/>'
        else:
            o += l + f' fill="{edge}" stroke="{edge}" stroke-width="20" stroke-linejoin="round"/>'
    for l in limbs:   # fill pass
        if "stroke-width" in l:
            o += l + f' stroke="{body}" stroke-linejoin="round"/>'
        else:
            o += l + f' fill="{body}" stroke="{body}" stroke-width="2"/>'
    def glow(d, w, op=1):
        return (f'<path d="{d}" fill="none" stroke="{halo2}" stroke-opacity=".16" stroke-width="{w*4.2:.0f}" stroke-linecap="round" stroke-linejoin="round"/>'
                f'<path d="{d}" fill="none" stroke="{halo}" stroke-opacity=".34" stroke-width="{w*2.2:.0f}" stroke-linecap="round" stroke-linejoin="round"/>'
                f'<path d="{d}" fill="none" stroke="{core}" stroke-opacity="{op}" stroke-width="{w}" stroke-linecap="round" stroke-linejoin="round"/>')
    # soft light pools (the light inside the body)
    o += (f'<defs><radialGradient id="fgl"><stop offset="0" stop-color="{core}" stop-opacity=".55"/><stop offset=".5" stop-color="{halo}" stop-opacity=".22"/>'
          f'<stop offset="1" stop-color="{halo}" stop-opacity="0"/></radialGradient></defs>')
    for (px, py, r) in [(cx, 120, 190), (cx, 520, 250), (cx, 820, 240), (cx - 215, 700, 120), (cx + 215, 700, 120), (cx - 105, 1350, 130), (cx + 105, 1350, 130)]:
        o += f'<circle cx="{px}" cy="{py}" r="{r}" fill="url(#fgl)"/>'
    # spinal cord
    o += glow(f"M{cx},212 L{cx},1000", 12)
    # brain
    o += (f'<ellipse cx="{cx}" cy="112" rx="58" ry="66" fill="{halo}" fill-opacity=".30" stroke="{core}" stroke-width="7"/>'
          f'<path d="M{cx},50 L{cx},172 M{cx-44},80 C{cx-20},96 {cx-18},128 {cx-40},148 M{cx+44},80 C{cx+20},96 {cx+18},128 {cx+40},148" fill="none" stroke="{core}" stroke-width="5" stroke-opacity=".8"/>')
    # vagus nerves: brain stem, down the neck, to heart and gut
    for sg in (1, -1):
        o += glow(f"M{cx+sg*16},196 C{cx+sg*60},250 {cx+sg*96},330 {cx+sg*96},440 C{cx+sg*96},560 {cx+sg*70},640 {cx+sg*18},760", 6, .95)
    # brachial plexus into the arms, then the fingers
    for sg in (1, -1):
        o += glow(f"M{cx},360 C{cx+sg*90},340 {cx+sg*190},360 {cx+sg*230},430 C{cx+sg*262},560 {cx+sg*290},800 {cx+sg*302},1050", 7, .95)
        for dx in (-26, 0, 26):
            o += glow(f"M{cx+sg*302},1050 C{cx+sg*308},1090 {cx+sg*(316+dx)},1130 {cx+sg*(318+dx*1.5):.0f},1180", 4, .85)
    # peripheral branches: irregular forks off the cord, not evenly spaced
    for y, ln, sg in [(430, 120, 1), (470, 90, -1), (560, 150, 1), (600, 110, -1), (680, 170, -1), (720, 120, 1), (800, 150, 1), (850, 120, -1), (910, 100, 1)]:
        ex, ey = cx + sg * ln, y + 60
        o += glow(f"M{cx},{y} C{cx+sg*ln*.4:.0f},{y-8} {cx+sg*ln*.8:.0f},{y+14} {ex},{ey}", 4, .8)
        o += f'<path d="M{cx+sg*ln*.7:.0f},{y+22} L{ex+sg*34},{ey+8} M{cx+sg*ln*.7:.0f},{y+22} L{ex+sg*14},{ey+44}" fill="none" stroke="{core}" stroke-width="3" stroke-opacity=".75" stroke-linecap="round"/>'
    # lumbar and sacral plexus into the legs
    for sg in (1, -1):
        o += glow(f"M{cx},990 C{cx+sg*40},1030 {cx+sg*100},1070 {cx+sg*106},1180 C{cx+sg*110},1360 {cx+sg*108},1540 {cx+sg*106},1690", 8, .95)
        for dx in (-30, 0, 30):
            o += glow(f"M{cx+sg*106},1690 C{cx+sg*(108+dx*.4):.0f},1712 {cx+sg*(110+dx):.0f},1730 {cx+sg*(112+dx*1.4):.0f},1752", 4, .8)
    # plexus nodes (ganglia) that glow
    for px, py, r in [(cx, 360, 16), (cx, 760, 18), (cx, 990, 16), (cx - 96, 440, 9), (cx + 96, 440, 9)]:
        o += f'<circle cx="{px}" cy="{py}" r="{r*2.2:.0f}" fill="{halo}" fill-opacity=".30"/><circle cx="{px}" cy="{py}" r="{r}" fill="{node}"/>'
    return f'<g transform="translate(0,0)">{o}</g>', 880, 1790
