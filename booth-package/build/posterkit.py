#!/usr/bin/env python3
"""Shared helpers for the 24 x 36 in explainer posters. Light fields (Linen or Pale Teal) with Deep Teal type, for legibility under venue lighting.
Units 0.01 in; file 24.25 x 36.25 in (0.125 in bleed)."""
import pathlib
SRC = pathlib.Path(__file__).resolve().parent.parent / "src"
DEEP, LIGHT, PALE, LINEN, WHITE, INK = "#103C41", "#9BC4BD", "#E4F2F2", "#EEEADD", "#FEFCF8", "#24211D"
HEAD = """<!doctype html><html lang="en"><head><meta charset="utf-8"><title>{title}</title>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;700&family=DM+Serif+Display:ital@0;1&display=swap">
<style>
/* Poster 24 x 36 in trim, file 24.25 x 36.25 in (0.125 in bleed). Units 0.01 in. Keep text 1.5 in inside the file edge. */
@page {{ size: 24.25in 36.25in; margin: 0; }}
html, body {{ margin: 0; padding: 0; width: 24.25in; height: 36.25in; overflow: hidden; -webkit-print-color-adjust: exact; print-color-adjust: exact; }}
svg.page {{ display: block; width: 24.25in; height: 36.25in; }}
</style></head><body>
<svg class="page" viewBox="0 0 2425 3625" xmlns="http://www.w3.org/2000/svg">
"""
TAIL = "</svg></body></html>\n"
def eyebrow(x, y, t, c=DEEP):
    return f'<polygon points="{x},{y} {x+34},{y-60} {x+68},{y}" fill="{c}"/><text x="{x+100}" y="{y}" font-family="DM Sans" font-weight="700" font-size="56" letter-spacing="9" fill="{c}">{t}</text>\n'
def lines(x, y, rows, size, lh, fill, family="DM Sans", style="", weight="400", anchor="start"):
    st = f' font-style="{style}"' if style else ""
    return "".join(f'<text x="{x}" y="{y+i*lh}" text-anchor="{anchor}" font-family="{family}" font-weight="{weight}" font-size="{size}" fill="{fill}"{st}>{t}</text>\n' for i, t in enumerate(rows))
def write(name, title, body): (SRC / f"{name}.html").write_text(HEAD.format(title=title) + body + TAIL)

