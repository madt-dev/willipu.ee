"""
Willipu Karavanipark — Facebook reklaam (kaasaegne, puhas disain)
Mõõdud: 1080 × 1350 px (FB feed portrait)
"""
from PIL import Image, ImageDraw, ImageFilter, ImageFont
import math, os

W, H = 1080, 1350

DARK   = (16, 32, 27)
GREEN  = (45, 74, 62)
GOLD   = (222, 168, 62)
YELLOW = (244, 205, 95)
CREAM  = (247, 244, 238)
WHITE  = (255, 255, 255)

SRC = os.path.join(os.path.dirname(__file__), 'public', 'kar4.jpg')
BOLD   = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
NORMAL = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"

def F(size, bold=True):
    return ImageFont.truetype(BOLD if bold else NORMAL, size)


def rounded_panel(base, box, radius, fill, blur_bg=False):
    """Poolläbipaistev ümar paneel, soovi korral blur-iga tausta peal."""
    x0, y0, x1, y1 = box
    if blur_bg:
        region = base.crop(box).filter(ImageFilter.GaussianBlur(12))
        mask = Image.new('L', (x1-x0, y1-y0), 0)
        ImageDraw.Draw(mask).rounded_rectangle([0, 0, x1-x0, y1-y0], radius=radius, fill=255)
        base.paste(region, (x0, y0), mask)
    layer = Image.new('RGBA', base.size, (0,0,0,0))
    ImageDraw.Draw(layer).rounded_rectangle(box, radius=radius, fill=fill)
    return Image.alpha_composite(base, layer)


def make_ad(filename):
    # ── 1. Taustpilt ───────────────────────────────────────────────────────
    bg = Image.open(SRC).convert('RGB')
    ratio = W / H
    src = bg.width / bg.height
    if src > ratio:
        nw = int(bg.height * ratio)
        bg = bg.crop(((bg.width-nw)//2, 0, (bg.width+nw)//2, bg.height))
    else:
        nh = int(bg.width / ratio)
        bg = bg.crop((0, (bg.height-nh)//2, bg.width, (bg.height-nh)//2+nh))
    bg = bg.resize((W, H), Image.LANCZOS)
    base = bg.convert('RGBA')

    # Gradient: üleval kerge, all tugev — loetavuse jaoks
    grad = Image.new('RGBA', (W, H), (0,0,0,0))
    gd = ImageDraw.Draw(grad)
    for y in range(H):
        t = y / H
        if t < 0.28:
            a = int((0.28 - t) / 0.28 * 160)
        elif t > 0.42:
            a = int((t - 0.42) / 0.58 * 235)
        else:
            a = 0
        gd.line([(0, y), (W, y)], fill=(*DARK, a))
    base = Image.alpha_composite(base, grad)

    M = 56  # üldine veeris

    # ── 2. Ülaosa: eyebrow + pealkiri ──────────────────────────────────────
    d = ImageDraw.Draw(base)

    f_eye = F(26)
    eye = "PEIPSI JÄRVE ÄÄRES  ·  PUSI KÜLA, TARTUMAA"
    ew = d.textbbox((0,0), eye, font=f_eye)[2]
    # kuldne aktsendijoon + eyebrow
    d.text(((W-ew)//2, 72), eye, font=f_eye, fill=YELLOW)

    f_title1 = F(108)
    t1 = "Willipu"
    t1w = d.textbbox((0,0), t1, font=f_title1)[2]
    d.text(((W-t1w)//2, 118), t1, font=f_title1, fill=WHITE)

    f_title2 = F(64)
    t2 = "KARAVANIPARK"
    t2w = d.textbbox((0,0), t2, font=f_title2)[2]
    # harvendatud tähevahe efekt — joonista täht haaval
    spacing = 14
    total = t2w + spacing * (len(t2)-1)
    tx = (W - total)//2
    for ch in t2:
        d.text((tx, 252), ch, font=f_title2, fill=WHITE)
        tx += d.textbbox((0,0), ch, font=f_title2)[2] + spacing

    # kuldne joon pealkirja all
    d.rounded_rectangle([(W-220)//2, 348, (W+220)//2, 354], radius=3, fill=GOLD)

    # ── 3. Hinnamärgis — puhas kuldne ring paremal ─────────────────────────
    pr_cx, pr_cy, pr_r = W - 200, 520, 128
    # kerge vari
    shadow = Image.new('RGBA', (W, H), (0,0,0,0))
    ImageDraw.Draw(shadow).ellipse(
        [pr_cx-pr_r+6, pr_cy-pr_r+10, pr_cx+pr_r+6, pr_cy+pr_r+10], fill=(0,0,0,90))
    shadow = shadow.filter(ImageFilter.GaussianBlur(10))
    base = Image.alpha_composite(base, shadow)
    d = ImageDraw.Draw(base)
    d.ellipse([pr_cx-pr_r, pr_cy-pr_r, pr_cx+pr_r, pr_cy+pr_r], fill=GOLD)

    f_pr_small = F(30)
    f_pr_big   = F(74)
    s1 = "alates"
    s1w = d.textbbox((0,0), s1, font=f_pr_small)[2]
    d.text((pr_cx-s1w//2, pr_cy-86), s1, font=f_pr_small, fill=DARK)
    s2 = "20€"
    s2w = d.textbbox((0,0), s2, font=f_pr_big)[2]
    d.text((pr_cx-s2w//2, pr_cy-46), s2, font=f_pr_big, fill=DARK)
    s3 = "öö / karavan"
    s3w = d.textbbox((0,0), s3, font=f_pr_small)[2]
    d.text((pr_cx-s3w//2, pr_cy+48), s3, font=f_pr_small, fill=DARK)

    # ── 4. Märksõna-pillid vasakul ─────────────────────────────────────────
    pills = ["41 kohta", "Elekter", "Vesi & purgimine", "Telkimine lubatud"]
    f_pill = F(28)
    py = 430
    px = M
    for ptxt in pills:
        pw = d.textbbox((0,0), ptxt, font=f_pill)[2]
        pill_w, pill_h = pw + 48, 58
        if px + pill_w > W - 360:  # ära mine hinnaringi alla
            px = M
            py += pill_h + 16
        layer = Image.new('RGBA', base.size, (0,0,0,0))
        ld = ImageDraw.Draw(layer)
        ld.rounded_rectangle([px, py, px+pill_w, py+pill_h], radius=pill_h//2,
                             fill=(*GREEN, 215), outline=(*YELLOW, 120), width=2)
        base = Image.alpha_composite(base, layer)
        d = ImageDraw.Draw(base)
        d.text((px+24, py+12), ptxt, font=f_pill, fill=WHITE)
        px += pill_w + 16

    # ── 5. Info-kaart (üks puhas paneel) ───────────────────────────────────
    card_y0 = 760
    card_y1 = 1115
    base = rounded_panel(base, (M, card_y0, W-M, card_y1), 28, (*DARK, 200), blur_bg=True)
    d = ImageDraw.Draw(base)

    f_h  = F(33)
    f_b  = F(26, bold=False)

    rows = [
        ("✓", "Hind sisaldab", "elekter, puhas vesi, purgimine, duššid, WC"),
        ("✓", "Mugavused", "köök, pesumasin, tasuta kiire WiFi"),
        ("✓", "Check-in 24/7", "iseteeninduslik sisseregistreerimine"),
        ("✓", "Vaba aeg", "liivane rand, saun, lõkkeplats, surf"),
    ]
    ry = card_y0 + 36
    for mark, head, body in rows:
        # kuldne linnuke ringis
        cr = 21
        ccx, ccy = M + 52, ry + 26
        d.ellipse([ccx-cr, ccy-cr, ccx+cr, ccy+cr], fill=GOLD)
        mw = d.textbbox((0,0), mark, font=F(26))[2]
        d.text((ccx-mw//2, ccy-17), mark, font=F(26), fill=DARK)
        d.text((M + 96, ry), head, font=f_h, fill=YELLOW)
        d.text((M + 96, ry + 42), body, font=f_b, fill=CREAM)
        ry += 80

    # ── 6. CTA-riba all ────────────────────────────────────────────────────
    cta_y0 = 1155
    cta_h  = 96
    layer = Image.new('RGBA', base.size, (0,0,0,0))
    ld = ImageDraw.Draw(layer)
    ld.rounded_rectangle([M, cta_y0, W-M, cta_y0+cta_h], radius=cta_h//2, fill=GOLD)
    base = Image.alpha_composite(base, layer)
    d = ImageDraw.Draw(base)

    f_cta  = F(40)
    f_ph   = ImageFont.truetype(NORMAL, 40)
    cta = "Broneeri:  +372 56 955 758"
    cw = d.textbbox((0,0), cta, font=f_cta)[2]
    icon_w = d.textbbox((0,0), "☎ ", font=f_ph)[2]
    start = (W - cw - icon_w) // 2
    d.text((start, cta_y0 + 24), "☎ ", font=f_ph, fill=DARK)
    d.text((start + icon_w, cta_y0 + 22), cta, font=f_cta, fill=DARK)

    # ── 7. Veebileht kõige all ─────────────────────────────────────────────
    f_web = F(36)
    web = "www.willipu.ee"
    ww = d.textbbox((0,0), web, font=f_web)[2]
    d.text(((W-ww)//2, cta_y0 + cta_h + 26), web, font=f_web, fill=WHITE)

    result = base.convert('RGB')
    result.save(filename, 'JPEG', quality=95, optimize=True)
    print(f"✓ {filename}  ({W}×{H} px)")


make_ad("/home/user/willipu.ee/willipu_fb_ad_karavan.jpg")
