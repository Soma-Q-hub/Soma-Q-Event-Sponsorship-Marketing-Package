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
p += lines(40, 126, ["BECOME YOUR OWN ADVISOR. ENERGY, CLARITY, JOY."], 17, 0, DEEP, weight="700", ls="1.4")
p += f'<rect x="40" y="158" width="150" height="232" rx="12" fill="#16494F"/>\n'
p += placed("{{FIGURE:dark}}", 115 - 880*0.118/2, 166, 0.118)
p += lines(222, 198, ["Learn to read", "your nervous", "system’s signals."], 33, 38, WHITE, family="DM Serif Display")
p += lines(222, 306, ["You know what to do.", "Pressure decides whether you", "react or respond."], 13.5, 18, PALE, weight="500")
p += hair(222, 585, 350, op=.45, w=1)
p += lines(222, 372, ["HEALTH &#160;·&#160; WEALTH &#160;·&#160; RELATIONSHIPS &#160;·&#160; CAREER"], 9.5, 0, LIGHT, weight="700", ls="1")
p += lines(222, 390, ["SOMA-Q.COM"], 11, 0, PALE, weight="700", ls="2")
p += TAIL
(SRC / "postcard_front_b.html").write_text(p)

# ---------------- FRONT C: Shift happens + Burnout ends here ----------------
p = head("Postcard front C, 6 x 4 in", 6.25, 4.25, "Postcard front, option C: one image, one idea. 6 x 4 in trim, file 6.25 x 4.25 in (0.125 in bleed).")
p += f'<rect width="{W}" height="{H}" fill="{DEEP}"/>\n' + logo(40, 28, 140, True)
p += lines(585, 44, ["NERVOUS SYSTEM ALIGNMENT", "FOR HIGH-PERFORMING LEADERS"], 10.5, 15, WHITE, weight="700", anchor="end", ls="1")
p += f'<rect y="100" width="{W}" height="40" fill="{LIGHT}"/>\n'
p += lines(40, 126, ["BECOME YOUR OWN ADVISOR. SHIFT HAPPENS™"], 17, 0, DEEP, weight="700", ls="1.2")
p += f'<rect x="40" y="158" width="150" height="232" rx="12" fill="#16494F"/>\n'
p += placed("{{FIGURE:dark}}", 115 - 880*0.118/2, 166, 0.118)
p += lines(222, 198, ["Learn to read", "your nervous", "system’s signals."], 33, 38, WHITE, family="DM Serif Display")
p += lines(222, 306, ["You know what to do.", "Pressure decides whether you", "react or respond."], 13.5, 18, PALE, weight="500")
p += hair(222, 585, 350, op=.45, w=1)
p += lines(222, 372, ["HEALTH &#160;·&#160; WEALTH &#160;·&#160; RELATIONSHIPS &#160;·&#160; CAREER"], 9.5, 0, LIGHT, weight="700", ls="1")
p += lines(222, 390, ["SOMA-Q.COM"], 11, 0, PALE, weight="700", ls="2")
p += TAIL
(SRC / "postcard_front_c.html").write_text(p)

# ---------------- FRONT D: Everyone around you can feel your stress ----------------
p = head("Postcard front D, 6 x 4 in", 6.25, 4.25, "Postcard front, option D: one image, one idea. 6 x 4 in trim, file 6.25 x 4.25 in (0.125 in bleed).")
p += f'<rect width="{W}" height="{H}" fill="{DEEP}"/>\n' + logo(40, 28, 140, True)
p += lines(585, 44, ["NERVOUS SYSTEM ALIGNMENT", "FOR HIGH-PERFORMING LEADERS"], 10.5, 15, WHITE, weight="700", anchor="end", ls="1")
p += f'<rect y="100" width="{W}" height="40" fill="{LIGHT}"/>\n'
p += lines(40, 126, ["BECOME YOUR OWN ADVISOR. SHIFT HAPPENS™"], 17, 0, DEEP, weight="700", ls="1.2")
p += f'<rect x="40" y="158" width="150" height="232" rx="12" fill="#16494F"/>\n'
p += placed("{{FIGURE:dark}}", 115 - 880*0.118/2, 166, 0.118)
p += lines(222, 196, ["Everyone around", "you can feel", "your stress."], 31, 36, WHITE, family="DM Serif Display")
p += lines(222, 292, ["What do you do next?"], 19, 0, LIGHT, family="DM Serif Display")
p += lines(222, 316, ["It isn’t a character flaw.", "It’s a stress response, and", "you can learn to work with it."], 12.5, 15.5, PALE, weight="500")
p += lines(222, 372, ["HEALTH &#160;·&#160; WEALTH &#160;·&#160; RELATIONSHIPS &#160;·&#160; CAREER"], 9.5, 0, LIGHT, weight="700", ls="1")
p += lines(222, 390, ["SOMA-Q.COM"], 11, 0, PALE, weight="700", ls="2")
p += TAIL
(SRC / "postcard_front_d.html").write_text(p)

# ---------------- FRONT E: three-quarters dark teal, one-quarter white strip ----------------
p = head("Postcard front E, 6 x 4 in", 6.25, 4.25, "Postcard front, option 1 redesign: 3/4 Deep Teal, 1/4 white strip. 6 x 4 in trim, file 6.25 x 4.25 in (0.125 in bleed).")
SX = 450
CXS = (SX + 612.5) / 2          # centre of the visible white strip (trim edge at 612.5)
p += f'<rect width="{W}" height="{H}" fill="{DEEP}"/>\n<rect x="{SX}" width="{W-SX}" height="{H}" fill="#FFFFFF"/>\n'
# bottom margin banner on the teal side
p += f'<rect x="0" y="372" width="{SX}" height="{H-372}" fill="#16494F"/>\n'
p += lines(40, 397, ["NERVOUS SYSTEM ALIGNMENT FOR HIGH-PERFORMING LEADERS"], 9.2, 0, WHITE, weight="700", ls="1")
# teal side
p += lines(40, 62, ["SHIFT HAPPENS™"], 11, 0, LIGHT, weight="700", ls="2.2")
p += f'<rect x="40" y="80" width="160" height="272" rx="12" fill="#16494F"/>\n'
p += placed("{{FIGURE:dark}}", 120 - 880*0.14/2, 90, 0.14)
p += lines(222, 112, ["Reading your", "nervous system’s", "signals is critical", "to your well-being."], 22.5, 28, WHITE, family="DM Serif Display")
p += lines(222, 244, ["Pressure decides whether", "you react or respond."], 13.5, 18, LIGHT, weight="700")
p += lines(222, 300, ["The wellness playbook we’ve", "been taught needs a rewrite."], 12.5, 17, WHITE, weight="700")
# white strip, centred
p += logo(CXS - 63, 40, 126, False)
p += lines(CXS, 116, ["Become your own", "advisor to shift", "outcomes:"], 11.5, 15, INK, weight="500", anchor="middle")
for k, word in enumerate(["Health", "Wealth", "Relationships", "Career"]):
    y = 188 + k * 42
    if k:
        p += f'<line x1="{CXS-22}" y1="{y-26}" x2="{CXS+22}" y2="{y-26}" stroke="{LIGHT}" stroke-width="1.5"/>'
    p += lines(CXS, y, [word], 17 if len(word) < 9 else 15.5, 0, DEEP, family="DM Serif Display", anchor="middle")
p += lines(CXS, 397, ["SOMA-Q.COM"], 10.5, 0, DEEP, weight="700", anchor="middle", ls="1.6")
p += TAIL
(SRC / "postcard_front_e.html").write_text(p)

# ---------------- BACK ----------------
p = head("Postcard back, 6 x 4 in", 6.25, 4.25, "Postcard back, 6 x 4 in trim, file 6.25 x 4.25 in. Address area intentionally not reserved (hand-out card, not mailed). If mailing is wanted, reserve the right half for postage and address.")
p += f'<rect width="{W}" height="{H}" fill="{LINEN}"/>\n'
p += "<!--PHOTO-->" + photo_circle(112, 112, 56, cid="pcp") + "<!--/PHOTO-->"
p += lines(40, 200, ["Megan McDonald"], 19, 0, DEEP, family="DM Serif Display") + lines(40, 215, ["Founder, Soma-Q"], 11, 0, DEEP, weight="700", ls="1")
p += lines(40, 237, ["I led healthcare tech teams", "until burnout and a health crisis", "left me depleted, in pain and", "unable to sleep."], 10, 13, INK)
p += lines(40, 292, ["I rebuilt how I lead and live.", "Now I help leaders do the same."], 10, 13.5, DEEP, weight="700")
p += vhair(212, 36, 300)
p += label(231, 52, "", "HOW I WORK", 12)
items = [("Tools that fit your day", "Five to twenty minute practices that stack into your schedule."),
         ("Structure you can measure", "Assessment, targeted practices and weekly measurement."),
         ("Body and mind together", "Where physiology, emotion and thinking meet."),
         ("A safe place for real work", "Supportive and free of judgment, at a pace your system can sustain."),
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
(SRC / "postcard_back_w.html").write_text(p.replace(f'fill="{LINEN}"', 'fill="#FFFFFF"').replace("Postcard back, 6 x 4 in", "Postcard back B (white), 6 x 4 in"))
print("ok postcard")
