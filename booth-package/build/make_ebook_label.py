#!/usr/bin/env python3
"""Display-copy card, 4 x 2.5 in trim (file 4.25 x 2.75 in, 0.125 in bleed). Sits on or beside the printed display copies of The Missing Intelligence:
makes clear it is for looking at, and sends people to their own free copy. DRAFT."""
from svgkit import *
from svgkit import head as head_
W, H = 425, 275
p = head_("Display copy card, The Missing Intelligence, 4 x 2.5 in", 4.25, 2.75, "Display copy card 4 x 2.5 in trim, file 4.25 x 2.75 in (0.125 in bleed). Tells visitors this printout is for looking at and where to scan for their own free copy. CONFIRM the ebook link (/go/ebook).")
p += f'<rect width="{W}" height="{H}" fill="#FFFFFF"/>\n'
p += lines(36, 66, ["DISPLAY COPY"], 8.5, 0, "#3E807A", weight="700", ls="2.4")
p += lines(36, 98, ["The Missing", "Intelligence."], 28, 31, DEEP, family="DM Serif Display")
p += lines(36, 172, ["Please leave this copy here."], 11, 0, INK, weight="500")
p += lines(36, 190, ["Scan for your own, free."], 11, 0, DEEP, weight="700")
p += lines(36, 232, ["SOMA-Q.COM"], 7.5, 0, "#3E807A", weight="700", ls="2")
qs = 112; qx, qy = 277, 80
p += f'<rect x="{qx-6}" y="{qy-6}" width="{qs+12}" height="{qs+12}" rx="9" fill="{LINEN}"/><rect x="{qx}" y="{qy}" width="{qs}" height="{qs}" rx="6" fill="#FFFFFF" stroke="{DEEP}" stroke-width="1"/><svg x="{qx+6}" y="{qy+6}" width="{qs-12}" height="{qs-12}">{{{{QR_EBOOK}}}}</svg>'
p += TAIL
(SRC / "ebook_display_card.html").write_text(p)
print("ok")
