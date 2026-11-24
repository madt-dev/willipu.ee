#!/usr/bin/env python3
"""Mastlifti juhtpaneeli märgutulede kleebis (eestikeelne) — 135x85 mm.

Asendab soomekeelse tähenduste tabeli (NRO / MERKITYS) juhtkapil.
Outputs willipu_kleebis_lift.{svg,pdf,png} (vector PDF 1.4 + 300 dpi preview).
All text is converted to outlines, so the PDF needs no fonts at the print shop.
"""
import os

import cairosvg
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.ttLib import TTFont
from PIL import Image

from pdf_compat import svg_to_pdf

REPO = os.path.dirname(os.path.abspath(__file__))
FONT_DIR = "/usr/share/fonts/opentype/inter"
BOLD = "Inter-Bold.otf"
SEMI = "Inter-SemiBold.otf"
MED = "Inter-Medium.otf"

W, H = 135.0, 85.0
RED = "#e30b3c"          # signal red-magenta like the original label
INK = "#111111"

ROWS = [
    ("7", "MASTI PIIRLÜLITI", ""),
    ("8", "MOOTORI KAITSELÜLITI RAKENDUNUD", ""),
    ("9", "HÄDASEISKAMINE", ""),
    ("10", "KORRUSEPOOLNE UKS AVATUD", ""),
    ("11", "MAAPINNAPOOLNE UKS AVATUD", ""),
    ("12", "PAIGALDUSSILD ALUMISES ASENDIS", "(lisavarustus)"),
    ("13", "KATUSELUUK AVATUD", ""),
    ("14", "TURVAPIDUR RAKENDUNUD", ""),
    ("15", "LIFTIKORV MASTI TURVAPIIRIL", ""),
    ("16", "LIFTIKORVI KÜLGUKS AVATUD", "(lisavarustus)"),
    ("17", "SAGEDUSMUUNDURI RIKE", "(lisavarustus)"),
]

_fonts = {}


def _font(name):
    if name not in _fonts:
        _fonts[name] = TTFont(os.path.join(FONT_DIR, name))
    return _fonts[name]


def outline(font_name, text, size, x, baseline, fill=INK, anchor="start", track=0.0):
    """Text as SVG paths. size = em in mm, track = extra letter spacing in mm."""
    f = _font(font_name)
    upm = f["head"].unitsPerEm
    gs = f.getGlyphSet()
    cmap = f.getBestCmap()
    s = size / upm
    pos, parts = 0.0, []
    for ch in text:
        g = gs[cmap.get(ord(ch), ".notdef")]
        pen = SVGPathPen(gs)
        g.draw(pen)
        d = pen.getCommands()
        if d:
            parts.append(f'<path transform="translate({pos / s:.2f} 0)" d="{d}"/>')
        pos += g.width * s + track
    width = pos - track if text else 0
    if anchor == "end":
        x -= width
    elif anchor == "middle":
        x -= width / 2
    return width, (f'<g fill="{fill}" transform="translate({x:.3f} {baseline:.3f}) '
                   f'scale({s:.6f} {-s:.6f})">{"".join(parts)}</g>')


# ---- frame -------------------------------------------------------------
M = 3.0          # white margin outside the red frame
FW = 3.2         # red frame width
frame_out = (M, M, W - 2 * M, H - 2 * M)
inner = (M + FW, M + FW, W - 2 * (M + FW), H - 2 * (M + FW))

# ---- table layout ------------------------------------------------------
NUM_R = 19.5     # right edge of the number column
TXT_X = 24.0     # start of meaning text
HEAD_Y = 12.9
ROW0 = 20.2
STEP = 5.48
SIZE = 3.85      # cap-height ≈ 2.8 mm — readable at arm's length
OPT = 3.1
MAX_R = inner[0] + inner[2] - 3.0

parts = []
_, f = outline(BOLD, "NR", 2.9, NUM_R, HEAD_Y, anchor="end", track=0.15)
parts.append(f)
_, f = outline(BOLD, "TÄHENDUS", 2.9, TXT_X, HEAD_Y, track=0.15)
parts.append(f)
parts.append(f'<line x1="{inner[0] + 3:.2f}" y1="{HEAD_Y + 1.6:.2f}" '
             f'x2="{MAX_R:.2f}" y2="{HEAD_Y + 1.6:.2f}" stroke="{RED}" stroke-width="0.35"/>')

for i, (num, txt, opt) in enumerate(ROWS):
    y = ROW0 + i * STEP
    if i % 2 == 1:
        parts.append(f'<rect x="{inner[0] + 2:.2f}" y="{y - 3.95:.2f}" width="{MAX_R - inner[0] - 1:.2f}" '
                     f'height="{STEP:.2f}" rx="0.8" fill="{RED}" fill-opacity="0.07"/>')
    _, f = outline(BOLD, num, SIZE, NUM_R, y, anchor="end")
    parts.append(f)
    w, f = outline(SEMI, txt, SIZE, TXT_X, y)
    parts.append(f)
    if opt:
        w2, f = outline(MED, opt, OPT, TXT_X + w + 1.3, y, fill="#555555")
        parts.append(f)
        assert TXT_X + w + 1.3 + w2 <= MAX_R, f"row {num} too wide"
    assert TXT_X + w <= MAX_R, f"row {num} too wide"

svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W:g}mm" height="{H:g}mm" viewBox="0 0 {W:g} {H:g}">
  <rect width="{W:g}" height="{H:g}" rx="3" fill="#ffffff"/>
  <rect x="{frame_out[0]:g}" y="{frame_out[1]:g}" width="{frame_out[2]:g}" height="{frame_out[3]:g}" rx="1" fill="{RED}"/>
  <rect x="{inner[0]:g}" y="{inner[1]:g}" width="{inner[2]:g}" height="{inner[3]:g}" fill="#ffffff"/>
  {"".join(parts)}
</svg>'''

base = f"{REPO}/willipu_kleebis_lift"
with open(base + ".svg", "w") as fh:
    fh.write(svg)
svg_to_pdf(svg, base + ".pdf")
cairosvg.svg2png(bytestring=svg.encode(), write_to=base + ".png",
                 output_width=round(W / 25.4 * 300), output_height=round(H / 25.4 * 300))
Image.open(base + ".png").save(base + ".png", "PNG", dpi=(300, 300))
print(base + ".{svg,pdf,png}", f"· {W:g}x{H:g} mm")
