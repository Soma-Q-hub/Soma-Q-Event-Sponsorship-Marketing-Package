#!/usr/bin/env python3
"""Booth t-shirt artwork for a DARK shirt (Deep Teal or black): light ink only, no background, vector.
Front: left-chest logo, 4 x 4 in. Back: 'Shift Happens' with the core line, 11 x 10 in.
Ink colors: White #FEFCF8 and Light Teal #9BC4BD (two spot colors)."""
from svgkit import *
from svgkit import head as head_
# ---- front, left chest, 4 x 4 in
p = head_("T-shirt front, left chest, 4 x 4 in", 4, 4, "Left-chest print 4 x 4 in. No background. Light ink for a dark shirt.")
p += logo(200 - 170, 128, 340, True, center=False)
p += TAIL
(SRC / "tshirt_front.html").write_text(p)
# ---- back, 11 x 10 in
p = head_("T-shirt back, 11 x 10 in", 11, 10, "Back print 11 x 10 in. No background. Light ink for a dark shirt: White and Light Teal.")
p += f'<text x="550" y="300" text-anchor="middle" font-family="DM Serif Display" font-size="163"><tspan fill="{WHITE}">Shift </tspan><tspan fill="{LIGHT}">Happens</tspan><tspan fill="{LIGHT}" font-size="46" dy="-86">™</tspan></text>\n'
p += f'<rect x="425" y="400" width="250" height="3" fill="{LIGHT}"/>\n'
p += lines(550, 520, ["Pressure happens.", "Burnout doesn’t have to."], 72, 92, WHITE, family="DM Serif Display", anchor="middle")
p += lines(550, 800, ["SOMA-Q.COM"], 56, 0, LIGHT, weight="700", anchor="middle", ls="10")
p += TAIL
(SRC / "tshirt_back.html").write_text(p)
print("ok tshirt")
