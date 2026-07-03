"""
Willipu logo — vektorfail (SVG) e-mailide, vormide ja turundusmaterjalide jaoks.
Koosneb: päise laineikoon (roheline ring + 2 valget lainet) + "Willipu" tekst kõveratena.
Genereerib:
  - willipu_logo.svg        (tume tekst, heledale taustale)
  - willipu_logo_white.svg  (valge tekst, tumedale taustale)
  - willipu_logo.pdf        (vektor-PDF, trükiks)
"""
from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen

FONT_PATH = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
TEXT = "Willipu"

ACCENT = "#2d4a3e"   # roheline ring
INK    = "#1c2620"   # tume tekst (nagu saidi --ink)
WHITE  = "#ffffff"

# Laineikoon saidi Icon.jsx-ist (viewBox 0 0 24 24):
WAVE_D1 = "M3 14c3 0 3-3 6-3s3 3 6 3 3-3 6-3 3 3 6 3"
WAVE_D2 = "M3 19c3 0 3-3 6-3s3 3 6 3 3-3 6-3 3 3 6 3"


def text_to_paths(text, font_path, font_size):
    """Teisenda tekst SVG path-ideks. Tagastab (paths, total_width)."""
    font = TTFont(font_path)
    glyph_set = font.getGlyphSet()
    cmap = font.getBestCmap()
    units_per_em = font['head'].unitsPerEm
    scale = font_size / units_per_em

    paths = []
    x = 0.0
    for ch in text:
        glyph_name = cmap[ord(ch)]
        glyph = glyph_set[glyph_name]
        pen = SVGPathPen(glyph_set)
        glyph.draw(pen)
        d = pen.getCommands()
        if d:
            # Font-koordinaadid on Y-üles; SVG on Y-alla → peegelda ja nihuta
            paths.append(
                f'<path transform="translate({x:.2f},0) scale({scale:.6f},{-scale:.6f})" d="{d}"/>'
            )
        x += glyph.width * scale
    return paths, x


def build_svg(text_color, filename):
    FONT_SIZE = 100
    paths, text_w = text_to_paths(TEXT, FONT_PATH, FONT_SIZE)

    # Ikooni geomeetria
    ICON_D   = 110              # ringi läbimõõt
    GAP      = 28               # ikooni ja teksti vahe
    ASC      = 74               # teksti cap-kõrgus u. baseline'ist üles
    DESC     = 26               # allapikendused (p)
    PAD      = 10

    total_w = ICON_D + GAP + text_w + PAD * 2
    total_h = ICON_D + PAD * 2
    icon_cx = PAD + ICON_D / 2
    icon_cy = total_h / 2
    # Teksti baseline: keskjoondus ikooni suhtes
    baseline = icon_cy + ASC / 2 - 4
    text_x   = PAD + ICON_D + GAP

    # Laineikooni skaleerimine: viewBox 24×24 → ICON_D sees (72% ringist)
    wave_scale = ICON_D * 0.68 / 24
    wave_off_x = icon_cx - 12 * wave_scale
    wave_off_y = icon_cy - 12 * wave_scale

    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {total_w:.0f} {total_h:.0f}" width="{total_w:.0f}" height="{total_h:.0f}">
  <!-- Willipu logo — willipu.ee -->
  <g>
    <circle cx="{icon_cx:.1f}" cy="{icon_cy:.1f}" r="{ICON_D/2:.1f}" fill="{ACCENT}"/>
    <g transform="translate({wave_off_x:.2f},{wave_off_y:.2f}) scale({wave_scale:.4f})"
       fill="none" stroke="{WHITE}" stroke-width="1.8" stroke-linecap="round">
      <path d="{WAVE_D1}"/>
      <path d="{WAVE_D2}"/>
    </g>
  </g>
  <g transform="translate({text_x:.2f},{baseline:.2f})" fill="{text_color}">
    {chr(10).join('    ' + p for p in paths)}
  </g>
</svg>'''

    with open(filename, 'w') as f:
        f.write(svg)
    print(f"✓ {filename}  ({total_w:.0f}×{total_h:.0f})")
    return filename


def svg_to_pdf(svg_file, pdf_file):
    """Renderda SVG PDF-iks ReportLab-iga (joonistame samad elemendid)."""
    from reportlab.graphics import renderPDF
    try:
        from svglib.svglib import svg2rlg
        drawing = svg2rlg(svg_file)
        renderPDF.drawToFile(drawing, pdf_file)
        print(f"✓ {pdf_file}")
        return True
    except ImportError:
        return False


build_svg(INK,   "/home/user/willipu.ee/willipu_logo.svg")
build_svg(WHITE, "/home/user/willipu.ee/willipu_logo_white.svg")

if not svg_to_pdf("/home/user/willipu.ee/willipu_logo.svg",
                  "/home/user/willipu.ee/willipu_logo.pdf"):
    print("svglib puudub — proovin paigaldada")
