"""
Willipu Facebook profiilipilt
Mõõdud: 800 × 800 px (soovitatav, kuvatakse ringis)
"""
from PIL import Image, ImageDraw, ImageFont
import math

S = 800  # ruudukujuline

BG          = (45, 74, 62)       # --accent #2d4a3e
LOGO_WATER  = (127, 179, 213)    # #7fb3d5
LOGO_SUN    = (244, 211, 94)     # #f4d35e
WHITE       = (255, 255, 255)
CREAM       = (247, 244, 238)
GOLD        = (200, 155, 60)

def bezier_points(p0, p1, p2, steps=60):
    pts = []
    for i in range(steps + 1):
        t = i / steps
        x = (1-t)**2*p0[0] + 2*(1-t)*t*p1[0] + t**2*p2[0]
        y = (1-t)**2*p0[1] + 2*(1-t)*t*p1[1] + t**2*p2[1]
        pts.append((x, y))
    return pts

def make_profile(filename):
    img = Image.new('RGBA', (S, S), (*BG, 255))
    draw = ImageDraw.Draw(img)

    cx, cy = S // 2, S // 2

    # ── Logo ring (kergelt läbipaistev valge piirjoon) ───────────────────
    ring_r = 290
    draw.ellipse([cx-ring_r, cy-ring_r-30, cx+ring_r, cy+ring_r-30],
                 fill=(*BG, 255), outline=(*WHITE, 30), width=3)

    # ── Laine skaleeritud SVG viewBox 0 0 32 32 → meie koordinaatidesse ──
    # Laine on logo ülemises/alumises pooles, skaleerime suuremaks
    wave_r = 250   # "ring" raadius laine jaoks
    s = wave_r / 16.0
    ox = cx - 16*s
    oy = (cy - 30) - 16*s   # nihe üles et logo oleks teksti kohal

    def sp(x, y):
        return (ox + x*s, oy + y*s)   # SVG Y = alla, jätame sama suunda

    # Laine kuju: M6,20 Q12,16 16,20 T26,20 V26 H6 Z
    wave_pts = []
    wave_pts += bezier_points(sp(6,20), sp(12,16), sp(16,20))
    wave_pts += bezier_points(sp(16,20), sp(20,24), sp(26,20))
    wave_pts.append(sp(26, 26))
    wave_pts.append(sp(6, 26))
    draw.polygon(wave_pts, fill=(*LOGO_WATER, 230))

    # ── Päike ─────────────────────────────────────────────────────────────
    sun_r = int(3 * s)
    sc = sp(22, 10)
    draw.ellipse([sc[0]-sun_r, sc[1]-sun_r, sc[0]+sun_r, sc[1]+sun_r],
                 fill=(*LOGO_SUN, 245))

    # ── "Willipu" tekst logo all ──────────────────────────────────────────
    try:
        font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 100)
    except:
        font = ImageFont.load_default()

    text = "Willipu"
    bbox = draw.textbbox((0, 0), text, font=font)
    tw = bbox[2] - bbox[0]
    text_y = cy + wave_r - 20
    draw.text(((S - tw) // 2, text_y), text, font=font, fill=(*WHITE, 255))

    # ── Kuldne allajoon teksti all ────────────────────────────────────────
    line_y = text_y + (bbox[3] - bbox[1]) + 8
    line_len = tw - 20
    draw.line([(cx - line_len//2, line_y), (cx + line_len//2, line_y)],
              fill=(*GOLD, 180), width=3)

    # ── Salvesta ──────────────────────────────────────────────────────────
    result = img.convert('RGB')
    result.save(filename, 'JPEG', quality=97, optimize=True)
    print(f"✓ Profiilipilt salvestatud: {filename}  ({S}×{S} px)")

make_profile("/home/user/willipu.ee/willipu_facebook_profile.jpg")
