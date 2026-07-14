#!/usr/bin/env python3
"""Generate the dump station (purgimisplats) info board for print.

A3 portrait (297x420 mm), all text converted to vector outlines.
Outputs: willipu_tahvel_purgimine.svg / .pdf / .png (preview).
"""
import os
import re
import urllib.request

import cairosvg
from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen

REPO = os.path.dirname(os.path.abspath(__file__))
FONTS = os.path.join(REPO, "fonts")

GREEN = "#2d4a3e"
LIGHT = "#e9efe9"
CREAM = "#f5f2ea"
DARK = "#22322b"
RED = "#c8102e"
BLUE = "#0072ce"

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


fetch_fonts()
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


def placed(font_file, text, em_mm, baseline_y, fill, center_x=None, left_x=None):
    w, frag = text_outline(font_file, text, em_mm)
    tx = (center_x - w / 2) if center_x is not None else left_x
    return f'<g transform="translate({tx:.3f} {baseline_y:.3f})" fill="{fill}">{frag}</g>'


W, H = 297, 420

# --- Willipu wordmark (vector paths from willipu_logo.svg) ---
WORDMARK_PATHS = (
    '<path transform="translate(0.00 0) scale(0.048828 -0.048828)" d="M1745 0H1487L1149 1087L811 0H553L127 1372H-18V1493H690V1372H530L815 455L1137 1493H1421L1749 438L2040 1372H1862V1493H2324V1372H2171Z"/>'
    '<path transform="translate(112.30 0) scale(0.048828 -0.048828)" d="M188 1364Q188 1445 244.0 1500.5Q300 1556 381 1556Q460 1556 515.5 1500.5Q571 1445 571 1364Q571 1285 515.5 1229.5Q460 1174 381 1174Q300 1174 244.0 1229.0Q188 1284 188 1364ZM575 121H727V0H70V121H221V942H70V1063H575Z"/>'
    '<path transform="translate(150.29 0) scale(0.048828 -0.048828)" d="M575 121H727V0H70V121H221V1436H70V1556H575Z"/>'
    '<path transform="translate(188.28 0) scale(0.048828 -0.048828)" d="M575 121H727V0H70V121H221V1436H70V1556H575Z"/>'
    '<path transform="translate(226.27 0) scale(0.048828 -0.048828)" d="M188 1364Q188 1445 244.0 1500.5Q300 1556 381 1556Q460 1556 515.5 1500.5Q571 1445 571 1364Q571 1285 515.5 1229.5Q460 1174 381 1174Q300 1174 244.0 1229.0Q188 1284 188 1364ZM575 121H727V0H70V121H221V942H70V1063H575Z"/>'
    '<path transform="translate(264.26 0) scale(0.048828 -0.048828)" d="M553 584V479Q553 293 600.5 210.0Q648 127 754 127Q863 127 907.5 215.0Q952 303 952 532Q952 761 907.5 848.5Q863 936 754 936Q648 936 600.5 853.0Q553 770 553 584ZM199 942H47V1063H553V928Q598 1011 674.0 1051.5Q750 1092 862 1092Q1089 1092 1219.5 942.5Q1350 793 1350 532Q1350 271 1219.5 121.0Q1089 -29 862 -29Q750 -29 674.0 11.5Q598 52 553 135V-305H717V-426H47V-305H199Z"/>'
    '<path transform="translate(334.18 0) scale(0.048828 -0.048828)" d="M1268 1063V121H1419V0H913V150Q850 55 768.0 13.0Q686 -29 561 -29Q382 -29 290.5 76.5Q199 182 199 387V942H47V1063H553V442Q553 244 586.0 190.5Q619 137 707 137Q814 137 863.5 216.0Q913 295 913 467V942H784V1063Z"/>'
)

# header: icon 20mm + wordmark (glyph height ~73px in logo units)
ICON_S = 20 / 130
WM_S = 14.5 / 72.9
header = f'''
  <g transform="translate(24 16) scale({ICON_S:.5f})">
    <circle cx="65" cy="65" r="55" fill="#ffffff" fill-opacity="0.14"/>
    <g transform="translate(27.60 27.60) scale(3.1167)" fill="none" stroke="#ffffff" stroke-width="1.8" stroke-linecap="round">
      <path d="M3 14c3 0 3-3 6-3s3 3 6 3 3-3 6-3 3 3 6 3"/>
      <path d="M3 19c3 0 3-3 6-3s3 3 6 3 3-3 6-3 3 3 6 3"/>
    </g>
  </g>
  <g transform="translate(50 31) scale({WM_S:.5f})" fill="#ffffff">{WORDMARK_PATHS}</g>
'''

# --- panel 1: dump station ---
P1_Y, P1_H = 52, 158
ICON_CX, ICON_CY, ICON_R = 78, P1_Y + P1_H / 2, 44
# dump pictogram: WC pot emptying into a container below (24-unit viewBox → ~60mm)
DUMP_S = 60 / 24
dump_icon = f'''
  <circle cx="{ICON_CX}" cy="{ICON_CY}" r="{ICON_R}" fill="{LIGHT}"/>
  <g transform="translate({ICON_CX - 30} {ICON_CY - 30}) scale({DUMP_S:.4f})"
     fill="none" stroke="{GREEN}" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">
    <path d="M9.5 2.5h5a1 1 0 011 1V5c0 1.9-1 3.4-2.3 4.2h-2.4C9.5 8.4 8.5 6.9 8.5 5V3.5a1 1 0 011-1z"/>
    <path d="M10.8 9.2v1.6h2.4V9.2"/>
    <path d="M12 12.8v1.7M9.6 12.3v1.4M14.4 12.3v1.4"/>
    <path d="M5 17h14"/>
    <path d="M7 17v2a2 2 0 002 2h6a2 2 0 002-2v-2"/>
  </g>
'''
TXT1_X = 138
p1_texts = (
    placed("fraunces-700.ttf", "Purgimiskoht", 13.5, P1_Y + 48, DARK, left_x=TXT1_X)
    + placed("inter-500.ttf", "Entsorgungsstation", 6.8, P1_Y + 72, "#5a6b62", left_x=TXT1_X)
    + placed("inter-500.ttf", "Tyhjennyspiste", 6.8, P1_Y + 85, "#5a6b62", left_x=TXT1_X)
    + placed("inter-500.ttf", "Слив отходов", 6.8, P1_Y + 98, "#5a6b62", left_x=TXT1_X)
    + placed("inter-500.ttf", "Hallvesi · keemiline WC", 6.8, P1_Y + 124, GREEN, left_x=TXT1_X)
)

# --- panel 2: no parking ---
P2_Y, P2_H = 226, 158
S_CX, S_CY, S_R = 78, P2_Y + P2_H / 2, 44
pw, p_frag = text_outline("inter-600.ttf", "P", 52)
sign = f'''
  <circle cx="{S_CX}" cy="{S_CY}" r="{S_R}" fill="{RED}"/>
  <circle cx="{S_CX}" cy="{S_CY}" r="{S_R - 7}" fill="{BLUE}"/>
  <g transform="translate({S_CX - pw / 2:.3f} {S_CY + 18:.3f})" fill="#ffffff">{p_frag}</g>
  <line x1="{S_CX - (S_R - 4) * 0.7071:.3f}" y1="{S_CY - (S_R - 4) * 0.7071:.3f}"
        x2="{S_CX + (S_R - 4) * 0.7071:.3f}" y2="{S_CY + (S_R - 4) * 0.7071:.3f}"
        stroke="{RED}" stroke-width="9" stroke-linecap="round"/>
'''
TXT2_X = 138
p2_texts = (
    placed("fraunces-700.ttf", "Parkimine keelatud", 11.5, P2_Y + 42, RED, left_x=TXT2_X)
    + placed("inter-600.ttf", "purgimisplatsi alal", 7.2, P2_Y + 57, DARK, left_x=TXT2_X)
    + placed("inter-500.ttf", "Parken im Entsorgungsbereich verboten", 6.4, P2_Y + 82, "#5a6b62", left_x=TXT2_X)
    + placed("inter-500.ttf", "Pysäköinti kielletty tyhjennysalueella", 6.4, P2_Y + 96, "#5a6b62", left_x=TXT2_X)
    + placed("inter-500.ttf", "Парковка в зоне слива запрещена", 6.4, P2_Y + 110, "#5a6b62", left_x=TXT2_X)
    + placed("inter-500.ttf", "Palun hoia plats purgijatele vaba", 6.4, P2_Y + 136, GREEN, left_x=TXT2_X)
)

footer = placed("inter-600.ttf", "willipu.ee  ·  +372 56 955 758", 7, 405, CREAM, center_x=W / 2)

svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}mm" height="{H}mm" viewBox="0 0 {W} {H}">
  <rect width="{W}" height="{H}" fill="{GREEN}"/>
  {header}
  <rect x="20" y="{P1_Y}" width="257" height="{P1_H}" rx="6" fill="#ffffff"/>
  {dump_icon}
  {p1_texts}
  <rect x="20" y="{P2_Y}" width="257" height="{P2_H}" rx="6" fill="#ffffff"/>
  {sign}
  {p2_texts}
  {footer}
</svg>'''

base = os.path.join(REPO, "willipu_tahvel_purgimine")
open(base + ".svg", "w").write(svg)
cairosvg.svg2pdf(bytestring=svg.encode(), write_to=base + ".pdf")
cairosvg.svg2png(bytestring=svg.encode(), write_to=base + ".png", output_width=1403)
for ext in (".svg", ".pdf", ".png"):
    print(base + ext, os.path.getsize(base + ext) // 1024, "KB")
