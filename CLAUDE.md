# CLAUDE.md

Guidance for Claude Code when working in this repository.

## Git workflow

- **Always commit and push directly to the `main` branch.** The owner has
  explicitly requested this — do not create feature branches or pull
  requests unless asked.
- Commit messages are written in Estonian (see `git log` for style).

## Project overview

willipu.ee — website for Willipu Külalistemaja ja Karavanipark (guesthouse
and caravan park on Lake Peipus, Pusi küla, Tartumaa, Estonia).

- Single-page React app built with Vite (`npm run build`, output in `dist/`).
- All user-facing text lives in `src/content.js`, translated into 7
  languages: et (default), en, de, fi, lv, lt, ru. Any copy change must be
  applied to all languages, including the per-language `seo` block
  (title/description).
- `src/App.jsx` updates `document.title` and the description/og/twitter
  meta tags from `content[lang].seo` on language switch.
- SEO essentials (meta tags, keywords, schema.org JSON-LD with
  Campground/RVPark types) are in `index.html` — keep caravan-parking
  keywords when editing.
- Static assets, `robots.txt` and `sitemap.xml` are in `public/` — bump the
  sitemap `lastmod` when content changes.
- Caravan park bookings go through https://willipu.pargihaldur.ee; rooms
  and cottages are booked by email.

## QR manual pages (`/juhend/`)

- Standalone multilingual manual/info pages live in
  `public/juhend/<slug>/index.html`. They are reachable only by direct URL
  (QR-code stickers on-site), are NOT linked from the main site, and carry
  `noindex, nofollow` — keep them out of the sitemap.
- To add a new manual: copy `public/juhend/pesumasin/index.html`, edit the
  `T` translations object (all 7 languages), and add a card link to the
  list in `public/juhend/index.html`.
- Generate the QR code + print-ready sticker (120x120 mm, 300 dpi):
  `python3 make_qr_kleebis.py <slug> "<Estonian title>" "<Estonian subtitle>" "<English line>"`.

## Marketing materials page (`/turundus/`)

- `public/turundus/index.html` is a hidden download page (noindex, not
  linked from the site) listing all logos, banners, Facebook ads and QR
  stickers. Share by direct URL only.
- Generated assets live in the repo root (script outputs); the copies
  served for download live in `public/turundus/`. All PDFs are written
  through `pdf_compat.py` (PDF 1.4, classic xref) — cairosvg's default
  PDF 1.7 output fails to open in CorelDRAW and Photoshop. When a new asset is
  generated, copy it there and add a row to the page.
