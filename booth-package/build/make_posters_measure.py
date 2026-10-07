#!/usr/bin/env python3
"""Generate src/poster_progress.html and src/poster_capacity.html (measurement visuals from the Measurement Overview).
Example numbers are copied from SomaQ_Measurement_Overview_Oct2026.pdf and labeled as examples, not client data."""
import pathlib
SRC = pathlib.Path(__file__).resolve().parent.parent / "src"
HEAD = '''<!doctype html><html lang="en"><head><meta charset="utf-8"><title>{title}</title>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;700&family=DM+Serif+Display:ital@0;1&display=swap">
<style>
/* Poster 24 x 36 in trim, file at 24.25 x 36.25 in (0.125 in bleed). Drawn in units of 0.01 in. Keep text 1.5 in inside the file edge. */
@page {{ size: 24.25in 36.25in; margin: 0; }}
html, body {{ margin: 0; padding: 0; width: 24.25in; height: 36.25in; overflow: hidden; -webkit-print-color-adjust: exact; print-color-adjust: exact; }}
svg.page {{ display: block; width: 24.25in; height: 36.25in; }}
</style></head><body>
<svg class="page" viewBox="0 0 2425 3625" xmlns="http://www.w3.org/2000/svg">
'''
TAIL = '</svg></body></html>\n'
DEEP, LIGHT, PALE, LINEN, WHITE, INK, MID = "#103C41", "#9BC4BD", "#E4F2F2", "#EEEADD", "#FEFCF8", "#24211D", "#4F8078"
def eyebrow(x, y, t, color):
    return f'<g><polygon points="{x},{y} {x+34},{y-60} {x+68},{y}" fill="{color}"/><text x="{x+100}" y="{y}" font-family="DM Sans" font-weight="700" font-size="56" letter-spacing="9" fill="{color}">{t}</text></g>\n'

# ---------------- progress ----------------
p = HEAD.format(title="Poster: Watch your progress") + f'<rect width="2425" height="3625" fill="{LINEN}"/>\n' + eyebrow(175, 330, "A WEEKLY VIEW", DEEP)
for i, t in enumerate(["Watch your progress,", "week by week."]):
    p += f'<text x="175" y="{570+i*205}" font-family="DM Serif Display" font-size="186" fill="{DEEP}">{t}</text>\n'
for i, t in enumerate(["Each week you rate the same questions from 0 to 10.", "Higher always means better. Your Soma-Q Metrics Report", "shows where you started and where you are now."]):
    p += f'<text x="175" y="{1000+i*70}" font-family="DM Sans" font-size="58" fill="{INK}">{t}</text>\n'
p += f'<rect x="175" y="1185" width="730" height="80" rx="40" fill="{PALE}"/><text x="540" y="1241" text-anchor="middle" font-family="DM Sans" font-weight="700" font-size="40" letter-spacing="5" fill="{DEEP}">EXAMPLE, NOT CLIENT DATA</text>\n'
groups = [("BODY", [("Energy", 7, 4), ("Regulation", 7, 3), ("Somatic Awareness", 6, 4)]),
          ("EMOTION", [("Fulfillment", 8, 5), ("Response / Reactivity", 6, 3), ("Emotional Charge", 8, 5)]),
          ("MIND", [("Clarity", 6, 4), ("Focus Agility", 4, 3), ("Mental Processing", 4, 4)]),
          ("FOCUS AREAS", [("Foundation &amp; Stability", 7, 5), ("Creativity &amp; Connection", 7, 5), ("Confidence &amp; Drive", 6, 4)])]
x0, unit = 900, 125
p += f'<rect x="175" y="1320" width="2075" height="1480" rx="30" fill="{WHITE}"/>\n'
for v in (0, 5, 10):
    p += f'<line x1="{x0+v*unit}" y1="1355" x2="{x0+v*unit}" y2="2725" stroke="#D6D2C4" stroke-width="4"/>\n'
y = 1355
for gname, rows in groups:
    p += f'<polygon points="215,{y+44} 241,{y} 267,{y+44}" fill="{DEEP}"/><text x="290" y="{y+46}" font-family="DM Sans" font-weight="700" font-size="42" letter-spacing="7" fill="{DEEP}">{gname}</text>\n'
    y += 62
    for name, val, base in rows:
        cy = y + 36
        p += f'<text x="{x0-30}" y="{cy+16}" text-anchor="end" font-family="DM Sans" font-size="46" fill="{INK}">{name}</text>\n'
        p += f'<rect x="{x0}" y="{cy-30}" width="{val*unit}" height="60" rx="8" fill="{LIGHT}"/>\n'
        p += f'<circle cx="{x0+base*unit}" cy="{cy}" r="24" fill="{WHITE}" stroke="{DEEP}" stroke-width="10"/>\n'
        lx = x0 + val * unit + (60 if base == val else 22)
        p += f'<text x="{lx}" y="{cy+17}" font-family="DM Sans" font-weight="700" font-size="48" fill="{DEEP}">{val}</text>\n'
        y += 88
    y += 22
for v in (0, 5, 10):
    p += f'<text x="{x0+v*unit}" y="2765" text-anchor="middle" font-family="DM Sans" font-size="38" fill="#5C5A53">{v}</text>\n'
p += f'<rect x="1500" y="2832" width="52" height="30" rx="5" fill="{LIGHT}"/><text x="1568" y="2860" font-family="DM Sans" font-size="40" fill="{INK}">Week 10</text><circle cx="1838" cy="2847" r="18" fill="{WHITE}" stroke="{DEEP}" stroke-width="8"/><text x="1872" y="2860" font-family="DM Sans" font-size="40" fill="{INK}">Week 1 baseline</text>\n'
p += f'<rect x="175" y="2915" width="2075" height="160" rx="30" fill="{DEEP}"/>\n'
for i, t in enumerate(["Not every measure moves at the same pace. Here Regulation rose from 3 to 7 while", "Mental Processing held steady, and that tells the facilitator where to focus next."]):
    p += f'<text x="225" y="{2995+i*58}" font-family="DM Sans" font-size="46" fill="{WHITE}">{t}</text>\n'
p += '{{FOOTER:light:call}}\n' + TAIL
(SRC / "poster_progress.html").write_text(p)

# ---------------- capacity first ----------------
p = HEAD.format(title="Poster: Capacity comes first") + f'<rect width="2425" height="3625" fill="{LINEN}"/>\n<polygon points="2425,0 2425,900 1500,0" fill="{PALE}"/>\n' + eyebrow(175, 330, "HOW WE MEASURE", DEEP)
for i, t in enumerate(["Capacity comes first.", "Results follow."]):
    p += f'<text x="175" y="{570+i*205}" font-family="DM Serif Display" font-size="186" fill="{DEEP}">{t}</text>\n'
for i, t in enumerate(["Two things are tracked separately, so a strong result", "cannot hide growing strain."]):
    p += f'<text x="175" y="{1010+i*72}" font-family="DM Sans" font-size="58" fill="{INK}">{t}</text>\n'
p += f'<rect x="175" y="1170" width="1000" height="330" rx="40" fill="{WHITE}" stroke="{DEEP}" stroke-width="8"/><rect x="1250" y="1170" width="1000" height="330" rx="40" fill="{PALE}"/>\n'
p += f'<text x="225" y="1275" font-family="DM Sans" font-weight="700" font-size="38" letter-spacing="6" fill="{DEEP}">THE CAUSE</text><text x="225" y="1360" font-family="DM Serif Display" font-size="72" fill="{DEEP}">The method taking hold</text>\n'
for i, t in enumerate(["Is it landing in the body and", "nervous system? Five capacity measures."]):
    p += f'<text x="225" y="{1425+i*50}" font-family="DM Sans" font-size="40" fill="{INK}">{t}</text>\n'
p += f'<text x="1300" y="1275" font-family="DM Sans" font-weight="700" font-size="38" letter-spacing="6" fill="{DEEP}">THE EFFECT</text><text x="1300" y="1360" font-family="DM Serif Display" font-size="72" fill="{DEEP}">How you lead</text>\n'
for i, t in enumerate(["Is the change showing up in how people", "lead? Five competency measures."]):
    p += f'<text x="1300" y="{1425+i*50}" font-family="DM Sans" font-size="40" fill="{INK}">{t}</text>\n'
cx0, cx1 = 640, 2050
wk = lambda w: cx0 + (w - 1) * (cx1 - cx0) / 11
base, u = 2630, 80
yv = lambda v: base - v * u
p += f'<rect x="175" y="1580" width="2075" height="1230" rx="40" fill="{WHITE}" stroke="{DEEP}" stroke-width="8"/>\n'
for v in (0, 2, 4, 6, 8, 10):
    p += f'<line x1="520" y1="{yv(v)}" x2="2220" y2="{yv(v)}" stroke="#D6D2C4" stroke-width="4"/><text x="480" y="{yv(v)+14}" text-anchor="end" font-family="DM Sans" font-size="40" fill="#5C5A53">{v}</text>\n'
for w in (1, 6, 12):
    p += f'<text x="{wk(w):.0f}" y="{base+62}" text-anchor="middle" font-family="DM Sans" font-weight="700" font-size="44" fill="{INK}">Week {w}</text>\n'
cap = [(1, 4.6), (6, 5.9), (12, 6.8)]; comp = [(1, 5.2), (6, 5.6), (12, 6.4)]
pl = lambda pts, c, w: f'<polyline points="{" ".join(f"{wk(a):.0f},{yv(b):.0f}" for a, b in pts)}" fill="none" stroke="{c}" stroke-width="{w}" stroke-linejoin="round" stroke-linecap="round"/>'
p += pl(comp, LIGHT, 22) + pl(cap, DEEP, 16) + "\n"
for (a, b), (a2, b2) in zip(cap, comp):
    p += f'<circle cx="{wk(a2):.0f}" cy="{yv(b2):.0f}" r="26" fill="{LIGHT}" stroke="{DEEP}" stroke-width="8"/><circle cx="{wk(a):.0f}" cy="{yv(b):.0f}" r="24" fill="{DEEP}"/>\n'
for (w, vc), (w2, vm) in zip(cap, comp):
    up = vc > vm
    p += f'<text x="{wk(w):.0f}" y="{yv(vc)+(-44 if up else 76):.0f}" text-anchor="middle" font-family="DM Sans" font-weight="700" font-size="48" fill="{DEEP}">{vc}</text>\n'
    p += f'<text x="{wk(w):.0f}" y="{yv(vm)+(76 if up else -44):.0f}" text-anchor="middle" font-family="DM Sans" font-weight="700" font-size="48" fill="{MID}">{vm}</text>\n'
p += f'<rect x="570" y="1636" width="52" height="16" rx="8" fill="{DEEP}"/><text x="640" y="1656" font-family="DM Sans" font-size="42" fill="{INK}">The method taking hold (capacity)</text>\n'
p += f'<rect x="570" y="1706" width="52" height="20" rx="10" fill="{LIGHT}"/><text x="640" y="1730" font-family="DM Sans" font-size="42" fill="{INK}">How you lead (leadership competencies)</text>\n'
p += f'<rect x="1560" y="2400" width="610" height="150" rx="75" fill="{PALE}"/><text x="1865" y="2460" text-anchor="middle" font-family="DM Sans" font-weight="700" font-size="34" letter-spacing="4" fill="{DEEP}">ILLUSTRATIVE EXAMPLE</text><text x="1865" y="2510" text-anchor="middle" font-family="DM Sans" font-weight="700" font-size="34" letter-spacing="4" fill="{DEEP}">NOT CLIENT DATA</text>\n'
for i, t in enumerate(["In the Soma-Q method, capacity comes before outcomes, so those scores", "often begin to move first. A gain in results without capacity underneath it may be", "harder to sustain. This is a working expectation of the method, not a research", "finding, and individuals move differently."]):
    p += f'<text x="175" y="{2905+i*54}" font-family="DM Sans" font-size="44" fill="{INK}">{t}</text>\n'
p += '{{FOOTER:light:call}}\n' + TAIL
(SRC / "poster_capacity.html").write_text(p)
print("ok")
