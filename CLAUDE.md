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
