import { useEffect, useRef, useMemo, useState } from 'react'
import { content, heroImage } from './content.js'
import { Icon } from './Icon.jsx'

const SUPPORTED = ['et', 'en', 'de', 'fi', 'lv', 'lt', 'ru']

// Languages supported by the booking system at willipu.pargihaldur.ee
const BOOKING_LANGS = new Set(['et', 'en', 'de', 'fi', 'lv', 'lt', 'ru'])
const BOOKING_BASE = 'https://willipu.pargihaldur.ee'
const bookingUrl = lang => `${BOOKING_BASE}?lang=${BOOKING_LANGS.has(lang) ? lang : 'en'}`

const COUNTRY_LANG = {
  EE: 'et', LV: 'lv', LT: 'lt', FI: 'fi',
  DE: 'de', AT: 'de', CH: 'de', LI: 'de',
  RU: 'ru', BY: 'ru',
}

const LANGS = [
  { code: 'et', label: 'Eesti' },
  { code: 'en', label: 'English' },
  { code: 'de', label: 'Deutsch' },
  { code: 'fi', label: 'Suomi' },
  { code: 'lv', label: 'Latviešu' },
  { code: 'lt', label: 'Lietuvių' },
  { code: 'ru', label: 'Русский' },
]

export default function App() {
  const [lang, setLangState] = useState(() => {
    const saved = typeof window !== 'undefined' && localStorage.getItem('willipu_lang')
    return SUPPORTED.includes(saved) ? saved : 'et'
  })
  const [navOpen, setNavOpen] = useState(false)
  const [scrolled, setScrolled] = useState(false)

  const chooseLang = (code) => {
    localStorage.setItem('willipu_lang', code)
    setLangState(code)
  }

  useEffect(() => {
    document.documentElement.lang = lang
  }, [lang])

  useEffect(() => {
    if (localStorage.getItem('willipu_lang')) return
    const ctrl = new AbortController()
    const timer = setTimeout(() => ctrl.abort(), 3000)
    fetch('https://ipapi.co/json/', { signal: ctrl.signal })
      .then(r => r.json())
      .then(({ country_code }) => {
        const detected = COUNTRY_LANG[country_code]
        if (detected) setLangState(detected)
      })
      .catch(() => {})
      .finally(() => clearTimeout(timer))
    return () => { ctrl.abort(); clearTimeout(timer) }
  }, [])

  useEffect(() => {
    const onScroll = () => setScrolled(window.scrollY > 40)
    onScroll()
    window.addEventListener('scroll', onScroll, { passive: true })
    return () => window.removeEventListener('scroll', onScroll)
  }, [])

  useEffect(() => {
    const footer = document.querySelector('.site-footer')
    if (!footer) return
    let startY = 0
    let atBottom = false
    const lerp = (a, b, t) => Math.round(a + (b - a) * t)
    const isAtBottom = () =>
      window.scrollY + window.innerHeight >= document.documentElement.scrollHeight - 5
    const onTouchStart = e => {
      startY = e.touches[0].clientY
      atBottom = isAtBottom()
    }
    const onTouchMove = e => {
      if (!atBottom) return
      const pull = Math.max(0, Math.min((startY - e.touches[0].clientY) / 110, 1))
      if (pull <= 0) { footer.style.background = ''; return }
      // interpolate from --ink #1c2620 → --accent-2 #5d8a6a
      footer.style.transition = 'none'
      footer.style.background = `rgb(${lerp(28,93,pull)},${lerp(38,138,pull)},${lerp(32,106,pull)})`
    }
    const onTouchEnd = () => {
      atBottom = false
      footer.style.transition = 'background 0.55s ease'
      footer.style.background = ''
      setTimeout(() => { footer.style.transition = '' }, 600)
    }
    document.addEventListener('touchstart', onTouchStart, { passive: true })
    document.addEventListener('touchmove', onTouchMove, { passive: true })
    document.addEventListener('touchend', onTouchEnd, { passive: true })
    return () => {
      document.removeEventListener('touchstart', onTouchStart)
      document.removeEventListener('touchmove', onTouchMove)
      document.removeEventListener('touchend', onTouchEnd)
    }
  }, [])

  const t = useMemo(() => content[lang], [lang])

  return (
    <>
      <Header
        t={t}
        lang={lang}
        chooseLang={chooseLang}
        scrolled={scrolled}
        navOpen={navOpen}
        setNavOpen={setNavOpen}
      />
      <main>
        <Hero t={t.hero} lang={lang} />
        <About t={t.about} />
        <Amenities t={t.amenities} />
        <Pricing t={t.pricing} />
        <Contact t={t.contact} />
      </main>
      <Footer t={t.footer} />
    </>
  )
}

function LangDropdown({ lang, chooseLang, scrolled }) {
  const [open, setOpen] = useState(false)
  const ref = useRef(null)

  useEffect(() => {
    const onDown = e => { if (ref.current && !ref.current.contains(e.target)) setOpen(false) }
    const onKey = e => { if (e.key === 'Escape') setOpen(false) }
    document.addEventListener('mousedown', onDown)
    document.addEventListener('keydown', onKey)
    return () => { document.removeEventListener('mousedown', onDown); document.removeEventListener('keydown', onKey) }
  }, [])

  const current = LANGS.find(l => l.code === lang)

  return (
    <div className="lang-dropdown" ref={ref}>
      <button
        className={`lang-dropdown-btn ${scrolled ? 'scrolled' : ''}`}
        onClick={() => setOpen(o => !o)}
        aria-expanded={open}
        aria-haspopup="listbox"
      >
        {current?.code.toUpperCase()}
        <svg className="lang-dropdown-chevron" viewBox="0 0 10 6" width="10" height="6" aria-hidden>
          <path d="M1 1l4 4 4-4" fill="none" stroke="currentColor" strokeWidth="1.5" strokeLinecap="round" strokeLinejoin="round"/>
        </svg>
      </button>
      {open && (
        <ul className="lang-dropdown-menu" role="listbox">
          {LANGS.map(l => (
            <li key={l.code} role="option" aria-selected={lang === l.code}>
              <button
                className={lang === l.code ? 'active' : ''}
                onClick={() => { chooseLang(l.code); setOpen(false) }}
              >
                <span className="lang-code">{l.code.toUpperCase()}</span>
                <span className="lang-name">{l.label}</span>
              </button>
            </li>
          ))}
        </ul>
      )}
    </div>
  )
}

function Header({ t, lang, chooseLang, scrolled, navOpen, setNavOpen }) {
  const links = [
    ['about', t.nav.about],
    ['amenities', t.nav.amenities],
    ['pricing', t.nav.pricing],
    ['contact', t.nav.contact],
  ]
  return (
    <header className={`site-header ${scrolled ? 'scrolled' : ''}`}>
      <div className="container header-row">
        <a href="/" className="brand" onClick={e => { e.preventDefault(); location.href = '/' }}>
          <span className="brand-mark" aria-hidden>
            <Icon name="wave" />
          </span>
          <span className="brand-text">Willipu</span>
        </a>

        <nav className={`nav ${navOpen ? 'open' : ''}`} aria-label="Main">
          {links.map(([id, label]) => (
            <a key={id} href={`#${id}`} onClick={() => setNavOpen(false)}>
              {label}
            </a>
          ))}
        </nav>

        <div className="header-actions">
          <LangDropdown lang={lang} chooseLang={chooseLang} scrolled={scrolled} />
          <button
            className="nav-toggle"
            aria-label="Toggle navigation"
            aria-expanded={navOpen}
            onClick={() => setNavOpen(o => !o)}
          >
            <span />
            <span />
            <span />
          </button>
        </div>
      </div>
    </header>
  )
}

function Hero({ t, lang }) {
  return (
    <section id="top" className="hero">
      <div
        className="hero-bg"
        style={{ backgroundImage: `url(${heroImage})` }}
        aria-hidden
      />
      <div className="hero-overlay" aria-hidden />
      <div className="container hero-inner">
        <span className="eyebrow light">{t.eyebrow}</span>
        <h1 className="hero-title">{t.title}</h1>
        <p className="hero-sub">{t.subtitle}</p>
        <div className="hero-cta">
          <a href={bookingUrl(lang)} target="_blank" rel="noopener noreferrer" className="btn btn-primary">
            {t.cta}
          </a>
          <p className="hero-cta-note">{t.ctaNote}</p>
          <a href="#pricing" className="btn btn-ghost">
            {t.ctaAlt} →
          </a>
        </div>
      </div>
      <a href="#about" className="hero-scroll" aria-label="Scroll to content">
        <span />
      </a>
    </section>
  )
}

function About({ t }) {
  return (
    <section id="about" className="section">
      <div className="container about-grid">
        <div className="about-copy">
          <span className="eyebrow">{t.kicker}</span>
          <h2>{t.title}</h2>
          <p className="lede">{t.body}</p>
        </div>
        <ul className="stats">
          {t.stats.map(s => (
            <li key={s.label}>
              <span className="stat-value">{s.value}</span>
              <span className="stat-label">{s.label}</span>
            </li>
          ))}
        </ul>
      </div>
    </section>
  )
}



function Amenities({ t }) {
  return (
    <section id="amenities" className="section">
      <div className="container">
        <header className="section-head">
          <span className="eyebrow">{t.kicker}</span>
          <h2>{t.title}</h2>
        </header>
        <div className="amenities-grid">
          {t.items.map(item => (
            <div key={item.title} className="amenity">
              <span className="amenity-icon">
                <Icon name={item.icon} />
              </span>
              <h3>{item.title}</h3>
              <p>{item.body}</p>
            </div>
          ))}
        </div>
      </div>
    </section>
  )
}

function CardCarousel({ photos, onOpenLightbox }) {
  const [idx, setIdx] = useState(0)
  const touchStartX = useRef(null)

  const prev = (e) => { e.stopPropagation(); setIdx(i => (i - 1 + photos.length) % photos.length) }
  const next = (e) => { e.stopPropagation(); setIdx(i => (i + 1) % photos.length) }

  const onTouchStart = e => { touchStartX.current = e.touches[0].clientX }
  const onTouchEnd = e => {
    if (touchStartX.current === null) return
    const dx = e.changedTouches[0].clientX - touchStartX.current
    if (Math.abs(dx) > 40) dx < 0 ? setIdx(i => (i + 1) % photos.length) : setIdx(i => (i - 1 + photos.length) % photos.length)
    touchStartX.current = null
  }

  return (
    <div className="card-carousel" onTouchStart={onTouchStart} onTouchEnd={onTouchEnd}>
      <button className="card-carousel-img-btn" onClick={() => onOpenLightbox(idx)} aria-label="View photo">
        <img src={photos[idx].url} alt={photos[idx].alt} className="card-carousel-img" loading="lazy" />
      </button>
      {photos.length > 1 && (
        <>
          <button className="card-carousel-arrow card-carousel-prev" onClick={prev} aria-label="Previous">‹</button>
          <button className="card-carousel-arrow card-carousel-next" onClick={next} aria-label="Next">›</button>
          <div className="card-carousel-dots">
            {photos.map((_, i) => (
              <button
                key={i}
                className={`card-carousel-dot ${i === idx ? 'active' : ''}`}
                onClick={e => { e.stopPropagation(); setIdx(i) }}
                aria-label={`Photo ${i + 1}`}
              />
            ))}
          </div>
        </>
      )}
    </div>
  )
}

function Lightbox({ photos, startIndex, onClose }) {
  const [idx, setIdx] = useState(startIndex)
  const [swipeHint, setSwipeHint] = useState(photos.length > 1)
  const [swipeHintKey, setSwipeHintKey] = useState(0)
  const triggerHint = () => {
    if (photos.length <= 1) return
    setSwipeHintKey(k => k + 1)
    setSwipeHint(true)
  }
  const prev = () => setIdx(i => (i - 1 + photos.length) % photos.length)
  const next = () => setIdx(i => (i + 1) % photos.length)
  const touchStartX = useRef(null)
  const onTouchStart = e => { touchStartX.current = e.touches[0].clientX }
  const onTouchEnd = e => {
    if (touchStartX.current === null) return
    const dx = e.changedTouches[0].clientX - touchStartX.current
    if (Math.abs(dx) > 40) dx < 0 ? next() : prev()
    touchStartX.current = null
  }

  useEffect(() => {
    const onKey = e => {
      if (e.key === 'Escape') onClose()
      if (e.key === 'ArrowLeft') prev()
      if (e.key === 'ArrowRight') next()
    }
    document.addEventListener('keydown', onKey)

    // Push a history entry so mobile back button closes the lightbox instead of leaving the page
    history.pushState({ lightbox: true }, '')
    let closedByBack = false
    const onPopState = () => { closedByBack = true; onClose() }
    window.addEventListener('popstate', onPopState)

    return () => {
      document.removeEventListener('keydown', onKey)
      window.removeEventListener('popstate', onPopState)
      if (!closedByBack && history.state?.lightbox) history.back()
    }
  }, [])

  return (
    <div className="lightbox-backdrop" onClick={onClose}>
      <div className="lightbox" onClick={e => e.stopPropagation()} onTouchStart={onTouchStart} onTouchEnd={onTouchEnd}>
        <img src={photos[idx].url} alt={photos[idx].alt} className="lightbox-img" onClick={triggerHint} />
        {photos.length > 1 && (
          <>
            <button className="lightbox-arrow lightbox-prev" onClick={prev}>‹</button>
            <button className="lightbox-arrow lightbox-next" onClick={next}>›</button>
            <span className="lightbox-count">{idx + 1} / {photos.length}</span>
          </>
        )}
        {swipeHint && (
          <div key={swipeHintKey} className="lightbox-swipe-hint" onAnimationEnd={() => setSwipeHint(false)}>
            <svg className="lightbox-swipe-icon" viewBox="0 0 48 22" width="48" height="22" fill="none" aria-hidden>
              <path d="M13 11H3M3 11l5-4M3 11l5 4" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"/>
              <circle cx="24" cy="11" r="5.5" fill="currentColor" opacity="0.85"/>
              <path d="M35 11h10M45 11l-5-4M45 11l-5 4" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"/>
            </svg>
            <span>swipe</span>
          </div>
        )}
        <button className="lightbox-close" onClick={onClose} aria-label="Close">
          <svg viewBox="0 0 14 14" width="16" height="16" aria-hidden>
            <path d="M1 1l12 12M13 1L1 13" stroke="currentColor" strokeWidth="2" strokeLinecap="round"/>
          </svg>
        </button>
      </div>
    </div>
  )
}

function Pricing({ t }) {
  const [lightbox, setLightbox] = useState(null)

  return (
    <section id="pricing" className="section section-soft">
      <div className="container">
        <header className="section-head">
          <span className="eyebrow">{t.kicker}</span>
          <h2>{t.title}</h2>
        </header>
        <div className="pricing-grid">
          {t.groups.map(group => (
            <div key={group.label} className="pricing-group">
              <div className="pricing-group-header">
                <span className="pricing-group-icon">{group.icon}</span>
                <h3 className="pricing-group-title">{group.label}</h3>
              </div>
              {group.amenities && (
                <ul className="amenity-badges">
                  {group.amenities.map(a => (
                    <li key={a.icon} title={a.tooltip || a.label}>
                      <Icon name={a.icon} />
                      <span>{a.label}</span>
                    </li>
                  ))}
                </ul>
              )}
              {group.photos?.length > 0 && (
                <CardCarousel
                  photos={group.photos}
                  onOpenLightbox={startIndex => setLightbox({ photos: group.photos, startIndex })}
                />
              )}
              <ul className="price-list">
                {group.rows.map(row => (
                  <li key={row.item}>
                    <div className="price-item-wrap">
                      <span className="price-item">{row.item}</span>
                      {row.note && <span className="price-note-inline">{row.note}</span>}
                    </div>
                    <span className="price-value">{row.price}</span>
                  </li>
                ))}
              </ul>
            </div>
          ))}
        </div>
        <p className="price-note-global">{t.note}</p>
        <div className="price-download-wrap">
          <a href="/hinnakiri.xlsx" download className="price-download-link">
            <svg viewBox="0 0 20 20" width="16" height="16" fill="none" aria-hidden>
              <path d="M10 2v10M6 8l4 4 4-4" stroke="currentColor" strokeWidth="1.8" strokeLinecap="round" strokeLinejoin="round"/>
              <path d="M3 14v2a1 1 0 001 1h12a1 1 0 001-1v-2" stroke="currentColor" strokeWidth="1.8" strokeLinecap="round"/>
            </svg>
            {t.downloadLabel}
          </a>
        </div>
      </div>
      {lightbox && (
        <Lightbox
          photos={lightbox.photos}
          startIndex={lightbox.startIndex}
          onClose={() => setLightbox(null)}
        />
      )}
    </section>
  )
}


const NAV_APPS = [
  { name: 'Google Maps', url: 'https://www.google.com/maps/search/?api=1&query=58.64483549867105,27.166508285762042' },
  { name: 'Waze',        url: 'https://waze.com/ul?ll=58.64483549867105,27.166508285762042&navigate=yes' },
  { name: 'Apple Maps',  url: 'https://maps.apple.com/?q=58.64483549867105,27.166508285762042' },
  { name: 'HERE Maps',   url: 'https://share.here.com/l/58.64483549867105,27.166508285762042' },
]

function NavPicker({ address, onClose }) {
  const ref = useRef(null)
  useEffect(() => {
    function onKey(e) { if (e.key === 'Escape') onClose() }
    function onClick(e) { if (ref.current && !ref.current.contains(e.target)) onClose() }
    document.addEventListener('keydown', onKey)
    document.addEventListener('mousedown', onClick)
    return () => { document.removeEventListener('keydown', onKey); document.removeEventListener('mousedown', onClick) }
  }, [onClose])
  return (
    <div className="nav-picker-backdrop" aria-modal role="dialog">
      <div className="nav-picker" ref={ref}>
        <p className="nav-picker-address">{address}</p>
        <ul className="nav-picker-list">
          {NAV_APPS.map(app => (
            <li key={app.name}>
              <a href={app.url} target="_blank" rel="noopener noreferrer" onClick={onClose}>
                {app.name}
              </a>
            </li>
          ))}
        </ul>
        <button className="nav-picker-close" onClick={onClose}>✕</button>
      </div>
    </div>
  )
}

function Contact({ t }) {
  const ref = useRef(null)
  const [navOpen, setNavOpen] = useState(false)

  useEffect(() => {
    const el = ref.current
    if (!el) return
    const obs = new IntersectionObserver(
      ([entry]) => { if (entry.isIntersecting) { el.classList.add('in-view'); obs.disconnect() } },
      { threshold: 0.12 }
    )
    obs.observe(el)
    return () => obs.disconnect()
  }, [])

  return (
    <section id="contact" className="section section-dark">
      <div className="container">
        <div className="contact-wrap" ref={ref}>
          <div className="contact-head">
            <span className="eyebrow light">{t.kicker}</span>
            <h2>{t.title}</h2>
          </div>
          <div className="contact-items">
            <a href={`tel:${t.phone.replace(/\s/g, '')}`} className="contact-item">
              <span className="contact-item-label">Tel</span>
              <span className="contact-item-value">{t.phone}</span>
            </a>
            <a href={`mailto:${t.email}`} className="contact-item">
              <span className="contact-item-label">Email</span>
              <span className="contact-item-value">{t.email}</span>
            </a>
            <button className="contact-item contact-item-nav" onClick={() => setNavOpen(true)}>
              <span className="contact-item-label">{t.locationLabel}</span>
              <span className="contact-item-value">
                {t.address}
                <span className="contact-nav-icon" aria-hidden>
                  <Icon name="location" />
                </span>
              </span>
            </button>
            <div className="contact-item">
              <span className="contact-item-label">{t.hoursLabel}</span>
              <span className="contact-item-value">{t.hours}</span>
            </div>
          </div>
          <a className="btn btn-primary contact-cta" href={`mailto:${t.email}`}>
            {t.cta}
          </a>
          {t.legal && (
            <p className="contact-legal">
              {t.legal.companyName}<br />
              Reg nr. {t.legal.reg} &nbsp;·&nbsp; KMKR (VAT) {t.legal.vat}
              <br />{t.legal.legalAddress}
              <br />{t.legal.bankLabel}: {t.legal.iban} &nbsp;·&nbsp; {t.legal.bank} &nbsp;·&nbsp; SWIFT: {t.legal.swift}
            </p>
          )}
        </div>
      </div>
      {navOpen && <NavPicker address={t.address} onClose={() => setNavOpen(false)} />}
    </section>
  )
}

function Footer({ t }) {
  return (
    <footer className="site-footer">
      <div className="container footer-row">
        <span><strong>Willipu</strong> · {t.tagline}</span>
        <span>© {new Date().getFullYear()} · {t.rights}</span>
      </div>
    </footer>
  )
}
