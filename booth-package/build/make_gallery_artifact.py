#!/usr/bin/env python3
"""Build a single self-contained HTML gallery (images embedded) from output/preview/*.png.
Usage: python3 build/make_gallery_artifact.py /path/to/gallery.html"""
import base64, io, pathlib, sys, html
from PIL import Image

ROOT = pathlib.Path(__file__).resolve().parent.parent
PREV = ROOT / "output" / "preview"
out_path = pathlib.Path(sys.argv[1])

SECTIONS = [
  ("banner", "Banners, backdrop and table cover", "The large pieces that stop people in the aisle: light fields, dark type, no QR codes. Banner 2 and the backdrop come with and without your photo.", [
    ("banner_story-1", "Banner 1: the story", "32 x 80 in"),
    ("banner_proof-1", "Banner 2: the proof, no photo", "32 x 80 in"),
    ("banner_proof_photo-1", "Banner 2: the proof, with photo", "32 x 80 in"),
    ("backdrop-1", "Backdrop, no photo", "120 x 90 in, placeholder size"),
    ("backdrop_photo-1", "Backdrop, with photo", "120 x 90 in, placeholder size"),
    ("table_front-1", "Table cover front panel", "72 x 30 in, placeholder size"),
  ]),
  ("table", "On the table and in the hand", "The pieces visitors scan and take home.", [
    ("counter_sign-1", "Counter sign", "8.5 x 11 in"),
    ("card_individual-1", "Take-home card, front", "4 x 6 in"),
    ("card_individual-2", "Take-home card, back", "4 x 6 in"),
    ("business_card-1", "Business card, front", "3.5 x 2 in"),
    ("business_card-2", "Business card, back", "3.5 x 2 in"),
  ]),
  ("posters", "Explainer posters", "Four pictures that make the work understandable to someone who has never heard of it.", [
    ("poster_loop-1", "The Pressure Loop", "24 x 36 in"),
    ("poster_shift-1", "The Soma-Q Shift", "24 x 36 in"),
    ("poster_outcomes-1", "What Changes", "24 x 36 in"),
    ("poster_where-1", "Where do you feel pressure first?", "24 x 36 in"),
  ]),
]
EXTRA = ROOT / "build" / "gallery_extra.py"
if EXTRA.exists():
    ns = {}
    exec(EXTRA.read_text(), ns)
    for sec in ns.get("MORE_SECTIONS", []):
        SECTIONS.insert(sec.get("at", len(SECTIONS)), sec["data"])
SECTIONS.append(("plan", "Plan and order guide", "The strategy packet, then the order guide with vendors, prices and the timeline to October 24.", 
    [(f"strategy_packet-{i:02d}", f"Strategy packet, page {i}", "8.5 x 11 in") for i in range(1, len(list(PREV.glob("strategy_packet-*.png"))) + 1)] +
    [(f"order_guide-{i}", f"Order guide, page {i}", "8.5 x 11 in") for i in range(1, 4)]))

def data_uri(stem, maxside):
    p = PREV / f"{stem}.png"
    if not p.exists():
        return None, None
    im = Image.open(p).convert("RGB")
    r = maxside / max(im.size)
    if r < 1:
        im = im.resize((round(im.width * r), round(im.height * r)), Image.LANCZOS)
    b = io.BytesIO(); im.save(b, "JPEG", quality=80, optimize=True)
    return "data:image/jpeg;base64," + base64.b64encode(b.getvalue()).decode(), im.size

figs = []; nav = []
for sid, title, blurb, items in SECTIONS:
    nav.append(f'<a href="#{sid}">{html.escape(title.split(",")[0])}</a>')
    cards = []
    for stem, label, size in items:
        maxside = 1500 if stem.startswith(("strategy", "order")) else 1700
        uri, dim = data_uri(stem, maxside)
        if not uri:
            continue
        wide = dim[0] > dim[1] * 1.15
        cards.append(f'<figure class="card{" wide" if wide else ""}"><button type="button" class="open" data-src="{stem}" aria-label="View {html.escape(label)} larger"><img src="{uri}" alt="{html.escape(label)}" width="{dim[0]}" height="{dim[1]}" loading="lazy"></button><figcaption><b>{html.escape(label)}</b><span>{html.escape(size)}</span></figcaption></figure>')
    cls = "docs" if sid == "plan" else ""
    figs.append(f'<section id="{sid}"><header><h2>{html.escape(title)}</h2><p>{html.escape(blurb)}</p></header><div class="grid {cls}">{"".join(cards)}</div></section>')

page = f'''<title>Soma-Q Booth Package</title>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;700&family=DM+Serif+Display&display=swap">
<style>
/* Layout: sticky section index, then one band per piece family; click any image to enlarge. Brand palette from the Soma-Q v2 teal system. */
:root {{
  --bg:#F4F1EA; --surface:#FEFCF8; --fg:#24211D; --muted:#5C5A53; --accent:#103C41; --accent-ink:#FEFCF8; --line:#D6D2C4; --chip:#E4F2F2;
  --font-display:'DM Serif Display', Georgia, serif; --font-body:'DM Sans', system-ui, sans-serif;
}}
@media (prefers-color-scheme: dark) {{ :root:not([data-theme="light"]) {{ --bg:#0C2427; --surface:#133137; --fg:#EAF1EF; --muted:#9FB8B3; --accent:#9BC4BD; --accent-ink:#0C2427; --line:#24474D; --chip:#1A3B41; color-scheme:dark }} }}
:root[data-theme="dark"] {{ --bg:#0C2427; --surface:#133137; --fg:#EAF1EF; --muted:#9FB8B3; --accent:#9BC4BD; --accent-ink:#0C2427; --line:#24474D; --chip:#1A3B41; color-scheme:dark }}
body {{ background:var(--bg); color:var(--fg); font-family:var(--font-body); font-size:16px; line-height:1.5; padding-inline:max(16px,4vw); }}
.wrap {{ max-width:1280px; margin:0 auto; padding-block:28px 64px; }}
h1,h2 {{ font-family:var(--font-display); font-weight:400; text-wrap:balance; margin:0; }}
h1 {{ font-size:clamp(34px,5vw,56px); line-height:1.05; color:var(--accent); }}
.lede {{ max-width:62ch; color:var(--muted); margin:12px 0 0; }}
.top {{ display:flex; flex-direction:column; gap:6px; padding-bottom:20px; }}
.eyebrow {{ font-size:12px; font-weight:700; letter-spacing:.14em; text-transform:uppercase; color:var(--muted); }}
nav {{ position:sticky; top:env(safe-area-inset-top,0px); z-index:5; background:var(--bg); padding-block:10px; display:flex; gap:8px; flex-wrap:wrap; border-bottom:1px solid var(--line); }}
nav a {{ text-decoration:none; color:var(--fg); background:var(--chip); padding:7px 14px; border-radius:999px; font-size:14px; font-weight:500; }}
nav a:hover, nav a:focus-visible {{ background:var(--accent); color:var(--accent-ink); outline:none }}
section {{ padding-top:44px; scroll-margin-top:64px; }}
section header {{ display:flex; flex-direction:column; gap:6px; margin-bottom:20px; }}
h2 {{ font-size:clamp(26px,3.2vw,36px); color:var(--accent); }}
section header p {{ margin:0; color:var(--muted); max-width:70ch; }}
.grid {{ display:grid; gap:22px; grid-template-columns:repeat(auto-fill,minmax(min(100%,260px),1fr)); align-items:start; }}
.grid.docs {{ grid-template-columns:repeat(auto-fill,minmax(min(100%,210px),1fr)); gap:16px; }}
.card {{ margin:0; min-width:0; }}
.card.wide {{ grid-column:span 2; }}
@media (max-width:620px) {{ .card.wide {{ grid-column:span 1; }} }}
.open {{ display:block; width:100%; padding:0; border:1px solid var(--line); border-radius:6px; background:var(--surface); cursor:zoom-in; overflow:hidden; }}
.open:focus-visible {{ outline:3px solid var(--accent); outline-offset:2px; }}
.open img {{ display:block; width:100%; height:auto; }}
figcaption {{ display:flex; flex-direction:column; gap:2px; padding-top:8px; font-size:14px; }}
figcaption span {{ color:var(--muted); font-size:13px; }}
.note {{ margin-top:44px; padding:16px 18px; background:var(--surface); border:1px solid var(--line); border-radius:6px; max-width:78ch; font-size:15px; }}
dialog {{ border:0; padding:0; background:transparent; max-width:100vw; max-height:100vh; width:100%; height:100%; }}
dialog::backdrop {{ background:rgba(8,20,22,.88); }}
.lb {{ display:flex; flex-direction:column; align-items:center; justify-content:center; height:100%; gap:10px; padding:16px; }}
.lb img {{ max-width:min(100%,1500px); max-height:calc(100% - 64px); object-fit:contain; background:#fff; }}
.lb .bar {{ display:flex; gap:8px; align-items:center; color:#EAF1EF; font-size:14px; }}
.lb button {{ font:inherit; color:#EAF1EF; background:#1A3B41; border:1px solid #3B6169; border-radius:6px; padding:7px 14px; cursor:pointer; }}
.lb button:focus-visible {{ outline:3px solid #9BC4BD; }}
@media (prefers-reduced-motion:no-preference) {{ .open img {{ transition:transform .2s }} .open:hover img {{ transform:scale(1.015) }} }}
</style>
<div class="wrap">
  <div class="top">
    <span class="eyebrow">Event booth, October 24, 2026</span>
    <h1>Soma-Q Booth Package</h1>
    <p class="lede">Every piece as it will print, one picture per page. Click any image to enlarge it. The PDFs are the print files and live in the project's output folder; these are for review only.</p>
  </div>
  <nav aria-label="Sections">{"".join(nav)}</nav>
  {"".join(figs)}
  <p class="note">The logo and photo are the website copies, so the banner and backdrop need the original large files before final export. Sizes marked placeholder must be matched to the printer's template. Scan codes on these previews point to addresses that go live with the new website.</p>
</div>
<dialog id="lb" aria-label="Enlarged view"><div class="lb"><img id="lbimg" alt=""><div class="bar"><button type="button" id="prev">Previous</button><span id="cap"></span><button type="button" id="next">Next</button><button type="button" id="close">Close</button></div></div></dialog>
<script>
(function(){{
  var imgs = Array.prototype.slice.call(document.querySelectorAll('.open'));
  var dlg = document.getElementById('lb'), big = document.getElementById('lbimg'), cap = document.getElementById('cap'), i = 0;
  function show(n){{ i = (n + imgs.length) % imgs.length; var im = imgs[i].querySelector('img'); big.src = im.src; big.alt = im.alt; cap.textContent = im.alt + '  (' + (i+1) + ' of ' + imgs.length + ')'; }}
  imgs.forEach(function(b, n){{ b.addEventListener('click', function(){{ show(n); if (dlg.showModal) dlg.showModal(); else dlg.setAttribute('open',''); }}); }});
  document.getElementById('prev').addEventListener('click', function(){{ show(i-1); }});
  document.getElementById('next').addEventListener('click', function(){{ show(i+1); }});
  document.getElementById('close').addEventListener('click', function(){{ dlg.close ? dlg.close() : dlg.removeAttribute('open'); }});
  dlg.addEventListener('click', function(e){{ if (e.target === dlg) dlg.close(); }});
  document.addEventListener('keydown', function(e){{ if (!dlg.open) return; if (e.key === 'ArrowRight') show(i+1); if (e.key === 'ArrowLeft') show(i-1); }});
}})();
</script>
'''
out_path.write_text(page)
print("wrote", out_path, round(out_path.stat().st_size/1e6, 1), "MB")
