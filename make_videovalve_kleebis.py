#!/usr/bin/env python3
"""Video-surveillance notice sticker for Willipu — GDPR info, 80x120 mm.

Outputs willipu_kleebis_videovalve.{svg,pdf,png} (vector + 300 dpi preview).
Reuses the fonts fetched by make_qr_kleebis.py (./fonts/).
"""
import os

from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen

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

def centered(font_file, text, em_mm, baseline_y, fill, center_x=40):
    w, frag = text_outline(font_file, text, em_mm)
    return f'<g transform="translate({center_x - w / 2:.3f} {baseline_y:.3f})" fill="{fill}">{frag}</g>'

def left(font_file, text, em_mm, baseline_y, fill, x=7.5):
    w, frag = text_outline(font_file, text, em_mm)
    return w, f'<g transform="translate({x:.3f} {baseline_y:.3f})" fill="{fill}">{frag}</g>'

def tracked(font_file, text, em_mm, baseline_y, fill, tracking=0.14, center_x=40):
    """Letter-spaced uppercase label."""
    f = _tt(font_file)
    upm = f["head"].unitsPerEm
    glyphset = f.getGlyphSet()
    cmap = f.getBestCmap()
    s = em_mm / upm
    extra = tracking * em_mm
    x = 0.0
    parts = []
    for ch in text:
        gname = cmap.get(ord(ch), ".notdef")
        glyph = glyphset[gname]
        pen = SVGPathPen(glyphset)
        glyph.draw(pen)
        cmds = pen.getCommands()
        if cmds:
            parts.append(f'<g transform="translate({x:.4f} 0) scale({s:.6f} {-s:.6f})"><path d="{cmds}"/></g>')
        x += glyph.width * s + extra
    total = x - extra if text else 0
    return f'<g transform="translate({center_x - total / 2:.3f} {baseline_y:.3f})" fill="{fill}">{"".join(parts)}</g>'


# ── content ────────────────────────────────────────────────────────────────
INFO = [
    ("Eesmärk:", " õigusrikkumiste tuvastamine,"),
    ("", "vara ja isikute kaitse."),
    ("Õiguslik alus:", " õigustatud huvi"),
    ("Vastutav töötleja:", " OÜ Willipu Turism"),
    ("Täpsem info:", " willipu.willipu@gmail.com"),
]

BODY_EM = 2.55
LINE_H = 4.85
info_start_y = 91.5

info_frags = []
for i, (label, rest) in enumerate(INFO):
    y = info_start_y + i * LINE_H
    x = 7.5
    if label:
        w, frag = left("inter-600.ttf", label, BODY_EM, y, "#ffffff", x)
        info_frags.append(frag)
        x += w
    if rest:
        _, frag = left("inter-500.ttf", rest.lstrip() if not label else rest, BODY_EM, y, MUTED, x)
        info_frags.append(frag)
info_block = "\n  ".join(info_frags)

brand_w, brand_frag = left("fraunces-700.ttf", "Willipu", 5.0, 12.6, "#ffffff", x=16.6)
title = tracked("inter-600.ttf", "VIDEOVALVE", 4.9, 71.5, "#ffffff", tracking=0.10)
title_en = tracked("inter-500.ttf", "VIDEO SURVEILLANCE", 2.6, 77.8, MUTED, tracking=0.16)

svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="80mm" height="120mm" viewBox="0 0 80 120">
  <rect width="80" height="120" rx="4" fill="{GREEN_HEX}"/>

  <!-- header: wave mark + wordmark -->
  <g transform="translate(5.4 4.4) scale(0.0725)">
    <circle cx="65" cy="65" r="55" fill="#ffffff" fill-opacity="0.14"/>
    <g transform="translate(27.60 27.60) scale(3.1167)" fill="none" stroke="#ffffff" stroke-width="1.8" stroke-linecap="round">
      <path d="M3 14c3 0 3-3 6-3s3 3 6 3 3-3 6-3 3 3 6 3"/>
      <path d="M3 19c3 0 3-3 6-3s3 3 6 3 3-3 6-3 3 3 6 3"/>
    </g>
  </g>
  {brand_frag}

  <!-- CCTV camera pictogram -->
  <g transform="translate(40 42.5)" fill="#ffffff">
    <g transform="rotate(-20)">
      <rect x="-10.5" y="-5.0" width="21.5" height="10.0" rx="2.6"/>
      <rect x="-14.8" y="-6.6" width="5.0" height="13.2" rx="1.5"/>
      <rect x="10.6" y="-2.8" width="3.4" height="5.6" rx="1.1"/>
    </g>
    <rect x="3.0" y="3.2" width="3.0" height="13.4" rx="1.2"/>
    <rect x="-3.4" y="16.0" width="15.8" height="3.0" rx="1.5"/>
  </g>

  {title}
  {title_en}

  <line x1="7.5" y1="84.0" x2="72.5" y2="84.0" stroke="#ffffff" stroke-opacity="0.28" stroke-width="0.5"/>

  {info_block}
</svg>'''

svg_path = f"{REPO}/willipu_kleebis_videovalve.svg"
with open(svg_path, "w") as fh:
    fh.write(svg)

import cairosvg
pdf_path = f"{REPO}/willipu_kleebis_videovalve.pdf"
cairosvg.svg2pdf(bytestring=svg.encode(), write_to=pdf_path)

png_path = f"{REPO}/willipu_kleebis_videovalve.png"
cairosvg.svg2png(bytestring=svg.encode(), write_to=png_path,
                 output_width=945, output_height=1417)
from PIL import Image
Image.open(png_path).save(png_path, "PNG", dpi=(300, 300))

print(svg_path)
print(pdf_path, "· vektor, 80x120 mm")
print(png_path, "· 300 dpi")
