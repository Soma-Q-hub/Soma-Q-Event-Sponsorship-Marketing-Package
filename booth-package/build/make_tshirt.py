#!/usr/bin/env python3
"""Booth t-shirt artwork for a DARK shirt (Deep Teal or black): light ink only, no background, vector.
Front: left-chest logo, 4 x 4 in. Back: 'Shift Happens' with the core line, 11 x 10 in.
Ink colors: White #FEFCF8 and Light Teal #9BC4BD (two spot colors)."""
from svgkit import *
from svgkit import head as head_
# ---- front, left chest, 4 x 4 in: logo with the practice name line under it
p = head_("T-shirt front, left chest, 4 x 4 in", 4, 4, "Left-chest print 4 x 4 in. No background. Light ink for a dark shirt.")
p += logo(200 - 170, 100, 340, True, center=False)
p += lines(200, 232, ["NERVOUS SYSTEM ALIGNMENT"], 21, 0, LIGHT, weight="700", anchor="middle", ls="3.2")
p += TAIL
(SRC / "tshirt_front.html").write_text(p)
# ---- back, 11 x 13 in: who Soma-Q is, then the core line
p = head_("T-shirt back, 11 x 13 in", 11, 13, "Back print 11 x 13 in. No background. Light ink for a dark shirt: White and Light Teal.")
p += logo(550 - 170, 70, 340, True, center=False)
p += f'<text x="550" y="440" text-anchor="middle" font-family="DM Serif Display" font-size="163"><tspan fill="{WHITE}">Shift </tspan><tspan fill="{LIGHT}">Happens</tspan><tspan fill="{LIGHT}" font-size="46" dy="-86">\u2122</tspan></text>\n'
p += f'<rect x="425" y="500" width="250" height="3" fill="{LIGHT}"/>\n'
p += lines(550, 620, ["Nervous system alignment", "education and training to change", "your response to stress."], 56, 70, WHITE, weight="500", anchor="middle")
p += lines(550, 880, ["FOR HIGH-PERFORMING LEADERS"], 34, 0, LIGHT, weight="700", anchor="middle", ls="6")
p += lines(550, 1020, ["Pressure happens.", "Burnout doesn\u2019t have to."], 64, 80, WHITE, family="DM Serif Display", anchor="middle")
p += lines(550, 1235, ["SOMA-Q.COM"], 52, 0, LIGHT, weight="700", anchor="middle", ls="10")
p += TAIL
(SRC / "tshirt_back.html").write_text(p)
print("ok tshirt")
