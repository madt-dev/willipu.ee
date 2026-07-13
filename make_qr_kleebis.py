#!/usr/bin/env python3
"""Generate a QR code + print-ready sticker for a willipu.ee manual page.

Usage: python3 make_qr_kleebis.py [slug] [title_et] [title_en]
Defaults to the washing machine manual. Outputs:
  willipu_qr_<slug>.png       — plain QR code (for custom layouts)
  willipu_kleebis_<slug>.png  — print-ready sticker, 80x100mm at 300dpi

Fonts are downloaded to ./fonts/ by make_og_image.py (run it once first,
or this script fetches them the same way).
"""
import os
import re
import sys
import urllib.request

import qrcode
from qrcode.constants import ERROR_CORRECT_H
from PIL import Image, ImageDraw, ImageFont

REPO = os.path.dirname(os.path.abspath(__file__))
FONTS = os.path.join(REPO, "fonts")
GREEN = (45, 74, 62)  # site theme #2d4a3e
WHITE = (255, 255, 255)
CREAM = (245, 242, 234)
DARKTXT = (34, 50, 43)

FONT_CSS = {
    "fraunces": "https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,600;9..144,700&display=swap",
    "inter": "https://fonts.googleapis.com/css2?family=Inter:wght@500;600&display=swap",
}
FONT_WEIGHTS = {"fraunces": ["600", "700"], "inter": ["500", "600"]}


def fetch_fonts():
    for family, css_url in FONT_CSS.items():
        weights = FONT_WEIGHTS[family]
        if all(os.path.exists(os.path.join(FONTS, f"{family}-{wt}.ttf")) for wt in weights):
            continue
        os.makedirs(FONTS, exist_ok=True)
        req = urllib.request.Request(css_url, headers={"User-Agent": "Mozilla/5.0"})
        css = urllib.request.urlopen(req).read().decode()
        urls = re.findall(r"https://fonts\.gstatic\.com/[^)]+", css)
        for wt, u in zip(weights, urls):
            urllib.request.urlretrieve(u, os.path.join(FONTS, f"{family}-{wt}.ttf"))


slug = sys.argv[1] if len(sys.argv) > 1 else "pesumasin"
title_et = sys.argv[2] if len(sys.argv) > 2 else "Pesumasina kasutusjuhend"
title_en = sys.argv[3] if len(sys.argv) > 3 else "Washing machine · Инструкция"
url = f"https://willipu.ee/juhend/{slug}/"

fetch_fonts()

def F(name, size):
    return ImageFont.truetype(os.path.join(FONTS, name), size)

# --- plain QR (dark green on white, high error correction) ---
qr = qrcode.QRCode(error_correction=ERROR_CORRECT_H, box_size=20, border=2)
qr.add_data(url)
qr.make(fit=True)
qr_img = qr.make_image(fill_color=GREEN, back_color="white").convert("RGB")
qr_path = f"{REPO}/willipu_qr_{slug}.png"
qr_img.save(qr_path)

# --- sticker: 80x100 mm at 300 dpi = 945x1181 px ---
W, H = 945, 1181
img = Image.new("RGB", (W, H), GREEN)
d = ImageDraw.Draw(img)

# header: wave icon + wordmark
logo = Image.open(f"{REPO}/willipu_logo_white.png").convert("RGBA")
bbox = logo.crop((0, 0, 300, logo.height)).getbbox()
icon = logo.crop(bbox).resize((92, 92), Image.LANCZOS)
img.paste(icon, (64, 56), icon)
d.text((180, 62), "Willipu", font=F("fraunces-700.ttf", 68), fill=WHITE)

# white card with QR
CARD = 700
card = ((W - CARD) // 2, 190, (W + CARD) // 2, 190 + CARD)
d.rounded_rectangle(card, radius=28, fill=WHITE)
qr_size = CARD - 72
qr_big = qr_img.resize((qr_size, qr_size), Image.NEAREST)
img.paste(qr_big, (card[0] + 36, card[1] + 36))

# titles under the card
y = card[3] + 40
f_et = F("fraunces-600.ttf", 44)
tw = d.textbbox((0, 0), title_et, font=f_et)[2]
d.text(((W - tw) // 2, y), title_et, font=f_et, fill=WHITE)

f_en = F("inter-500.ttf", 27)
tw2 = d.textbbox((0, 0), title_en, font=f_en)[2]
d.text(((W - tw2) // 2, y + 66), title_en, font=f_en, fill=(255, 255, 255, 220))

# url pill at the bottom
f_url = F("inter-600.ttf", 26)
short = url.replace("https://", "")
tb = d.textbbox((0, 0), short, font=f_url)
pw, ph = tb[2] - tb[0], tb[3] - tb[1]
px1, px2 = (W - pw - 72) // 2, (W + pw + 72) // 2
py2 = H - 56
py1 = py2 - ph - 40
d.rounded_rectangle((px1, py1, px2, py2), radius=(py2 - py1) // 2, fill=CREAM)
d.text(((px1 + px2 - pw) // 2 - tb[0], (py1 + py2 - ph) // 2 - tb[1]),
       short, font=f_url, fill=DARKTXT)

out = f"{REPO}/willipu_kleebis_{slug}.png"
img.save(out, "PNG", dpi=(300, 300))
print(qr_path)
print(out, "· 80x100 mm @ 300 dpi")

# ---------------------------------------------------------------------------
# Vector outputs: SVG (all text converted to outlines) + print-ready PDF
# ---------------------------------------------------------------------------
from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen

_font_cache = {}

def _tt(path):
    if path not in _font_cache:
        _font_cache[path] = TTFont(os.path.join(FONTS, path))
    return _font_cache[path]

def text_outline(font_file, text, em_mm):
    """Return (width_mm, svg_fragment) with the text as vector paths."""
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

def placed_text(font_file, text, em_mm, baseline_y, fill, center_x=None, left_x=None):
    w, frag = text_outline(font_file, text, em_mm)
    tx = (center_x - w / 2) if center_x is not None else left_x
    return w, f'<g transform="translate({tx:.3f} {baseline_y:.3f})" fill="{fill}">{frag}</g>'

def qr_svg_path(matrix, size_mm):
    n = len(matrix)
    m = size_mm / n
    cells = []
    for r, row in enumerate(matrix):
        for c, v in enumerate(row):
            if v:
                cells.append(f'M{c * m:.3f} {r * m:.3f}h{m:.3f}v{m:.3f}h{-m:.3f}z')
    return "".join(cells)

GREEN_HEX = "#2d4a3e"
CREAM_HEX = "#f5f2ea"

qr0 = qrcode.QRCode(error_correction=ERROR_CORRECT_H, border=0)
qr0.add_data(url)
qr0.make(fit=True)
matrix = qr0.get_matrix()

QR_MM = 49.0
qr_x, qr_y = (80 - QR_MM) / 2, 21.5

_, et_frag = placed_text("fraunces-600.ttf", title_et, 3.73, 81.6, "#ffffff", center_x=40)
_, en_frag = placed_text("inter-500.ttf", title_en, 2.29, 86.2, "#ffffff", center_x=40)
url_w, url_frag = placed_text("inter-600.ttf", url.replace("https://", ""), 2.2, 93.1, GREEN_HEX, center_x=40)
pill_w = url_w + 6
# wordmark from the existing vector logo (already outlines)
WORDMARK = (
    '<g transform="translate(15.2 10.55) scale(0.0796)" fill="#ffffff">'
    '<path transform="translate(0.00 0) scale(0.048828 -0.048828)" d="M1745 0H1487L1149 1087L811 0H553L127 1372H-18V1493H690V1372H530L815 455L1137 1493H1421L1749 438L2040 1372H1862V1493H2324V1372H2171Z"/>'
    '<path transform="translate(112.30 0) scale(0.048828 -0.048828)" d="M188 1364Q188 1445 244.0 1500.5Q300 1556 381 1556Q460 1556 515.5 1500.5Q571 1445 571 1364Q571 1285 515.5 1229.5Q460 1174 381 1174Q300 1174 244.0 1229.0Q188 1284 188 1364ZM575 121H727V0H70V121H221V942H70V1063H575Z"/>'
    '<path transform="translate(150.29 0) scale(0.048828 -0.048828)" d="M575 121H727V0H70V121H221V1436H70V1556H575Z"/>'
    '<path transform="translate(188.28 0) scale(0.048828 -0.048828)" d="M575 121H727V0H70V121H221V1436H70V1556H575Z"/>'
    '<path transform="translate(226.27 0) scale(0.048828 -0.048828)" d="M188 1364Q188 1445 244.0 1500.5Q300 1556 381 1556Q460 1556 515.5 1500.5Q571 1445 571 1364Q571 1285 515.5 1229.5Q460 1174 381 1174Q300 1174 244.0 1229.0Q188 1284 188 1364ZM575 121H727V0H70V121H221V942H70V1063H575Z"/>'
    '<path transform="translate(264.26 0) scale(0.048828 -0.048828)" d="M553 584V479Q553 293 600.5 210.0Q648 127 754 127Q863 127 907.5 215.0Q952 303 952 532Q952 761 907.5 848.5Q863 936 754 936Q648 936 600.5 853.0Q553 770 553 584ZM199 942H47V1063H553V928Q598 1011 674.0 1051.5Q750 1092 862 1092Q1089 1092 1219.5 942.5Q1350 793 1350 532Q1350 271 1219.5 121.0Q1089 -29 862 -29Q750 -29 674.0 11.5Q598 52 553 135V-305H717V-426H47V-305H199Z"/>'
    '<path transform="translate(334.18 0) scale(0.048828 -0.048828)" d="M1268 1063V121H1419V0H913V150Q850 55 768.0 13.0Q686 -29 561 -29Q382 -29 290.5 76.5Q199 182 199 387V942H47V1063H553V442Q553 244 586.0 190.5Q619 137 707 137Q814 137 863.5 216.0Q913 295 913 467V942H784V1063Z"/>'
    "</g>"
)

svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="80mm" height="100mm" viewBox="0 0 80 100">
  <rect width="80" height="100" fill="{GREEN_HEX}"/>
  <g transform="translate(4.8 4.6) scale(0.0615)">
    <circle cx="65" cy="65" r="55" fill="#ffffff" fill-opacity="0.14"/>
    <g transform="translate(27.60 27.60) scale(3.1167)" fill="none" stroke="#ffffff" stroke-width="1.8" stroke-linecap="round">
      <path d="M3 14c3 0 3-3 6-3s3 3 6 3 3-3 6-3 3 3 6 3"/>
      <path d="M3 19c3 0 3-3 6-3s3 3 6 3 3-3 6-3 3 3 6 3"/>
    </g>
  </g>
  {WORDMARK}
  <rect x="10" y="16" width="60" height="60" rx="2.4" fill="#ffffff"/>
  <path transform="translate({qr_x:.3f} {qr_y:.3f})" d="{qr_svg_path(matrix, QR_MM)}" fill="{GREEN_HEX}"/>
  {et_frag}
  <g opacity="0.88">{en_frag}</g>
  <rect x="{40 - pill_w / 2:.3f}" y="89.2" width="{pill_w:.3f}" height="6.1" rx="3.05" fill="{CREAM_HEX}"/>
  {url_frag}
</svg>'''

svg_path = f"{REPO}/willipu_kleebis_{slug}.svg"
with open(svg_path, "w") as fh:
    fh.write(svg)

import cairosvg
pdf_path = f"{REPO}/willipu_kleebis_{slug}.pdf"
cairosvg.svg2pdf(bytestring=svg.encode(), write_to=pdf_path)

# plain QR as SVG too
qr_plain = f'''<svg xmlns="http://www.w3.org/2000/svg" width="50mm" height="50mm" viewBox="-4 -4 {len(matrix) + 8} {len(matrix) + 8}">
  <rect x="-4" y="-4" width="{len(matrix) + 8}" height="{len(matrix) + 8}" fill="#ffffff"/>
  <path d="{qr_svg_path(matrix, len(matrix))}" fill="{GREEN_HEX}"/>
</svg>'''
qr_svg_file = f"{REPO}/willipu_qr_{slug}.svg"
with open(qr_svg_file, "w") as fh:
    fh.write(qr_plain)

print(svg_path)
print(pdf_path, "· vektor, 80x100 mm")
print(qr_svg_file)
