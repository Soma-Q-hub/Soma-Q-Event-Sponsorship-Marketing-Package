#!/usr/bin/env python3
"""Postcard 6 x 4 in trim (file 6.25 x 4.25, 0.125 in bleed): FRONT = images about the work, BACK = How I work (About page) + photo.
Units 0.01 in. Run: python3 build/make_postcard.py"""
from svgkit import *
W, H = 625, 425
WHAT = ["Soma-Q is a nervous system alignment practice. We train", "high-performing leaders to notice stress sooner, shift", "in the moment and recover faster."]

# ---------------- FRONT ----------------
p = head("Postcard front, 6 x 4 in", 6.25, 4.25, "Postcard 6 x 4 in trim, file 6.25 x 4.25 in (0.125 in bleed). Keep type 0.25 in inside trim. CONFIRM printer template and stock.")
p += f'<rect width="{W}" height="{H}" fill="{DEEP}"/>\n' + logo(40, 34, 150, True)
p += lines(585, 52, ["NERVOUS SYSTEM ALIGNMENT", "FOR HIGH-PERFORMING LEADERS"], 11, 16, LIGHT, weight="700", anchor="end", ls="1")
p += f'<rect y="86" width="{W}" height="44" fill="{LIGHT}"/>\n'
p += lines(40, 117, ["BURNOUT ENDS HERE.™"], 25, 0, DEEP, weight="700", ls="3")
tiles = [(40, "Stress lives in the body", "{{FIGURE:dark}}", "fig"), (225, "Interrupt the loop", "{{LOOP:light:nogloss:men}}", "loop"), (410, "See it in your numbers", "", "met")]
for x, cap, tok, kind in tiles:
    fill = "#16494F" if kind == "fig" else WHITE
    p += f'<rect x="{x}" y="150" width="175" height="200" rx="10" fill="{fill}"/>\n'
    if kind == "fig":
        p += placed(tok, x + 175/2 - 880*0.1/2, 160, 0.1)
    elif kind == "loop":
        p += placed(tok, x + 6, 185, 0.0795)
    else:
        for i, (nm, v, b0) in enumerate([("Stress recovery", 7.4, 3.8), ("Steadiness", 7.1, 3.5), ("Clear thinking", 7.8, 4.1)]):
            y = 188 + i * 48
            p += f'<text x="{x+14}" y="{y}" font-family="DM Sans" font-size="12" fill="{INK}">{nm}</text>'
            p += f'<rect x="{x+14}" y="{y+8}" width="147" height="9" rx="4" fill="{PALE}"/><rect x="{x+14}" y="{y+8}" width="{v*14.7:.0f}" height="9" rx="4" fill="{DEEP}"/>'
            p += f'<circle cx="{x+14+b0*14.7:.0f}" cy="{y+12.5}" r="5" fill="{WHITE}" stroke="{LIGHT}" stroke-width="2"/>'
        p += lines(x + 14, 335, ["Example format, not client data."], 9, 0, "#5C5A53")
    p += lines(x, 372, [cap], 14, 0, WHITE, family="DM Serif Display")
p += lines(585, 400, ["SOMA-Q.COM"], 11, 0, LIGHT, weight="700", anchor="end", ls="2")
p += lines(40, 400, ["Everyone around you can feel your stress. Can you?"], 11, 0, PALE, weight="500")
p += TAIL
(SRC / "postcard_front.html").write_text(p)

# ---------------- BACK ----------------
p = head("Postcard back, 6 x 4 in", 6.25, 4.25, "Postcard back, 6 x 4 in trim, file 6.25 x 4.25 in. Address area intentionally not reserved (hand-out card, not mailed). If mailing is wanted, reserve the right half for postage and address.")
p += f'<rect width="{W}" height="{H}" fill="{LINEN}"/>\n'
p += "<!--PHOTO-->" + photo_circle(112, 112, 56, cid="pcp") + "<!--/PHOTO-->"
p += lines(40, 200, ["Megan McDonald"], 19, 0, DEEP, family="DM Serif Display") + lines(40, 215, ["Founder, Soma-Q"], 11, 0, DEEP, weight="700", ls="1")
p += lines(40, 235, ["13 years as a healthcare", "technology executive. RYT-500.", "Certified and accredited through", "SOMA Breath as a trauma-informed", "breathwork practitioner."], 10, 13, INK)
p += vhair(212, 36, 300)
p += label(231, 52, "", "HOW I WORK", 12)
items = [("A safe place for real work", "Supportive and free of judgment, at a pace your system can sustain."),
         ("Structure you can measure", "Assessment, targeted practices and weekly measurement."),
         ("Tools that fit your day", "Five to twenty minute practices that stack into your schedule."),
         ("Body and mind together", "Where physiology, emotion and thinking meet."),
         ("Alongside your other support", "Never replaces medical or mental health care."),
         ("Direct and compassionate", "Clear about what the work asks, kind about how hard change is.")]
for i, (t, d) in enumerate(items):
    col, row = i % 2, i // 2
    x, y = 228 + col * 184, 82 + row * 76
    p += f'<rect x="{x}" y="{y-14}" width="3" height="52" fill="{LIGHT}"/>'
    p += lines(x + 10, y, [t], 11.5, 0, DEEP, weight="700")
    words, ln, rows = d.split(), "", []
    for w_ in words:
        if len(ln + " " + w_) > 30 and ln:
            rows.append(ln); ln = w_
        else:
            ln = (ln + " " + w_).strip()
    rows.append(ln)
    p += lines(x + 10, y + 15, rows, 10.5, 13.5, INK)
p += f'<rect y="318" width="{W}" height="107" fill="{DEEP}"/>\n'
p += label(40, 342, "", "WHAT WE DO", 10).replace(f'fill="{DEEP}"', f'fill="{LIGHT}"')
p += lines(40, 362, WHAT, 12, 16, WHITE)
p += '<rect x="505" y="328" width="82" height="82" rx="8" fill="#FFFFFF"/><svg x="511" y="334" width="70" height="70">{{QR_CALL}}</svg>'
p += lines(490, 352, ["Scan to book a", "free discovery", "call"], 10.5, 13, PALE, weight="700", anchor="end")
p += TAIL
(SRC / "postcard_back.html").write_text(p)
print("ok postcard")
