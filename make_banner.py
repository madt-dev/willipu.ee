"""
Willipu Guesthouse and Caravan - reklaambanner
Mõõdud: 2200mm × 1000mm (laius × kõrgus)
Taust: kar4.jpg pilt tumedaks tehtud
"""
from reportlab.lib.units import mm
from reportlab.lib.colors import HexColor, white, black, Color
from reportlab.pdfgen import canvas
from PIL import Image as PILImage
import io, os

W = 2200 * mm
H = 1000 * mm

GOLD      = HexColor('#c89b3c')
GOLD_LIGHT= HexColor('#e8c96a')
CREAM     = HexColor('#f7f4ee')
DARK      = HexColor('#14201b')
ACCENT    = HexColor('#2d4a3e')
ACCENT2   = HexColor('#5d8a6a')


def prepare_bg_image(src_path):
    """Laiendab pildi banneri kuvasuhtele, ei lõika midagi ära."""
    img = PILImage.open(src_path).convert('RGB')
    # Skaleerime pildi nii et see katab kogu banneri
    target_ratio = 2200 / 1000
    src_ratio = img.width / img.height
    if src_ratio > target_ratio:
        new_h = img.height
        new_w = int(img.height * target_ratio)
        left = (img.width - new_w) // 2
        img = img.crop((left, 0, left + new_w, new_h))
    else:
        new_w = img.width
        new_h = int(img.width / target_ratio)
        top = (img.height - new_h) // 2
        img = img.crop((0, top, new_w, top + new_h))
    buf = io.BytesIO()
    img.save(buf, format='JPEG', quality=95)
    buf.seek(0)
    return buf


def draw_banner(filename):
    c = canvas.Canvas(filename, pagesize=(W, H))

    # ── 1. Taustpilt ─────────────────────────────────────────────────────
    src = os.path.join(os.path.dirname(__file__), 'public', 'kar4.jpg')
    bg_buf = prepare_bg_image(src)
    c.drawImage(
        __import__('reportlab.lib.utils', fromlist=['ImageReader']).ImageReader(bg_buf),
        0, 0, width=W, height=H,
        preserveAspectRatio=False
    )

    # ── 2. Ühtlane tumendav overlay kogu pildile ─────────────────────────
    c.saveState()
    c.setFillColor(DARK)
    c.setFillAlpha(0.32)
    c.rect(0, 0, W, H, fill=1, stroke=0)
    c.restoreState()

    # ── 3. Logo (ring + laine + päike) ───────────────────────────────────
    def draw_logo(cx, cy, r):
        LOGO_GREEN = HexColor('#2d4a3e')
        LOGO_WATER = HexColor('#7fb3d5')
        LOGO_SUN   = HexColor('#f4d35e')

        # Roheline ring
        c.saveState()
        c.setFillColor(LOGO_GREEN)
        c.setFillAlpha(1)
        c.circle(cx, cy, r, fill=1, stroke=0)

        # Laine (Q12 16 16 20 T26 20 V26 H6 — skaleeritud)
        # SVG viewBox 0 0 32 32, skaleerime r/16 faktoriga
        s = r / 16.0
        ox = cx - 16*s   # SVG cx=0 → meie cx - r
        oy = cy - 16*s   # SVG cy=0 → meie cy - r (NB: Y on ReportLab-is ülespoole)

        def sx(x): return ox + x * s
        def sy(y): return oy + (32 - y) * s   # SVG Y pööratud

        c.setFillColor(LOGO_WATER)
        p = c.beginPath()
        # M6 20
        p.moveTo(sx(6), sy(20))
        # Q12 16 16 20  (quadratic → cubikis approx)
        p.curveTo(sx(6 + (12-6)*2/3), sy(20 + (16-20)*2/3),
                  sx(16 + (12-16)*2/3), sy(20 + (16-20)*2/3),
                  sx(16), sy(20))
        # T26 20 (reflect)
        p.curveTo(sx(16 + (16-12)*2/3), sy(20 + (20-16)*2/3),
                  sx(26 + (20-16)*2/3), sy(20 + (20-20)*2/3),
                  sx(26), sy(20))
        # V26 H6 Z
        p.lineTo(sx(26), sy(26))
        p.lineTo(sx(6),  sy(26))
        p.close()
        c.drawPath(p, fill=1, stroke=0)

        # Päike
        c.setFillColor(LOGO_SUN)
        c.circle(sx(22), sy(10), 3*s, fill=1, stroke=0)
        c.restoreState()

    logo_r = 120 * mm
    logo_x = W - 220 * mm
    logo_y = H / 2
    draw_logo(logo_x, logo_y, logo_r)

    # ── 4. Kuldne riba ülaosas ja alaosas ────────────────────────────────
    bar_h = 7 * mm
    c.setFillColor(GOLD)
    c.setFillAlpha(0.9)
    c.rect(0, H - bar_h, W, bar_h, fill=1, stroke=0)
    c.rect(0, 0, W, bar_h, fill=1, stroke=0)

    # ── 4. Vasak pool: tekstiblokk ───────────────────────────────────────
    tx  = 80 * mm
    mid = H / 2

    # Eyebrow
    c.saveState()
    c.setFillColor(white)
    c.setFillAlpha(1)
    c.setFont("Helvetica-Bold", 24*mm)
    c.drawString(tx, mid + 210*mm, "PUHKEMAJUTUS  ·  KARAVAN PARK")
    c.restoreState()

    # "Willipu" - suur pealkiri
    c.saveState()
    c.setFillColor(white)
    c.setFillAlpha(1)
    c.setFont("Helvetica-Bold", 200*mm)
    c.drawString(tx, mid + 5*mm, "Willipu")
    c.restoreState()

    # Kuldne eraldajajoon
    sep_y = mid - 15*mm
    c.saveState()
    c.setStrokeColor(GOLD)
    c.setStrokeAlpha(0.75)
    c.setLineWidth(1.5*mm)
    c.line(tx, sep_y, tx + 900*mm, sep_y)
    c.restoreState()

    # "Guesthouse and Caravan" - suurelt
    c.saveState()
    c.setFillColor(CREAM)
    c.setFillAlpha(0.96)
    c.setFont("Helvetica-Bold", 95*mm)
    c.drawString(tx, mid - 120*mm, "Guesthouse and Caravan")
    c.restoreState()

    # Veebiaadress
    c.saveState()
    c.setFillColor(white)
    c.setFillAlpha(1)
    c.setFont("Helvetica-Bold", 28*mm)
    c.drawString(tx, mid - 190*mm, "willipu.ee")
    c.restoreState()

    # ── 5. Nurga kaunistused ──────────────────────────────────────────────
    pad = 30*mm
    arm = 55*mm
    lw  = 2.2*mm
    corners = [
        (pad,   pad,   1,  1),
        (pad,   H-pad, 1, -1),
        (W-pad, pad,  -1,  1),
        (W-pad, H-pad,-1, -1),
    ]
    c.saveState()
    c.setStrokeColor(GOLD)
    c.setStrokeAlpha(0.5)
    c.setLineWidth(lw)
    for (x, y, dx, dy) in corners:
        c.line(x, y, x + dx*arm, y)
        c.line(x, y, x, y + dy*arm)
    c.restoreState()

    c.save()
    print(f"✓ Banner salvestatud: {filename}")


draw_banner("/home/user/willipu.ee/willipu_banner_2200x1000.pdf")
