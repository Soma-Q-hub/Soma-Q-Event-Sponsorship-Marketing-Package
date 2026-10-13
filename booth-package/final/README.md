# Final pieces (decided)

Pieces Megan has approved for print. Sources are the build scripts in `../build/`.

| Folder | Piece | Source | Notes |
|---|---|---|---|
| `postcard/` | Postcard front v3 and back v2, 6 x 4 in trim + 0.125 in bleed. Front: "Pressure happens. Burnout doesn't have to." with "Understanding and shifting your nervous system's signals is critical to your well-being. White column: Create the outcomes you want in the four places pressure shows up.", Shift Happens™ under the image, education and training line in the bottom banner. Back: How I work, What we do ending in Burnout ends here™, QR to the free Burnout Signal Check. Old v1 files are in `postcard/Archive/` | `postcard_front_l`, `postcard_back_w_photo` (`make_postcard.py`) | Confirm the printer template. The practice and trademark notes in `../review/README.md` still apply. |
| `tabletop_stand_sign/` | Tabletop stand sign for the 12 x 6 in slanted acrylic holder: three free ways to start (Burnout Signal Check, discovery call, Shift Happens reset), one QR each | `stand_sign` (`make_round2.py`) | Confirm the holder's actual insert size and the weekly reset time (Wednesdays 12:00 PM Mountain) before print. Kept 0.5 in from the corners. |
| `banner_D1/` | Hero banner D1, 32 x 80 in trim, quiz QR, logo left, white band under the QR, Deep Teal base | `banner_men_hero_dark_shift` (`make_men_hero.py`) | Closing line: "Discover how to reclaim your energy, clarity and joy." Confirm the vendor template. Core-line wording may still change. |
| `business_card/` | Business card front, type only (R7d), 3.5 x 2 in trim + 0.125 in bleed. "Pressure happens. Reacting doesn't have to." with "Education and training to change your response." | `bizcard2_front_plain_b` (`make_round2.py`) | Back not filed yet (R7 or R14). Wording note: the postcard says "Burnout doesn't have to." Confirm this card should keep "Reacting doesn't have to." |

Still open before print: discovery-call booking link and `/go/call` redirect, printer template and size, "What we do" sentence approval.
To update a piece: rebuild, copy here as `_v2`, move `_v1` into an `Archive/` subfolder.
