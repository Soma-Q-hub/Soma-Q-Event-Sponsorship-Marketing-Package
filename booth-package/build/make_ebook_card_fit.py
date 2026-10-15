#!/usr/bin/env python3
"""Ebook card resized for the YAHQNIG magnetic frameless acrylic holder (the listing's page address says 2.95 x 4.13 in; shown here landscape).
Trim 4 x 2.8 in (a little under the holder), plus 0.25 in bleed on every side: file 4.5 x 3.3 in. Larger type, title reads 'The Missing Intelligence E-Book'.
Type and QR stay 0.3 in inside the trim so the corner magnets never cover them. CONFIRM the holder's display size before printing."""
from svgkit import *
from svgkit import head as head_
W, H = 450, 330
p = head_("Ebook card, The Missing Intelligence E-Book, 4 x 2.8 in trim", 4.5, 3.3, "Ebook card for the 2.95 x 4.13 in acrylic holder shown landscape. Trim 4 x 2.8 in, file 4.5 x 3.3 in (0.25 in bleed). Type kept 0.3 in inside the trim.")
p += f'<rect width="{W}" height="{H}" fill="#FFFFFF"/>\n'
qw = 270; qh = qw * 376 / 367
p += f'<g opacity=".5">' + qmark(W / 2 - qw / 2, H / 2 - qh / 2, qw, True) + '</g>\n'
p += lines(58, 112, ["The Missing", "Intelligence", "E-Book"], 37, 41, DEEP, family="DM Serif Display")
p += lines(58, 240, ["Scan for your free copy."], 16.5, 0, DEEP, weight="700")
qs = 116; qx, qy = 272, 107
p += f'<rect x="{qx-6}" y="{qy-6}" width="{qs+12}" height="{qs+12}" rx="9" fill="{LINEN}"/><rect x="{qx}" y="{qy}" width="{qs}" height="{qs}" rx="6" fill="#FFFFFF" stroke="{DEEP}" stroke-width="1"/><svg x="{qx+6}" y="{qy+6}" width="{qs-12}" height="{qs-12}">{{{{QR_EBOOK}}}}</svg>'
p += TAIL
(SRC / "ebook_card_fit.html").write_text(p)
print("ok ebook card fit")
