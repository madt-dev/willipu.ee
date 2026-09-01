#!/usr/bin/env python3
"""LED indicator sticker for Willipu — 35 mm tall, aperture for the LED.

A 20 mm round hole sits at the left end; the device's LED shows through it.
Chevrons point at the hole and the text explains what a lit LED means.
Height is fixed; the width follows the text and is capped at 600 mm.

Usage: python3 make_led_kleebis.py ["<Estonian>"] ["<ENGLISH>"]
Outputs willipu_kleebis_led.{svg,pdf,png}. Fonts come from ./fonts/
(run make_qr_kleebis.py once first to fetch them).
"""
import os
import sys

from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen

from pdf_compat import svg_to_pdf

REPO = os.path.dirname(os.path.abspath(__file__))
FONTS = os.path.join(REPO, "fonts")
GREEN_HEX = "#2d4a3e"

if not os.path.exists(os.path.join(FONTS, "fraunces-600.ttf")):
    raise SystemExit("Run make_qr_kleebis.py once first to fetch fonts.")

et_text = sys.argv[1] if len(sys.argv) > 1 else "Seade kasutusvalmis"
en_text = sys.argv[2] if len(sys.argv) > 2 else "DEVICE READY TO USE"

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

def cap_ratio(fn):
    f = _tt(fn)
    return f["OS/2"].sCapHeight / f["head"].unitsPerEm

def em_width(fn, text, tracking=0.0):
    w, _ = text_outline(fn, text, 1.0)
    return w + tracking * max(len(text) - 1, 0)


# ── geometry ──────────────────────────────────────────────────────────────
H = 35.0            # fixed height
MAX_W = 600.0       # hard ceiling
RADIUS = 4.0        # corner radius

LED_D = 20.0        # aperture the LED shows through
LED_R = LED_D / 2
LED_CX = 6.0 + LED_R          # 6 mm of green left of the hole
CY = H / 2

RING_GAP = 0.9      # white ring sits just outside the hole
RING_W = 1.6

CHEV_X = [34.0, 42.0, 50.0]   # apex positions, pointing left at the hole
CHEV_HALF = 5.6
CHEV_RUN = 4.6

TEXT_X = CHEV_X[-1] + CHEV_RUN + 9.0
RIGHT_MARGIN = 11.0

ET_FN, EN_FN = "fraunces-600.ttf", "inter-600.ttf"
EN_TRACK = 0.14

et_cap, en_cap, gap = 9.0, 5.0, 3.6
et_em = et_cap / cap_ratio(ET_FN)
en_em = en_cap / cap_ratio(EN_FN)

block_h = et_cap + gap + en_cap
et_y = (H - block_h) / 2 + et_cap
en_y = et_y + gap + en_cap

et_w = em_width(ET_FN, et_text) * et_em
en_w = em_width(EN_FN, en_text, EN_TRACK) * en_em

W = round((TEXT_X + max(et_w, en_w) + RIGHT_MARGIN) / 5) * 5
if W > MAX_W:
    raise SystemExit(f"Text needs {W:g} mm — over the {MAX_W:g} mm limit.")

_, et_frag = at(ET_FN, et_text, et_em, et_y, "#ffffff", TEXT_X)
_, en_frag = tracked(EN_FN, en_text, en_em, en_y, "#c3d0c8", EN_TRACK, TEXT_X)

# background with the LED hole knocked out (even-odd fill)
bg = (
    f"M {RADIUS} 0 H {W - RADIUS} A {RADIUS} {RADIUS} 0 0 1 {W} {RADIUS} "
    f"V {H - RADIUS} A {RADIUS} {RADIUS} 0 0 1 {W - RADIUS} {H} "
    f"H {RADIUS} A {RADIUS} {RADIUS} 0 0 1 0 {H - RADIUS} "
    f"V {RADIUS} A {RADIUS} {RADIUS} 0 0 1 {RADIUS} 0 Z "
    f"M {LED_CX - LED_R} {CY} a {LED_R} {LED_R} 0 1 0 {LED_D} 0 "
    f"a {LED_R} {LED_R} 0 1 0 {-LED_D} 0 Z"
)

chevrons = "\n  ".join(
    f'<path d="M {x + CHEV_RUN:.2f} {CY - CHEV_HALF:.2f} L {x:.2f} {CY:.2f} '
    f'L {x + CHEV_RUN:.2f} {CY + CHEV_HALF:.2f}" fill="none" stroke="#ffffff" '
    f'stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" '
    f'opacity="{op}"/>'
    for x, op in zip(CHEV_X, ["1", "0.72", "0.44"])
)

svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W:g}mm" height="{H:g}mm" viewBox="0 0 {W:g} {H:g}">
  <path d="{bg}" fill="{GREEN_HEX}" fill-rule="evenodd"/>
  <circle cx="{LED_CX:g}" cy="{CY:g}" r="{LED_R + RING_GAP + RING_W / 2:g}"
          fill="none" stroke="#ffffff" stroke-width="{RING_W:g}"/>
  {chevrons}
  {et_frag}
  {en_frag}
</svg>'''

svg_path = f"{REPO}/willipu_kleebis_led.svg"
with open(svg_path, "w") as fh:
    fh.write(svg)

pdf_path = svg_to_pdf(svg, f"{REPO}/willipu_kleebis_led.pdf")

import cairosvg
png_path = f"{REPO}/willipu_kleebis_led.png"
cairosvg.svg2png(bytestring=svg.encode(), write_to=png_path,
                 output_width=round(W / 25.4 * 300), output_height=round(H / 25.4 * 300))
from PIL import Image
Image.open(png_path).save(png_path, "PNG", dpi=(300, 300))

print(svg_path)
print(pdf_path, f"· vektor, {W:g}x{H:g} mm · LED-ava ⌀{LED_D:g} mm")
print(png_path, "· 300 dpi")
