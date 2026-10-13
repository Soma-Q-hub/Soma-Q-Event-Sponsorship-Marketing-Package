# Final pieces (decided)

Pieces Megan has approved for print. Sources are the build scripts in `../build/`.

| Folder | Piece | Source | Notes |
|---|---|---|---|
| `postcard/` | Postcard front and back are out of FINAL while being reworked (Oct 13). Old v1 front and back are in `postcard/Archive/`. Working versions: `postcard_front_g` and `postcard_back_w_photo` in `../review/` | `make_postcard.py` | Move the new front and back here as `_v2` when Megan says they are done. |
| `tabletop_stand_sign/` | Tabletop stand sign for the 12 x 6 in slanted acrylic holder: three free ways to start (Burnout Signal Check, discovery call, Shift Happens reset), one QR each | `stand_sign` (`make_round2.py`) | Confirm the holder's actual insert size and the weekly reset time (Wednesdays 12:00 PM Mountain) before print. Kept 0.5 in from the corners. |
| `banner_D1/` | Hero banner D1, 32 x 80 in trim, quiz QR, logo left, white band under the QR, Deep Teal base | `banner_men_hero_dark_shift` (`make_men_hero.py`) | Closing line: "Discover how to reclaim your energy, clarity and joy." Confirm the vendor template. Core-line wording may still change. |

Still open before print: discovery-call booking link and `/go/call` redirect, printer template and size, "What we do" sentence approval.
To update a piece: rebuild, copy here as `_v2`, move `_v1` into an `Archive/` subfolder.
