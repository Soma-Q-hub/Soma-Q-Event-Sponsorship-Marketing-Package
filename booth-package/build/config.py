"""Edit this file, then run: python3 build/build.py   (from booth-package/)
Anything in [BRACKETS] is a placeholder that prints visibly, so it cannot slip through a proof unnoticed."""

EVENT_NAME = "[EVENT NAME]"
EVENT_DATES = "Saturday, October 24, 2026"
EVENT_VENUE = "[VENUE, CITY]"
BOOTH_NUMBER = "[BOOTH #]"
BOOTH_SIZE = "[BOOTH SIZE, e.g. 10 x 10 ft]"

# Short campaign slug carried on every QR so scans can be attributed to this event.
CAMPAIGN = "oct24"

SITE = "https://www.soma-q.com"

# --- QR destinations -------------------------------------------------------------------------------------------
# MODE "go":     QR codes point to stable redirects on soma-q.com (/go/quiz, /go/ebook, /go/reset, /go/call).
#                A printed code can then never go stale, because the destination can be changed later.
#                Requires the designer to build the redirects first (see output/redirects_for_designer.md).
# MODE "direct": QR codes point straight at the final pages today. Works without any site work, but cannot be
#                changed after printing. Switch to "direct" only if /go/ is not live before the print date.
QR_MODE = "go"

DIRECT = {
    "quiz": f"{SITE}/assessment",
    "ebook": f"{SITE}/free-resources",          # the ebook signup lives on the Free Resources page
    "reset": f"{SITE}/free-resources",          # Shift Happens weekly reset is described there; swap for a Zoom registration link if you have one
    "call": "https://somaqcoaching.as.me/schedule/34334163/appointment/84765700/calendar/12916710",  # Acuity link from the website handoff
    "org": f"{SITE}/contact?topic=organization",
}

# Final destinations for the /go/ redirects (what the designer should redirect to).
GO_TARGETS = {
    "quiz": f"{SITE}/assessment",
    "ebook": f"{SITE}/free-resources",
    "reset": "[ZOOM REGISTRATION OR FREE-RESOURCES RESET SECTION]",
    "call": "[ACUITY LINK OR /book PAGE]",
    "org": f"{SITE}/contact?topic=organization",
}

# --- Photo (optional) ------------------------------------------------------------------------------------------
# The banner and backdrop are produced both without a photo (default recommendation) and with one.
# Put a cropped, web-or-print-sized headshot at assets/megan-headshot.jpg (the website's About photo is
# casual-headshot-about.jpg in 2_FILE_IN_DRIVE). If absent, the photo version prints a placeholder frame.
PHOTO_PATH = "assets/megan-headshot.jpg"

# --- Contact details printed on the business card -----------------------------------------------------------------
CARD_NAME = "Megan McDonald"
CARD_TITLE = "Founder"
CARD_EMAIL = "Megan@Soma-Q.com"
CARD_WEB = "soma-q.com"
CARD_PHONE = "[PHONE]"   # optional; decide whether it stays public (open item on the website handoff)

# --- Image assets (official files from Drive: Marketing & Socials > Branding > 2026 Logos > UPDATED SEPT 2026 LOGOS) ---
LOGO_ON_DARK = "assets/soma-q-logo-teal-reversed.png"
LOGO_ON_LIGHT = "assets/soma-q-logo-teal.png"
POPL_QR_IMAGE = "assets/popl-qr.png"   # export the QR image from the POPL app
