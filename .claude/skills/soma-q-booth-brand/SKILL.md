---
name: soma-q-booth-brand
description: Brand and design rules for Soma-Q booth, event and print collateral (banners, backdrop, posters, postcards, cards). Use whenever building or editing anything in booth-package/ so every piece stays consistent. Covers palette, the pressure accent (copper), the nervous-system figure, the canonical What we do sentence, legibility rules and the men's track exception.
---

# Soma-Q booth brand rules

Source of truth for this repo. It extends the Soma-Q brand for print and event pieces; where it disagrees with an older document, this file governs for booth-package/. Decisions below were made by Megan McDonald (Founder) in the October 2026 booth sessions.

## Palette (new brand, locked)
- Deep Teal `#103C41`: fields, headlines on light.
- Light Teal `#9BC4BD`: ribbon, accents on Deep Teal.
- Pale `#E4F2F2`, Linen `#EEEADD`, White `#FEFCF8`, Ink `#24211D`.
- Fonts: DM Serif Display for headlines, DM Sans for everything else.
- No em dashes anywhere. Plain, direct sentences. Never say "coach".

## Pressure accent: copper (approved Oct 2026)
- Copper `#C9763F`, used as a soft glow on Deep Teal and on light fields.
- Use ONLY to show where pressure or stress sits: the head (brain), the heart and the gut on the nervous-system figure, and matching pressure indications in diagrams.
- Never for headlines, buttons, borders, text or decoration.
- Legacy brand copper was `#C85A3C` (Master Brand Standards, June 2026, old teal `#096C6C`). Do not use the old teal. If the pressure accent must change, change `COPPER` in `booth-package/build/art.py`.

## Frame for every piece
Keep people in the tension to name the pain, then show the outcome. Practices are the tools; capacity is the product. The stress loop shows where to interrupt it.
- Header: logo, descriptor "Nervous system alignment for high-performing leaders" (large, Light Teal), Light Teal ribbon with "BURNOUT ENDS HERE.™" or another ribbon line from the website.
- "WHAT WE DO" appears on everything, with the same sentence (draft awaiting Megan's approval): "Soma-Q is a nervous system alignment practice. We train high-performing leaders to notice stress sooner, shift in the moment and recover faster."
- Problem cards (consumer wording): Depletion "Running on empty, and calling it normal." Decisions "Choices made from pressure, not clarity." Communication "Short with the people you love." Resources "You know what to do. You can't reach it." The organization version uses the website's For Organizations copy verbatim.
- Metrics: show the report format (week 1 marker vs current bar, scored 0 to 10) and always label it "Example of the report format, not client data."
- Seven areas of focus come from the website's The Work page; use its wording exactly.

## Nervous-system figure
- One figure everywhere: the neutral silhouette with the nervous system lit from inside (white glow like the logo) and copper stress glows at head, heart and gut. Code: `nervous_figure()` in `booth-package/build/art.py`; the body map uses it too. Do not use stock or watermarked figures.
- Keep it gender-neutral and accessible: no hair, no breasts or waist emphasis. Megan works with men, women and anyone, however they identify.
- The model drawing and the Awareness / Regulation / Organization / Integration callouts were scrapped for booth pieces.

## Legibility (print, viewed from a distance)
- Rule of thumb about 30 ft of viewing distance per inch of letter height in ideal conditions. Realistic: headline text readable at 50 to 60 ft; only one huge phrase ("Burnout ends here") is for 100 ft.
- Banners 32 x 80 in: everything that must be read sits in the top 54 in (a table hides the lower part). Backdrop: key content in the top 60 in.
- At most five words in a headline where possible; one main graphic per piece; contrast near 10:1.
- Always print one piece to scale and step back before ordering.

## Men's track (documented exception)
A second front door for a men-skewing room. Headlines are pain-led instead of the three-outcome set (energy, clarity, joy). Current question under the tension line: "What do you do next?" (draft). Concept notes: `booth-package/men-track/CONCEPT.md`.

## Claims and credentials
- Credentials exactly as on the website About page. Research claims only from verified citation rows. Soma-Q is education and training: no diagnosing or treating, never replaces medical or mental health care.

## Build
Run generators first (`python3 build/make_*.py`), then `python3 build/build.py <piece>`; previews land in `booth-package/output/preview/`.
