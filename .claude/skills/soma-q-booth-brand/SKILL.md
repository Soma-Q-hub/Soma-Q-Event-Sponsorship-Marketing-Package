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
- QR codes are always centered in their callout box (Megan's rule, Oct 13 2026): center the code horizontally in the panel, with the label above or below it, never beside it off-center.
- Align by measurement, not by eye (Oct 13 2026): when a QR sits beside text, the top and bottom of the text block line up with the top and bottom of the QR box (do not shrink the QR below about 0.8 in to make it fit). Measure ink rows on the rendered PNG and keep gaps above and below a block equal.
- Business card back: the Q mark sits top left. A callout beside a heading has its top on the heading's cap top and its bottom on the last line of the list under it. Keep all type 0.125 in or more inside the trim.
- No em dashes anywhere. Plain, direct sentences. Never say "coach".
- **Oxford (serial) comma everywhere**, in every list of three or more, on every piece, including approved website lines (Megan's rule, Oct 13 2026): "energy, clarity, and joy", "notice stress sooner, shift in the moment, and recover faster", "diagnose, treat, or manage". Check every list before a piece goes to review.

## Pressure accent: copper (approved Oct 2026)
- Copper `#C9763F`, used as a soft glow on Deep Teal and on light fields.
- Use ONLY to show where pressure or stress sits: the head (brain), the heart and the gut on the nervous-system figure, and matching pressure indications in diagrams.
- Never for headlines, buttons, borders, text or decoration.
- Legacy brand copper was `#C85A3C` (Master Brand Standards, June 2026, old teal `#096C6C`). Do not use the old teal. If the pressure accent must change, change `COPPER` in `booth-package/build/art.py`.

## Frame for every piece
Keep people in the tension to name the pain, then show the outcome. Practices are the tools; steadiness is the product ("capacity" is a nervous-system term that does not translate to the public). The stress loop shows where to interrupt it.
- Header: logo, descriptor "Nervous system alignment for high-performing leaders" (large, Light Teal), Light Teal ribbon with "BURNOUT ENDS HERE.™" or another ribbon line from the website.
- "WHAT WE DO" appears on everything, with the same sentence (draft awaiting Megan's approval): "Soma-Q is a nervous system alignment practice. Training high-performing leaders to notice stress sooner, shift in the moments of pressure, and lead with powerful presence." (Oct 13: avoid the word "we" in booth copy. Business card fronts drop the first sentence and use only "Training high-performing leaders to notice stress sooner, shift in the moments of pressure, and lead with powerful presence.")
- Problem cards (consumer wording): Depletion "Running on empty, and calling it normal." Decisions "Choices made from pressure, not clarity." Communication "Short with the people you love." Resources "You know what to do. You can't reach it." The organization version uses the website's For Organizations copy verbatim.
- Metrics: show the report format (week 1 marker vs current bar, scored 0 to 10) and always label it "Example of the report format, not client data."
- Seven areas of focus come from the website's The Work page; use its wording exactly.

## Approved lines from the website (use verbatim)
- "Leadership does not happen from the neck up." / "Steadiness doesn't happen from the neck up."
- "Regulation is a skill. Recovery is a skill. Choice under pressure is a skill."
- RETIRED Oct 13 2026: "Pressure decides whether you react or respond." It is not accurate. The core line is now **"Pressure happens. Burnout doesn't have to."**, with the support line "Noticing your nervous system's signals is critical to your well-being." The offer line is "Education and training to change your response to stress." The three beats come from the website: "Notice the signal. Locate what is happening. Choose your next response."
- Contrast line for banners, from the Positioning Manifesto ("The market gap"): "An app. A meditation. A breathwork class. A resilience webinar. A one-time workshop." then "Each may help. None trains your response to stress." ("Coaching session" is left out because we never say "coach".)
- Taglines: "Burnout ends here.™", "Shift happens™" (trademarked; written SHIFT HAPPENS™), "Become your own advisor."

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
- Sub tagline for "Shift Happens" (chosen by Megan Oct 21, 2026, still being finalized): "Shift happens. Choice under pressure is a skill." (from the Positioning Manifesto). Messaging Architecture v2 says "Burnout ends here." is primary and "Shift happens." is the secondary campaign line; do not stack the two directly. No outcome numbers or promises (SQ-LPMS is self-report, not validated).
