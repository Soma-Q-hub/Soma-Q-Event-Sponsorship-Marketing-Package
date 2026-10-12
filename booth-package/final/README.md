# Final pieces (decided)

Pieces Megan has approved for print. Sources are the build scripts in `../build/`.

| Folder | Piece | Source | Notes |
|---|---|---|---|
| `postcard/` | Postcard front and back, 6 x 4 in trim + 0.125 in bleed | `postcard_front_e`, `postcard_back_w_photo` (`make_postcard.py`) | Headline: "Noticing your nervous system's signals is critical to your well-being." |
| `banner_D1_hero_dark_shift/` | Hero banner D1, dark, "Shift Happens™", 32 x 80 in | `banner_men_hero_dark_shift` (`make_men_hero.py`) | Bottom footer band is crisp white (#FFFFFF), not Linen. Built on the men's-track hero script, hence the file name. |

Still open before print: discovery-call booking link and `/go/call` redirect, printer template and size, "What we do" sentence approval.
To update a piece: rebuild, copy here as `_v2`, move `_v1` into an `Archive/` subfolder.
