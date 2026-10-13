#!/usr/bin/env python3
"""Shared SVG page helpers for the large-format pieces.
Light fields with Deep Teal type and Light Teal accents: easier to read under venue lighting and on large prints than a
solid Deep Teal field. Units are 0.01 in."""
import pathlib
SRC = pathlib.Path(__file__).resolve().parent.parent / "src"
DEEP, LIGHT, PALE, LINEN, WHITE, INK = "#103C41", "#9BC4BD", "#E4F2F2", "#EEEADD", "#FEFCF8", "#24211D"

def head(title, w_in, h_in, note):
    return f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><title>{title}</title>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;700&family=DM+Serif+Display:ital@0;1&display=swap">
<style>
/* {note} */
@page {{ size: {w_in}in {h_in}in; margin: 0; }}
html, body {{ margin: 0; padding: 0; width: {w_in}in; height: {h_in}in; overflow: hidden; -webkit-print-color-adjust: exact; print-color-adjust: exact; }}
svg.page {{ display: block; width: {w_in}in; height: {h_in}in; }}
</style></head><body>
<svg class="page" viewBox="0 0 {int(w_in*100)} {int(h_in*100)}" xmlns="http://www.w3.org/2000/svg">
'''
TAIL = '</svg></body></html>\n'

def lines(x, y, rows, size, lh, fill, family="DM Sans", weight="400", anchor="start", style="", ls=""):
    o = ""
    for i, t in enumerate(rows):
        o += (f'<text x="{x}" y="{y+i*lh}" text-anchor="{anchor}" font-family="{family}" font-weight="{weight}" font-size="{size}" '
              f'fill="{fill}"{(" font-style=" + chr(34) + style + chr(34)) if style else ""}{(" letter-spacing=" + chr(34) + str(ls) + chr(34)) if ls else ""}>{t}</text>')
    return o + "\n"

def justified(x, y, rows, size, lh, fill, width, family="DM Sans", weight="400"):
    """Full-justified block: every row is stretched (word spacing) to exactly `width`, so both edges are even."""
    o = ""
    for i, t in enumerate(rows):
        o += (f'<text x="{x}" y="{y+i*lh}" textLength="{width}" lengthAdjust="spacing" font-family="{family}" font-weight="{weight}" '
              f'font-size="{size}" fill="{fill}">{t}</text>')
    return o + "\n"

def tri(x, y, w, color, op=1):
    return f'<polygon points="{x},{y+w*0.866:.0f} {x+w/2:.0f},{y} {x+w},{y+w*0.866:.0f}" fill="{color}" fill-opacity="{op}"/>\n'

LOGO_INK_LEFT = 42.5 / 1378   # the logo PNG has transparent padding; its ink starts 3.1 percent in. Measured on the asset.

def logo(x, y, w, dark, center=False):
    """x is where the logo's visible left edge lands (so it lines up with the text margin). center=True skips the correction for logos centered by their box."""
    uri = "{{LOGO_DARK_URI}}" if dark else "{{LOGO_LIGHT_URI}}"
    if not center:
        x = round(x - w * LOGO_INK_LEFT, 2)
    return f'<image href="{uri}" x="{x}" y="{y}" width="{w}" height="{w*512/1378:.0f}" preserveAspectRatio="xMinYMid meet"/>\n'

def qmark(x, y, w, dark):
    uri = "{{QMARK_DARK_URI}}" if dark else "{{QMARK_LIGHT_URI}}"
    return f'<image href="{uri}" x="{x}" y="{y}" width="{w}" height="{w*376/367:.1f}" preserveAspectRatio="xMidYMid meet"/>\n'

def placed(inner_token, x, y, scale):
    return f'<g transform="translate({x},{y}) scale({scale})">{inner_token}</g>\n'


def hair(x1, x2, y, op=.28, w=8):
    return f'<line x1="{x1}" y1="{y}" x2="{x2}" y2="{y}" stroke="{DEEP}" stroke-width="{w}" stroke-opacity="{op}"/>\n'

def vhair(x, y1, y2, op=.2, w=8):
    return f'<line x1="{x}" y1="{y1}" x2="{x}" y2="{y2}" stroke="{DEEP}" stroke-width="{w}" stroke-opacity="{op}"/>\n'

def photo_circle(cx, cy, r, cid="ph", ring=LIGHT):
    """Circle crop of the headshot (760 x 915 px). Crop window is centered on the face with headroom and some jacket:
    source center (270, 290), source radius 260 px, so the hair, face and shoulders sit inside the circle."""
    s = r / 260.0
    return (f'<clipPath id="{cid}"><circle cx="{cx}" cy="{cy}" r="{r}"/></clipPath>'
            f'<image href="{{{{PHOTO_URI}}}}" x="{cx-270*s:.0f}" y="{cy-290*s:.0f}" width="{760*s:.0f}" height="{915*s:.0f}" clip-path="url(#{cid})"/>'
            f'<circle cx="{cx}" cy="{cy}" r="{r+r*0.07:.0f}" fill="none" stroke="{ring}" stroke-width="{max(10, r*0.045):.0f}"/>\n')

def label(x, y, n, text, size, anchor="start"):
    t = f"{n}&#160;&#160;{text}" if n else text
    return lines(x, y, [t], size, 0, DEEP, weight="700", anchor=anchor, ls=str(round(size*.11)))


def decision_flow():
    """Pressure happens -> Interrupt here -> No = reaction (loop runs) / Yes = response. Local box 2800 x 2000."""
    o = f'<circle cx="1400" cy="100" r="235" fill="#C9763F" fill-opacity=".20"/><circle cx="1400" cy="100" r="150" fill="#C9763F" fill-opacity=".22"/>'
    o += f'<rect x="900" y="0" width="1000" height="200" rx="100" fill="{WHITE}" stroke="{DEEP}" stroke-width="10"/>'
    o += f'<text x="1400" y="132" text-anchor="middle" font-family="DM Serif Display" font-size="104" fill="{DEEP}">Pressure happens</text>'
    arrow = lambda d: f'<path d="{d}" fill="none" stroke="{DEEP}" stroke-width="12" stroke-linecap="round" stroke-linejoin="round"/>'
    head = lambda x, y, dx=0: f'<polygon points="{x-34},{y-50} {x+34},{y-50} {x},{y}" fill="{DEEP}"/>'
    o += arrow("M1400,200 L1400,330") + head(1400, 340)
    o += f'<rect x="650" y="340" width="1500" height="400" rx="56" fill="{LIGHT}"/>'
    o += lines(1400, 462, ["INTERRUPT HERE"], 92, 0, DEEP, weight="700", anchor="middle", ls="8")
    o += lines(1400, 560, ["Notice the signal. Locate it in your body."], 66, 0, DEEP, anchor="middle")
    o += lines(1400, 680, ["Do you catch it?"], 84, 0, DEEP, family="DM Serif Display", anchor="middle", style="italic")
    # branches
    o += arrow("M1000,740 L1000,820 L650,820 L650,930") + head(650, 940)
    o += arrow("M1800,740 L1800,820 L2150,820 L2150,930") + head(2150, 940)
    for cx, t in ((650, "NO"), (2150, "YES")):
        o += f'<rect x="{cx-110}" y="776" width="220" height="108" rx="54" fill="{WHITE}" stroke="{DEEP}" stroke-width="10"/><text x="{cx}" y="852" text-anchor="middle" font-family="DM Sans" font-weight="700" font-size="76" letter-spacing="6" fill="{DEEP}">{t}</text>'
    # reaction
    o += f'<rect x="0" y="950" width="1300" height="1050" rx="60" fill="{DEEP}"/>'
    o += lines(80, 1090, ["REACTION"], 124, 0, WHITE, family="DM Serif Display")
    o += lines(80, 1170, ["The loop runs again."], 70, 0, LIGHT, weight="500")
    for i, t in enumerate(["Body tightens, mind races.", "Short with your people.", "Choices made from pressure.", "Running on empty."]):
        y = 1350 + i * 170
        o += f'<circle cx="112" cy="{y-26}" r="16" fill="#C9763F"/>' + lines(160, y, [t], 79, 0, WHITE)
    # response
    o += f'<rect x="1500" y="950" width="1300" height="1050" rx="60" fill="{WHITE}" stroke="{DEEP}" stroke-width="12"/>'
    o += lines(1580, 1090, ["RESPONSE"], 124, 0, DEEP, family="DM Serif Display")
    o += lines(1580, 1170, ["You choose what happens next."], 66, 0, DEEP, weight="500")
    for i, t in enumerate(["Body settles, mind clears.", "Present with your people.", "Choices made from clarity.", "Energy left at day’s end."]):
        y = 1350 + i * 170
        o += f'<circle cx="1612" cy="{y-26}" r="16" fill="{LIGHT}" stroke="{DEEP}" stroke-width="5"/>' + lines(1660, y, [t], 79, 0, DEEP)
    return o
