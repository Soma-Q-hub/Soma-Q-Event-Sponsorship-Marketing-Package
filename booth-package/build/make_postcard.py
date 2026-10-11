#!/usr/bin/env python3
"""Postcard 6 x 4 in trim (file 6.25 x 4.25, 0.125 in bleed): FRONT = images about the work, BACK = How I work (About page) + photo.
Units 0.01 in. Run: python3 build/make_postcard.py"""
from svgkit import *
W, H = 625, 425
WHAT = ["Soma-Q is a nervous system alignment practice. We train", "high-performing leaders to notice stress sooner, shift", "in the moment and recover faster."]

# ---------------- FRONT ----------------
p = head("Postcard front, 6 x 4 in", 6.25, 4.25, "Postcard 6 x 4 in trim, file 6.25 x 4.25 in (0.125 in bleed). Keep type 0.25 in inside trim. CONFIRM printer template and stock.")
p += f'<rect width="{W}" height="{H}" fill="{DEEP}"/>\n' + logo(40, 28, 140, True)
p += lines(585, 44, ["NERVOUS SYSTEM ALIGNMENT", "FOR HIGH-PERFORMING LEADERS"], 10.5, 15, LIGHT, weight="700", anchor="end", ls="1")
p += f'<rect y="100" width="{W}" height="40" fill="{LIGHT}"/>\n'
p += lines(40, 127, ["NOTICE THE SIGNAL. LOCATE IT. CHOOSE YOUR RESPONSE."], 17, 0, DEEP, weight="700", ls="1.2")
tiles = [(40, 130, "1  Notice the signal", "fig"), (185, 215, "2  Locate it, interrupt the loop", "loop"), (415, 170, "3  Choose, and measure it", "met")]
for x, w_, cap, kind in tiles:
    fill = "#16494F" if kind == "fig" else WHITE
    p += f'<rect x="{x}" y="158" width="{w_}" height="190" rx="10" fill="{fill}"/>\n'
    if kind == "fig":
        p += placed("{{FIGURE:dark}}", x + w_/2 - 880*0.1/2, 166, 0.1)
    elif kind == "loop":
        p += placed("{{LOOP:light:nogloss:men}}", x + 4, 158 + (190 - 1480*0.1)/2, 0.1)
    else:
        for i, (nm, v, b0) in enumerate([("Stress recovery", 7.4, 3.8), ("Steadiness", 7.1, 3.5), ("Clear thinking", 7.8, 4.1)]):
            y = 192 + i * 46
            p += f'<text x="{x+12}" y="{y}" font-family="DM Sans" font-size="12" fill="{INK}">{nm}</text>'
            p += f'<rect x="{x+12}" y="{y+8}" width="146" height="9" rx="4" fill="{PALE}"/><rect x="{x+12}" y="{y+8}" width="{v*14.6:.0f}" height="9" rx="4" fill="{DEEP}"/>'
            p += f'<circle cx="{x+12+b0*14.6:.0f}" cy="{y+12.5}" r="5" fill="{WHITE}" stroke="{LIGHT}" stroke-width="2"/>'
        p += lines(x + 12, 336, ["Example format, not client data."], 8.5, 0, "#5C5A53")
    p += lines(x, 368, [cap], 11.5, 0, WHITE, weight="700")
p += lines(40, 399, ["Knowing you need to slow down has never been the hard part."], 11, 0, PALE, weight="500")
p += lines(585, 399, ["SOMA-Q.COM"], 11, 0, LIGHT, weight="700", anchor="end", ls="2")
p += TAIL
(SRC / "postcard_front.html").write_text(p)

# ---------------- FRONT B: one image, one idea ----------------
p = head("Postcard front B, 6 x 4 in", 6.25, 4.25, "Postcard front, option B: one image, one idea. 6 x 4 in trim, file 6.25 x 4.25 in (0.125 in bleed).")
p += f'<rect width="{W}" height="{H}" fill="{DEEP}"/>\n' + logo(40, 28, 140, True)
p += lines(585, 44, ["NERVOUS SYSTEM ALIGNMENT", "FOR HIGH-PERFORMING LEADERS"], 10.5, 15, LIGHT, weight="700", anchor="end", ls="1")
p += f'<rect y="100" width="{W}" height="40" fill="{LIGHT}"/>\n'
p += lines(40, 127, ["BECOME YOUR OWN ADVISOR."], 20, 0, DEEP, weight="700", ls="2.5")
p += f'<rect x="40" y="158" width="150" height="232" rx="12" fill="#16494F"/>\n'
p += placed("{{FIGURE:dark}}", 115 - 880*0.118/2, 166, 0.118)
p += lines(222, 205, ["Learn to read", "your nervous", "system’s signals."], 33, 38, WHITE, family="DM Serif Display")
p += lines(222, 322, ["You know what to do.", "Pressure decides whether you", "react or respond."], 13.5, 18, PALE, weight="500")
p += lines(222, 394, ["SOMA-Q.COM"], 12, 0, LIGHT, weight="700", ls="2")
p += TAIL
(SRC / "postcard_front_b.html").write_text(p)

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
