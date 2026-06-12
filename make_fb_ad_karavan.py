"""
Willipu Karavanipark — Facebook reklaam (kaasaegne, infoküllane)
Stiil: pintslitõmbe-plokid, hinnaring, info-blokid
Mõõdud: 1080 × 1350 px (FB feed portrait — rohkem ruumi infole)
"""
from PIL import Image, ImageDraw, ImageFont
import random, os, math

W, H = 1080, 1350

DARK_NAVY  = (16, 38, 33)      # tume sini-roheline plokk
GREEN      = (45, 74, 62)      # --accent
GREEN_SOFT = (58, 96, 78)
GOLD       = (222, 168, 62)    # erksam kuld (nagu näites oranž ring)
GOLD_DEEP  = (200, 155, 60)
CREAM      = (247, 244, 238)
WHITE      = (255, 255, 255)
YELLOW     = (244, 200, 80)

SRC = os.path.join(os.path.dirname(__file__), 'public', 'kar4.jpg')

BOLD   = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
NORMAL = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"

def F(size, bold=True):
    return ImageFont.truetype(BOLD if bold else NORMAL, size)


def brush_block(draw, x0, y0, x1, y1, fill, seed=1, rough=14, layer=None):
    """Pintslitõmbe-stiilis plokk — sakilised servad."""
    rng = random.Random(seed)
    pts = []
    steps_h = max(4, (x1-x0)//60)
    steps_v = max(3, (y1-y0)//60)
    # ülemine serv
    for i in range(steps_h+1):
        t = i/steps_h
        pts.append((x0 + t*(x1-x0), y0 + rng.randint(-rough, rough)))
    # parem serv
    for i in range(1, steps_v+1):
        t = i/steps_v
        pts.append((x1 + rng.randint(-rough, rough), y0 + t*(y1-y0)))
    # alumine serv
    for i in range(steps_h+1):
        t = 1 - i/steps_h
        pts.append((x0 + t*(x1-x0), y1 + rng.randint(-rough, rough)))
    # vasak serv
    for i in range(1, steps_v):
        t = 1 - i/steps_v
        pts.append((x0 + rng.randint(-rough, rough), y0 + t*(y1-y0)))
    draw.polygon(pts, fill=fill)


def draw_pin(draw, cx, cy, r, color):
    """Asukoha-nõel."""
    draw.ellipse([cx-r, cy-r*1.45, cx+r, cy+r*0.55-r*0.45], fill=color)
    draw.polygon([(cx-r*0.62, cy-r*0.25), (cx+r*0.62, cy-r*0.25), (cx, cy+r*1.0)], fill=color)
    hole = r*0.42
    draw.ellipse([cx-hole, cy-r*1.45+r*0.45-hole+ r*0.45, cx+hole, cy-r*1.45+r*0.45+hole+ r*0.45], fill=DARK_NAVY)


def draw_plug(draw, cx, cy, s, color):
    """Elektripistik."""
    lw = max(3, s//8)
    # pistiku keha
    draw.rounded_rectangle([cx-s*0.45, cy-s*0.15, cx+s*0.45, cy+s*0.75], radius=s//4, outline=color, width=lw)
    # harud
    draw.line([(cx-s*0.22, cy-s*0.15), (cx-s*0.22, cy-s*0.65)], fill=color, width=lw)
    draw.line([(cx+s*0.22, cy-s*0.15), (cx+s*0.22, cy-s*0.65)], fill=color, width=lw)
    # juhe
    draw.line([(cx, cy+s*0.75), (cx, cy+s*1.1)], fill=color, width=lw)


def draw_calendar(draw, cx, cy, s, color):
    lw = max(3, s//8)
    draw.rounded_rectangle([cx-s*0.7, cy-s*0.55, cx+s*0.7, cy+s*0.65], radius=s//6, outline=color, width=lw)
    draw.line([(cx-s*0.7, cy-s*0.2), (cx+s*0.7, cy-s*0.2)], fill=color, width=lw)
    draw.line([(cx-s*0.35, cy-s*0.55), (cx-s*0.35, cy-s*0.8)], fill=color, width=lw)
    draw.line([(cx+s*0.35, cy-s*0.55), (cx+s*0.35, cy-s*0.8)], fill=color, width=lw)
    # täpid
    for i, dx in enumerate((-0.4, 0, 0.4)):
        for dy in (0.05, 0.35):
            draw.ellipse([cx+dx*s-3, cy+dy*s-3, cx+dx*s+3, cy+dy*s+3], fill=color)


def draw_shower(draw, cx, cy, s, color):
    lw = max(3, s//8)
    # dušipea
    draw.arc([cx-s*0.5, cy-s*0.7, cx+s*0.5, cy+s*0.3], 180, 360, fill=color, width=lw)
    draw.line([(cx-s*0.5, cy-s*0.2), (cx+s*0.5, cy-s*0.2)], fill=color, width=lw)
    # toru
    draw.line([(cx, cy-s*0.7+lw), (cx, cy-s*1.0)], fill=color, width=lw)
    draw.line([(cx, cy-s*1.0), (cx-s*0.5, cy-s*1.0)], fill=color, width=lw)
    # piisad
    for dx in (-0.3, 0, 0.3):
        draw.line([(cx+dx*s, cy+0.0*s), (cx+dx*s-s*0.1, cy+s*0.35)], fill=color, width=lw)


def draw_wifi(draw, cx, cy, s, color):
    lw = max(3, s//8)
    for r_mult in (1.0, 0.65, 0.32):
        r = s * r_mult
        draw.arc([cx-r, cy-r, cx+r, cy+r], 225, 315, fill=color, width=lw)
    draw.ellipse([cx-4, cy-4, cx+4, cy+4], fill=color)


def make_ad(filename):
    rng = random.Random(7)

    # ── 1. Taustpilt ────────────────────────────────────────────────────────
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

    # Kerge gradient all et alumine info loetav oleks
    grad = Image.new('RGBA', (W, H), (0,0,0,0))
    gd = ImageDraw.Draw(grad)
    for y in range(H):
        t = y / H
        a = int(max(0, (t-0.45)) / 0.55 * 200)
        gd.line([(0,y),(W,y)], fill=(*DARK_NAVY, a))
    base = Image.alpha_composite(base, grad)

    overlay = Image.new('RGBA', (W, H), (0,0,0,0))
    draw = ImageDraw.Draw(overlay)

    # ── 2. Pealkiri — tume pintslitõmbe-plokk üleval ────────────────────────
    brush_block(draw, 30, 55, W-30, 185, (*DARK_NAVY, 245), seed=3, rough=16)

    f_title = F(88)
    t = "WILLIPU KARAVANIPARK"
    # mahuta kahele kui ei mahu — mõõda
    tw = draw.textbbox((0,0), t, font=f_title)[2]
    if tw > W - 120:
        f_title = F(72)
        tw = draw.textbbox((0,0), t, font=f_title)[2]
    draw.text(((W-tw)//2, 120 - 40), t, font=f_title, fill=WHITE)

    # ── 3. Asukoht pealkirja all ────────────────────────────────────────────
    f_loc = F(40)
    draw_pin(draw, 80, 255, 22, GOLD)
    draw.text((120, 225), "Peipsi järve ääres,", font=f_loc, fill=WHITE,
              stroke_width=2, stroke_fill=(*DARK_NAVY, 200))
    draw.text((120, 275), "Pusi küla, Tartumaa", font=f_loc, fill=WHITE,
              stroke_width=2, stroke_fill=(*DARK_NAVY, 200))

    # ── 4. Hinnaring paremal ────────────────────────────────────────────────
    pr_cx, pr_cy, pr_r = W-185, 330, 140
    draw.ellipse([pr_cx-pr_r, pr_cy-pr_r, pr_cx+pr_r, pr_cy+pr_r], fill=(*GOLD, 250))
    f_price = F(72)
    f_per   = F(34)
    pt = "al. 20€"
    ptw = draw.textbbox((0,0), pt, font=f_price)[2]
    draw.text((pr_cx-ptw//2, pr_cy-82), pt, font=f_price, fill=DARK_NAVY)
    # punktiirjoon
    for x in range(pr_cx-80, pr_cx+80, 14):
        draw.line([(x, pr_cy+10), (x+7, pr_cy+10)], fill=DARK_NAVY, width=3)
    pt2 = "/ öö"
    pt2w = draw.textbbox((0,0), pt2, font=f_per)[2]
    draw.text((pr_cx-pt2w//2, pr_cy+26), pt2, font=f_per, fill=DARK_NAVY)

    # ── 5. Roheline infoplokk: kohad + elekter ──────────────────────────────
    brush_block(draw, 40, 430, 640, 640, (*GREEN, 240), seed=11, rough=14)
    draw_calendar(draw, 110, 505, 40, YELLOW)
    f_b1 = F(42)
    f_b2 = F(30, bold=True)
    draw.text((170, 470), "41 karavanikohta", font=f_b1, fill=YELLOW)
    draw.text((170, 525), "elektri, vee ja", font=f_b2, fill=WHITE)
    draw.text((170, 563), "kanalisatsiooniga", font=f_b2, fill=WHITE)

    # ── 6. Tume plokk: kirjeldus ────────────────────────────────────────────
    brush_block(draw, 40, 680, 700, 880, (*DARK_NAVY, 235), seed=21, rough=13)
    f_d = F(30)
    lines = [
        ("Liivane rand, ujumine ja surf —", WHITE),
        ("saun ja lõkkeplats seltskonnale.", WHITE),
        ("Telkimine lubatud!", YELLOW),
    ]
    yy = 715
    for txt, col in lines:
        draw.text((75, yy), txt, font=f_d, fill=col)
        yy += 46

    # ── 7. Alumine info: mugavused ──────────────────────────────────────────
    f_lab  = F(34)
    f_val  = F(27, bold=False)

    ix, iy = 80, 935
    # Check-in 24/7
    draw_calendar(draw, ix, iy+15, 32, GOLD)
    draw.text((ix+60, iy-12), "Check-in 24/7", font=f_lab, fill=WHITE)
    draw.text((ix+60, iy+30), "iseteeninduslik sisseregistreerimine", font=f_val, fill=CREAM)

    iy2 = iy + 105
    draw_plug(draw, ix, iy2+5, 30, GOLD)
    draw.text((ix+60, iy2-12), "Hind sisaldab:", font=f_lab, fill=WHITE)
    draw.text((ix+60, iy2+30), "elekter, puhas vesi, purgimine,", font=f_val, fill=CREAM)
    draw.text((ix+60, iy2+65), "duššid, WC, köök ja pesumasin", font=f_val, fill=CREAM)

    iy3 = iy2 + 140
    draw_wifi(draw, ix, iy3+15, 30, GOLD)
    draw.text((ix+60, iy3-12), "Tasuta WiFi", font=f_lab, fill=WHITE)
    draw.text((ix+60, iy3+30), "kiire internet kogu territooriumil", font=f_val, fill=CREAM)

    iy4 = iy3 + 105
    # Telefon
    f_ph_ico = ImageFont.truetype(NORMAL, 44)
    draw.text((ix-20, iy4), "☎", font=f_ph_ico, fill=GOLD)
    draw.text((ix+45, iy4-8), "Broneeri: +372 56 955 758", font=f_lab, fill=WHITE)
    draw.text((ix+45, iy4+38), "www.willipu.ee", font=F(30), fill=YELLOW)

    # ── 8. Logo-ring all paremal (nagu näites Sadama logo) ─────────────────
    lg_cx, lg_cy, lg_r = W-180, H-220, 130
    draw.ellipse([lg_cx-lg_r, lg_cy-lg_r, lg_cx+lg_r, lg_cy+lg_r], fill=(*DARK_NAVY, 245))
    # lainejooned (nagu päise wave-ikoon)
    def wave_y(x_norm, phase):
        return math.sin(x_norm * math.pi * 2 + phase) * 9
    for wy_off, ph in ((-58, 0), (-38, math.pi)):
        pts = []
        for i in range(41):
            t = i/40
            x = lg_cx - lg_r*0.5 + t*lg_r
            pts.append((x, lg_cy + wy_off + wave_y(t, ph)))
        draw.line(pts, fill=WHITE, width=4, joint='curve')
    # "Willipu" kiri
    f_logo = F(52)
    lt = "Willipu"
    ltw = draw.textbbox((0,0), lt, font=f_logo)[2]
    draw.text((lg_cx-ltw//2, lg_cy-15), lt, font=f_logo, fill=WHITE)
    f_logo2 = F(20)
    lt2 = "GUESTHOUSE &"
    lt3 = "CARAVAN PARK"
    for i, s in enumerate((lt2, lt3)):
        sw = draw.textbbox((0,0), s, font=f_logo2)[2]
        draw.text((lg_cx-sw//2, lg_cy+52+i*26), s, font=f_logo2, fill=CREAM)
    # kuldne kaar logo all
    draw.arc([lg_cx-70, lg_cy+95, lg_cx+70, lg_cy+125], 20, 160, fill=GOLD, width=5)

    base = Image.alpha_composite(base, overlay)
    result = base.convert('RGB')
    result.save(filename, 'JPEG', quality=95, optimize=True)
    print(f"✓ {filename}  ({W}×{H} px)")


make_ad("/home/user/willipu.ee/willipu_fb_ad_karavan.jpg")
