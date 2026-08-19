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

def placed_text_left(font_file, text, em_mm, baseline_y, fill, left_x=0):
    _, frag = text_outline(font_file, text, em_mm)
    return f'<g transform="translate({left_x:.3f} {baseline_y:.3f})" fill="{fill}">{frag}</g>'

et = placed_text("fraunces-600.ttf", "Läbipääs keelatud", 6.4, 56.6, "#ffffff")
en = placed_text("inter-600.ttf", "Private · Staff only", 3.7, 64.2, "#ffffff")
brand = placed_text_left("fraunces-700.ttf", "Willipu", 6.5, 14.4, "#ffffff", left_x=21.0)

svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="120mm" height="70mm" viewBox="0 0 120 70">
  <rect width="120" height="70" rx="4" fill="{GREEN_HEX}"/>
  <g transform="translate(7.2 5.2) scale(0.083)">
    <circle cx="65" cy="65" r="55" fill="#ffffff" fill-opacity="0.14"/>
    <g transform="translate(27.60 27.60) scale(3.1167)" fill="none" stroke="#ffffff" stroke-width="1.8" stroke-linecap="round">
      <path d="M3 14c3 0 3-3 6-3s3 3 6 3 3-3 6-3 3 3 6 3"/>
      <path d="M3 19c3 0 3-3 6-3s3 3 6 3 3-3 6-3 3 3 6 3"/>
    </g>
  </g>
  {brand}
  <!-- prohibition pictogram: stop hand (Font Awesome Free, CC BY 4.0) in white crossed ring -->
  <g transform="translate(53.5 28.5) scale(0.0253)" fill="#ffffff">
    <path d="M288 32c0-17.7-14.3-32-32-32s-32 14.3-32 32l0 208c0 8.8-7.2 16-16 16s-16-7.2-16-16l0-176c0-17.7-14.3-32-32-32s-32 14.3-32 32l0 272c0 1.5 0 3.1 .1 4.6L67.6 283c-16-15.2-41.3-14.6-56.6 1.4S-3.6 325.7 12.4 341L124.8 448c43.1 41.1 100.4 64 160 64l19.2 0c97.2 0 176-78.8 176-176l0-208c0-17.7-14.3-32-32-32s-32 14.3-32 32l0 112c0 8.8-7.2 16-16 16s-16-7.2-16-16l0-176c0-17.7-14.3-32-32-32s-32 14.3-32 32l0 176c0 8.8-7.2 16-16 16s-16-7.2-16-16l0-208z"/>
  </g>
  <line x1="51.8" y1="26.8" x2="68.2" y2="43.2" stroke="{GREEN_HEX}" stroke-width="4.2"/>
  <line x1="51.8" y1="26.8" x2="68.2" y2="43.2" stroke="#ffffff" stroke-width="2.2"/>
  <circle cx="60" cy="35" r="11.6" fill="none" stroke="#ffffff" stroke-width="2.2"/>
  {et}
  {en}
</svg>'''

svg_path = f"{REPO}/willipu_kleebis_privaatruum.svg"
with open(svg_path, "w") as fh:
    fh.write(svg)

import cairosvg
from pdf_compat import svg_to_pdf
pdf_path = f"{REPO}/willipu_kleebis_privaatruum.pdf"
svg_to_pdf(svg, pdf_path)

png_path = f"{REPO}/willipu_kleebis_privaatruum.png"
cairosvg.svg2png(bytestring=svg.encode(), write_to=png_path, output_width=1417, output_height=827)
from PIL import Image
im = Image.open(png_path)
im.save(png_path, "PNG", dpi=(300, 300))

print(svg_path)
print(pdf_path, "· vektor, 120x70 mm")
print(png_path, "· 300 dpi")
