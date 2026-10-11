#!/usr/bin/env python3
"""System v3 banners (men's and consumer wording). One story across the set: 1 THE TENSION (name the pain), 2 THE CAPACITY
(practices are the tools, capacity is the product; the loop and where to interrupt it; metrics). Same header, same
Burnout ends here ribbon, same What we do footer on every banner. Sources: website v2 pages (problem boxes, metrics report).
Run: python3 build/make_system_banners.py"""
from svgkit import *
from svgkit import head as head_

W, H = 3300, 8100
WHAT_WE_DO = ["Soma-Q is a nervous system alignment practice. We train", "high-performing leaders to notice stress sooner, shift", "in the moment and recover faster."]
PROBLEMS = [("DEPLETION", "Running on empty, and calling it normal."),
            ("DECISIONS", "Choices made from pressure, not clarity."),
            ("COMMUNICATION", "Short with the people you love."),
            ("RESOURCES", "You know what to do. You can’t reach it.")]
METRICS = [("Stress recovery", 7.4, 3.8), ("Emotional steadiness", 7.1, 3.5), ("Clear thinking", 7.8, 4.1)]

def chrome(title, note):
    p = head_(f"{title}, 32 x 80 in", 33, 81, note)
    p += f'<rect width="{W}" height="{H}" fill="{LINEN}"/>\n'
    return p

def header(p):
    p += f'<rect width="{W}" height="700" fill="{DEEP}"/>\n' + logo(250, 170, 1050, True)
    p += lines(3050, 320, ["NERVOUS SYSTEM ALIGNMENT", "FOR HIGH-PERFORMING LEADERS"], 90, 140, WHITE, weight="700", anchor="end", ls="3")
    p += f'<rect y="700" width="{W}" height="330" fill="{LIGHT}"/>\n'
    if V == "shift":
        p += lines(250, 905, ["SHIFT HAPPENS™"], 150, 0, DEEP, weight="700", ls="16")
        p += lines(3050, 850, ["BECOME YOUR", "OWN ADVISOR."], 72, 90, DEEP, weight="700", anchor="end", ls="6")
    else:
        p += lines(250, 905, ["BURNOUT ENDS HERE.™"], 150, 0, DEEP, weight="700", ls="16")
    return p

def footer(p, y=5700):
    p += hair(250, 3050, y)
    p += label(250, y + 200, "", "WHAT WE DO", 64)
    p += lines(250, y + 360, WHAT_WE_DO, 100, 130, INK)
    p += lines(250, y + 860, ["Book a free", "discovery call."], 130, 150, DEEP, family="DM Serif Display")
    p += lines(250, y + 1210, ["An honest conversation about what pressure", "is costing you. No obligation."], 66, 90, INK, weight="500")
    p += f'<rect x="2330" y="{y + 640}" width="720" height="720" rx="40" fill="#FFFFFF" stroke="{DEEP}" stroke-width="10"/><svg x="2400" y="{y + 710}" width="580" height="580">{{{{QR_CALL}}}}</svg>'
    p += lines(250, y + 1480, ["SOMA-Q.COM"], 90, 0, DEEP, weight="700", ls="12")
    return p

for V, SUF in (("burnout", ""), ("shift", "_shift")):
    # ============================ 1 THE TENSION ============================
    p = chrome("System v3, banner 1: the tension", "Retractable banner 32 x 80 in trim, file 33 x 81 in (0.5 in bleed). Banner 1 of 2: name the pain. Everything key sits above the 54 in line; the footer is close-range. CONFIRM the vendor template.")
    p = header(p)
    p += f'<rect y="1030" width="{W}" height="2200" fill="{DEEP}"/>\n'
    p += lines(250, 1540, ["Everyone", "around you", "can feel", "your stress."], 225, 245, WHITE, family="DM Serif Display")
    p += lines(250, 2540, ["What do you do next?"], 150, 0, LIGHT, family="DM Serif Display")
    p += lines(250, 2860, ["It isn’t a character flaw.", "It’s a stress response, and", "you can learn to work with it."], 88, 120, WHITE, weight="500")
    p += placed("{{FIGURE:dark}}", 2130, 1100, 1.12)
    for i, (tag, line) in enumerate(PROBLEMS):
        y = 3380 + i * 480
        p += f'<rect x="250" y="{y}" width="2800" height="440" rx="36" fill="{WHITE}"/><rect x="250" y="{y}" width="2800" height="16" rx="8" fill="{DEEP}"/>\n'
        p += lines(340, y + 130, [tag], 60, 0, DEEP, weight="700", ls="8")
        p += lines(340, y + 305, [line], 122, 0, INK, family="DM Serif Display")
    p = footer(p, 5600)
    p += TAIL
    (SRC / f"banner_sys_tension{SUF}.html").write_text(p)

    # ============================ 2 THE CAPACITY ============================
    p = chrome("System v3, banner 2: the capacity", "Retractable banner 32 x 80 in trim, file 33 x 81 in (0.5 in bleed). Banner 2 of 2: the resolution. Practices are the tools, steadiness is the product; the loop and where to interrupt it, large. CONFIRM the vendor template.")
    p = header(p)
    p += f'<rect y="1030" width="{W}" height="2260" fill="{DEEP}"/>\n'
    p += lines(250, 1560, ["Practices are", "the tools.", "Steadiness is", "the product."], 380, 368, WHITE, family="DM Serif Display")
    p += lines(250, 2900, ["Regulation is a skill.", "Recovery is a skill.", "Choice under pressure is a skill."], 92, 124, WHITE, weight="500")
    p += label(250, 3440, "", "THE STRESS LOOP, AND WHERE TO INTERRUPT IT", 58)
    p += placed("{{LOOP:light:nogloss:men}}", 250, 3540, 1.35)
    p = footer(p, 5800)
    p += TAIL
    (SRC / f"banner_sys_capacity{SUF}.html").write_text(p)

print("ok system")
