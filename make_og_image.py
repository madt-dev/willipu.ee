#!/usr/bin/env python3
"""Generate the 1200x630 Open Graph image (public/og-image.jpg) for willipu.ee.

Fonts (Fraunces, Inter — the site's brand fonts) are downloaded from
Google Fonts into ./fonts/ on first run.
"""
import os
import re
import urllib.request

from PIL import Image, ImageDraw, ImageFont

REPO = os.path.dirname(os.path.abspath(__file__))
FONTS = os.path.join(REPO, "fonts")

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
        for wt, url in zip(weights, urls):
            urllib.request.urlretrieve(url, os.path.join(FONTS, f"{family}-{wt}.ttf"))


fetch_fonts()

W, H = 1200, 630
SS = 2  # supersample factor
w, h = W * SS, H * SS

GREEN = (45, 74, 62)        # site theme #2d4a3e
DARK = (18, 32, 26)
WHITE = (255, 255, 255)
CREAM = (245, 242, 234)

def F(path, size):
    return ImageFont.truetype(os.path.join(FONTS, path), size * SS)

fraunces_big = F("fraunces-700.ttf", 104)
fraunces_sub = F("fraunces-600.ttf", 44)
inter_en = F("inter-500.ttf", 27)
inter_pill = F("inter-600.ttf", 26)
inter_credit = F("inter-500.ttf", 16)

# --- background photo: kar1.jpg scaled to width, cropped vertically ---
photo = Image.open(f"{REPO}/public/kar1.jpg").convert("RGB")
scale = w / photo.width
photo = photo.resize((w, round(photo.height * scale)), Image.LANCZOS)
top = round(100 * SS)  # keep sunset sky, caravans in upper-middle third
img = photo.crop((0, top, w, top + h))

# --- bottom gradient for text legibility ---
grad = Image.new("L", (1, h), 0)
for y in range(h):
    t = (y / h - 0.45) / 0.55  # starts at 45% height
    if t > 0:
        grad.putpixel((0, y), min(255, int(235 * t ** 1.3)))
overlay = Image.new("RGB", (w, h), DARK)
img = Image.composite(overlay, img, grad.resize((w, h)))

# subtle top-right shade so the tiny credit stays readable
d = ImageDraw.Draw(img, "RGBA")

# --- logo badge: crop circle icon from willipu_logo_white.png ---
logo = Image.open(f"{REPO}/willipu_logo_white.png").convert("RGBA")
alpha_bbox = logo.crop((0, 0, 300, logo.height)).getbbox()
icon = logo.crop(alpha_bbox)
icon_size = 96 * SS
icon = icon.resize((icon_size, icon_size), Image.LANCZOS)

PAD = 64 * SS
title_y = 388 * SS
img.paste(icon, (PAD, title_y), icon)

# --- title next to badge ---
tx = PAD + icon_size + 28 * SS
d.text((tx, title_y - 26 * SS), "Willipu", font=fraunces_big, fill=WHITE)

# --- subtitle lines ---
sub_y = title_y + 116 * SS
d.text((PAD, sub_y), "Külalistemaja ja Karavanipark", font=fraunces_sub, fill=CREAM)
d.text((PAD, sub_y + 62 * SS), "Caravan Park & Guesthouse · Lake Peipus, Estonia",
       font=inter_en, fill=(255, 255, 255, 225))

# --- pills, top right over the sky ---
py1, py2 = 64 * SS, 130 * SS

pill_txt = "willipu.ee"
tb = d.textbbox((0, 0), pill_txt, font=inter_pill)
pw, ph = tb[2] - tb[0], tb[3] - tb[1]
px2 = w - PAD
px1 = px2 - pw - 56 * SS
d.rounded_rectangle((px1, py1, px2, py2), radius=(py2 - py1) // 2, fill=GREEN)
d.text(((px1 + px2 - pw) // 2 - tb[0], (py1 + py2 - ph) // 2 - tb[1]),
       pill_txt, font=inter_pill, fill=WHITE)

p2_txt = "Check-in 24/7"
tb2 = d.textbbox((0, 0), p2_txt, font=inter_pill)
p2w, p2h = tb2[2] - tb2[0], tb2[3] - tb2[1]
q2 = px1 - 20 * SS
q1 = q2 - p2w - 56 * SS
d.rounded_rectangle((q1, py1, q2, py2), radius=(py2 - py1) // 2,
                    fill=(18, 32, 26, 110), outline=(255, 255, 255, 185), width=2 * SS)
d.text(((q1 + q2 - p2w) // 2 - tb2[0], (py1 + py2 - p2h) // 2 - tb2[1]),
       p2_txt, font=inter_pill, fill=WHITE)

# --- photo credit, top right above pills ---
credit = "photo: Liisi Laanemäe"
cb = d.textbbox((0, 0), credit, font=inter_credit)
d.text((w - PAD - (cb[2] - cb[0]), 28 * SS), credit,
       font=inter_credit, fill=(255, 255, 255, 150))

# --- downscale and save ---
img = img.resize((W, H), Image.LANCZOS)
out = f"{REPO}/public/og-image.jpg"
img.save(out, "JPEG", quality=88, optimize=True, progressive=True)
print(out, os.path.getsize(out) // 1024, "KB")
