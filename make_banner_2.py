"""
Willipu Banner 2 — trükibanner
Laius: 2200 mm  |  Kõrgus: 1000 mm
"""
from reportlab.lib.units import mm
from reportlab.lib.colors import HexColor, white
from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader
from PIL import Image as PILImage
import io, os

# ── Mõõdud ──────────────────────────────────────────────────────────────
W = 2200 * mm   # laius
H = 1000 * mm   # kõrgus

# ── Värvid (willipu.ee) ──────────────────────────────────────────────────
DARK    = HexColor('#14201b')
ACCENT  = HexColor('#2d4a3e')
ACCENT2 = HexColor('#5d8a6a')
GOLD    = HexColor('#c89b3c')
CREAM   = HexColor('#f7f4ee')
LINE    = HexColor('#d9d2c2')

SRC = os.path.join(os.path.dirname(__file__), 'public', 'kar4.jpg')


def prepare_bg():
    img = PILImage.open(SRC).convert('RGB')
    target = W / H
    src    = img.width / img.height
    if src > target:
        nw = int(img.height * target)
        img = img.crop(((img.width - nw)//2, 0, (img.width - nw)//2 + nw, img.height))
    else:
        nh = int(img.width / target)
        img = img.crop((0, (img.height - nh)//2, img.width, (img.height - nh)//2 + nh))
    buf = io.BytesIO()
    img.save(buf, 'JPEG', quality=95)
    buf.seek(0)
    return buf


def wave_pts_svg(base_y, steps=60):
    """Tagastab SVG lainekõvera punktid (viewBox 0 0 24 24)."""
    def cubic(p0, p1, p2, p3):
        return [
            ((1-t)**3*p0[0]+3*(1-t)**2*t*p1[0]+3*(1-t)*t**2*p2[0]+t**3*p3[0],
             (1-t)**3*p0[1]+3*(1-t)**2*t*p1[1]+3*(1-t)*t**2*p2[1]+t**3*p3[1])
            for t in [i/steps for i in range(steps+1)]
        ]
    y = base_y
    pts  = cubic((3,y),  (6,y),   (6,y-3),  (9,y-3))
    pts += cubic((9,y-3),(12,y-3),(12,y),   (15,y))
    pts += cubic((15,y), (18,y),  (18,y-3), (21,y-3))
    pts += cubic((21,y-3),(24,y-3),(24,y),  (27,y))
    return pts


def draw_wave_icon(c, cx, cy, radius):
    """Joonistab päise laikeikooniga rohelise ringi."""
    # Taust-ring
    c.saveState()
    c.setFillColor(ACCENT)
    c.circle(cx, cy, radius, fill=1, stroke=0)

    # Skaleerimistegur: SVG viewBox X=3..27 (24 ühikut laius), Y=11..22
    vb_w, vb_h = 24, 11
    scale = (radius * 1.5) / vb_w
    ox = cx - (27+3)/2 * scale
    oy = cy - (22+11)/2 * scale

    def tr(x, y):
        return (ox + x*scale, oy + (33 - y)*scale)   # SVG Y pööratud

    # Kaks lainekõverat
    c.setStrokeColor(white)
    c.setLineWidth(radius * 0.10)
    c.setLineCap(1)   # round
    for base_y in (14, 19):
        raw = wave_pts_svg(base_y)
        scaled = [tr(x, y) for x, y in raw]
        p = c.beginPath()
        p.moveTo(*scaled[0])
        for pt in scaled[1:]:
            p.lineTo(*pt)
        c.drawPath(p, stroke=1, fill=0)
    c.restoreState()


def make_banner(filename):
    c = canvas.Canvas(filename, pagesize=(W, H))
    c.setTitle("Willipu Guesthouse and Caravan — Reklaambanner")

    # ── 1. Taustpilt ────────────────────────────────────────────────────
    c.drawImage(ImageReader(prepare_bg()), 0, 0, width=W, height=H,
                preserveAspectRatio=False)

    # ── 2. Tumendav overlay ──────────────────────────────────────────────
    c.saveState()
    c.setFillColor(DARK)
    c.setFillAlpha(0.38)
    c.rect(0, 0, W, H, fill=1, stroke=0)
    c.restoreState()

    # ── 3. Kuldne riba üla ja alla ───────────────────────────────────────
    bar = 7 * mm
    c.setFillColor(GOLD)
    c.setFillAlpha(0.9)
    c.rect(0, H-bar, W, bar, fill=1, stroke=0)
    c.rect(0, 0,     W, bar, fill=1, stroke=0)

    # ── 4. Tekstiblokk (vasak pool) ──────────────────────────────────────
    tx  = 85 * mm
    mid = H * 0.5

    # Eyebrow
    c.saveState()
    c.setFillColor(white)
    c.setFillAlpha(1)
    c.setFont("Helvetica-Bold", 36*mm)
    c.drawString(tx, mid + 215*mm, "PUHKEMAJUTUS  ·  KARAVAN PARK")
    c.restoreState()

    # "Willipu"
    c.saveState()
    c.setFillColor(white)
    c.setFillAlpha(1)
    c.setFont("Helvetica-Bold", 260*mm)
    c.drawString(tx, mid - 10*mm, "Willipu")
    c.restoreState()

    # Kuldne eraldajajoon
    c.saveState()
    c.setStrokeColor(GOLD)
    c.setStrokeAlpha(0.8)
    c.setLineWidth(1.5*mm)
    c.line(tx, mid - 15*mm, tx + 900*mm, mid - 15*mm)
    c.restoreState()

    # "Guesthouse and Caravan"
    c.saveState()
    c.setFillColor(CREAM)
    c.setFillAlpha(0.96)
    c.setFont("Helvetica-Bold", 95*mm)
    c.drawString(tx, mid - 120*mm, "Guesthouse and Caravan")
    c.restoreState()

    # "willipu.ee"
    c.saveState()
    c.setFillColor(white)
    c.setFillAlpha(1)
    c.setFont("Helvetica-Bold", 28*mm)
    c.drawString(tx, mid - 190*mm, "willipu.ee")
    c.restoreState()

    # ── 5. Nurga kaunistused ─────────────────────────────────────────────
    pad, arm, lw = 30*mm, 55*mm, 2*mm
    c.saveState()
    c.setStrokeColor(GOLD)
    c.setStrokeAlpha(0.5)
    c.setLineWidth(lw)
    for (x, y, dx, dy) in [(pad,pad,1,1),(pad,H-pad,1,-1),(W-pad,pad,-1,1),(W-pad,H-pad,-1,-1)]:
        c.line(x, y, x+dx*arm, y)
        c.line(x, y, x, y+dy*arm)
    c.restoreState()

    c.save()

    print(f"✓ {filename}")
    print(f"  Laius: {W/mm:.1f} mm  |  Kõrgus: {H/mm:.1f} mm")


make_banner("/home/user/willipu.ee/willipu_banner_2.pdf")
