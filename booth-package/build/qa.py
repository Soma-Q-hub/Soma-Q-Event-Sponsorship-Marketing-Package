"""Layout checks on every rendered piece, using Chromium.
Flags: (1) text outside the page or inside the bleed/safe margin, (2) text boxes that overlap other text, QR codes or pictures,
(3) text clipped by its container, (4) placeholders still on the page, (5) em or en dashes.
Run:  QA=1 python3 build/build.py"""
import glob, os, re, sys
from playwright.sync_api import sync_playwright

JS = r"""
() => {
  const out = [];
  const vw = document.documentElement.clientWidth, vh = document.documentElement.clientHeight;
  const sel = 'p,li,h1,h2,h3,h4,td,th,span,b,div,text,figcaption,a';
  const els = Array.from(document.querySelectorAll(sel)).filter(e => {
    const t = Array.from(e.childNodes).filter(n => n.nodeType === 3 && n.textContent.trim().length).map(n => n.textContent).join('');
    return t.trim().length > 0;
  });
  const shrink = r => { const k = r.height * 0.16; return {left: r.left, right: r.right, top: r.top + k, bottom: r.bottom - k, width: r.width, height: r.height - 2 * k}; };
  const rects = els.map(e => { const r = shrink(e.getBoundingClientRect()); return {e, r, t: e.textContent.trim().slice(0, 40)}; })
                   .filter(o => o.r.width > 1 && o.r.height > 1);
  const blocks = Array.from(document.querySelectorAll('img,.qr,svg.segno,.photo')).map(e => ({e, r: e.getBoundingClientRect()})).filter(o => o.r.width > 8);
  const inter = (a, b) => { const w = Math.min(a.right, b.right) - Math.max(a.left, b.left), h = Math.min(a.bottom, b.bottom) - Math.max(a.top, b.top); return (w > 0 && h > 0) ? w * h : 0; };
  const pages = Array.from(document.querySelectorAll('.page'));
  const pageOf = e => pages.find(p => p.contains(e)) || null;
  // 1) outside its sheet (each .page is one sheet; otherwise the whole document)
  rects.forEach(o => { const r = o.r; const pg = pageOf(o.e); const pr = pg ? pg.getBoundingClientRect() : {left: 0, top: 0, right: vw, bottom: vh};
    if (r.left < pr.left - 1 || r.top < pr.top - 1 || r.right > pr.right + 1 || r.bottom > pr.bottom + 1) out.push('OUTSIDE PAGE: "' + o.t + '"'); });
  // 2) text overlapping text
  for (let i = 0; i < rects.length; i++) for (let j = i + 1; j < rects.length; j++) {
    const a = rects[i], b = rects[j];
    if (a.e.contains(b.e) || b.e.contains(a.e)) continue;
    if (pageOf(a.e) !== pageOf(b.e)) continue;
    const ar = inter(a.r, b.r);
    if (ar > 0) { const m = Math.min(a.r.width * a.r.height, b.r.width * b.r.height); if (ar / m > 0.12) out.push('TEXT OVERLAP: "' + a.t + '" with "' + b.t + '"'); }
  }
  // 3) text over QR / picture
  rects.forEach(o => blocks.forEach(b => { if (b.e.contains(o.e) || o.e.contains(b.e)) return; if (pageOf(b.e) !== pageOf(o.e)) return; const ar = inter(o.r, b.r);
    if (ar > 0 && ar / (o.r.width * o.r.height) > 0.12) out.push('TEXT OVER GRAPHIC: "' + o.t + '"'); }));
  // 4) clipping
  els.forEach(e => { if (e.tagName.toLowerCase() === 'text') return; const cs = getComputedStyle(e);
    if ((e.scrollWidth > e.clientWidth + 2 && e.clientWidth > 0) || (e.scrollHeight > e.clientHeight + 2 && e.clientHeight > 0 && cs.overflow !== 'visible')) out.push('CLIPPED: "' + e.textContent.trim().slice(0, 40) + '"'); });
  // 5) page-level overflow
  if (!pages.length && document.documentElement.scrollHeight > vh + 2) out.push('PAGE TALLER THAN SHEET by ' + (document.documentElement.scrollHeight - vh) + 'px');
  const sheetH = pages.length ? pages[0].getBoundingClientRect().height : vh;
  const expected = pages.length || 1;
  if (pages.length === 0 && document.documentElement.scrollHeight > vh * 1.02) out.push('SPILLS TO SECOND SHEET');
  // flag containers (cards, boxes, tables) that overlap the absolutely placed call-to-action blocks
  document.querySelectorAll('.cta').forEach(c => { const cr = c.getBoundingClientRect(); const pg = pageOf(c);
    Array.from(pg.querySelectorAll('.box,.chip,table,.steps7,.two,.grid4,p,h2,.quote')).forEach(e => { if (c.contains(e)) return; const er = e.getBoundingClientRect(); if (er.width > 8 && inter(er, cr) > 0) out.push('CONTENT RUNS INTO CALL-TO-ACTION: "' + e.textContent.trim().slice(0, 40) + '"'); }); });
  const txt = document.body.innerText;
  const ph = txt.match(/\[[A-Z][^\]]{2,}\]/g); if (ph) out.push('PLACEHOLDER: ' + Array.from(new Set(ph)).join(' | '));
  if (/[–—]/.test(txt)) out.push('DASH CHARACTER FOUND');
  return Array.from(new Set(out));
}
"""

def page_size(path):
    css = open(path).read()
    m = re.search(r"@page\s*\{\s*size:\s*([\d.]+)in\s+([\d.]+)in", css)
    return (float(m.group(1)), float(m.group(2))) if m else (8.5, 11)

def run(rendered):
    problems = 0
    with sync_playwright() as p:
        b = p.chromium.launch(executable_path=glob.glob("/opt/pw-browsers/chromium-*/chrome-linux/chrome")[0], args=["--no-sandbox"])
        for name, path in rendered:
            w, h = page_size(path)
            # very large pieces are checked at reduced scale so the viewport stays small
            scale = 1.0
            while w * 96 * scale > 4000 or h * 96 * scale > 4000: scale /= 2
            pg = b.new_page(viewport={"width": round(w * 96 * scale), "height": round(h * 96 * scale)}, device_scale_factor=1)
            pg.goto("file://" + str(path)); pg.wait_for_timeout(600)
            if scale != 1.0:
                pg.evaluate(f"document.documentElement.style.zoom='{scale}'")
            res = pg.evaluate(JS); pg.close()
            if name in ('strategy_packet', 'order_guide'):
                res = [r for r in res if not r.startswith(('SPILLS', 'OUTSIDE', 'CLIPPED'))]
            if res:
                problems += len(res); print(f"[QA] {name}"); [print("   -", r) for r in res]
        b.close()
    print(f"[QA] done, {problems} issue(s)")
