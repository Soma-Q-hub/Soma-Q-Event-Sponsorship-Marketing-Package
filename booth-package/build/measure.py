"""Measure text widths in Chromium with the same fonts the build uses (so centering is measured, not guessed)."""
import json, glob, shutil
from playwright.sync_api import sync_playwright
def widths(items):
    """items: list of (text, family, size, weight). Returns widths in SVG units."""
    exe = shutil.which("chromium") or (glob.glob("/opt/pw-browsers/chromium-*/chrome-linux/chrome") or [None])[0]
    html = '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;700&family=DM+Serif+Display:ital@0;1&display=swap"><svg id="s" width="800" height="200" xmlns="http://www.w3.org/2000/svg"></svg>'
    with sync_playwright() as p:
        b = p.chromium.launch(executable_path=exe) if exe else p.chromium.launch()
        pg = b.new_page(); pg.set_content(html); pg.wait_for_timeout(800)
        out = pg.evaluate("""async (items) => {
          await document.fonts.ready;
          const s=document.getElementById('s'); const r=[];
          for (const [t,f,z,w] of items) {
            await document.fonts.load(`${w} ${z}px "${f}"`, t);
            const e=document.createElementNS('http://www.w3.org/2000/svg','text');
            e.setAttribute('font-family',f); e.setAttribute('font-size',z); e.setAttribute('font-weight',w); e.textContent=t; s.appendChild(e);
            r.push(e.getComputedTextLength());
          }
          return r; }""", items)
        b.close()
    return out
if __name__ == "__main__":
    print(widths([("Health","DM Serif Display",12,"400"),("Burnout","DM Serif Display",23,"400")]))
