"""
Willipu Banner 2 — trükibanner
Laius: 2200 mm  |  Kõrgus: 1000 mm
"""
from reportlab.lib.units import mm
from reportlab.lib.colors import HexColor, white
from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from PIL import Image as PILImage
import io, os

pdfmetrics.registerFont(TTFont('DejaVu', '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'))
pdfmetrics.registerFont(TTFont('DejaVuBold', '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'))

W = 2200 * mm   # laius
H = 1000 * mm   # kõrgus

DARK   = HexColor('#14201b')
ACCENT = HexColor('#2d4a3e')
GOLD   = HexColor('#c89b3c')
CREAM  = HexColor('#f7f4ee')

SRC = os.path.join(os.path.dirname(__file__), 'public', 'kar4.jpg')


def prepare_bg():
    img = PILImage.open(SRC).convert('RGB')
    ratio = W / H  # 2.2
    src   = img.width / img.height
    if src > ratio:
        nw = int(img.height * ratio)
        img = img.crop(((img.width - nw)//2, 0, (img.width + nw)//2, img.height))
    else:
        nh = int(img.width / ratio)
        img = img.crop((0, (img.height - nh)//2, img.width, (img.height + nh)//2))
    buf = io.BytesIO()
    img.save(buf, 'JPEG', quality=95)
    buf.seek(0)
    return buf


def make_banner(filename):
    c = canvas.Canvas(filename, pagesize=(W, H))
    c.setTitle("Willipu Guesthouse and Caravan — Reklaambanner")

    # ── 1. Taustpilt ────────────────────────────────────────────────────────
    c.drawImage(ImageReader(prepare_bg()), 0, 0, width=W, height=H,
                preserveAspectRatio=False)

    # ── 2. Tumendav overlay ──────────────────────────────────────────────────
    c.saveState()
    c.setFillColor(DARK)
    c.setFillAlpha(0.42)
    c.rect(0, 0, W, H, fill=1, stroke=0)
    c.restoreState()

    # ── 3. Kuldne riba üla ja alla ──────────────────────────────────────────
    bar = 8 * mm
    c.setFillColor(GOLD)
    c.setFillAlpha(1)
    c.rect(0, H - bar, W, bar, fill=1, stroke=0)
    c.rect(0, 0,       W, bar, fill=1, stroke=0)

    # ── 4. Tekstiblokk — töötan ülevalt alla ────────────────────────────────
    tx = 80 * mm   # vasak veeris

    # Fondisuurused
    fs_eye  = 52 * mm   # "PUHKEMAJUTUS · KARAVAN PARK"
    fs_main = 230 * mm  # "Willipu"
    fs_sub  = 90 * mm   # "Guesthouse and Caravan"
    fs_con  = 44 * mm   # kontaktinfo

    # Cap-height ≈ 72% fondisuurusest (tekst kerkib baasjoone KOHALE)
    cap_eye  = fs_eye  * 0.72
    cap_main = fs_main * 0.72
    cap_sub  = fs_sub  * 0.72
    cap_con  = fs_con  * 0.72

    top_pad  = bar + 45 * mm   # algus ülevalt

    # Y-asukohad: anname teksti ülemise serva kauguse ülevalt,
    # teisendame ReportLab baasjoone kordinaadiks (Y ülevalt → RL-i baasele)
    def y_from_top(dist_from_top, cap_h):
        """dist_from_top = ülemisest servast teksti ülemise servani."""
        return H - dist_from_top - cap_h

    # Eyebrow ülemine serv: 45mm alla ülemisest ribast
    y_eye  = y_from_top(top_pad, cap_eye)

    # "Willipu" — 30mm allpool eyebrow'i alumisest servast
    gap_1  = 30 * mm
    y_main = y_eye - gap_1 - cap_main   # baasejoon

    # Kuldne eraldajajoon
    y_line = y_main - 18 * mm

    # "Guesthouse and Caravan" — 20mm allpool joont
    gap_2  = 20 * mm
    y_sub  = y_line - gap_2 - cap_sub

    # Eyebrow
    c.saveState()
    c.setFillColor(white)
    c.setFillAlpha(1)
    c.setFont("Helvetica-Bold", fs_eye)
    c.drawString(tx, y_eye, "PUHKEMAJUTUS  ·  KARAVAN PARK")
    c.restoreState()

    # "Willipu"
    c.saveState()
    c.setFillColor(white)
    c.setFillAlpha(1)
    c.setFont("Helvetica-Bold", fs_main)
    c.drawString(tx, y_main, "Willipu")
    c.restoreState()

    # Kuldne eraldajajoon
    c.saveState()
    c.setStrokeColor(GOLD)
    c.setStrokeAlpha(0.85)
    c.setLineWidth(1.5 * mm)
    c.line(tx, y_line, tx + 1000 * mm, y_line)
    c.restoreState()

    # "Guesthouse and Caravan"
    c.saveState()
    c.setFillColor(CREAM)
    c.setFillAlpha(0.97)
    c.setFont("Helvetica-Bold", fs_sub)
    c.drawString(tx, y_sub, "Guesthouse and Caravan")
    c.restoreState()

    # ── 5. Kontaktinfo — parem alaserv ──────────────────────────────────────
    pad_right = 75 * mm
    row_phone_y = bar + 28 * mm          # telefonirida
    row_web_y   = row_phone_y + fs_con + 16 * mm   # veebilehekülje rida

    phone_text = "+372 56 955 758"
    web_text   = "www.willipu.ee"

    phone_w = c.stringWidth(phone_text, "Helvetica-Bold", fs_con)
    web_w   = c.stringWidth(web_text,   "Helvetica-Bold", fs_con)

    phone_x = W - pad_right - phone_w
    web_x   = W - pad_right - web_w

    icon_gap = 22 * mm   # tühimik ikooni ja teksti vahel

    # Telefoniikoon ☎
    phone_icon_w = c.stringWidth('☎', 'DejaVu', fs_con)
    c.saveState()
    c.setFillColor(white)
    c.setFillAlpha(1)
    c.setFont('DejaVu', fs_con)
    c.drawString(phone_x - icon_gap - phone_icon_w, row_phone_y, '☎')
    c.restoreState()

    # Telefoni number
    c.saveState()
    c.setFillColor(white)
    c.setFillAlpha(1)
    c.setFont("Helvetica-Bold", fs_con)
    c.drawString(phone_x, row_phone_y, phone_text)
    c.restoreState()

    # Globuse ikoon
    def draw_globe(cx, cy, r):
        c.saveState()
        c.setStrokeColor(white)
        c.setStrokeAlpha(1)
        c.setLineWidth(r * 0.17)
        c.setLineCap(1)
        c.circle(cx, cy, r, fill=0, stroke=1)
        for dx in (0.5, -0.5):
            p = c.beginPath()
            p.moveTo(cx, cy + r)
            p.curveTo(cx + dx*r, cy + r*0.6, cx + dx*r, cy - r*0.6, cx, cy - r)
            c.drawPath(p, stroke=1, fill=0)
        c.line(cx - r, cy, cx + r, cy)
        c.restoreState()

    globe_r   = cap_con * 0.5
    globe_cx  = web_x - icon_gap - globe_r
    globe_cy  = row_web_y + cap_con * 0.5

    draw_globe(globe_cx, globe_cy, globe_r)

    c.saveState()
    c.setFillColor(white)
    c.setFillAlpha(1)
    c.setFont("Helvetica-Bold", fs_con)
    c.drawString(web_x, row_web_y, web_text)
    c.restoreState()

    # ── 6. Nurga kaunistused ────────────────────────────────────────────────
    pad_c, arm, lw = 28*mm, 52*mm, 2*mm
    c.saveState()
    c.setStrokeColor(GOLD)
    c.setStrokeAlpha(0.5)
    c.setLineWidth(lw)
    for (x, y, dx, dy) in [
        (pad_c, pad_c,   1,  1),
        (pad_c, H-pad_c, 1, -1),
        (W-pad_c, pad_c, -1,  1),
        (W-pad_c, H-pad_c, -1, -1),
    ]:
        c.line(x, y, x + dx*arm, y)
        c.line(x, y, x, y + dy*arm)
    c.restoreState()

    c.save()
    print(f"✓ {filename}  —  Laius: {W/mm:.0f} mm  |  Kõrgus: {H/mm:.0f} mm")


make_banner("/home/user/willipu.ee/willipu_banner_2.pdf")
