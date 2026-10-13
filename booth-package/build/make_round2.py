#!/usr/bin/env python3
"""Round 2 pieces, built to match the final postcard and banner D1 (Deep Teal fields, Linen and white panels, copper only on
pressure). Wording is from the website v2 pages (Home, The Work, Programs).
  poster_flow                      24 x 36 in   the Pressure Loop redesigned as the banner's decision flow
  insert_flow, insert_metrics, insert_call   8.5 x 11 in stand-up holder inserts (white margin so any printer can print them)
  bizcard2_front, bizcard2_back    3.5 x 2 in business card
  table_cover_v2                   72 x 30 in table cover front (placeholder size)
  giveaway_tag_front, _back        bag tag, 2.5 x 4.25 in (placeholder: match the vendor's die line)
  booklet                          5.5 x 8.5 in, 8 pages, saddle stitch (take-away "What do you do next?")
Units 0.01 in. Run: python3 build/make_round2.py"""
from svgkit import *
from svgkit import head as head_

NOT_DATA = "Example of the report format only; not client data."
FOUR = [("Health", "Sleep that doesn’t restore you, and a body that has been running on alarm for too long."),
        ("Wealth", "Money and business decisions made from pressure instead of clarity."),
        ("Relationships", "Less patience for the people you love than you give everyone else."),
        ("Career", "Leading well on the outside while running on empty on the inside.")]
STEPS = ["Notice the signal.", "Locate what is happening.", "Choose your next response."]
CHART = [("Clear thinking", "Cognitive", 7.8, 4.1), ("Emotional steadiness", "Emotional", 7.1, 3.5), ("Stress recovery", "Somatic", 7.4, 3.8)]


def qr(x, y, size, kind="CALL", pad=0.09):
    """White rounded card with a Deep Teal QR inside."""
    q = size * (1 - 2 * pad)
    return (f'<rect x="{x}" y="{y}" width="{size}" height="{size}" rx="{size*.07:.1f}" fill="#FFFFFF" stroke="{DEEP}" stroke-width="{max(1, size*.012):.1f}"/>'
            f'<svg x="{x+size*pad:.1f}" y="{y+size*pad:.1f}" width="{q:.1f}" height="{q:.1f}">{{{{QR_{kind}}}}}</svg>\n')


def bars(x, y, w, rows, unit_h, name_size, show_tag=True, ring=WHITE):
    """Week 1 marker vs current bar, scored 0 to 10, as on the website Metrics Report."""
    o = ""
    for i, (nm, tag, v, b0) in enumerate(rows):
        yy = y + i * unit_h
        o += lines(x, yy, [nm], name_size, 0, INK, weight="700")
        if show_tag:
            o += lines(x + w, yy, [tag.upper()], name_size * .62, 0, "#5C5A53", weight="700", anchor="end", ls=str(round(name_size * .06, 1)))
        by = yy + name_size * .55
        bh = name_size * .62
        o += f'<rect x="{x}" y="{by:.1f}" width="{w}" height="{bh:.1f}" rx="{bh/2:.1f}" fill="{PALE}"/>'
        o += f'<rect x="{x}" y="{by:.1f}" width="{w*v/10:.1f}" height="{bh:.1f}" rx="{bh/2:.1f}" fill="{DEEP}"/>'
        o += f'<circle cx="{x+w*b0/10:.1f}" cy="{by+bh/2:.1f}" r="{bh*.62:.1f}" fill="{ring}" stroke="{LIGHT}" stroke-width="{bh*.28:.1f}"/>'
        o += lines(x + w * v / 10 - bh * .4, by + bh * .78, [f"{v}"], bh * .8, 0, WHITE, weight="700", anchor="end")
    return o


# ========================================================= POSTER: the pressure flow, 24 x 36 =========================================================
W, H = 2425, 3625
p = head_("Poster: Pressure happens, 24 x 36 in", 24.25, 36.25, "Poster 24 x 36 in trim, file 24.25 x 36.25 in (0.125 in bleed). Keep type 1.5 in inside the file edge. Replaces the Linen Pressure Loop poster; same flow as banner E1.")
p += f'<rect width="{W}" height="{H}" fill="{LINEN}"/><rect width="{W}" height="1230" fill="{DEEP}"/>\n'
p += logo(175, 170, 760, True)
p += lines(2250, 250, ["NERVOUS SYSTEM ALIGNMENT", "FOR HIGH-PERFORMING LEADERS"], 50, 70, LIGHT, weight="700", anchor="end", ls="3")
p += lines(175, 700, ["Pressure happens.", "What do you do next?"], 190, 215, WHITE, family="DM Serif Display")
p += lines(175, 1130, ["Notice the signal. Locate it. Choose your next response."], 62, 0, LIGHT, weight="700")
p += f'<g transform="translate(175,1420) scale(0.74)">{decision_flow()}</g>\n'
p += lines(1212, 3060, ["Regulation is a skill. Recovery is a skill.", "Choice under pressure is a skill."], 62, 82, DEEP, family="DM Serif Display", anchor="middle", style="italic")
p += f'<rect y="3225" width="{W}" height="400" fill="#FFFFFF"/>\n' + logo(175, 3290, 520, False)
p += lines(180, 3520, ["SOMA-Q.COM"], 46, 0, DEEP, weight="700", ls="6")
p += lines(1850, 3350, ["Scan to book a", "free discovery call."], 54, 70, DEEP, weight="700", anchor="end")
p += qr(1930, 3260, 320)
p += TAIL
(SRC / "poster_flow.html").write_text(p)


# ========================================================= STAND-UP INSERTS, 8.5 x 11 =========================================================
def insert_head(title):
    p = head_(title, 8.5, 11, "Stand-up holder insert, 8.5 x 11 in, no bleed. 0.4 in white margin so an office or copy-shop printer will not clip it. Print on heavy white stock.")
    return p + f'<rect width="850" height="1100" fill="#FFFFFF"/>\n'


def insert_foot(p, y=956, h=104, dark=True):
    fill, fg, sub = (DEEP, WHITE, LIGHT) if dark else (LINEN, DEEP, INK)
    p += f'<rect x="40" y="{y}" width="770" height="{h}" rx="16" fill="{fill}"/>\n'
    p += logo(64, y + 20, 130, dark)
    p += lines(220, y + 46, ["Book a free discovery call."], 25, 0, fg, family="DM Serif Display")
    p += lines(220, y + 74, ["SOMA-Q.COM  ·  An honest conversation. No obligation."], 12.5, 0, sub, weight="700", ls="1")
    p += qr(710, y + 8, h - 16)
    return p


# --- insert 1: the flow ---
p = insert_head("Insert 1: Pressure happens (stand-up holder)")
p += f'<rect x="40" y="40" width="770" height="270" rx="22" fill="{DEEP}"/>\n' + logo(68, 66, 190, True)
p += lines(786, 94, ["WHEN PRESSURE HITS"], 13, 0, LIGHT, weight="700", anchor="end", ls="3")
p += lines(68, 190, ["Pressure happens.", "What do you do next?"], 56, 64, WHITE, family="DM Serif Display")
p += lines(68, 292, ["Notice the signal. Locate it. Choose your next response."], 17, 0, LIGHT, weight="700")
p += f'<g transform="translate(75,350) scale(0.25)">{decision_flow()}</g>\n'
p += f'<rect x="40" y="880" width="770" height="58" rx="14" fill="{LINEN}"/>\n'
p += lines(425, 917, ["Regulation is a skill. Recovery is a skill. Choice under pressure is a skill."], 15, 0, DEEP, weight="700", anchor="middle")
p = insert_foot(p)
p += TAIL
(SRC / "insert_flow.html").write_text(p)

# --- insert 2: the metrics (website Metrics Report) ---
p = insert_head("Insert 2: Watch your progress in your own numbers (stand-up holder)")
p += f'<rect x="40" y="40" width="770" height="250" rx="22" fill="{DEEP}"/>\n' + logo(68, 66, 190, True)
p += lines(786, 94, ["THE PROOF"], 13, 0, LIGHT, weight="700", anchor="end", ls="3")
p += lines(68, 178, ["Watch your progress", "in your own numbers."], 52, 60, WHITE, family="DM Serif Display")
p += lines(68, 276, ["Scored 0 to 10. Higher always means better."], 17, 0, LIGHT, weight="700")
p += f'<rect x="40" y="310" width="770" height="340" rx="20" fill="{WHITE}" stroke="{DEEP}" stroke-width="2"/>\n'
p += lines(70, 352, ["SOMA-Q METRICS REPORT"], 12.5, 0, DEEP, weight="700", ls="2.5")
p += lines(780, 352, ["Week 1 compared with week 16"], 12.5, 0, INK, anchor="end")
p += bars(70, 410, 710, CHART, 82, 20)
p += f'<circle cx="72" cy="632" r="6" fill="{WHITE}" stroke="{LIGHT}" stroke-width="3"/>' + lines(86, 637, ["Week 1"], 11, 0, INK)
p += f'<rect x="140" y="626" width="22" height="9" rx="4" fill="{DEEP}"/>' + lines(168, 637, ["Week 16"], 11, 0, INK)
p += lines(780, 637, [NOT_DATA], 11, 0, "#5C5A53", anchor="end")
p += f'<rect x="40" y="670" width="770" height="260" rx="20" fill="{LINEN}"/>\n'
cols = [("1", "Weekly Check-In", ["Before every session, a short", "set of questions, each", "scored from 0 to 10."]),
        ("2", "Metrics Report", ["A week-by-week view of how", "clearly you think, how steady", "you stay and how quickly you", "recover from stress."]),
        ("3", "What happens next", ["It shows what is shifting and", "what still needs attention, so", "practice goes where it counts."])]
for i, (n, t, rows) in enumerate(cols):
    x = 68 + i * 252
    p += f'<circle cx="{x+16}" cy="724" r="16" fill="{DEEP}"/><text x="{x+16}" y="731" text-anchor="middle" font-family="DM Serif Display" font-size="20" fill="{WHITE}">{n}</text>'
    p += lines(x + 42, 731, [t], 18, 0, DEEP, family="DM Serif Display")
    p += lines(x, 774, rows, 14.5, 21, INK)
p += lines(68, 905, ["Progress becomes something you can see for yourself, not something you take on faith."], 14, 0, DEEP, weight="700")
p = insert_foot(p)
p += TAIL
(SRC / "insert_metrics.html").write_text(p)

# --- insert 3: book a call ---
p = insert_head("Insert 3: Every path starts with a conversation (stand-up holder)")
p += f'<rect x="40" y="40" width="770" height="250" rx="22" fill="{DEEP}"/>\n' + logo(68, 66, 190, True)
p += lines(786, 94, ["SHIFT HAPPENS™"], 13, 0, LIGHT, weight="700", anchor="end", ls="3")
p += lines(68, 178, ["Every path starts", "with a conversation."], 52, 60, WHITE, family="DM Serif Display")
p += lines(68, 276, ["Pressure shows up in four places. Which one is yours?"], 17, 0, LIGHT, weight="700")
for i, (nm, d) in enumerate(FOUR):
    x, y = 40 + (i % 2) * 391, 312 + (i // 2) * 150
    p += f'<rect x="{x}" y="{y}" width="379" height="138" rx="18" fill="{LINEN}"/>\n'
    p += lines(x + 26, y + 52, [nm], 30, 0, DEEP, family="DM Serif Display")
    words, rows, cur = d.split(), [], ""
    for wd in words:
        if len(cur) + len(wd) > 34:
            rows.append(cur); cur = wd
        else:
            cur = (cur + " " + wd).strip()
    rows.append(cur)
    p += lines(x + 26, y + 82, rows, 14.5, 20, INK)
p += f'<rect x="40" y="622" width="770" height="438" rx="22" fill="{DEEP}"/>\n'
p += qr(70, 656, 270)
p += lines(370, 700, ["Book a free", "discovery call."], 44, 50, WHITE, family="DM Serif Display")
p += lines(370, 820, ["We look at what pressure is costing you", "right now and whether this work is the", "right fit, with no obligation to go further."], 16, 24, PALE)
p += lines(370, 920, ["Not ready? Take the free Burnout Signal Check:"], 14.5, 0, LIGHT, weight="700")
p += qr(370, 934, 100, "QUIZ")
p += lines(490, 970, ["SOMA-Q.COM"], 16, 0, WHITE, weight="700", ls="2")
p += lines(490, 994, ["Nervous system alignment for", "high-performing leaders."], 12.5, 17, LIGHT)
p += TAIL
(SRC / "insert_call.html").write_text(p)


# --- insert 4: the system (what makes Soma-Q different) ---
p = insert_head("Insert 4: Your practice creates the data (stand-up holder)")
p += f'<rect x="40" y="40" width="770" height="250" rx="22" fill="{DEEP}"/>\n' + logo(68, 66, 190, True)
p += lines(786, 94, ["WHAT MAKES SOMA-Q DIFFERENT"], 13, 0, LIGHT, weight="700", anchor="end", ls="2.5")
p += lines(68, 176, ["The tools you practice", "also create the data."], 50, 58, WHITE, family="DM Serif Display")
p += lines(68, 272, ["So we can see what is working, what is not, and adjust."], 17, 0, LIGHT, weight="700")
cyc = [("BASELINE", "Soma-Q Assessment at the start"), ("WEEKLY", "Soma-Q Weekly Check-In, under five minutes"), ("TRENDED", "SQ-M and SQ-C, tracked separately"),
       ("REPORT", "Progress in plain, usable language"), ("ADJUST", "Practice follows the data")]
for i, (t, d) in enumerate(cyc):
    x = 40 + i * 156
    p += f'<rect x="{x}" y="312" width="146" height="104" rx="14" fill="{PALE}"/>'
    p += lines(x + 73, 340, [t], 11.5, 0, DEEP, weight="700", anchor="middle", ls="2")
    rows, cur = [], ""
    for wd in d.split():
        if len(cur) + len(wd) > 17:
            rows.append(cur); cur = wd
        else:
            cur = (cur + " " + wd).strip()
    rows.append(cur)
    p += lines(x + 73, 364, rows, 12.5, 16, INK, anchor="middle")
    if i < 4:
        p += f'<polygon points="{x+148},{356} {x+156},{364} {x+148},{372}" fill="{DEEP}"/>'
p += lines(40, 446, ["SOMA-Q LEADERSHIP PROGRESS MEASUREMENT SYSTEM (SQ-LPMS)  ·  ONE SYSTEM, TWO SEPARATE MEASURES"], 11, 0, DEEP, weight="700", ls="1.4")
for x, tag, nm, desc, fill in ((40, "THE CAUSE", "SQ-M", ["Soma-Q Method Metrics.", "Is the method landing in the", "body and nervous system?"], LINEN),
                               (431, "THE EFFECT", "SQ-C", ["Soma-Q Leadership Competencies.", "Is the change showing up", "in how you lead?"], PALE)):
    p += f'<rect x="{x}" y="462" width="379" height="150" rx="18" fill="{fill}"/>'
    p += lines(x + 26, 494, [tag], 11, 0, DEEP, weight="700", ls="2.5")
    p += lines(x + 26, 538, [nm], 36, 0, DEEP, family="DM Serif Display")
    p += lines(x + 26, 566, desc, 13.5, 18, INK)
p += lines(40, 642, ["Kept apart on purpose, so a strong quarter of results cannot hide growing strain,", "and a slow start is not mistaken for a lack of capability."], 13.5, 19, INK)
p += f'<rect x="40" y="700" width="770" height="240" rx="20" fill="{LINEN}"/>'
p += lines(68, 740, ["WHAT YOU KEEP"], 12, 0, DEEP, weight="700", ls="3")
keep = [("Your Metrics Report", "Week by week, in plain language, from the first session to the last."),
        ("Your session notes", "What we worked on and what shifted, written down."),
        ("Your practice reference", "The practices chosen for your system, to use on your own.")]
for i, (t, d) in enumerate(keep):
    x = 68 + i * 252
    p += lines(x, 786, [t], 19, 0, DEEP, family="DM Serif Display")
    rows, cur = [], ""
    for wd in d.split():
        if len(cur) + len(wd) > 30:
            rows.append(cur); cur = wd
        else:
            cur = (cur + " " + wd).strip()
    rows.append(cur)
    p += lines(x, 812, rows, 13.5, 19, INK)
p += lines(68, 914, ["Soma-Q is an education and training practice. No score is a medical or psychological measure."], 10.5, 0, "#5C5A53")
p = insert_foot(p)
p += TAIL
(SRC / "insert_system.html").write_text(p)

# --- insert 5: the seven areas of focus (node work, themes only) ---
AREAS = [("Foundation & Stability", "Feel grounded and secure enough to make decisions without bracing for the worst."),
         ("Creativity & Connection", "Think flexibly, generate fresh ideas and stay connected to the people you lead."),
         ("Confidence & Drive", "Act with steady confidence and hold clear boundaries without pushing yourself into depletion."),
         ("Compassion & Relationships", "Stay open and steady in difficult conversations, so trust holds when the pressure is on."),
         ("Expression & Communication", "Say what needs to be said clearly and calmly, even when the stakes are high."),
         ("Clarity & Intuition", "See a situation clearly and trust your read on it when the information is incomplete."),
         ("Purpose & Perspective", "Keep the larger picture in view, so daily pressure stays connected to what matters most to you.")]
AXIS = [("Awareness", "Notice the signal early."), ("Regulation", "Shift your state in the moment."), ("Organization", "Build a steadier baseline."), ("Integration", "Lead from it by default.")]
p = insert_head("Insert 5: Seven areas of focus (stand-up holder)")
p += f'<rect x="40" y="40" width="770" height="226" rx="22" fill="{DEEP}"/>\n' + logo(68, 66, 190, True)
p += lines(786, 94, ["THE METHOD"], 13, 0, LIGHT, weight="700", anchor="end", ls="3")
p += lines(68, 168, ["Seven areas where body,", "emotion and thinking meet."], 44, 51, WHITE, family="DM Serif Display")
p += lines(68, 246, ["Each one tied to how you lead."], 17, 0, LIGHT, weight="700")
for i, (nm, d) in enumerate(AXIS):
    x = 40 + i * 195
    p += f'<rect x="{x}" y="278" width="185" height="62" rx="12" fill="{PALE}"/>'
    p += f'<text x="{x+14}" y="302" font-family="DM Serif Display" font-size="17" fill="{DEEP}">{i+1}  {nm}</text>'
    p += lines(x + 14, 324, [d], 11.5, 0, INK)
for i, (nm, d) in enumerate(AREAS):
    col, row = i % 2, i // 2
    x, y = 40 + col * 391, 358 + row * 120
    w_ = 379 if i < 6 else 770
    p += f'<rect x="{x}" y="{y}" width="{w_}" height="110" rx="16" fill="{LINEN}"/>'
    p += f'<circle cx="{x+30}" cy="{y+32}" r="15" fill="{DEEP}"/><text x="{x+30}" y="{y+38}" text-anchor="middle" font-family="DM Serif Display" font-size="17" fill="{WHITE}">{i+1}</text>'
    p += lines(x + 56, y + 38, [nm], 20, 0, DEEP, family="DM Serif Display")
    rows, cur = [], ""
    for wd in d.split():
        if len(cur) + len(wd) > (34 if w_ == 379 else 80):
            rows.append(cur); cur = wd
        else:
            cur = (cur + " " + wd).strip()
    rows.append(cur)
    p += lines(x + 26, y + 66, rows, 13, 18, INK)
p += lines(40, 850, ["The Soma-Q Assessment you complete when you begin shows which of these need attention first,"], 13.5, 0, DEEP, weight="700")
p += lines(40, 870, ["so your practice is built for your system, not borrowed from someone else’s."], 13.5, 0, DEEP, weight="700")
p += lines(40, 930, ["Built on research-supported practices for nervous system regulation."], 12, 0, "#5C5A53")
p = insert_foot(p)
p += TAIL
(SRC / "insert_areas.html").write_text(p)


# ========================================================= BUSINESS CARD, 3.5 x 2 =========================================================
p = head_("Business card front, 3.5 x 2 in", 3.75, 2.25, "Business card 3.5 x 2 in trim, file 3.75 x 2.25 in (0.125 in bleed). Keep type 0.2 in inside trim. CONFIRM printer template.")
p += f'<rect width="375" height="225" fill="{DEEP}"/>\n'
p += logo(34, 30, 140, True)
p += lines(34, 112, ["Shift", "Happens™"], 25, 27, WHITE, family="DM Serif Display")
p += lines(34, 160, ["NERVOUS SYSTEM", "ALIGNMENT FOR", "HIGH-PERFORMING LEADERS"], 8.4, 12.5, PALE, weight="700", ls=".9")
p += f'<rect x="224" y="22" width="130" height="182" rx="12" fill="#16494F"/>\n'
p += placed("{{FIGURE:dark}}", 289 - 880 * 0.093 / 2, 30, 0.093)
p += TAIL
(SRC / "bizcard2_front.html").write_text(p)

p = head_("Business card front, no image, 3.5 x 2 in", 3.75, 2.25, "Business card front, type only (no figure). Pairs with the same back.")
p += f'<rect width="375" height="225" fill="{DEEP}"/>\n'
p += logo(34, 28, 124, True)
p += lines(34, 92, ["Pressure decides", "whether you react", "or respond."], 20, 24, WHITE, family="DM Serif Display")
p += f'<rect x="34" y="150" width="300" height="1" fill="{LIGHT}" fill-opacity=".5"/>\n'
p += lines(34, 170, ["NERVOUS SYSTEM ALIGNMENT", "FOR HIGH-PERFORMING LEADERS"], 9.2, 13.5, PALE, weight="700", ls="1")
p += TAIL
(SRC / "bizcard2_front_plain.html").write_text(p)

p = head_("Business card back, 3.5 x 2 in", 3.75, 2.25, "Business card back. Two QR codes: book a call, and the free Burnout Signal Check. Phone left off on purpose (the website brief asks whether the phone stays public).")
p += f'<rect width="375" height="225" fill="{LINEN}"/>\n'
p += lines(34, 66, ["Megan", "McDonald"], 22, 24, DEEP, family="DM Serif Display")
p += lines(34, 108, ["Founder of Soma-Q"], 9.2, 0, INK, weight="700")
p += hair(34, 150, 120, op=.35, w=.8)
p += lines(34, 138, ["A nervous system", "alignment practice."], 8, 11, INK)
p += lines(34, 176, ["Megan@Soma-Q.com"], 9, 0, DEEP, weight="700")
p += lines(34, 190, ["soma-q.com"], 9, 0, DEEP, weight="700")
for x, kind, cap in ((172, "CALL", ["Book a free", "discovery call"]), (264, "QUIZ", ["Take the free", "Burnout Signal Check"])):
    p += qr(x, 34, 82, kind)
    p += lines(x + 41, 138, cap, 7.4, 10, DEEP, weight="700", anchor="middle")
p += f'<rect x="172" y="162" width="174" height="30" rx="8" fill="{DEEP}"/>\n'
p += lines(259, 181, ["Two ways to start. Both free."], 8.2, 0, WHITE, weight="700", anchor="middle")
p += TAIL
(SRC / "bizcard2_back.html").write_text(p)


# ========================================================= TABLE COVER, 72 x 30 =========================================================
p = head_("Table cover front, 72 x 30 in", 73, 31, "PLACEHOLDER trim 72 x 30 in, file 73 x 31 in (0.5 in bleed). Viewed from far away and partly hidden by chairs and boxes: logo, two phrases, one QR. CONFIRM the vendor template (hems, folds, corners).")
p += f'<rect width="7300" height="3100" fill="{DEEP}"/><rect y="2160" width="7300" height="940" fill="{LINEN}"/>\n'
p += logo(400, 300, 1500, True)
p += lines(400, 1520, ["Shift Happens™"], 560, 0, WHITE, family="DM Serif Display")
p += lines(400, 1850, ["NERVOUS SYSTEM ALIGNMENT FOR HIGH-PERFORMING LEADERS"], 104, 0, LIGHT, weight="700", ls="10")
p += qr(5500, 300, 1400)
p += lines(6200, 1910, ["Book a free discovery call"], 150, 0, WHITE, family="DM Serif Display", anchor="middle")
p += lines(3650, 2540, ["PRESSURE SHOWS UP IN FOUR PLACES"], 96, 0, DEEP, weight="700", anchor="middle", ls="14")
p += lines(3650, 2880, ["Health  ·  Wealth  ·  Relationships  ·  Career"], 300, 0, DEEP, family="DM Serif Display", anchor="middle")
p += TAIL
(SRC / "table_cover_v2.html").write_text(p)


# ========================================================= BAG TAG (giveaway), 2.5 x 4.25 =========================================================
p = head_("Bag tag front, 2.5 x 4.25 in", 2.75, 4.5, "Bag tag 2.5 x 4.25 in trim, file 2.75 x 4.5 in (0.125 in bleed). PLACEHOLDER: match the vendor's die line, hole position and strap slot. Keep art 0.2 in inside trim.")
p += f'<rect width="275" height="450" fill="{DEEP}"/>\n'
p += f'<circle cx="137.5" cy="58" r="15" fill="none" stroke="{LIGHT}" stroke-width="1.2" stroke-dasharray="3 3"/>'
p += f'<rect x="34" y="112" width="207" height="150" rx="20" fill="{LIGHT}"/>\n'
p += lines(137.5, 168, ["INTERRUPT"], 29, 0, DEEP, weight="700", anchor="middle", ls="3")
p += lines(137.5, 218, ["HERE."], 48, 0, DEEP, family="DM Serif Display", anchor="middle")
p += lines(137.5, 298, ["Notice the signal.", "Locate it.", "Choose your next response."], 13, 20, WHITE, weight="700", anchor="middle")
p += logo(56, 360, 163, True)
p += TAIL
(SRC / "giveaway_tag_front.html").write_text(p)

p = head_("Bag tag back, 2.5 x 4.25 in", 2.75, 4.5, "Bag tag back: owner details lines (so it works as a real bag tag), then the call to action.")
p += f'<rect width="275" height="450" fill="{LINEN}"/>\n'
p += lines(137.5, 92, ["THIS BAG BELONGS TO"], 9.5, 0, DEEP, weight="700", anchor="middle", ls="2.5")
for y, t in ((136, "Name"), (178, "Phone")):
    p += hair(40, 235, y, op=.5, w=1) + lines(40, y + 13, [t], 8.5, 0, "#5C5A53")
p += lines(137.5, 236, ["Pressure happens.", "What do you do next?"], 19, 23, DEEP, family="DM Serif Display", anchor="middle")
p += qr(86, 278, 100)
p += lines(137.5, 396, ["Scan to book a free discovery call"], 9.5, 0, DEEP, weight="700", anchor="middle")
p += lines(137.5, 412, ["SOMA-Q.COM"], 9.5, 0, DEEP, weight="700", anchor="middle", ls="2.5")
p += TAIL
(SRC / "giveaway_tag_back.html").write_text(p)


# ========================================================= BOOKLET, 5.5 x 8.5, 8 pages =========================================================
BW, BH = 575, 875
HEAD = f"""<!doctype html><html lang="en"><head><meta charset="utf-8"><title>Booklet: What do you do next?</title>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;700&family=DM+Serif+Display:ital@0;1&display=swap">
<style>
/* Booklet 5.5 x 8.5 in trim, file 5.75 x 8.75 in (0.125 in bleed), 8 pages, saddle stitch. Pages in reading order. CONFIRM printer template and paper. */
@page {{ size: 5.75in 8.75in; margin: 0; }}
html, body {{ margin: 0; padding: 0; -webkit-print-color-adjust: exact; print-color-adjust: exact; }}
.pg {{ width: 5.75in; height: 8.75in; overflow: hidden; page-break-after: always; break-after: page; }}
.pg:last-child {{ page-break-after: auto; break-after: auto; }}
svg.bk {{ display: block; width: 5.75in; height: 8.75in; }}
</style></head><body>
"""
pages = []


def page(bg, body):
    pages.append(f'<div class="pg"><svg class="bk" viewBox="0 0 {BW} {BH}" xmlns="http://www.w3.org/2000/svg"><rect width="{BW}" height="{BH}" fill="{bg}"/>{body}</svg></div>\n')


def pnum(n, dark=False):
    return lines(BW / 2, 842, [str(n)], 9, 0, LIGHT if dark else "#5C5A53", weight="700", anchor="middle")


# 1 cover
b = logo(46, 50, 190, True)
b += lines(46, 190, ["What do you", "do next?"], 56, 62, WHITE, family="DM Serif Display")
b += lines(46, 296, ["A short guide to noticing pressure sooner,", "and watching your progress in your own numbers."], 12.5, 18, LIGHT, weight="500")
b += placed("{{FIGURE:dark}}", 177, 350, 0.25)
b += lines(BW / 2, 836, ["NERVOUS SYSTEM ALIGNMENT FOR HIGH-PERFORMING LEADERS"], 7.6, 0, PALE, weight="700", anchor="middle", ls="1")
page(DEEP, b)

# 2 neck up
b = lines(46, 92, ["PRESSURE LANDS IN THE BODY FIRST"], 8.8, 0, DEEP, weight="700", ls="2.4")
b += lines(46, 164, ["Leadership does", "not happen from", "the neck up."], 42, 48, DEEP, family="DM Serif Display")
b += lines(46, 330, ["Strategy matters. Emotional intelligence matters. But", "pressure lands in the body before it becomes the", "thought, the tone, the decision or the reaction", "everyone else sees."], 12.5, 19.5, INK)
b += lines(46, 430, ["When your body tightens and your mind speeds up,", "you can lose access to capabilities you already", "have. That is why more information rarely changes", "what happens in the hard moment. A trained", "response does."], 12.5, 19.5, INK)
for i, s in enumerate(STEPS):
    y = 580 + i * 70
    b += f'<rect x="46" y="{y}" width="483" height="56" rx="12" fill="{DEEP}"/><circle cx="76" cy="{y+28}" r="14" fill="{LIGHT}"/>'
    b += f'<text x="76" y="{y+34}" text-anchor="middle" font-family="DM Serif Display" font-size="17" fill="{DEEP}">{i+1}</text>'
    b += lines(104, y + 35, [s], 20, 0, WHITE, family="DM Serif Display")
b += pnum(2)
page(LINEN, b)

# 3 the flow
b = lines(46, 92, ["WHEN PRESSURE HITS"], 8.8, 0, DEEP, weight="700", ls="2.4")
b += lines(46, 150, ["Pressure happens.", "Then what?"], 38, 44, DEEP, family="DM Serif Display")
b += f'<g transform="translate(46,230) scale(0.172)">{decision_flow()}</g>\n'
b += lines(46, 640, ["The moment you notice the signal is the moment you can choose.", "That is what we train."], 14, 21, INK, weight="500")
b += lines(46, 720, ["Left alone, running depleted starts to feel normal.", "It draws down your energy, narrows your thinking and", "wears on your judgment."], 11.5, 17.5, "#5C5A53")
b += pnum(3)
page("#FFFFFF", b)

# 4 skills + four places
b = lines(46, 92, ["THE METHOD"], 8.8, 0, LIGHT, weight="700", ls="2.4")
b += lines(46, 150, ["Regulation is a skill.", "Recovery is a skill.", "Choice under pressure", "is a skill."], 34, 40, WHITE, family="DM Serif Display")
b += lines(46, 330, ["And skills can be practiced, strengthened and measured."], 13, 0, LIGHT, weight="700")
b += lines(46, 392, ["PRESSURE SHOWS UP IN FOUR PLACES"], 8.8, 0, LIGHT, weight="700", ls="2.4")
for i, (nm, d) in enumerate(FOUR):
    x, y = 46 + (i % 2) * 246, 412 + (i // 2) * 188
    b += f'<rect x="{x}" y="{y}" width="237" height="176" rx="14" fill="#16494F"/>'
    b += lines(x + 18, y + 44, [nm], 24, 0, WHITE, family="DM Serif Display")
    words, rows, cur = d.split(), [], ""
    for wd in words:
        if len(cur) + len(wd) > 24:
            rows.append(cur); cur = wd
        else:
            cur = (cur + " " + wd).strip()
    rows.append(cur)
    b += lines(x + 18, y + 74, rows, 11.5, 17, PALE)
b += pnum(4, True)
page(DEEP, b)

# 5 the system (how it is measured)
b = lines(46, 92, ["WHAT MAKES SOMA-Q DIFFERENT"], 8.8, 0, DEEP, weight="700", ls="2.4")
b += lines(46, 150, ["The tools you practice", "also create the data."], 33, 39, DEEP, family="DM Serif Display")
b += lines(46, 232, ["So we can see what is working, what is not, and adjust."], 12.5, 0, INK, weight="700")
cyc = [("1", "Baseline", "Soma-Q Assessment at the start"), ("2", "Weekly", "Soma-Q Weekly Check-In, under five minutes"),
       ("3", "Trended", "SQ-M and SQ-C, tracked separately"), ("4", "Report", "Soma-Q Metrics Report, in plain language"), ("5", "Adjust", "Practice follows the data")]
for i, (n, t, d) in enumerate(cyc):
    y = 262 + i * 52
    b += f'<rect x="46" y="{y}" width="483" height="44" rx="10" fill="{WHITE}"/><circle cx="68" cy="{y+22}" r="12" fill="{DEEP}"/>'
    b += f'<text x="68" y="{y+27}" text-anchor="middle" font-family="DM Serif Display" font-size="14" fill="{WHITE}">{n}</text>'
    b += lines(92, y + 27, [t], 15, 0, DEEP, family="DM Serif Display")
    b += lines(168, y + 27, [d], 10.2, 0, INK)
b += lines(46, 548, ["SQ-LPMS: ONE SYSTEM, TWO SEPARATE MEASURES"], 8.2, 0, DEEP, weight="700", ls="1.8")
for x, tag, nm, desc, fill in ((46, "THE CAUSE", "SQ-M", ["Soma-Q Method Metrics.", "Is the method landing in the", "body and nervous system?"], WHITE),
                               (294, "THE EFFECT", "SQ-C", ["Soma-Q Leadership Competencies.", "Is the change showing up", "in how you lead?"], PALE)):
    b += f'<rect x="{x}" y="562" width="235" height="132" rx="14" fill="{fill}"/>'
    b += lines(x + 16, 586, [tag], 7.8, 0, DEEP, weight="700", ls="2")
    b += lines(x + 16, 622, [nm], 26, 0, DEEP, family="DM Serif Display")
    b += lines(x + 16, 644, desc, 10.2, 14, INK)
b += lines(46, 726, ["Kept apart on purpose, so a strong quarter of results", "cannot hide growing strain, and a slow start is not", "mistaken for a lack of capability."], 11.5, 17, INK)
b += pnum(5)
page(LINEN, b)

# 6 sample report: senior leader
b = lines(46, 92, ["WHAT A REPORT LOOKS LIKE"], 8.8, 0, DEEP, weight="700", ls="2.4")
b += lines(46, 150, ["Example: a senior leader,", "16 weeks in."], 30, 36, DEEP, family="DM Serif Display")
rows = [("Stress recovery", "Somatic", 7.6, 4.2), ("Emotional steadiness", "Emotional", 7.1, 4.8), ("Clear thinking", "Cognitive", 7.2, 4.5)]
b += f'<rect x="46" y="200" width="483" height="270" rx="16" fill="{LINEN}"/>'
b += bars(70, 252, 435, rows, 68, 15.5)
b += f'<circle cx="72" cy="448" r="5" fill="{WHITE}" stroke="{LIGHT}" stroke-width="2.5"/>' + lines(84, 452, ["Week 1"], 9.5, 0, INK) + f'<rect x="130" y="443" width="18" height="8" rx="4" fill="{DEEP}"/>' + lines(154, 452, ["Now"], 9.5, 0, INK)
b += lines(46, 520, ["Every measure is above where it started, and the", "body-based measures moved first."], 13, 19, INK, weight="700")
b += lines(46, 580, ["The largest gain is in staying calm under pressure,", "up four points since week 1."], 12.5, 19, INK)
b += lines(46, 630, ["One measure is still behind: focus late in the day.", "That is where the next phase of practice goes."], 12.5, 19, INK)
b += f'<rect x="46" y="690" width="483" height="84" rx="14" fill="{LINEN}"/>'
b += lines(66, 718, ["WHAT YOU KEEP"], 8.4, 0, DEEP, weight="700", ls="2.4")
b += lines(66, 744, ["Your Metrics Report, your session notes and your", "practice reference guides."], 12, 17, INK, weight="700")
b += lines(46, 810, [NOT_DATA], 9.5, 0, "#5C5A53")
b += pnum(6)
page("#FFFFFF", b)

# 7 hard week
b = lines(46, 92, ["AND A HARD WEEK, SHOWN PLAINLY"], 8.8, 0, LIGHT, weight="700", ls="2.4")
b += lines(46, 150, ["Example: a founder,", "week 11."], 30, 36, WHITE, family="DM Serif Display")
rows = [("Stress recovery", "Somatic", 6.1, 4.0), ("Emotional steadiness", "Emotional", 5.0, 4.4), ("Clear thinking", "Cognitive", 5.8, 4.9)]
b += f'<rect x="46" y="200" width="483" height="270" rx="16" fill="{WHITE}"/>'
b += bars(70, 252, 435, rows, 68, 15.5)
b += lines(46, 520, ["A demanding stretch pulled emotional steadiness down", "from last week, and the check-in shows it plainly."], 12.5, 19, WHITE, weight="700")
b += lines(46, 580, ["Stress recovery held steady through it. The hard days", "still came, but they no longer took the whole week."], 12.5, 19, PALE)
b += lines(46, 630, ["The long view still points up: every measure is above", "week 1, and bouncing back is the one moving fastest."], 12.5, 19, PALE)
b += lines(46, 770, [NOT_DATA], 9.5, 0, LIGHT)
b += lines(46, 800, ["Soma-Q is an education and training practice. No score is a medical or psychological measure."], 8.2, 0, LIGHT)
b += pnum(7, True)
page(DEEP, b)

# 8 back cover
b = lines(46, 112, ["Every path starts", "with a conversation."], 38, 44, DEEP, family="DM Serif Display")
b += lines(46, 220, ["On a discovery call we look at what pressure is costing", "you right now and whether this work is the right fit,", "with no obligation to go further."], 12.5, 19.5, INK)
b += f'<rect x="46" y="300" width="483" height="290" rx="20" fill="{DEEP}"/>'
b += qr(76, 332, 226)
b += lines(326, 372, ["Book a free", "discovery call."], 26, 30, WHITE, family="DM Serif Display")
b += lines(326, 452, ["Scan the code, or", "visit soma-q.com."], 12.5, 18, PALE)
b += lines(326, 492, ["Not ready? Take the", "free Burnout Signal Check."], 11.5, 16, LIGHT, weight="700")
b += qr(326, 526, 52, "QUIZ", 0.06)
b += logo(46, 648, 180, False)
b += lines(46, 750, ["Megan McDonald, Founder of Soma-Q", "Megan@Soma-Q.com  ·  soma-q.com"], 11, 16, DEEP, weight="700")
b += lines(46, 806, ["Soma-Q is an education and training practice. It does not diagnose, treat or manage any", "condition and does not replace care from a qualified health provider."], 7.6, 11, "#5C5A53")
page(LINEN, b)
(SRC / "booklet.html").write_text(HEAD + "".join(pages) + "</body></html>\n")
print("ok round2")


# ========================================================= CARD SET (business-card size), 5 cards, 10 sides =========================================================
CW, CH = 375, 225
CHEAD = f"""<!doctype html><html lang="en"><head><meta charset="utf-8"><title>Card set: pressure decides, four places</title>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;700&family=DM+Serif+Display:ital@0;1&display=swap">
<style>
/* Card set 3.5 x 2 in trim, file 3.75 x 2.25 in (0.125 in bleed). 10 pages: front and back of 5 cards. Same stock as the business card. Draft questions need approval. */
@page {{ size: 3.75in 2.25in; margin: 0; }}
html, body {{ margin: 0; padding: 0; -webkit-print-color-adjust: exact; print-color-adjust: exact; }}
.pg {{ width: 3.75in; height: 2.25in; overflow: hidden; page-break-after: always; break-after: page; }}
.pg:last-child {{ page-break-after: auto; break-after: auto; }}
svg.cd {{ display: block; width: 3.75in; height: 2.25in; }}
</style></head><body>
"""
cpages = []


def cpage(bg, body):
    cpages.append(f'<div class="pg"><svg class="cd" viewBox="0 0 {CW} {CH}" xmlns="http://www.w3.org/2000/svg"><rect width="{CW}" height="{CH}" fill="{bg}"/>{body}</svg></div>\n')


# card 0: the idea
b = logo(34, 30, 104, True)
b += lines(34, 96, ["Pressure decides", "whether you react", "or respond."], 21, 26, WHITE, family="DM Serif Display")
b += lines(34, 176, ["NERVOUS SYSTEM ALIGNMENT", "FOR HIGH-PERFORMING LEADERS"], 8.6, 12.5, PALE, weight="700", ls=".9")
cpage(DEEP, b)
b = lines(34, 62, ["Shift outcomes in the", "four places pressure", "shows up:"], 13.5, 18, DEEP, family="DM Serif Display")
b += qr(34, 128, 58, "CALL")
b += lines(100, 150, ["Book a free", "discovery call"], 8.4, 11.5, DEEP, weight="700")
for i, nm in enumerate(["Health", "Wealth", "Relationships", "Career"]):
    y = 70 + i * 30
    b += f'<circle cx="212" cy="{y-5}" r="4" fill="{LIGHT}"/>' + lines(226, y, [nm], 17, 0, DEEP, family="DM Serif Display")
cpage(LINEN, b)

# cards 1 to 4: the four places
PLACE_Q = {"Health": ["Where in your body", "does it land first?"],
           "Wealth": ["What decision are you", "making from pressure", "right now?"],
           "Relationships": ["Who is feeling it", "with you?"],
           "Career": ["Where are you leading", "well and running", "on empty?"]}
PLACE_CARDS = False   # the four place cards were dropped from the review set (Oct 13); flip to True to rebuild them
for i, (nm, d) in enumerate(FOUR if PLACE_CARDS else []):
    b = f'<circle cx="327" cy="48" r="13" fill="{LIGHT}"/><text x="327" y="53" text-anchor="middle" font-family="DM Serif Display" font-size="14" fill="{DEEP}">{i+1}</text>'
    b += lines(34, 56, ["PRESSURE SHOWS UP IN"], 7.2, 0, LIGHT, weight="700", ls="2.2")
    b += lines(34, 104, [nm], 33, 0, WHITE, family="DM Serif Display")
    rows, cur = [], ""
    for wd in d.split():
        if len(cur) + len(wd) > 40:
            rows.append(cur); cur = wd
        else:
            cur = (cur + " " + wd).strip()
    rows.append(cur)
    b += lines(34, 132, rows, 10.2, 14.5, PALE)
    b += lines(34, 192, ["SOMA-Q.COM"], 7.6, 0, LIGHT, weight="700", ls="2")
    cpage(DEEP, b)
    b = lines(34, 54, ["NOTICE THE SIGNAL. LOCATE IT.", "CHOOSE YOUR NEXT RESPONSE."], 6.8, 10, DEEP, weight="700", ls="1.4")
    b += lines(34, 102, PLACE_Q[nm], 19, 23, DEEP, family="DM Serif Display")
    b += lines(34, 190, ["Pressure decides whether you", "react or respond."], 8.2, 11, "#5C5A53", style="italic")
    b += qr(284, 128, 56, "CALL")
    b += lines(312, 196, ["Book a call"], 7, 0, DEEP, weight="700", anchor="middle")
    cpage(LINEN, b)
(SRC / "card_set.html").write_text(CHEAD + "".join(cpages) + "</body></html>\n")


# ========================================================= PAPER QUIZ CARD (Burnout Signal Check), 5.5 x 8.5 =========================================================
QW, QH = 575, 875
QHEAD = CHEAD.replace("3.75in", "5.75in").replace("2.25in", "8.75in").replace("svg.cd", "svg.qz").replace("Card set: pressure decides, four places", "Burnout Signal Check, paper card")
QHEAD = QHEAD.replace("Card set 3.5 x 2 in trim, file 3.75 x 2.25 in (0.125 in bleed). 10 pages: front and back of 5 cards. Same stock as the business card. Draft questions need approval.", "Paper Burnout Signal Check 5.5 x 8.5 in trim, file 5.75 x 8.75 in (0.125 in bleed). Page 1 questions, page 2 result. Wording is the live quiz wording.")
qpages = []


def qpage(bg, body):
    qpages.append(f'<div class="pg"><svg class="qz" viewBox="0 0 {QW} {QH}" xmlns="http://www.w3.org/2000/svg"><rect width="{QW}" height="{QH}" fill="{bg}"/>{body}</svg></div>\n')


QUIZ = [("1", "How long have you been feeling this way?", "Tick one.", [("Less than 6 months", ""), ("6 to 12 months", ""), ("1 to 2 years", ""), ("Several years or more", "")]),
        ("2", "What is your body telling you?", "Tick all that apply.", [("Tension I cannot release in my jaw, shoulders, or chest", ""), ("Exhaustion that sleep does not fix", "▲"), ("Wired and restless. I cannot power down", ""), ("Numb. I do not feel much of anything anymore", "▲"), ("None of these", "")]),
        ("3", "What is happening in your thinking mind?", "Tick all that apply.", [("Brain fog. Thoughts feel slow and scattered", ""), ("Racing thoughts I cannot quiet", ""), ("Simple decisions feel heavy", ""), ("I am in the room, but I am not present", ""), ("None of these", "")]),
        ("4", "What is happening underneath?", "Tick all that apply.", [("Emotionally flat. Things that used to matter do not land", ""), ("Reactive. Irritation surfaces faster than it should", ""), ("Going through the motions", ""), ("I have lost the thread of who I am outside of performing", "★"), ("None of these", "")]),
        ("5", "How much access do you have to your full energy, clarity, and joy?", "Tick one.", [("Most days, I can still get there", ""), ("It comes and goes", ""), ("It is mostly offline", "◆"), ("I cannot remember the last time I had full access", "★ ◆")])]
b = f'<rect width="{QW}" height="150" fill="{DEEP}"/>' + logo(40, 30, 150, True)
b += lines(535, 62, ["FREE · 2 MINUTES"], 8, 0, LIGHT, weight="700", anchor="end", ls="2.4")
b += lines(40, 124, ["Burnout Signal Check"], 31, 0, WHITE, family="DM Serif Display")
y = 182
for n, q, hint, opts in QUIZ:
    b += f'<circle cx="52" cy="{y-4}" r="11" fill="{DEEP}"/><text x="52" y="{y}" text-anchor="middle" font-family="DM Serif Display" font-size="14" fill="{WHITE}">{n}</text>'
    b += lines(72, y, [q], 11.6, 0, DEEP, weight="700")
    b += lines(535, y, [hint], 8.2, 0, "#5C5A53", anchor="end")
    y += 17
    for txt, mk in opts:
        b += f'<rect x="58" y="{y-8.5}" width="9" height="9" rx="2" fill="none" stroke="{DEEP}" stroke-width="1.1"/>'
        b += lines(76, y, [txt], 9.6, 0, INK)
        if mk:
            b += lines(535, y, [mk], 9.6, 0, LIGHT, weight="700", anchor="end")
        y += 19.8
    y += 11
b += lines(BW / 2 if False else 287.5, 846, ["Turn over for your result.   Not a diagnosis: a conversation starter."], 8.6, 0, DEEP, weight="700", anchor="middle")
qpage("#FFFFFF", b)

TIERS = [("1", "Long-term Dysregulation", ["Did you tick “Several years or more” in question 1,", "AND any answer marked ★?"], "Years of chronic dysregulation. The pattern has started to feel like who you are.", "Energy: running low   ·   Clarity: often clouded   ·   Joy: hard to reach", DEEP, WHITE, LIGHT),
         ("2", "Chronic Dysregulation", ["Not step 1, but: did you tick “1 to 2 years” or “Several years or more”?", "OR a ▲ answer in question 2 together with a ◆ answer in question 5?"], "Your system has been in survival mode for months to years, and it has become the baseline.", "Energy: depleted   ·   Clarity: fragmented   ·   Joy: offline", PALE, DEEP, DEEP),
         ("3", "Early Dysregulation", ["None of the above?"], "Early signals are present and your system still has capacity. A good time to act, before patterns deepen.", "Energy: strained   ·   Clarity: interrupted   ·   Joy: dimming", WHITE, DEEP, DEEP)]
b = lines(40, 70, ["YOUR RESULT"], 8.8, 0, DEEP, weight="700", ls="2.6")
b += lines(40, 116, ["Follow the steps in order.", "Stop at your first yes."], 27, 32, DEEP, family="DM Serif Display")
y = 180
for n, nm, cond, mean, st, fill, fg, sub in TIERS:
    h = 142
    b += f'<rect x="40" y="{y}" width="495" height="{h}" rx="16" fill="{fill}"/>'
    b += f'<circle cx="68" cy="{y+30}" r="14" fill="{fg}"/><text x="68" y="{y+36}" text-anchor="middle" font-family="DM Serif Display" font-size="17" fill="{fill}">{n}</text>'
    b += lines(92, y + 36, [nm], 19, 0, fg, family="DM Serif Display")
    b += lines(58, y + 66, cond, 9.8, 14, fg, weight="700")
    b += lines(58, y + 104 + (0 if len(cond) == 2 else -14), [mean], 9.6, 0, fg)
    b += lines(58, y + 126 + (0 if len(cond) == 2 else -14), [st], 8.8, 0, sub, weight="700")
    y += h + 12
b += f'<rect x="40" y="{y}" width="495" height="160" rx="16" fill="{DEEP}"/>'
b += qr(60, y + 25, 110, "CALL")
b += lines(190, y + 56, ["Book a free", "discovery call."], 24, 28, WHITE, family="DM Serif Display")
b += lines(190, y + 112, ["Whatever your result, a conversation is the", "next step. We look at what pressure is costing", "you and match you to the right level of support."], 9.4, 13.5, PALE)
b += lines(40, 846, ["Soma-Q is an education and training practice. It does not diagnose, treat or manage any condition. This check is not a medical or psychological measure."], 6.9, 0, "#5C5A53")
qpage(LINEN, b)
(SRC / "quiz_card.html").write_text(QHEAD + "".join(qpages) + "</body></html>\n")
print("ok cards+quiz")
