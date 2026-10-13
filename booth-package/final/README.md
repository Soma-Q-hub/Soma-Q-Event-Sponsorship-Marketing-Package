# Final pieces (decided)

Pieces Megan has approved for print. Sources are the build scripts in `../build/`.

| Folder | Piece | Source | Notes |
|---|---|---|---|
| `postcard/` | Postcard back only, 6 x 4 in trim + 0.125 in bleed. The front was pulled from FINAL on Oct 13 (new core line in review: `postcard_front_f`, `_g`); the old front is in `postcard/Archive/` | `postcard_back_w_photo` (`make_postcard.py`) | Old front headline: "Noticing your nervous system's signals is critical to your well-being." |
| `tabletop_stand_sign/` | Tabletop stand sign for the 12 x 6 in slanted acrylic holder: three free ways to start (Burnout Signal Check, discovery call, Shift Happens reset), one QR each | `stand_sign` (`make_round2.py`) | Confirm the holder's actual insert size and the weekly reset time (Wednesdays 12:00 PM Mountain) before print. Kept 0.5 in from the corners. |
| `banner_D1/` | Hero banner D1, 32 x 80 in trim, quiz QR, logo left, white band under the QR, Deep Teal base | `banner_men_hero_dark_shift` (`make_men_hero.py`) | Closing line: "Discover how to reclaim your energy, clarity and joy." Confirm the vendor template. Core-line wording may still change. |

Still open before print: discovery-call booking link and `/go/call` redirect, printer template and size, "What we do" sentence approval.
To update a piece: rebuild, copy here as `_v2`, move `_v1` into an `Archive/` subfolder.
