#!/usr/bin/env python3
"""Second table sign, 8.5 x 11 in portrait (file 8.75 x 11.25 in): the free ebook The Missing Intelligence, with the cover, three things inside, and a QR to /go/ebook.
Companion to the Five Signs table sign (same border, triangle and QR plate). DRAFT: confirm the ebook version and the QR destination."""
from svgkit import *
from svgkit import head as head_

W, H = 875, 1125
p = head_("Table sign: Free ebook, The Missing Intelligence, 8.5 x 11 in", 8.75, 11.25, "Table sign 8.5 x 11 in trim, file 8.75 x 11.25 in (0.125 in bleed). Free ebook The Missing Intelligence: cover, what is inside, QR to the ebook signup (/go/ebook). CONFIRM the ebook version and the destination link.")
p += f'<rect width="{W}" height="{H}" fill="{DEEP}"/>\n'
p += f'<rect x="35" y="35" width="{W-70}" height="{H-70}" rx="18" fill="none" stroke="{LINEN}" stroke-opacity=".85" stroke-width="2.5"/>\n'
CX = W / 2
p += f'<polygon points="650,790 1010,1330 290,1330" fill="none" stroke="{LIGHT}" stroke-opacity=".16" stroke-width="4"/>\n'
p += logo(70, 62, 170, True)
p += lines(70, 165, ["FREE EBOOK"], 14, 0, LIGHT, weight="700", ls="3.5")
p += lines(70, 248, ["The Missing", "Intelligence."], 62, 70, WHITE, family="DM Serif Display")
p += lines(70, 385, ["What is quietly costing you energy,", "clarity, and joy, and the intelligence", "most leaders were never taught to use."], 21, 30, PALE, weight="500")
# cover, with a soft shadow
cw, ch = 250, 323
cx0, cy0 = 70, 500
p += f'<defs><filter id="sh" x="-20%" y="-20%" width="140%" height="140%"><feDropShadow dx="0" dy="6" stdDeviation="8" flood-color="#000" flood-opacity=".45"/></filter></defs>'
p += f'<image href="{{{{EBOOK_COVER_URI}}}}" x="{cx0}" y="{cy0}" width="{cw}" height="{ch}" filter="url(#sh)" preserveAspectRatio="xMidYMid meet"/>\n'
p += f'<rect x="{cx0}" y="{cy0}" width="{cw}" height="{ch}" fill="none" stroke="{LINEN}" stroke-opacity=".5" stroke-width="1.5"/>\n'
# what is inside
p += lines(380, 535, ["INSIDE"], 13, 0, LIGHT, weight="700", ls="3")
rows = ["The Triad Intelligence Model™", "What the research suggests", "A two-minute self-check", "Five practices for the middle of a workday"]
for i, t in enumerate(rows):
    y = 580 + i * 62
    p += f'<polygon points="380,{y} 392,{y} 386,{y-10.4}" fill="{LINEN}"/>'
    p += lines(404, y, [t], 19, 0, WHITE, weight="700")
p += lines(380, 840, ["A short read. Free."], 24, 0, LINEN, family="DM Serif Display")
# QR in the triangle
TX = 650; qs = 112; qx, qy = TX - qs / 2, 922
p += f'<rect x="{qx-9}" y="{qy-9}" width="{qs+18}" height="{qs+18}" rx="12" fill="{LINEN}"/>\n'
p += f'<rect x="{qx}" y="{qy}" width="{qs}" height="{qs}" rx="7" fill="#FFFFFF"/><svg x="{qx+7}" y="{qy+7}" width="{qs-14}" height="{qs-14}">{{{{QR_EBOOK}}}}</svg>'
p += lines(TX, 1062, ["Scan for your free copy"], 13, 0, WHITE, weight="700", anchor="middle")
p += lines(70, 1062, ["SOMA-Q.COM"], 15, 0, LIGHT, weight="700", ls="3")
p += TAIL
(SRC / "table_sign_ebook.html").write_text(p)
print("ok ebook sign")
