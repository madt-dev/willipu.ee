#!/usr/bin/env python3
"""Private-room door sticker for Willipu — no QR, 120x70 mm.

Outputs willipu_kleebis_privaatruum.{svg,pdf,png} (vector + 300dpi preview).
Reuses the same fonts as make_qr_kleebis.py (downloads to ./fonts/ if missing).
"""
import os

from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen

REPO = os.path.dirname(os.path.abspath(__file__))
FONTS = os.path.join(REPO, "fonts")
GREEN_HEX = "#2d4a3e"

# ensure fonts exist (same fetch as make_qr_kleebis)
if not os.path.exists(os.path.join(FONTS, "fraunces-600.ttf")):
    import runpy
    raise SystemExit("Run make_qr_kleebis.py once first to fetch fonts.")

_font_cache = {}

def _tt(path):
    if path not in _font_cache:
        _font_cache[path] = TTFont(os.path.join(FONTS, path))
    return _font_cache[path]

def text_outline(font_file, text, em_mm):
    f = _tt(font_file)
    upm = f["head"].unitsPerEm
    glyphset = f.getGlyphSet()
    cmap = f.getBestCmap()
    x = 0
    parts = []
    for ch in text:
        gname = cmap.get(ord(ch), ".notdef")
        glyph = glyphset[gname]
        pen = SVGPathPen(glyphset)
        glyph.draw(pen)
        cmds = pen.getCommands()
        if cmds:
            parts.append(f'<path transform="translate({x} 0)" d="{cmds}"/>')
        x += glyph.width
    s = em_mm / upm
    frag = f'<g transform="scale({s:.6f} {-s:.6f})">{"".join(parts)}</g>'
    return x * s, frag

def placed_text(font_file, text, em_mm, baseline_y, fill, center_x=60):
    w, frag = text_outline(font_file, text, em_mm)
    return f'<g transform="translate({center_x - w / 2:.3f} {baseline_y:.3f})" fill="{fill}">{frag}</g>'

en = placed_text("inter-600.ttf", "Private · Staff only", 5.2, 56.4, "#ffffff")
brand = placed_text("fraunces-700.ttf", "Willipu", 3.2, 65.6, "#ffffff")

svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="120mm" height="70mm" viewBox="0 0 120 70">
  <rect width="120" height="70" rx="4" fill="{GREEN_HEX}"/>
  <g transform="translate(53.5 5.5) scale(0.1)">
    <circle cx="65" cy="65" r="55" fill="#ffffff" fill-opacity="0.14"/>
    <g transform="translate(27.60 27.60) scale(3.1167)" fill="none" stroke="#ffffff" stroke-width="1.8" stroke-linecap="round">
      <path d="M3 14c3 0 3-3 6-3s3 3 6 3 3-3 6-3 3 3 6 3"/>
      <path d="M3 19c3 0 3-3 6-3s3 3 6 3 3-3 6-3 3 3 6 3"/>
    </g>
  </g>
  <!-- prohibition pictogram: person inside crossed ring -->
  <g>
    <circle cx="60" cy="32.5" r="2.4" fill="#ffffff"/>
    <path d="M 56.6,42.6 v-3.1 a 3.4,3.4 0 0 1 6.8,0 v3.1 z" fill="#ffffff"/>
    <circle cx="60" cy="36.5" r="10.5" fill="none" stroke="#ffffff" stroke-width="2.1"/>
    <line x1="52.6" y1="29.1" x2="67.4" y2="43.9" stroke="#ffffff" stroke-width="2.1"/>
  </g>
  {en}
  <g opacity="0.55">{brand}</g>
</svg>'''

svg_path = f"{REPO}/willipu_kleebis_privaatruum.svg"
with open(svg_path, "w") as fh:
    fh.write(svg)

import cairosvg
pdf_path = f"{REPO}/willipu_kleebis_privaatruum.pdf"
cairosvg.svg2pdf(bytestring=svg.encode(), write_to=pdf_path)

png_path = f"{REPO}/willipu_kleebis_privaatruum.png"
cairosvg.svg2png(bytestring=svg.encode(), write_to=png_path, output_width=1417, output_height=827)
from PIL import Image
im = Image.open(png_path)
im.save(png_path, "PNG", dpi=(300, 300))

print(svg_path)
print(pdf_path, "· vektor, 120x70 mm")
print(png_path, "· 300 dpi")
