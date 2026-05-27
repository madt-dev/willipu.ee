import { useEffect, useMemo, useState } from 'react'
import { content, gallery, heroImage } from './content.js'
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

  const t = useMemo(() => content[lang], [lang])

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
        <Stay t={t.stay} />
        <Amenities t={t.amenities} />
        <Pricing t={t.pricing} />
        <Gallery />
        <Contact t={t.contact} />
      </main>
      <Footer t={t.footer} />
    </>
  )
}

function Header({ t, lang, setLang, scrolled, navOpen, setNavOpen }) {
  const links = [
    ['about', t.nav.about],
    ['stay', t.nav.stay],
    ['amenities', t.nav.amenities],
    ['pricing', t.nav.pricing],
    ['gallery', t.nav.gallery],
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
          <a href="#pricing" className="btn btn-ghost">
            {t.ctaAlt} →
          </a>
        </div>
        <p className="hero-cta-note">{t.ctaNote}</p>
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

function Stay({ t }) {
  return (
    <section id="stay" className="section section-soft">
      <div className="container">
        <header className="section-head">
          <span className="eyebrow">{t.kicker}</span>
          <h2>{t.title}</h2>
        </header>
        <div className="stay-grid">
          {t.cards.map(card => (
            <article key={card.name} className="stay-card">
              <div className="stay-card-head">
                <h3>{card.name}</h3>
                <span className="price-pill">{card.price}</span>
              </div>
              <p className="stay-tag">{card.tagline}</p>
              <p className="stay-desc">{card.desc}</p>
            </article>
          ))}
        </div>
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

function Pricing({ t }) {
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
    </section>
  )
}

function Gallery() {
  return (
    <section id="gallery" className="section">
      <div className="container">
        <div className="gallery-grid">
          {gallery.map((img, i) => (
            <figure key={img.url} className={`g-${i}`}>
              <img src={img.url} alt={img.alt} loading="lazy" />
            </figure>
          ))}
        </div>
      </div>
    </section>
  )
}

function Contact({ t }) {
  return (
    <section id="contact" className="section section-dark">
      <div className="container contact-grid">
        <div>
          <span className="eyebrow light">{t.kicker}</span>
          <h2>{t.title}</h2>
        </div>
        <div className="contact-details">
          <dl>
            <div>
              <dt>Tel.</dt>
              <dd>
                <a href={`tel:${t.phone.replace(/\s/g, '')}`}>{t.phone}</a>
              </dd>
            </div>
            <div>
              <dt>Email</dt>
              <dd>
                <a href={`mailto:${t.email}`}>{t.email}</a>
              </dd>
            </div>
            <div>
              <dt>↳</dt>
              <dd>{t.address}</dd>
            </div>
            <div>
              <dt>◷</dt>
              <dd>{t.hours}</dd>
            </div>
          </dl>
          <a className="btn btn-primary" href={`mailto:${t.email}`}>
            {t.cta}
          </a>
        </div>
      </div>
    </section>
  )
}

function Footer({ t }) {
  return (
    <footer className="site-footer">
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
}
