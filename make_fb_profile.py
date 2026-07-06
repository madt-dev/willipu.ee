"""
Willipu Facebook profiilipilt
Logo: roheline ring + 2× lainekaar (nagu päises) + "Willipu" tekst
Mõõdud: 800 × 800 px
"""
from PIL import Image, ImageDraw, ImageFont
import math

S = 800

BG     = (45, 74, 62)    # --accent #2d4a3e
WHITE  = (255, 255, 255)
CREAM  = (247, 244, 238)
GOLD   = (200, 155, 60)


def cubic_bezier(p0, p1, p2, p3, steps=60):
    pts = []
    for i in range(steps + 1):
        t = i / steps
        x = (1-t)**3*p0[0] + 3*(1-t)**2*t*p1[0] + 3*(1-t)*t**2*p2[0] + t**3*p3[0]
        y = (1-t)**3*p0[1] + 3*(1-t)**2*t*p1[1] + 3*(1-t)*t**2*p2[1] + t**3*p3[1]
        pts.append((x, y))
    return pts


def wave_points(base_y):
    """
    SVG path: M3 {y} c3 0 3-3 6-3 s3 3 6 3 3-3 6-3 3 3 6 3
    Viewbox 0 0 24 24, stroke only (fill none)
    """
    pts = []
    # Segment 1: cubic (3,y) → cp1=(6,y) cp2=(6,y-3) → (9,y-3)
    pts += cubic_bezier((3, base_y), (6, base_y), (6, base_y-3), (9, base_y-3))
    # Segment 2: smooth — prev cp2 reflected → cp1=(12,y-3), cp2=(12,y) → (15,y)
    pts += cubic_bezier((9, base_y-3), (12, base_y-3), (12, base_y), (15, base_y))
    # Segment 3: smooth — cp1=(18,y), cp2=(18,y-3) → (21,y-3)
    pts += cubic_bezier((15, base_y), (18, base_y), (18, base_y-3), (21, base_y-3))
    # Segment 4: smooth — cp1=(24,y-3), cp2=(24,y) → (27,y)
    pts += cubic_bezier((21, base_y-3), (24, base_y-3), (24, base_y), (27, base_y))
    return pts


def scale_pts(pts, vb_x, vb_y, vb_w, vb_h, cx, cy, r):
    """Skaleerib SVG viewBox punktid ringi sisse."""
    scale = (r * 2 * 0.72) / max(vb_w, vb_h)
    ox = cx - (vb_w / 2) * scale
    oy = cy - (vb_h / 2) * scale
    return [(ox + (x - vb_x) * scale, oy + (y - vb_y) * scale) for x, y in pts]


def make_profile(filename):
    img = Image.new('RGBA', (S, S), (*BG, 255))
    draw = ImageDraw.Draw(img)

    cx, cy_logo = S // 2, 300   # logo ring keskel ülaosas

    # ── Ring ──────────────────────────────────────────────────────────────
    ring_r = 230
    draw.ellipse([cx-ring_r, cy_logo-ring_r, cx+ring_r, cy_logo+ring_r],
                 fill=(*BG, 255), outline=(*WHITE, 40), width=4)

    # Teine, heledam rõngas kergeks sügavuseks
    inner_r = ring_r - 18
    draw.ellipse([cx-inner_r, cy_logo-inner_r, cx+inner_r, cy_logo+inner_r],
                 fill=None, outline=(*WHITE, 15), width=2)

    # ── Kaks lainejoont (SVG viewBox 0 0 24 24, y=14 ja y=19) ────────────
    # Lainete SVG X vahemik: 3..27, Y vahemik: 11..22  → vb_w=24, vb_h=11
    VBX, VBY, VBW, VBH = 3, 11, 24, 11
    lw = max(3, int(ring_r * 0.055))

    for base_y in (14, 19):
        raw = wave_points(base_y)
        scaled = scale_pts(raw, VBX, VBY, VBW, VBH, cx, cy_logo, ring_r)
        for i in range(len(scaled) - 1):
            draw.line([scaled[i], scaled[i+1]], fill=(*WHITE, 240), width=lw)

    # ── "Willipu" tekst ───────────────────────────────────────────────────
    try:
        font_w = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 110)
    except:
        font_w = ImageFont.load_default()

    text = "Willipu"
    bb = draw.textbbox((0, 0), text, font=font_w)
    tw = bb[2] - bb[0]
    text_y = cy_logo + ring_r + 40
    draw.text(((S - tw) // 2, text_y), text, font=font_w, fill=(*WHITE, 255))

    # ── Kuldne alajoon teksti all ─────────────────────────────────────────
    line_y = text_y + (bb[3] - bb[1]) + 14
    draw.line([(cx - tw//2, line_y), (cx + tw//2, line_y)],
              fill=(*GOLD, 200), width=3)

    result = img.convert('RGB')
    result.save(filename, 'JPEG', quality=97, optimize=True)
    print(f"✓ {filename}  ({S}×{S} px)")


make_profile("/home/user/willipu.ee/willipu_facebook_profile.jpg")
