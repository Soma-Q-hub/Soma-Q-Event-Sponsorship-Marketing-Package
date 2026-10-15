#!/usr/bin/env python3
"""Free drawing pieces: table sign (8.5 x 11 in, no QR) and the paper entry slip (4.25 x 5.5 in, 4-up on a letter sheet).
Prize wording has no dollar value (not stated by Megan). Fine print is a DRAFT for review (state drawing rules, event rules)."""
from svgkit import *
from svgkit import head as head_

# ---------------------------------------------------------------- TABLE SIGN
W, H = 875, 1125
p = head_("Table sign: Win a free 60-minute session, 8.5 x 11 in", 8.75, 11.25, "Table sign 8.5 x 11 in trim, file 8.75 x 11.25 in (0.125 in bleed). Free drawing: fill out an entry slip and drop it in the box. No QR. Fine print is a DRAFT: confirm drawing rules and any event rules.")
p += f'<rect width="{W}" height="{H}" fill="{DEEP}"/>\n'
p += f'<rect x="35" y="35" width="{W-70}" height="{H-70}" rx="18" fill="none" stroke="{LINEN}" stroke-opacity=".85" stroke-width="2.5"/>\n'
p += f'<polygon points="650,790 1010,1330 290,1330" fill="none" stroke="{LIGHT}" stroke-opacity=".16" stroke-width="4"/>\n'
p += logo(70, 62, 170, True)
p += lines(70, 165, ["FREE DRAWING"], 14, 0, LIGHT, weight="700", ls="3.5")
p += lines(70, 255, ["Win a free", "60-minute session", "with Megan."], 66, 76, WHITE, family="DM Serif Display")
steps = [("1", "Fill out an entry slip."), ("2", "Drop it in the box. Add your business card if you like."), ("3", "A winner is drawn and emailed.")]
y0 = 530
for i, (n, t) in enumerate(steps):
    y = y0 + i * 92
    p += f'<circle cx="{70+26}" cy="{y}" r="26" fill="{LINEN}"/><text x="{70+26}" y="{y+9}" text-anchor="middle" font-family="DM Sans" font-weight="700" font-size="26" fill="{DEEP}">{n}</text>'
    p += lines(70 + 74, y + 8, [t], 25, 0, WHITE, weight="700")
p += lines(70, 840, ["Entry slips are right here."], 34, 0, LINEN, family="DM Serif Display")
p += lines(70, 1000, ["No purchase necessary. One entry per person."], 14, 18, PALE, weight="500")
p += lines(70, 1020, ["Winner is drawn at random and contacted by email."], 14, 18, PALE, weight="500")
p += lines(70, 1062, ["SOMA-Q.COM"], 15, 0, LIGHT, weight="700", ls="3")
p += TAIL
(SRC / "table_sign_raffle.html").write_text(p)

# ---------------------------------------------------------------- TABLE SIGN
W, H = 875, 1125
p = head_("Table sign: Win a free 60-minute session, fade version, 8.5 x 11 in", 8.75, 11.25, "Table sign 8.5 x 11 in trim, file 8.75 x 11.25 in (0.125 in bleed). Free drawing: fill out an entry slip and drop it in the box. No QR. Fine print is a DRAFT: confirm drawing rules and any event rules.")
p += f'<defs><linearGradient id="fade" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{DEEP}"/><stop offset=".68" stop-color="{DEEP}"/><stop offset=".84" stop-color="{LINEN}"/><stop offset="1" stop-color="{LINEN}"/></linearGradient></defs><rect width="{W}" height="{H}" fill="url(#fade)"/>\n'
p += f'<rect x="35" y="35" width="{W-70}" height="{H-70}" rx="18" fill="none" stroke="{LINEN}" stroke-opacity=".85" stroke-width="2.5"/>\n'
p += f'<clipPath id="inframe"><rect x="35" y="35" width="{W-70}" height="{H-70}" rx="18"/></clipPath><linearGradient id="trifade" gradientUnits="userSpaceOnUse" x1="0" y1="110" x2="0" y2="560"><stop offset="0" stop-color="{LINEN}" stop-opacity=".9"/><stop offset="1" stop-color="{LIGHT}" stop-opacity=".75"/></linearGradient><polygon clip-path="url(#inframe)" points="745,110 1000,560 490,560" fill="none" stroke="url(#trifade)" stroke-width="5"/>\n'
p += logo(70, 62, 170, True)
p += lines(70, 165, ["FREE DRAWING"], 14, 0, LIGHT, weight="700", ls="3.5")
p += lines(70, 255, ["Win a free", "60-minute session", "with Megan."], 66, 76, WHITE, family="DM Serif Display")
steps = [("1", "Fill out an entry slip."), ("2", "Drop it in the box."), ("3", "Add your business card for an additional entry."), ("4", "A winner is drawn and emailed.")]
y0 = 530
for i, (n, t) in enumerate(steps):
    y = y0 + i * 92
    p += f'<circle cx="{70+26}" cy="{y}" r="26" fill="{LINEN}"/><text x="{70+26}" y="{y+9}" text-anchor="middle" font-family="DM Sans" font-weight="700" font-size="26" fill="{DEEP}">{n}</text>'
    p += lines(70 + 74, y + 8, [t], 25, 0, WHITE, weight="700")
p += lines(70, 985, ["Valued @ $397.00"], 46, 0, DEEP, family="DM Serif Display")
p += lines(70, 1030, ["No purchase necessary. One entry per person, plus one additional entry with a business card."], 14, 18, DEEP, weight="500")
p += lines(70, 1050, ["Winner is drawn at random and contacted by email."], 14, 18, DEEP, weight="500")
p += lines(70, 1085, ["SOMA-Q.COM"], 15, 0, DEEP, weight="700", ls="3")
p += TAIL
(SRC / "table_sign_raffle_fade.html").write_text(p)

# ---------------------------------------------------------------- ENTRY SLIP 4.25 x 5.5
W, H = 450, 575
p = head_("Raffle entry slip, 4.25 x 5.5 in", 4.5, 5.75, "Entry slip 4.25 x 5.5 in trim, file 4.5 x 5.75 in (0.125 in bleed); four fit on a letter sheet. Fine print is a DRAFT: confirm drawing rules; the contact opt-in is optional and separate from the entry.")
p += f'<rect width="{W}" height="{H}" fill="#FFFFFF"/>\n'
p += f'<rect width="{W}" height="150" fill="{DEEP}"/>\n'
p += logo(34, 28, 100, True)
p += lines(34, 94, ["Enter to win a free"], 21, 0, WHITE, family="DM Serif Display")
p += lines(34, 120, ["60-minute session with Megan."], 21, 0, LIGHT, family="DM Serif Display")
for i, lab in enumerate(["Name", "Email", "Company and title"]):
    y = 215 + i * 62
    p += lines(34, y - 24, [lab.upper()], 8.5, 0, DEEP, weight="700", ls="1.6")
    p += f'<rect x="34" y="{y}" width="{W-68}" height="1.2" fill="{DEEP}" fill-opacity=".55"/>\n'
p += f'<rect x="34" y="395" width="15" height="15" rx="2" fill="none" stroke="{DEEP}" stroke-width="1.4"/>'
p += lines(60, 407, ["Yes, send me occasional emails from Soma-Q.", "I can unsubscribe any time. (Optional.)"], 10.5, 15, DEEP, weight="500")
p += lines(34, 452, ["Have a business card? Add it for an additional entry."], 10.5, 0, DEEP, weight="700")
p += f'<rect x="34" y="470" width="{W-68}" height="1" fill="{DEEP}" fill-opacity=".2"/>\n'
p += lines(34, 487, ["No purchase necessary. One entry per person, plus one additional entry", "with a business card. A winner is drawn at random and contacted by email.", "Prize: one 60-minute session with Megan McDonald."], 8, 11, INK, weight="500")
p += lines(34, 530, ["SOMA-Q.COM"], 9, 0, DEEP, weight="700", ls="2")
p += TAIL
(SRC / "raffle_slip.html").write_text(p)
print("ok raffle")
