import { useEffect, useRef, useMemo, useState, forwardRef } from 'react'
import { content, heroImage } from './content.js'
import { Icon } from './Icon.jsx'

export default function App() {
  const [lang, setLang] = useState(() => {
    const saved = typeof window !== 'undefined' && localStorage.getItem('willipu_lang')
    if (saved === 'et' || saved === 'en') return saved
    if (typeof navigator !== 'undefined' && navigator.language?.startsWith('et')) return 'et'
    return 'et'
  })
  const [navOpen, setNavOpen] = useState(false)
  const [scrolled, setScrolled] = useState(false)

  useEffect(() => {
    localStorage.setItem('willipu_lang', lang)
    document.documentElement.lang = lang
  }, [lang])

  useEffect(() => {
    const onScroll = () => setScrolled(window.scrollY > 40)
    onScroll()
    window.addEventListener('scroll', onScroll, { passive: true })
    return () => window.removeEventListener('scroll', onScroll)
  }, [])

  const footerRef = useRef(null)
  const t = useMemo(() => content[lang], [lang])

  useEffect(() => {
    const footer = footerRef.current
    if (!footer) return
    const update = () =>
      document.documentElement.style.setProperty('--footer-h', footer.offsetHeight + 'px')
    update()
    window.addEventListener('resize', update)
    return () => window.removeEventListener('resize', update)
  }, [])

  return (
    <>
      <Header
        t={t}
        lang={lang}
        setLang={setLang}
        scrolled={scrolled}
        navOpen={navOpen}
        setNavOpen={setNavOpen}
      />
      <main>
        <Hero t={t.hero} />
        <About t={t.about} />

        <Amenities t={t.amenities} />
        <Pricing t={t.pricing} />

        <Contact t={t.contact} />
      </main>
      <Footer t={t.footer} ref={footerRef} />
    </>
  )
}

function Header({ t, lang, setLang, scrolled, navOpen, setNavOpen }) {
  const links = [
    ['about', t.nav.about],

    ['amenities', t.nav.amenities],
    ['pricing', t.nav.pricing],

    ['contact', t.nav.contact],
  ]
  return (
    <header className={`site-header ${scrolled ? 'scrolled' : ''}`}>
      <div className="container header-row">
        <a href="#top" className="brand">
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
          <div className="lang-toggle" role="group" aria-label="Language">
            <button
              className={lang === 'et' ? 'active' : ''}
              onClick={() => setLang('et')}
              aria-pressed={lang === 'et'}
            >
              ET
            </button>
            <button
              className={lang === 'en' ? 'active' : ''}
              onClick={() => setLang('en')}
              aria-pressed={lang === 'en'}
            >
              EN
            </button>
          </div>
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

function Hero({ t }) {
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
          <a href="https://willipu.pargihaldur.ee" target="_blank" rel="noopener noreferrer" className="btn btn-primary">
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

function Lightbox({ photos, startIndex, onClose }) {
  const [idx, setIdx] = useState(startIndex)
  const prev = () => setIdx(i => (i - 1 + photos.length) % photos.length)
  const next = () => setIdx(i => (i + 1) % photos.length)

  useEffect(() => {
    const onKey = e => {
      if (e.key === 'Escape') onClose()
      if (e.key === 'ArrowLeft') prev()
      if (e.key === 'ArrowRight') next()
    }
    document.addEventListener('keydown', onKey)
    return () => document.removeEventListener('keydown', onKey)
  }, [])

  return (
    <div className="lightbox-backdrop" onClick={onClose}>
      <div className="lightbox" onClick={e => e.stopPropagation()}>
        <img src={photos[idx].url} alt={photos[idx].alt} className="lightbox-img" />
        {photos.length > 1 && (
          <>
            <button className="lightbox-arrow lightbox-prev" onClick={prev}>‹</button>
            <button className="lightbox-arrow lightbox-next" onClick={next}>›</button>
            <span className="lightbox-count">{idx + 1} / {photos.length}</span>
          </>
        )}
        <button className="lightbox-close" onClick={onClose}>✕</button>
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
                {group.photos?.length > 0 && (
                  <button
                    className="pricing-gallery-btn"
                    onClick={() => setLightbox(group.photos)}
                  >
                    📷 {group.photos.length}
                  </button>
                )}
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
                <div className="pricing-thumbs">
                  {group.photos.slice(0, 3).map((p, i) => (
                    <button key={p.url} className="pricing-thumb" onClick={() => setLightbox(group.photos)}>
                      <img src={p.url} alt={p.alt} loading="lazy" />
                    </button>
                  ))}
                  {group.photos.length > 3 && (
                    <button className="pricing-thumb pricing-thumb-more" onClick={() => setLightbox(group.photos)}>
                      +{group.photos.length - 3}
                    </button>
                  )}
                </div>
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
      </div>
      {lightbox && <Lightbox photos={lightbox} startIndex={0} onClose={() => setLightbox(null)} />}
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
            <button className="contact-item" onClick={() => setNavOpen(true)}>
              <span className="contact-item-label">Asukoht ↗</span>
              <span className="contact-item-value">{t.address}</span>
            </button>
            <div className="contact-item">
              <span className="contact-item-label">Lahtiolekuajad</span>
              <span className="contact-item-value">{t.hours}</span>
            </div>
          </div>
          <a className="btn btn-primary contact-cta" href={`mailto:${t.email}`}>
            {t.cta}
          </a>
          {t.legal && (
            <p className="contact-legal">
              Reg nr. {t.legal.reg} &nbsp;·&nbsp; KMKR (VAT) {t.legal.vat}
              <br />{t.legal.legalAddress}
            </p>
          )}
        </div>
      </div>
      {navOpen && <NavPicker address={t.address} onClose={() => setNavOpen(false)} />}
    </section>
  )
}

const Footer = forwardRef(function Footer({ t }, ref) {
  return (
    <footer className="site-footer" ref={ref}>
      <div className="container footer-row">
        <div>
          <strong>Willipu Külalistemaja</strong>
          <p>{t.tagline}</p>
        </div>
        <p className="footer-rights">
          © {new Date().getFullYear()} · {t.rights}
        </p>
      </div>
    </footer>
  )
})
