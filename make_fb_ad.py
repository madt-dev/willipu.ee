"""
Willipu Facebook reklaampilt (ad)
Mõõdud: 1080 × 1080 px — ruudukujuline, töötab feed / marketplace / reels
"""
from PIL import Image, ImageDraw, ImageFont
import math, os

W, H = 1080, 1080

DARK       = (20, 32, 27)
ACCENT     = (45, 74, 62)
ACCENT2    = (93, 138, 106)
GOLD       = (200, 155, 60)
GOLD_LIGHT = (232, 201, 106)
CREAM      = (247, 244, 238)
WHITE      = (255, 255, 255)

SRC = os.path.join(os.path.dirname(__file__), 'public', 'kar4.jpg')

def load_font(path, size):
    try:
        return ImageFont.truetype(path, size)
    except:
        return ImageFont.load_default()

BOLD   = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
NORMAL = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"

def make_ad(filename):
    # ── 1. Taustpilt ───────────────────────────────────────────────────────
    bg = Image.open(SRC).convert('RGB')
    # Crop ruudule
    size = min(bg.width, bg.height)
    left = (bg.width  - size) // 2
    top  = (bg.height - size) // 2
    bg   = bg.crop((left, top, left + size, top + size))
    bg   = bg.resize((W, H), Image.LANCZOS)

    # ── 2. Gradient overlay: alt tumedam, ülalt heledam ───────────────────
    base = bg.convert('RGBA')
    grad = Image.new('RGBA', (W, H), (0, 0, 0, 0))
    gd   = ImageDraw.Draw(grad)
    for y in range(H):
        t = y / H   # 0=üles, 1=alla
        alpha = int((0.15 + 0.65 * t) * 255)
        gd.line([(0, y), (W, y)], fill=(*DARK, alpha))
    base = Image.alpha_composite(base, grad)

    draw = ImageDraw.Draw(base)

    # ── 3. Kuldne riba ülaosas ─────────────────────────────────────────────
    bar_h = 10
    draw.rectangle([0, 0, W, bar_h], fill=(*GOLD, 230))

    # ── 4. Ülemine osa: eyebrow ────────────────────────────────────────────
    f_eye = load_font(BOLD, 30)
    eye_text = "PUHKEMAJUTUS  ·  KARAVAN PARK"
    ew = draw.textbbox((0,0), eye_text, font=f_eye)[2]
    draw.text(((W - ew)//2, 38), eye_text, font=f_eye, fill=(*WHITE, 220))

    # ── 5. Pealkiri "Willipu" keskel ──────────────────────────────────────
    f_main = load_font(BOLD, 148)
    draw.text((W//2, H//2 - 60), "Willipu",
              font=f_main, fill=(*WHITE, 255), anchor="mm")

    # ── 6. Kuldne eraldajajoon ────────────────────────────────────────────
    line_w = 480
    ly = H//2 + 55
    draw.line([(W//2 - line_w//2, ly), (W//2 + line_w//2, ly)],
              fill=(*GOLD, 200), width=2)

    # ── 7. Alapealkiri ────────────────────────────────────────────────────
    f_sub = load_font(BOLD, 52)
    draw.text((W//2, ly + 42), "Guesthouse and Caravan",
              font=f_sub, fill=(*CREAM, 245), anchor="mm")

    # ── 8. CTA nupp — "Broneeri koht" ─────────────────────────────────────
    f_cta = load_font(BOLD, 34)
    cta_text = "Broneeri koht"
    cw = draw.textbbox((0,0), cta_text, font=f_cta)[2]
    ch = draw.textbbox((0,0), cta_text, font=f_cta)[3]
    pad_x, pad_y = 44, 18
    btn_w = cw + pad_x * 2
    btn_h = ch + pad_y * 2
    btn_x = (W - btn_w) // 2
    btn_y = H - 210

    # Nupu taust
    draw.rounded_rectangle([btn_x, btn_y, btn_x+btn_w, btn_y+btn_h],
                            radius=btn_h//2, fill=(*GOLD, 240))
    draw.text((W//2, btn_y + btn_h//2), cta_text,
              font=f_cta, fill=(*DARK, 255), anchor="mm")

    # ── 9. Kontaktinfo all ────────────────────────────────────────────────
    f_con = load_font(BOLD, 28)
    f_ico = load_font(NORMAL, 28)

    phone = "+372 56 955 758"
    web   = "www.willipu.ee"

    # Paiguta kaks elementi kõrvuti keskjoondusega
    phone_w2 = draw.textbbox((0,0), phone, font=f_con)[2]
    web_w2   = draw.textbbox((0,0), web,   font=f_con)[2]
    ico_w    = draw.textbbox((0,0), "☎",   font=f_ico)[2]
    glob_w   = 28
    gap      = 18
    spacing  = 60  # elementide vaheline tühimik

    total_w = (ico_w + gap + phone_w2) + spacing + (glob_w + gap + web_w2)
    start_x = (W - total_w) // 2
    con_y   = btn_y + btn_h + 30

    # Telefon
    draw.text((start_x, con_y), "☎", font=f_ico, fill=(*GOLD_LIGHT, 220))
    draw.text((start_x + ico_w + gap, con_y), phone,
              font=f_con, fill=(*WHITE, 230))

    # Veebileht
    wx = start_x + ico_w + gap + phone_w2 + spacing
    # Väike globuse ikoon joonistame
    gr = 12
    gcx = wx + gr
    gcy = con_y + gr + 2
    draw.ellipse([gcx-gr, gcy-gr, gcx+gr, gcy+gr],
                 outline=(*GOLD_LIGHT, 200), width=2)
    draw.line([(gcx-gr, gcy), (gcx+gr, gcy)], fill=(*GOLD_LIGHT, 200), width=2)
    draw.ellipse([gcx-gr//2, gcy-gr, gcx+gr//2, gcy+gr],
                 outline=(*GOLD_LIGHT, 180), width=2)
    draw.text((wx + glob_w + gap, con_y), web,
              font=f_con, fill=(*WHITE, 230))

    # ── 10. Kuldne riba all ───────────────────────────────────────────────
    draw.rectangle([0, H - bar_h, W, H], fill=(*GOLD, 230))

    # ── 11. Nurga kaunistused ─────────────────────────────────────────────
    pad, arm, lw = 20, 36, 3
    for (x, y, dx, dy) in [(pad,bar_h+pad,1,1),(pad,H-bar_h-pad,1,-1),
                            (W-pad,bar_h+pad,-1,1),(W-pad,H-bar_h-pad,-1,-1)]:
        draw.line([(x, y), (x+dx*arm, y)], fill=(*GOLD, 160), width=lw)
        draw.line([(x, y), (x, y+dy*arm)], fill=(*GOLD, 160), width=lw)

    result = base.convert('RGB')
    result.save(filename, 'JPEG', quality=96, optimize=True)
    print(f"✓ {filename}  ({W}×{H} px)")


make_ad("/home/user/willipu.ee/willipu_fb_ad_1080.jpg")
