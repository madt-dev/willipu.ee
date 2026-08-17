#!/usr/bin/env python3
"""Generate a QR code + print-ready sticker for a willipu.ee manual page.

Usage: python3 make_qr_kleebis.py [slug] [title_et] [sub_et] [title_en] [phone_line]
Defaults to the washing machine manual. Outputs:
  willipu_qr_<slug>.png       — plain QR code (for custom layouts)
  willipu_kleebis_<slug>.png  — print-ready sticker, 120x120mm at 300dpi
  willipu_kleebis_<slug>.svg / .pdf — vector versions (text as outlines)

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
title_et = sys.argv[2] if len(sys.argv) > 2 else "Tasuline pesumasin"
sub_et = sys.argv[3] if len(sys.argv) > 3 else "Juhend / osta kasutus"
title_en = sys.argv[4] if len(sys.argv) > 4 else "Paid washing machine · Instructions / purchase"
phone = sys.argv[5] if len(sys.argv) > 5 else "Sularahas maksmine / Cash payment · +372 5695 5758"
# Short tourist-friendly aliases (redirect pages in public/<short>/index.html)
SHORT_URLS = {"pesumasin": "wash", "pesukuivati": "dry"}
short_slug = SHORT_URLS.get(slug)
url = f"https://willipu.ee/{short_slug}/" if short_slug else f"https://willipu.ee/juhend/{slug}/"
url_display = url.replace("https://", "").rstrip("/") if short_slug else url.replace("https://", "")

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

# --- sticker: 120x120 mm at 300 dpi = 1417x1417 px ---
W, H = 1417, 1417
img = Image.new("RGB", (W, H), GREEN)
d = ImageDraw.Draw(img)

# header: wave icon + wordmark
logo = Image.open(f"{REPO}/willipu_logo_white.png").convert("RGBA")
bbox = logo.crop((0, 0, 300, logo.height)).getbbox()
icon = logo.crop(bbox).resize((132, 132), Image.LANCZOS)
img.paste(icon, (84, 58), icon)
d.text((248, 66), "Willipu", font=F("fraunces-700.ttf", 96), fill=WHITE)

# white card with QR
CARD = 732
card = ((W - CARD) // 2, 248, (W + CARD) // 2, 248 + CARD)
d.rounded_rectangle(card, radius=31, fill=WHITE)
qr_size = CARD - 94
qr_big = qr_img.resize((qr_size, qr_size), Image.NEAREST)
img.paste(qr_big, (card[0] + 47, card[1] + 47))

# titles under the card
y = card[3] + 30
f_et = F("fraunces-600.ttf", 64)
tw = d.textbbox((0, 0), title_et, font=f_et)[2]
d.text(((W - tw) // 2, y), title_et, font=f_et, fill=WHITE)

f_en = F("inter-600.ttf", 44)
tw2 = d.textbbox((0, 0), title_en, font=f_en)[2]
d.text(((W - tw2) // 2, y + 94), title_en, font=f_en, fill=WHITE)

f_sub = F("inter-500.ttf", 38)
tw_s = d.textbbox((0, 0), sub_et, font=f_sub)[2]
d.text(((W - tw_s) // 2, y + 168), sub_et, font=f_sub, fill=(205, 214, 208))

f_ph = F("inter-600.ttf", 34)
tw_p = d.textbbox((0, 0), phone, font=f_ph)[2]
d.text(((W - tw_p) // 2, y + 234), phone, font=f_ph, fill=WHITE)

# url pill at the bottom
f_url = F("inter-600.ttf", 30)
short = url_display
tb = d.textbbox((0, 0), short, font=f_url)
pw, ph = tb[2] - tb[0], tb[3] - tb[1]
px1, px2 = (W - pw - 76) // 2, (W + pw + 76) // 2
py2 = H - 38
py1 = py2 - ph - 40
d.rounded_rectangle((px1, py1, px2, py2), radius=(py2 - py1) // 2, fill=CREAM)
d.text(((px1 + px2 - pw) // 2 - tb[0], (py1 + py2 - ph) // 2 - tb[1]),
       short, font=f_url, fill=DARKTXT)

out = f"{REPO}/willipu_kleebis_{slug}.png"
img.save(out, "PNG", dpi=(300, 300))
print(qr_path)
print(out, "· 120x120 mm @ 300 dpi")

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

QR_MM = 54.0
qr_x, qr_y = (120 - QR_MM) / 2, 25.0

_, et_frag = placed_text("fraunces-600.ttf", title_et, 5.4, 90.6, "#ffffff", center_x=60)
_, en_frag = placed_text("inter-600.ttf", title_en, 3.7, 97.4, "#ffffff", center_x=60)
_, sub_frag = placed_text("inter-500.ttf", sub_et, 3.1, 103.0, "#ffffff", center_x=60)
_, ph_frag = placed_text("inter-600.ttf", phone, 2.8, 108.6, "#ffffff", center_x=60)
url_w, url_frag = placed_text("inter-600.ttf", url_display, 2.4, 115.5, GREEN_HEX, center_x=60)
pill_w = url_w + 7
# wordmark from the existing vector logo (already outlines)
WORDMARK = (
    '<g transform="translate(22.8 15.83) scale(0.1194)" fill="#ffffff">'
    '<path transform="translate(0.00 0) scale(0.048828 -0.048828)" d="M1745 0H1487L1149 1087L811 0H553L127 1372H-18V1493H690V1372H530L815 455L1137 1493H1421L1749 438L2040 1372H1862V1493H2324V1372H2171Z"/>'
    '<path transform="translate(112.30 0) scale(0.048828 -0.048828)" d="M188 1364Q188 1445 244.0 1500.5Q300 1556 381 1556Q460 1556 515.5 1500.5Q571 1445 571 1364Q571 1285 515.5 1229.5Q460 1174 381 1174Q300 1174 244.0 1229.0Q188 1284 188 1364ZM575 121H727V0H70V121H221V942H70V1063H575Z"/>'
    '<path transform="translate(150.29 0) scale(0.048828 -0.048828)" d="M575 121H727V0H70V121H221V1436H70V1556H575Z"/>'
    '<path transform="translate(188.28 0) scale(0.048828 -0.048828)" d="M575 121H727V0H70V121H221V1436H70V1556H575Z"/>'
    '<path transform="translate(226.27 0) scale(0.048828 -0.048828)" d="M188 1364Q188 1445 244.0 1500.5Q300 1556 381 1556Q460 1556 515.5 1500.5Q571 1445 571 1364Q571 1285 515.5 1229.5Q460 1174 381 1174Q300 1174 244.0 1229.0Q188 1284 188 1364ZM575 121H727V0H70V121H221V942H70V1063H575Z"/>'
    '<path transform="translate(264.26 0) scale(0.048828 -0.048828)" d="M553 584V479Q553 293 600.5 210.0Q648 127 754 127Q863 127 907.5 215.0Q952 303 952 532Q952 761 907.5 848.5Q863 936 754 936Q648 936 600.5 853.0Q553 770 553 584ZM199 942H47V1063H553V928Q598 1011 674.0 1051.5Q750 1092 862 1092Q1089 1092 1219.5 942.5Q1350 793 1350 532Q1350 271 1219.5 121.0Q1089 -29 862 -29Q750 -29 674.0 11.5Q598 52 553 135V-305H717V-426H47V-305H199Z"/>'
    '<path transform="translate(334.18 0) scale(0.048828 -0.048828)" d="M1268 1063V121H1419V0H913V150Q850 55 768.0 13.0Q686 -29 561 -29Q382 -29 290.5 76.5Q199 182 199 387V942H47V1063H553V442Q553 244 586.0 190.5Q619 137 707 137Q814 137 863.5 216.0Q913 295 913 467V942H784V1063Z"/>'
    "</g>"
)

svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="120mm" height="120mm" viewBox="0 0 120 120">
  <rect width="120" height="120" fill="{GREEN_HEX}"/>
  <g transform="translate(7.2 6.9) scale(0.09225)">
    <circle cx="65" cy="65" r="55" fill="#ffffff" fill-opacity="0.14"/>
    <g transform="translate(27.60 27.60) scale(3.1167)" fill="none" stroke="#ffffff" stroke-width="1.8" stroke-linecap="round">
      <path d="M3 14c3 0 3-3 6-3s3 3 6 3 3-3 6-3 3 3 6 3"/>
      <path d="M3 19c3 0 3-3 6-3s3 3 6 3 3-3 6-3 3 3 6 3"/>
    </g>
  </g>
  {WORDMARK}
  <rect x="29" y="21" width="62" height="62" rx="2.6" fill="#ffffff"/>
  <path transform="translate({qr_x:.3f} {qr_y:.3f})" d="{qr_svg_path(matrix, QR_MM)}" fill="{GREEN_HEX}"/>
  {et_frag}
  {en_frag}
  <g opacity="0.8">{sub_frag}</g>
  {ph_frag}
  <rect x="{60 - pill_w / 2:.3f}" y="111.6" width="{pill_w:.3f}" height="5.8" rx="2.9" fill="{CREAM_HEX}"/>
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
print(pdf_path, "· vektor, 120x120 mm")
print(qr_svg_file)
