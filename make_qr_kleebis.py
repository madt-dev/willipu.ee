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
