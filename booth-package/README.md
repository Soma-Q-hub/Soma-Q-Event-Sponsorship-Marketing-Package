# Soma-Q Event Booth Package

Print-ready booth art, an internal strategy packet and an order guide, built for the October 24, 2026 event and reusable for later ones.

**Inline previews:** every page of every piece is a PNG in `output/preview/`, with a gallery in `output/PREVIEW.md` and `output/preview.html`. The PDFs in `output/` are the print files.

Start with `output/strategy_packet.pdf` (the plan, including the buyer's-eye view) and `output/order_guide.pdf` (what to buy, where, and when).

## Print files (`output/`)
| File | Piece | Trim |
| --- | --- | --- |
| banner_story.pdf | Banner 1: the question, what Soma-Q does, the Pressure Loop. No QR. | 32 x 80 in |
| banner_proof.pdf, banner_proof_photo.pdf | Banner 2: outcomes, weekly-progress example, who is behind it. With and without photo. No QR. | 32 x 80 in |
| table_front.pdf | Table cover front | 72 x 30 in (placeholder) |
| backdrop.pdf, backdrop_photo.pdf | Optional backdrop: the whole story on one wall | 120 x 90 in (placeholder) |
| poster_loop, poster_shift, poster_outcomes, poster_where | Explainer posters | 24 x 36 in |
| poster_progress, poster_capacity | Measurement posters from the Measurement Overview | 24 x 36 in |
| counter_sign.pdf | What Soma-Q does, four free first steps, POPL | 8.5 x 11 in |
| card_individual.pdf | Take-home card: body map front, loop and four scans back | 4 x 6 in |
| leavebehind.pdf | Working with Soma-Q: for you (front), for your team (back) | 8.5 x 11 in |
| handout_measurement.pdf | Measurement at a glance, for organizations | 8.5 x 11 in |
| business_card.pdf | Business card | 3.5 x 2 in |
| qr_urls.txt, redirects_for_designer.md | Every QR address, and the redirects the website needs | |

All files include bleed. Sizes marked placeholder must be matched to the vendor's template before final export. `lead_tracker_template.csv` is the lead tracker.

## Rebuild
1. Assets are in `assets/` (original-resolution logos from Drive, web-size photo). Add `popl-qr.png` from the POPL app.
2. Edit `build/config.py` (QR destinations, phone, campaign).
3. `pip install segno playwright`, then from this folder: `python3 build/build.py`. Needs Chromium and poppler-utils.
4. Layout check: `QA=1 python3 build/build.py` renders every piece in Chromium and reports text outside its sheet, overlaps, clipping, spills to a second sheet, placeholders and dash characters.
5. Generators for the SVG-based pieces: `build/make_large_pieces.py` (banners, backdrop, table cover), `build/make_posters.py`, `build/make_posters_measure.py`. Shared art (loop, outcomes triangle, body map) is in `build/art.py`.

Brand rules applied: six-color palette, no gold or copper, DM Serif Display and DM Sans, no em or en dashes, outcome-first copy. Large pieces use light fields with Deep Teal type.
