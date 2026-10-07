# Soma-Q Event Booth Package

Print-ready booth art, an internal strategy packet and an order guide, built for the October 24, 2026 event and reusable for later ones.

Start with `output/strategy_packet.pdf` (the plan) and `output/order_guide.pdf` (what to buy, where, and when).

## Print files (`output/`)
| File | Piece | Trim |
| --- | --- | --- |
| banner_retractable.pdf, banner_retractable_photo.pdf | Retractable banner, without and with photo | 32 x 80 in |
| backdrop.pdf, backdrop_photo.pdf | Optional backdrop, without and with photo | 120 x 90 in (placeholder) |
| table_front.pdf | Table front panel | 72 x 30 in (placeholder) |
| counter_sign.pdf | Counter sign, four free first steps plus POPL | 8.5 x 11 in |
| card_individual.pdf | Take-home card, two sides | 4 x 6 in |
| sheet_organizations.pdf | Organizations one-sheet | 8.5 x 11 in |
| business_card.pdf | New business card, two sides | 3.5 x 2 in |
| qr_urls.txt, redirects_for_designer.md | Every QR address, and the redirects the website needs |
| lead_tracker_template.csv (project root) | Lead tracker |

All files include bleed. Sizes marked placeholder must be matched to the vendor's template before final export.

## Rebuild
1. Put the logos, photo and POPL QR in `assets/` (see `assets/README.md`).
2. Edit `build/config.py` (event name, venue, booth number, QR destinations, phone).
3. `pip install segno`, then `python3 build/build.py` from this folder. Needs Chromium and poppler-utils.

Brand rules applied: six-color palette, no gold or copper, DM Serif Display and DM Sans, no em or en dashes, outcome-first copy.
