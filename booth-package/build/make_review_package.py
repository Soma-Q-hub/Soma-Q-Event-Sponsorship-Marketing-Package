#!/usr/bin/env python3
"""Build REVIEW/ at the repo root: overview images, individually named PNGs and one combined PDF per track, so the
whole package can be reviewed without opening print files. Run after build.py: python3 build/make_review_package.py"""
import pathlib, shutil, subprocess
from PIL import Image, ImageDraw, ImageFont

ROOT = pathlib.Path(__file__).resolve().parent.parent
PREV = ROOT / "output" / "preview"
OUT = ROOT.parent / "REVIEW"
LINEN, DEEP, MUTED = (238, 234, 221), (16, 60, 65), (92, 90, 83)

def font(size, bold=False):
    for f in ("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf" if bold else "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
              "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf" if bold else "/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf"):
        if pathlib.Path(f).exists():
            return ImageFont.truetype(f, size)
    return ImageFont.load_default()

MEN = [("banner_men_story-1", "Banner 1: the story", "32 x 80 in"), ("banner_men_proof-1", "Banner 2: the proof, no photo", "32 x 80 in"),
       ("banner_men_proof_photo-1", "Banner 2: the proof, with photo", "32 x 80 in"), ("backdrop_men-1", "Backdrop, no photo", "120 x 90 in placeholder"),
       ("backdrop_men_photo-1", "Backdrop, with photo", "120 x 90 in placeholder"), ("poster_men_fixer-1", "Poster: Stay steady when there is nothing to solve", "24 x 36 in"),
       ("poster_men_holder-1", "Poster: Hold space for others without losing touch with yourself", "24 x 36 in"),
       ("business_card_men-1", "Business card, front", "3.5 x 2 in"), ("business_card_men-2", "Business card, back", "3.5 x 2 in")]
MAIN = [("banner_story-1", "Banner 1: the story", "32 x 80 in"), ("banner_proof-1", "Banner 2: the proof, no photo", "32 x 80 in"),
        ("banner_proof_photo-1", "Banner 2: the proof, with photo", "32 x 80 in"), ("backdrop-1", "Backdrop, no photo", "120 x 90 in placeholder"),
        ("backdrop_photo-1", "Backdrop, with photo", "120 x 90 in placeholder"), ("table_front-1", "Table cover front", "72 x 30 in placeholder"),
        ("counter_sign-1", "Counter sign", "8.5 x 11 in"), ("card_individual-1", "Take-home card, front", "4 x 6 in"), ("card_individual-2", "Take-home card, back", "4 x 6 in"),
        ("business_card-1", "Business card, front", "3.5 x 2 in"), ("business_card-2", "Business card, back", "3.5 x 2 in"),
        ("leavebehind-1", "Leave-behind, for you", "8.5 x 11 in"), ("leavebehind-2", "Leave-behind, for your team", "8.5 x 11 in"),
        ("poster_loop-1", "Poster: The Pressure Loop", "24 x 36 in"), ("poster_shift-1", "Poster: The Soma-Q Shift", "24 x 36 in"),
        ("poster_outcomes-1", "Poster: What Changes", "24 x 36 in"), ("poster_where-1", "Poster: Where do you feel pressure first?", "24 x 36 in"),
        ("poster_progress-1", "Poster: Watch your progress, week by week", "24 x 36 in"), ("poster_capacity-1", "Poster: Capacity comes first", "24 x 36 in"),
        ("handout_measurement-1", "Measurement handout, front", "8.5 x 11 in"), ("handout_measurement-2", "Measurement handout, back", "8.5 x 11 in")]
PLAN = [(f"strategy_packet-{i:02d}", f"Strategy packet, page {i}", "8.5 x 11 in") for i in range(1, 16)] + [(f"order_guide-{i}", f"Order guide, page {i}", "8.5 x 11 in") for i in range(1, 4)]

def load(stem, long_side):
    im = Image.open(PREV / f"{stem}.png").convert("RGB")
    r = long_side / max(im.size)
    return im.resize((round(im.width * r), round(im.height * r)), Image.LANCZOS) if r < 1 else im

def fname(i, label):
    s = "".join(c if c.isalnum() else "_" for c in label).strip("_")
    while "__" in s: s = s.replace("__", "_")
    return f"{i:02d}_{s}.png"

def overview(items, title, sub, path, row_h=1250, width=3900, pad=70):
    import textwrap
    imgs = []
    for s_, l, z in items:
        if not (PREV / f"{s_}.png").exists(): continue
        im = load(s_, 2400)
        th = 520 if "card" in l.lower() and "take-home" not in l.lower() else row_h   # small pieces are drawn smaller
        w = max(round(im.width * th / im.height), 420)
        imgs.append((im, l, z, w, th))
    rows, cur, cw = [], [], 0
    for it in imgs:
        w = it[3]
        if cur and cw + w + pad > width - 2 * pad:
            rows.append(cur); cur, cw = [], 0
        cur.append(it); cw += w + pad
    if cur: rows.append(cur)
    cap_h = 230
    head = 330
    H = head + sum(max(t for *_, t in r) + cap_h for r in rows) + pad
    sheet = Image.new("RGB", (width, H), LINEN)
    d = ImageDraw.Draw(sheet)
    d.text((pad, 70), title, font=font(110, True), fill=DEEP)
    d.text((pad, 215), sub, font=font(46), fill=MUTED)
    y = head
    for row in rows:
        x = pad
        rh = max(t for *_, t in row)
        for im, l, z, w, th in row:
            iw = round(im.width * th / im.height)
            t = im.resize((iw, th), Image.LANCZOS)
            d.rectangle([x - 4, y - 4, x + iw + 3, y + th + 3], outline=(214, 210, 196), width=4)
            sheet.paste(t, (x, y))
            lines = textwrap.wrap(l, width=max(16, w // 22))[:3]
            ty = y + th + 24
            for ln in lines:
                d.text((x, ty), ln, font=font(38, True), fill=DEEP); ty += 50
            d.text((x, ty + 4), z, font=font(34), fill=MUTED)
            x += w + pad
        y += rh + cap_h
    sheet.save(path, optimize=True)

def pdf(items, path, title):
    pages = []
    for s, l, z in items:
        if not (PREV / f"{s}.png").exists(): continue
        im = load(s, 1700)
        cap = 130
        pg = Image.new("RGB", (max(im.width, 1100), im.height + cap), LINEN)
        pg.paste(im, ((pg.width - im.width) // 2, cap))
        d = ImageDraw.Draw(pg)
        d.text((40, 28), l, font=font(40, True), fill=DEEP)
        d.text((40, 82), f"{z}   |   {title}", font=font(28), fill=MUTED)
        pages.append(pg)
    pages[0].save(path, "PDF", save_all=True, append_images=pages[1:], resolution=150)

def folder(items, d):
    d.mkdir(parents=True, exist_ok=True)
    for i, (s, l, z) in enumerate(items, 1):
        if (PREV / f"{s}.png").exists():
            load(s, 2200).save(d / fname(i, l), optimize=True)

if OUT.exists(): shutil.rmtree(OUT)
OUT.mkdir()
overview(MEN, "Men's track (draft)", "Show up the way you mean to. One graphic per piece. Photo and no-photo versions where shown.", OUT / "1_START_HERE_Mens_Track_Overview.png")
overview(MAIN, "Main package", "The original booth set: banners, backdrop, table cover, cards, leave-behind, posters, measurement.", OUT / "2_Main_Package_Overview.png", row_h=1150)
pdf(MEN, OUT / "3_Mens_Track_all_pieces.pdf", "Men's track (draft)")
pdf(MAIN + PLAN, OUT / "4_Main_Package_and_Plan_all_pieces.pdf", "Main package and plan")
folder(MEN, OUT / "Mens_Track_pieces")
folder(MAIN, OUT / "Main_Package_pieces")
folder(PLAN, OUT / "Plan_and_Order_Guide_pages")
(OUT / "README.md").write_text("""# Soma-Q booth package: review folder

Open these in order. Everything here is an image or a plain PDF, so it previews directly; nothing needs a design program.

1. `1_START_HERE_Mens_Track_Overview.png`: every men's-track piece on one page.
2. `2_Main_Package_Overview.png`: the original booth set on one page.
3. `3_Mens_Track_all_pieces.pdf`: the men's pieces, one per page, with names and sizes.
4. `4_Main_Package_and_Plan_all_pieces.pdf`: the main pieces, then the strategy packet and order guide.
5. Folders `Mens_Track_pieces`, `Main_Package_pieces` and `Plan_and_Order_Guide_pages`: each piece as its own numbered image.

These are review copies. The print-ready PDFs (full size, with bleed) are in `booth-package/output`.
Notes behind the men's track: `booth-package/men-track/CONCEPT.md`.
""")
print("ok")
