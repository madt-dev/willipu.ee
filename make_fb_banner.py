"""
Willipu Facebook kaanefoto
Mõõdud: 1640 × 624 px (optimaalne Facebook page cover)
"""
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import math, os

W, H = 1640, 624

DARK       = (20, 32, 27)
ACCENT     = (45, 74, 62)
ACCENT2    = (93, 138, 106)
GOLD       = (200, 155, 60)
GOLD_LIGHT = (232, 201, 106)
CREAM      = (247, 244, 238)
WHITE      = (255, 255, 255)

LOGO_GREEN = (45, 74, 62)
LOGO_WATER = (127, 179, 213)
LOGO_SUN   = (244, 211, 94)

SRC = os.path.join(os.path.dirname(__file__), 'public', 'kar4.jpg')


def draw_logo(draw, img, cx, cy, r):
    """Joonistab favicon logo: roheline ring + laine + päike."""
    from PIL import Image as PILImage
    # Tee eraldi RGBA pind
    layer = PILImage.new('RGBA', (W, H), (0, 0, 0, 0))
    ld = ImageDraw.Draw(layer)

    # Ring
    ld.ellipse([cx-r, cy-r, cx+r, cy+r], fill=(*LOGO_GREEN, 230))

    # Laine – joonistame hulknurgaga (approx Bezier)
    s = r / 16.0
    ox = cx - 16*s
    oy = cy - 16*s

    def p(x, y):
        return (ox + x*s, oy + (32 - y)*s)

    # Approx lainekaar punktidena
    wave_pts = []
    steps = 60
    # M6,20 → Q12,16 16,20
    for i in range(steps+1):
        t = i / steps
        # Quadratic bezier: P0=(6,20) P1=(12,16) P2=(16,20)
        x = (1-t)**2*6 + 2*(1-t)*t*12 + t**2*16
        y = (1-t)**2*20 + 2*(1-t)*t*16 + t**2*20
        wave_pts.append(p(x, y))
    # T26,20 (mirrored: P1=(20,24) P2=(26,20))
    for i in range(steps+1):
        t = i / steps
        x = (1-t)**2*16 + 2*(1-t)*t*20 + t**2*26
        y = (1-t)**2*20 + 2*(1-t)*t*24 + t**2*20
        wave_pts.append(p(x, y))
    # suletud kuju alla
    wave_pts.append(p(26, 26))
    wave_pts.append(p(6, 26))

    ld.polygon(wave_pts, fill=(*LOGO_WATER, 230))

    # Päike
    sr = 3 * s
    sc = p(22, 10)
    ld.ellipse([sc[0]-sr, sc[1]-sr, sc[0]+sr, sc[1]+sr], fill=(*LOGO_SUN, 240))

    img.paste(layer, mask=layer.split()[3])


def make_fb_banner(filename):
    # ── 1. Taustpilt ────────────────────────────────────────────────────
    bg = Image.open(SRC).convert('RGB')
    # Crop banneri kuvasuhtele
    target_ratio = W / H
    src_ratio = bg.width / bg.height
    if src_ratio > target_ratio:
        new_w = int(bg.height * target_ratio)
        left = (bg.width - new_w) // 2
        bg = bg.crop((left, 0, left + new_w, bg.height))
    else:
        new_h = int(bg.width / target_ratio)
        top = (bg.height - new_h) // 2
        bg = bg.crop((0, top, bg.width, top + new_h))
    bg = bg.resize((W, H), Image.LANCZOS)

    # ── 2. Tumendav overlay ──────────────────────────────────────────────
    overlay = Image.new('RGBA', (W, H), (*DARK, int(0.38 * 255)))
    base = bg.convert('RGBA')
    base = Image.alpha_composite(base, overlay)

    draw = ImageDraw.Draw(base)

    # ── 3. Kuldne riba ülaosas ja alaosas ────────────────────────────────
    bar_h = 10
    draw.rectangle([0, 0, W, bar_h], fill=(*GOLD, 230))
    draw.rectangle([0, H-bar_h, W, H], fill=(*GOLD, 230))

    # ── 4. Tekstid ───────────────────────────────────────────────────────
    tx = 55
    mid = H // 2

    # Fondid (vaikimisi Pillow sisseehitatud)
    try:
        font_big  = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 155)
        font_sub  = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 58)
        font_sm   = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 22)
        font_eye  = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 18)
    except:
        font_big = font_sub = font_sm = font_eye = ImageFont.load_default()

    # Eyebrow
    draw.text((tx, mid - 195), "PUHKEMAJUTUS  ·  KARAVAN PARK",
              font=font_eye, fill=(*WHITE, 255))

    # "Willipu"
    draw.text((tx - 3, mid - 160), "Willipu",
              font=font_big, fill=(*WHITE, 255))

    # Kuldne eraldajajoon
    sep_y = mid + 10
    draw.line([(tx, sep_y), (tx + 700, sep_y)], fill=(*GOLD, 200), width=2)

    # "Guesthouse and Caravan"
    draw.text((tx, mid + 22), "Guesthouse and Caravan",
              font=font_sub, fill=(*CREAM, 245))

    # "willipu.ee"
    draw.text((tx, mid + 100), "willipu.ee",
              font=font_sm, fill=(*WHITE, 255))

    # ── 5. Nurga kaunistused ─────────────────────────────────────────────
    pad, arm, lw = 22, 45, 3
    for (x, y, dx, dy) in [(pad,pad,1,1),(pad,H-pad,1,-1),(W-pad,pad,-1,1),(W-pad,H-pad,-1,-1)]:
        draw.line([(x,y),(x+dx*arm,y)], fill=(*GOLD, 160), width=lw)
        draw.line([(x,y),(x,y+dy*arm)], fill=(*GOLD, 160), width=lw)

    # ── 7. Salvesta ──────────────────────────────────────────────────────
    result = base.convert('RGB')
    result.save(filename, 'JPEG', quality=95, optimize=True)
    print(f"✓ Facebook banner salvestatud: {filename}")
    print(f"  Mõõdud: {W} × {H} px (Facebook kaanefoto optimaalne)")


make_fb_banner("/home/user/willipu.ee/willipu_facebook_cover.jpg")
