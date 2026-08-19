#!/usr/bin/env python3
"""Kitchen door sign for Willipu — pictogram + 7 languages, 260x130 mm.

Outputs willipu_silt_kook.{svg,pdf,png}. Fonts come from ./fonts/
(run make_qr_kleebis.py once first to fetch them).
"""
import os

from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen

from pdf_compat import svg_to_pdf

REPO = os.path.dirname(os.path.abspath(__file__))
FONTS = os.path.join(REPO, "fonts")
GREEN_HEX = "#2d4a3e"
MUTED = "#c3d0c8"

if not os.path.exists(os.path.join(FONTS, "fraunces-600.ttf")):
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
    return x * s, f'<g transform="scale({s:.6f} {-s:.6f})">{"".join(parts)}</g>'

def at(font_file, text, em_mm, baseline_y, fill, x):
    w, frag = text_outline(font_file, text, em_mm)
    return w, f'<g transform="translate({x:.3f} {baseline_y:.3f})" fill="{fill}">{frag}</g>'

def tracked(font_file, text, em_mm, baseline_y, fill, tracking, x):
    f = _tt(font_file)
    upm = f["head"].unitsPerEm
    glyphset = f.getGlyphSet()
    cmap = f.getBestCmap()
    s = em_mm / upm
    extra = tracking * em_mm
    cx = 0.0
    parts = []
    for ch in text:
        gname = cmap.get(ord(ch), ".notdef")
        glyph = glyphset[gname]
        pen = SVGPathPen(glyphset)
        glyph.draw(pen)
        cmds = pen.getCommands()
        if cmds:
            parts.append(f'<g transform="translate({cx:.4f} 0) scale({s:.6f} {-s:.6f})"><path d="{cmds}"/></g>')
        cx += glyph.width * s + extra
    total = cx - extra if text else 0
    return total, f'<g transform="translate({x:.3f} {baseline_y:.3f})" fill="{fill}">{"".join(parts)}</g>'


# text block is centred in the area right of the divider
TEXT_CX = 175.0

def centred(fn, text, em, y, fill, tracking=None):
    if tracking is None:
        w, _ = text_outline(fn, text, em)
        return at(fn, text, em, y, fill, TEXT_CX - w / 2)[1]
    w, _ = tracked(fn, text, em, y, fill, tracking, 0)
    return tracked(fn, text, em, y, fill, tracking, TEXT_CX - w / 2)[1]

et_frag = centred("fraunces-600.ttf", "Köök", 33.0, 78.0, "#ffffff")
en_frag = centred("inter-600.ttf", "KITCHEN", 11.0, 97.0, "#ffffff", tracking=0.12)

brand_w, brand_frag = at("fraunces-700.ttf", "Willipu", 6.4, 22.5, "#ffffff", 25.5)

svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="260mm" height="130mm" viewBox="0 0 260 130">
  <rect width="260" height="130" rx="6" fill="{GREEN_HEX}"/>

  <!-- brand mark, top left -->
  <g transform="translate(12.5 12.5) scale(0.083)">
    <circle cx="65" cy="65" r="55" fill="#ffffff" fill-opacity="0.14"/>
    <g transform="translate(27.60 27.60) scale(3.1167)" fill="none" stroke="#ffffff"
       stroke-width="1.8" stroke-linecap="round">
      <path d="M3 14c3 0 3-3 6-3s3 3 6 3 3-3 6-3 3 3 6 3"/>
      <path d="M3 19c3 0 3-3 6-3s3 3 6 3 3-3 6-3 3 3 6 3"/>
    </g>
  </g>
  {brand_frag}

  <!-- pictogram: plate with fork and knife -->
  <g stroke="#ffffff" fill="none" stroke-linecap="round" stroke-linejoin="round">
    <circle cx="49" cy="76" r="19.5" stroke-width="3.0"/>
    <circle cx="49" cy="76" r="12.0" stroke-width="2.0"/>
  </g>
  <g fill="#ffffff">
    <!-- fork -->
    <rect x="14.2" y="49" width="2.4" height="15" rx="1.2"/>
    <rect x="19.0" y="49" width="2.4" height="15" rx="1.2"/>
    <rect x="23.8" y="49" width="2.4" height="15" rx="1.2"/>
    <path d="M 14.2 61 h 12 v 3.2 a 4.4 4.4 0 0 1 -4.4 4.4 h -0.5 v 34.4 a 1.9 1.9 0 0 1 -2.2 0 v -34.4 h -0.5 a 4.4 4.4 0 0 1 -4.4 -4.4 z"/>
    <rect x="18.9" y="66" width="3.0" height="37.4" rx="1.5"/>
    <!-- knife -->
    <path d="M 74.6 49 a 5.6 5.6 0 0 1 5.6 5.6 v 16.2 a 5.6 5.6 0 0 1 -5.6 5.6 z"/>
    <rect x="73.2" y="70" width="3.0" height="33.4" rx="1.5"/>
  </g>

  <!-- divider -->
  <line x1="88" y1="36" x2="88" y2="106" stroke="#ffffff" stroke-opacity="0.3" stroke-width="0.7"/>

  {et_frag}
  {en_frag}
</svg>'''

svg_path = f"{REPO}/willipu_silt_kook.svg"
with open(svg_path, "w") as fh:
    fh.write(svg)

pdf_path = svg_to_pdf(svg, f"{REPO}/willipu_silt_kook.pdf")

import cairosvg
png_path = f"{REPO}/willipu_silt_kook.png"
cairosvg.svg2png(bytestring=svg.encode(), write_to=png_path,
                 output_width=3071, output_height=1535)
from PIL import Image
Image.open(png_path).save(png_path, "PNG", dpi=(300, 300))

print(svg_path)
print(pdf_path, "· vektor, 260x130 mm")
print(png_path, "· 300 dpi")
