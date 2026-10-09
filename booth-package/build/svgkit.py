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

def tri(x, y, w, color, op=1):
    return f'<polygon points="{x},{y+w*0.866:.0f} {x+w/2:.0f},{y} {x+w},{y+w*0.866:.0f}" fill="{color}" fill-opacity="{op}"/>\n'

def logo(x, y, w, dark):
    uri = "{{LOGO_DARK_URI}}" if dark else "{{LOGO_LIGHT_URI}}"
    return f'<image href="{uri}" x="{x}" y="{y}" width="{w}" height="{w*512/1378:.0f}" preserveAspectRatio="xMinYMid meet"/>\n'

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
    return lines(x, y, [f"{n}&#160;&#160;{text}"], size, 0, DEEP, weight="700", anchor=anchor, ls=str(round(size*.11)))

