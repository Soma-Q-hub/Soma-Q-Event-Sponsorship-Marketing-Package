"""Edit this file, then run: python3 build/build.py   (from booth-package/)
Anything in [BRACKETS] is a placeholder that prints visibly, so it cannot slip through a proof unnoticed."""

EVENT_NAME = ""   # intentionally blank: the print pieces are event-neutral so they can be reused
EVENT_DATES = "Saturday, October 24, 2026"
EVENT_VENUE = ""
BOOTH_NUMBER = ""      # only used on the organizations sheet; leave blank to omit
BOOTH_SIZE = "[BOOTH SIZE, e.g. 10 x 10 ft]"   # only used in the planning documents

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
    "reset": "https://us06web.zoom.us/j/87654266823",   # Shift Happens weekly reset, Wednesdays 12:00 PM Mountain, 30 minutes
    "call": "https://somaqcoaching.as.me/schedule/34334163/appointment/84765700/calendar/12916710",  # CURRENT Acuity link, used only if you must print before the Replit /book page exists
    "org": f"{SITE}/contact?topic=organization",
}

# Final destinations for the /go/ redirects (what the designer should redirect to).
GO_TARGETS = {
    "quiz": f"{SITE}/assessment",
    "ebook": f"{SITE}/free-resources",
    "reset": "https://us06web.zoom.us/j/87654266823",
    "call": "[NEW REPLIT /book LINK, when ready]",
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
CARD_PHONE = "303-717-9995"   # the number printed on the website Terms page; confirm this is the one you want on the card

# --- Image assets (official files from Drive: Marketing & Socials > Branding > 2026 Logos > UPDATED SEPT 2026 LOGOS) ---
LOGO_ON_DARK = "assets/soma-q-logo-teal-reversed.png"
LOGO_ON_LIGHT = "assets/soma-q-logo-teal.png"
POPL_QR_IMAGE = "assets/popl-qr.png"   # export the QR image from the POPL app
