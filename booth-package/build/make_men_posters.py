#!/usr/bin/env python3
"""Men's track explainer posters: nervous system literacy from two lenses, the one who solves everything and the one who
holds space for everyone. Same brand system as the main posters. Copy rules: outcome first, composed sentences, no hype,
no em dashes, no energy language, no client details. Science lines are hedged and map to Verified rows in the citations
master (see men-track/CONCEPT.md). Run: python3 build/make_men_posters.py"""
from posterkit import *

# 1) the one who solves everything ---------------------------------------------------------------------------------
b = f'<rect width="2425" height="3625" fill="{LINEN}"/>\n' + eyebrow(175, 330, "NERVOUS SYSTEM LITERACY")
b += lines(175, 560, ["Stay steady when", "there is nothing", "to solve."], 176, 178, DEEP, family="DM Serif Display")
b += lines(175, 1090, ["You were taught to be the one who figures it out. That is a real", "strength, and under pressure it can become a loop: the mind keeps", "working while the body keeps running its alarm."], 56, 70, INK)
for x, title, items in [(175, "THE MIND", ["Analyzing", "Comparing", "Planning the fix", "Looking for what is wrong"]),
                        (1255, "THE BODY", ["Jaw set", "Chest tight", "Gut clenched", "Shoulders braced"])]:
    b += f'<rect x="{x}" y="1400" width="995" height="600" rx="50" fill="{WHITE}" stroke="{DEEP}" stroke-width="8"/>\n'
    b += lines(x + 70, 1520, [title], 54, 0, DEEP, weight="700") .replace('<text', '<text letter-spacing="9"')
    for i, it in enumerate(items):
        y = 1650 + i * 90
        b += f'<polygon points="{x+70},{y} {x+100},{y-52} {x+130},{y}" fill="{DEEP}"/>' + lines(x + 170, y, [it], 62, 0, INK)
b += lines(1212, 2130, ["More thinking rarely settles what the body is still running."], 58, 0, DEEP, family="DM Serif Display", style="italic", anchor="middle")
b += f'<line x1="175" y1="2260" x2="2250" y2="2260" stroke="{DEEP}" stroke-opacity=".28" stroke-width="8"/>\n'
b += lines(250, 2370, ["A DIFFERENT MOVE"], 54, 0, DEEP, weight="700").replace('<text', '<text letter-spacing="9"')
for i, (t, d1, d2) in enumerate([("Locate it", "Where is it in", "your body?"), ("Describe it", "Heat, pressure,", "tightness, buzzing?"), ("Settle it", "Feet on the floor,", "one slow exhale.")]):
    x = 250 + i * 690
    b += f'<circle cx="{x+60}" cy="2530" r="60" fill="{DEEP}"/><text x="{x+60}" y="2554" text-anchor="middle" font-family="DM Serif Display" font-size="70" fill="{WHITE}">{i+1}</text>\n'
    b += lines(x + 150, 2555, [t], 84, 0, DEEP, family="DM Serif Display") + lines(x, 2680, [d1, d2], 52, 66, INK)
b += lines(1212, 2880, ["You still solve the problem. You solve it from steady, not from alarm."], 52, 0, DEEP, family="DM Serif Display", style="italic", anchor="middle")
b += "{{FOOTER:light}}\n"
write("poster_men_fixer", "Men's track poster: Stay steady when there is nothing to solve", b)

# 2) the one who holds space for everyone ---------------------------------------------------------------------------
b = f'<rect width="2425" height="3625" fill="{PALE}"/>\n' + eyebrow(175, 330, "NERVOUS SYSTEM LITERACY")
b += lines(175, 560, ["Hold space for", "others without", "losing touch", "with yourself."], 176, 178, DEEP, family="DM Serif Display")
b += lines(175, 1270, ["Partners, colleagues and family bring you their feelings, and you carry them", "well. Your own signals are often the quietest in the room, because many", "men were never taught to listen for them."], 54, 68, INK)
b += lines(175, 1560, ["WHAT YOU CARRY"], 50, 0, DEEP, weight="700").replace('<text', '<text letter-spacing="9"')
b += lines(2250, 1560, ["WHAT GOES QUIET"], 50, 0, DEEP, weight="700", anchor="end").replace('<text', '<text letter-spacing="9"')
for i, t in enumerate(["Her stress", "The team's worry", "The family's needs", "A friend's hard week"]):
    y = 1620 + i * 170
    b += f'<rect x="175" y="{y}" width="760" height="130" rx="65" fill="{WHITE}" stroke="{DEEP}" stroke-width="7"/>\n' + lines(250, y + 87, [t], 56, 0, INK)
    b += f'<line x1="945" y1="{y+65}" x2="1090" y2="{1850 + (y+65-1850)*0.35:.0f}" stroke="{DEEP}" stroke-width="12" stroke-linecap="round"/>\n'
b += f'<circle cx="1260" cy="1850" r="210" fill="{DEEP}"/>' + lines(1260, 1905, ["You"], 150, 0, WHITE, family="DM Serif Display", anchor="middle")
b += f'<line x1="1480" y1="1850" x2="1830" y2="1850" stroke="{DEEP}" stroke-opacity=".5" stroke-width="8" stroke-dasharray="22 18"/>\n'
b += f'<circle cx="2000" cy="1850" r="150" fill="{LIGHT}" fill-opacity=".35" stroke="{DEEP}" stroke-opacity=".6" stroke-width="7" stroke-dasharray="22 16"/>\n'
b += lines(2000, 1850, ["Your own"], 50, 60, DEEP, anchor="middle", weight="500").replace('y="1850"', 'y="1840"') + lines(2000, 1905, ["signal"], 50, 0, DEEP, anchor="middle", weight="500")
b += lines(1212, 2440, ["Easy to miss when you are busy holding everything else."], 58, 0, DEEP, family="DM Serif Display", style="italic", anchor="middle")
b += f'<line x1="175" y1="2560" x2="2250" y2="2560" stroke="{DEEP}" stroke-opacity=".28" stroke-width="8"/>\n'
b += lines(250, 2670, ["A 30-SECOND CHECK-IN"], 54, 0, DEEP, weight="700").replace('<text', '<text letter-spacing="9"')
for i, (t, d) in enumerate([("Feel your feet", "on the floor."), ("Find one place", "you feel something."), ("Name it plainly:", "tight, hot, heavy.")]):
    x = 250 + i * 690
    b += f'<circle cx="{x+55}" cy="2790" r="55" fill="{DEEP}"/><text x="{x+55}" y="2812" text-anchor="middle" font-family="DM Serif Display" font-size="64" fill="{WHITE}">{i+1}</text>\n'
    b += lines(x + 140, 2800, [t, d], 56, 70, INK)
b += lines(1212, 2990, ["So you can stay steady for the people who count on you, and know what is true for you."], 46, 0, DEEP, family="DM Serif Display", style="italic", anchor="middle")
b += "{{FOOTER:light:call}}\n"
write("poster_men_holder", "Men's track poster: Hold space for others without losing touch with yourself", b)
print("ok")
