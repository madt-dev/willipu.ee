"""
Willipu — unisex WC + dušširuumi uksesilt
Stiil: willipu.ee (roheline taust, valged piktogrammid, kuldne aktsent)
Väljund: SVG (vektor), PDF (150×150 mm, trükiks), PNG (eelvaade)
"""

ACCENT = "#2d4a3e"
GOLD   = "#c89b3c"
WHITE  = "#ffffff"

# 300×300 viewBox
def build_svg(filename):
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 300 300" width="300" height="300">
  <!-- Willipu — unisex WC + dušš uksesilt -->

  <!-- Taust: ümarnurkne ruut -->
  <rect x="6" y="6" width="288" height="288" rx="28" fill="{ACCENT}"/>
  <rect x="14" y="14" width="272" height="272" rx="22" fill="none"
        stroke="{GOLD}" stroke-width="2.5" opacity="0.85"/>

  <!-- ══ Mees (vasakul) ══ -->
  <g fill="{WHITE}">
    <!-- pea -->
    <circle cx="78" cy="78" r="17"/>
    <!-- keha -->
    <path d="M78 100
             c -14 0 -22 8 -22 22
             l 0 40 c 0 3.5 2.7 6 6 6 c 3.3 0 6 -2.5 6 -6
             l 0 -36 l 4 0
             l 0 92 c 0 4.5 3.2 7.5 7 7.5 c 3.8 0 7 -3 7 -7.5
             l 0 -54 l 4 0 l 0 54 c 0 4.5 3.2 7.5 7 7.5 c 3.8 0 7 -3 7 -7.5
             l 0 -92 l 4 0 l 0 36 c 0 3.5 2.7 6 6 6 c 3.3 0 6 -2.5 6 -6
             l 0 -40 c 0 -14 -8 -22 -22 -22 z"/>
  </g>

  <!-- ══ Naine (keskel) ══ -->
  <g fill="{WHITE}">
    <!-- pea -->
    <circle cx="150" cy="78" r="17"/>
    <!-- keha + seelik -->
    <path d="M150 100
             c -12 0 -19 6.5 -22 17
             l -11 42 c -1 4 1.5 7 5 7.8 c 3.2 0.8 6.3 -1 7.3 -4.6
             l 9.7 -36.2 l 3 0
             l -14 52 l 15 0 l 0 44 c 0 4.5 3 7.5 7 7.5 c 4 0 7 -3 7 -7.5
             l 0 -44 l 15 0 l -14 -52 l 3 0 l 9.7 36.2
             c 1 3.6 4.1 5.4 7.3 4.6 c 3.5 -0.8 6 -3.8 5 -7.8
             l -11 -42 c -3 -10.5 -10 -17 -22 -17 z"/>
  </g>

  <!-- ══ Dušš (paremal) ══ -->
  <g stroke="{WHITE}" stroke-width="7" stroke-linecap="round" fill="none">
    <!-- toru -->
    <path d="M256 62 l -24 0 c -6 0 -10 4 -10 10 l 0 8"/>
    <!-- dušipea -->
    <path d="M204 88 a 18 18 0 0 1 36 0 z" fill="{WHITE}" stroke="none"/>
    <!-- veepiisad -->
    <g stroke-width="5.5">
      <line x1="207" y1="103" x2="203" y2="119"/>
      <line x1="222" y1="103" x2="220" y2="121"/>
      <line x1="237" y1="103" x2="239" y2="119"/>
      <line x1="212" y1="130" x2="208" y2="146"/>
      <line x1="228" y1="132" x2="228" y2="148"/>
    </g>
  </g>

  <!-- Kuldne eraldusjoon -->
  <line x1="40" y1="238" x2="260" y2="238" stroke="{GOLD}" stroke-width="2.5" opacity="0.9"/>

  <!-- Tekst: WC · DUŠŠ -->
  <text x="150" y="272" text-anchor="middle"
        font-family="Helvetica, Arial, sans-serif" font-size="26" font-weight="bold"
        letter-spacing="4" fill="{WHITE}">WC · DU&#352;&#352;</text>
</svg>'''
    with open(filename, 'w') as f:
        f.write(svg)
    print(f"✓ {filename}")


build_svg("/home/user/willipu.ee/willipu_wc_sign.svg")

# PDF 150×150 mm trükiks
import cairosvg
cairosvg.svg2pdf(url="/home/user/willipu.ee/willipu_wc_sign.svg",
                 write_to="/home/user/willipu.ee/willipu_wc_sign.pdf",
                 output_width=425.2, output_height=425.2)  # 150mm punktides
print("✓ willipu_wc_sign.pdf (150×150 mm)")

# PNG eelvaade
cairosvg.svg2png(url="/home/user/willipu.ee/willipu_wc_sign.svg",
                 write_to="/home/user/willipu.ee/willipu_wc_sign.png",
                 output_width=900)
print("✓ willipu_wc_sign.png (900px)")
