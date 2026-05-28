"""
Willipu Guesthouse and Caravan - reklaambanner
Mõõdud: 2200mm × 1000mm (laius × kõrgus)
Värvid ja stiil: willipu.ee
"""
from reportlab.lib.units import mm
from reportlab.lib.colors import HexColor, white, black
from reportlab.pdfgen import canvas
from reportlab.graphics.shapes import *
from reportlab.graphics import renderPDF
import math

W = 2200 * mm
H = 1000 * mm

DARK      = HexColor('#14201b')
ACCENT    = HexColor('#2d4a3e')
ACCENT2   = HexColor('#5d8a6a')
GOLD      = HexColor('#c89b3c')
GOLD_LIGHT= HexColor('#e0b84a')
CREAM     = HexColor('#f7f4ee')
BG_SOFT   = HexColor('#efe9dd')
INK_SOFT  = HexColor('#4a544d')


def draw_banner(filename):
    c = canvas.Canvas(filename, pagesize=(W, H))

    # ── 1. Gradient taust (tumemast heledamaks vasakult paremale) ─────────
    c.linearGradient(
        0, H/2, W, H/2,                          # x0,y0 → x1,y1
        (DARK, ACCENT),
        extend=True
    )

    # ── 2. Vasak dekoratiivne ring ────────────────────────────────────────
    cx1, cy1, r1 = 210*mm, H/2, 200*mm
    c.saveState()
    c.setFillColor(ACCENT2)
    c.setFillAlpha(0.12)
    c.circle(cx1, cy1, r1, fill=1, stroke=0)
    c.setFillAlpha(0.07)
    c.circle(cx1, cy1, r1 * 1.45, fill=1, stroke=0)
    c.restoreState()

    # Ringi äärejoon (kuldne)
    c.saveState()
    c.setStrokeColor(GOLD)
    c.setStrokeAlpha(0.45)
    c.setLineWidth(2.5 * mm)
    c.circle(cx1, cy1, r1, fill=0, stroke=1)
    c.restoreState()

    # "W" kiri ringis
    c.saveState()
    c.setFillColor(white)
    c.setFillAlpha(0.95)
    c.setFont("Helvetica-Bold", 190*mm)
    tw = c.stringWidth("W", "Helvetica-Bold", 190*mm)
    c.drawString(cx1 - tw/2, cy1 - 68*mm, "W")
    c.restoreState()

    # ── 3. Parem kaunistus-ring ───────────────────────────────────────────
    c.saveState()
    c.setFillColor(DARK)
    c.setFillAlpha(0.18)
    c.circle(W - 60*mm, H*0.5, 320*mm, fill=1, stroke=0)
    c.restoreState()

    # ── 4. Kuldne horisontaalne riba keskel ──────────────────────────────
    line_x0 = 440 * mm
    line_y   = H / 2
    c.saveState()
    c.setStrokeColor(GOLD)
    c.setStrokeAlpha(0.7)
    c.setLineWidth(1.8 * mm)
    c.line(line_x0, line_y, W - 80*mm, line_y)
    c.restoreState()

    # ── 5. Tekstid ────────────────────────────────────────────────────────
    tx = 450 * mm          # teksti alguspunkt X
    mid = H / 2            # vertikaalne keskpunkt

    # Eyebrow (väike suurtähtede rida)
    eyebrow = "PUHKEMAJUTUS  ·  KARAVAN PARK"
    c.saveState()
    c.setFillColor(GOLD)
    c.setFillAlpha(0.88)
    c.setFont("Helvetica", 20*mm)
    c.drawString(tx, mid + 195*mm, eyebrow)
    c.restoreState()

    # "Willipu" - suur serif-stiilis pealkiri
    c.saveState()
    c.setFillColor(white)
    c.setFillAlpha(1)
    c.setFont("Helvetica-Bold", 220*mm)
    c.drawString(tx - 4*mm, mid - 10*mm, "Willipu")
    c.restoreState()

    # Alapealkiri
    subtitle = "Guesthouse and Caravan"
    c.saveState()
    c.setFillColor(CREAM)
    c.setFillAlpha(0.85)
    c.setFont("Helvetica", 60*mm)
    c.drawString(tx, mid - 110*mm, subtitle)
    c.restoreState()

    # Kuldne riba pealkirja all
    c.saveState()
    c.setStrokeColor(GOLD)
    c.setStrokeAlpha(0.5)
    c.setLineWidth(1*mm)
    sub_w = c.stringWidth(subtitle, "Helvetica", 60*mm)
    c.line(tx, mid - 130*mm, tx + sub_w, mid - 130*mm)
    c.restoreState()

    # Veebiaadress
    c.saveState()
    c.setFillColor(CREAM)
    c.setFillAlpha(0.45)
    c.setFont("Helvetica", 21*mm)
    c.drawString(tx, mid - 185*mm, "willipu.ee")
    c.restoreState()

    # ── 6. Nurga kaunistused ──────────────────────────────────────────────
    pad   = 28 * mm
    arm   = 50 * mm
    lw    = 2 * mm
    corners = [
        (pad, pad,          1,  1),   # vasak-alumine
        (pad, H-pad,        1, -1),   # vasak-ülemine
        (W-pad, pad,       -1,  1),   # parem-alumine
        (W-pad, H-pad,     -1, -1),   # parem-ülemine
    ]
    c.saveState()
    c.setStrokeColor(GOLD)
    c.setStrokeAlpha(0.4)
    c.setLineWidth(lw)
    for (x, y, dx, dy) in corners:
        c.line(x, y, x + dx*arm, y)
        c.line(x, y, x, y + dy*arm)
    c.restoreState()

    # ── 7. Ülemine ja alumine dekoratiivne riba ───────────────────────────
    bar_h = 6 * mm
    c.saveState()
    c.setFillColor(GOLD)
    c.setFillAlpha(0.8)
    c.rect(0, H - bar_h, W, bar_h, fill=1, stroke=0)
    c.rect(0, 0, W, bar_h, fill=1, stroke=0)
    c.restoreState()

    # ── 8. Kontakt info allosas ───────────────────────────────────────────
    c.saveState()
    c.setFillColor(CREAM)
    c.setFillAlpha(0.35)
    c.setFont("Helvetica", 16*mm)
    info = "willipu.ee  ·  Võrumaa, Eesti"
    c.drawCentredString(W/2, 30*mm, info)
    c.restoreState()

    c.save()
    print(f"✓ Banner salvestatud: {filename}")
    print(f"  Mõõdud: {2200}mm × {1000}mm")


draw_banner("/home/user/willipu.ee/willipu_banner_2200x1000.pdf")
