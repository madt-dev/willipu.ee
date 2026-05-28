export const content = {
  et: {
    nav: {
      about: 'Meist',
      stay: 'Majutus',
      amenities: 'Tegevused',
      pricing: 'Hinnakiri',
      gallery: 'Galerii',
      contact: 'Kontakt',
    },
    hero: {
      eyebrow: 'Peipsi järve kaldal',
      title: 'Willipu külalisemaja ja karavanipark',
      subtitle:
        'Vaikne paik vee ääres — kohtumiseks, puhkuseks ja peoks. Tartumaal, Pusi külas.',
      cta: 'Broneeri ööbimine karavanipargis',
      ctaAlt: 'Vaata hindu',
      ctaNote: 'Tubade ja kämpingute broneerimine emaili teel.',
    },
    about: {
      kicker: 'Tere tulemast',
      title: 'Üle 20 aasta kogemusi',
      body:
        'Willipu asub Tartumaal, Alatskivi vallas, Pusi külas, otse Peipsi järve kaldal. Lähim linn Kallaste jääb 2 km kaugusele, Tartu 50 km ja Tallinn 200 km kaugusele. Pakume majutust nii peamajas kui ka suvemajakestes, ruumi pidudeks ja koolitusteks ning kohta haagissuvilatele.',
      stats: [
        { value: '10', label: 'kohta peamajas' },
        { value: '30', label: 'kohta peosaalis' },
        { value: '41', label: 'haagissuvila kohta' },
        { value: '2 km', label: 'Kallaste linna' },
        { value: '16', label: 'kohta kämpingutes' },
        { value: 'kuni 5', label: 'lisakohta' },
        { value: '🏖', label: 'lapsesõbralik liivarand' },
        { value: '🌿', label: 'suur muruplats väliürituste korraldamiseks' },
      ],
    },
    stay: {
      kicker: 'Majutus',
      title: 'Vali endale sobiv variant',
      cards: [
        {
          name: 'Peamaja',
          tagline: '2–3 inimese toad, kuni 10 külalist',
          desc:
            'Kolmes toas on TV, WiFi, dušš ja WC. Ühel toal on dušš ja WC koridoris. Esimesel korrusel asub peosaal kuni 30 inimesele.',
          price: 'al. 25 € / inimene',
        },
        {
          name: 'Pereaiamaja',
          tagline: '5 magamiskohta, köök, dušš, WC',
          desc:
            'Kaks tuba, WC, dušš ja köök. Konditsioneer. Sobib perele või väiksele seltskonnale.',
          price: '110 € / öö',
        },
        {
          name: 'Väike aiamaja',
          tagline: '2 magamiskohta, soojustatud',
          desc:
            'Talvel kasutatav, sooja vee ja WC-ga. Mõnus paaridele või paigaks, kui peamaja täis.',
          price: '40 € / öö',
        },
        {
          name: 'Karavani park',
          tagline: 'Elekter, vesi, duššid, WC',
          desc:
            'Kuni 41 haagissuvilakohta. Elektri-, vee- ja kanalisatsiooniühendused. Telkimine lubatud.',
          price: 'al. 14 € / öö',
        },
      ],
    },
    amenities: {
      kicker: 'Mida teha',
      title: 'Tegevused vee ääres',
      items: [
        { icon: 'wave', title: 'Ujumine ja surf', body: 'Liivane rand, sobib ka surfaritele.' },
        { icon: 'ball', title: 'Võrkpall ja mängud', body: 'Õueplatsid ja vabad muruväljakud.' },
        { icon: 'fire', title: 'Lõke ja saun', body: 'Lõkkeplats ning saun seltskonnale.' },
        { icon: 'hall', title: 'Peosaal kuni 30', body: 'Konverentsid, peod, koolitused.' },
        { icon: 'wifi', title: 'WiFi terves majas', body: 'Tasuta levi peamajas.' },
      ],
    },
    pricing: {
      kicker: 'Hinnakiri',
      title: 'Soodsad hinnad, kõigi mugavustega',
      note:
        'Broneeringu kinnitamiseks tasutakse 50% ettemaksuna. Tühistamisel alla 14 päeva ettemaks ei tagastata.',
      groups: [
        {
          label: 'Suur kämpingumaja',
          icon: '🏡',
          photos: [
            { url: 'https://images.unsplash.com/photo-1518780664697-55e3ad937233?w=1200&q=80', alt: 'Suur kämpingumaja' },
            { url: 'https://images.unsplash.com/photo-1499696010180-025ef6e1a8f9?w=1200&q=80', alt: 'Sisevaade' },
          ],
          amenities: [
            { icon: 'wc', label: 'WC' },
            { icon: 'shower', label: 'Dušš' },
            { icon: 'wifi', label: 'WiFi' },
            { icon: 'kitchen', label: 'Köök' },
            { icon: 'grill', label: 'Grill' },
          ],
          rows: [
            { item: '5 inimesele', price: '110 € / öö' },
            { item: '4 inimesele', price: '100 € / öö' },
            { item: '2–3 inimesele', price: '85 € / öö' },
          ],
        },
        {
          label: 'Väike kämpingumaja',
          icon: '🛖',
          photos: [
            { url: 'https://images.unsplash.com/photo-1518780664697-55e3ad937233?w=1200&q=80', alt: 'Väike kämpingumaja' },
            { url: 'https://images.unsplash.com/photo-1464822759023-fed622ff2c3b?w=1200&q=80', alt: 'Ümbrus' },
          ],
          amenities: [
            { icon: 'wc', label: 'WC' },
            { icon: 'wifi', label: 'WiFi' },
            { icon: 'grill', label: 'Grill' },
          ],
          rows: [
            { item: '2 inimesele', price: '55 € / öö' },
            { item: '1 inimesele', price: '35 € / öö' },
          ],
        },
        {
          label: 'Kahene tuba',
          icon: '🛏',
          photos: [
            { url: 'https://images.unsplash.com/photo-1499696010180-025ef6e1a8f9?w=1200&q=80', alt: 'Kahene tuba' },
            { url: 'https://images.unsplash.com/photo-1500530855697-b586d89ba3ee?w=1200&q=80', alt: 'Vaade järvele' },
          ],
          amenities: [
            { icon: 'wc', label: 'WC' },
            { icon: 'shower', label: 'Dušš' },
            { icon: 'wifi', label: 'WiFi' },
            { icon: 'kitchen', label: 'Ühine köök' },
            { icon: 'grill', label: 'Grill' },
          ],
          rows: [
            { item: '2 inimesele', price: '55 € / öö' },
            { item: '1 inimesele', price: '35 € / öö' },
          ],
        },
        {
          label: 'Kolmene tuba',
          icon: '🛏',
          photos: [
            { url: 'https://images.unsplash.com/photo-1499696010180-025ef6e1a8f9?w=1200&q=80', alt: 'Kolmene tuba' },
            { url: 'https://images.unsplash.com/photo-1505765050516-f72dcac9c60e?w=1200&q=80', alt: 'Rand' },
          ],
          amenities: [
            { icon: 'wc', label: 'WC' },
            { icon: 'shower', label: 'Dušš' },
            { icon: 'wifi', label: 'WiFi' },
            { icon: 'kitchen', label: 'Ühine köök' },
            { icon: 'grill', label: 'Grill' },
          ],
          rows: [
            { item: '3 inimesele', price: '80 € / öö' },
            { item: '2 inimesele', price: '60 € / öö' },
          ],
        },
        {
          label: 'Karavanipark',
          icon: '🚐',
          photos: [
            { url: 'https://images.unsplash.com/photo-1500530855697-b586d89ba3ee?w=1200&q=80', alt: 'Järv' },
            { url: 'https://images.unsplash.com/photo-1470770841072-f978cf4d019e?w=1200&q=80', alt: 'Männimets vee ääres' },
            { url: 'https://images.unsplash.com/photo-1505765050516-f72dcac9c60e?w=1200&q=80', alt: 'Rand kuldsel tunnil' },
          ],
          amenities: [
            { icon: 'checkin', label: 'Check-in 24/7', tooltip: 'Iseteeninduslik check-in' },
            { icon: 'electric', label: 'Elekter' },
            { icon: 'shower', label: 'Dušš' },
            { icon: 'wifi', label: 'WiFi' },
            { icon: 'water', label: 'Puhas vesi' },
            { icon: 'dump', label: 'Purgimine' },
            { icon: 'chemical', label: 'Keemiline WC' },
            { icon: 'kitchen', label: 'Köök' },
            { icon: 'washer', label: 'Pesumasin' },
            { icon: 'trash', label: 'Prügi äraandmine' },
            { icon: 'pets', label: 'Lemmikloomad lubatud' },
          ],
          rows: [
            { item: 'Haagissuvila ilma elektrita', price: '20 € / öö', note: 'sisaldab 2 inimest' },
            { item: 'Haagissuvila elektriga', price: '25 € / öö', note: 'sisaldab 2 inimest' },
            { item: 'Telkimine', price: '7 € / inimene' },
            { item: 'Lisa inimene', price: '3 € / inimene' },
          ],
        },
        {
          label: 'Muud',
          icon: '❄️',
          rows: [
            { item: 'Talvine järvetransport', price: 'küsi hinda' },
          ],
        },
      ],
    },
    contact: {
      kicker: 'Kontakt',
      title: 'Tule külla või võta ühendust',
      address: 'Pusi küla, Alatskivi vald, Tartumaa',
      mapUrl: 'https://www.google.com/maps/search/?api=1&query=58.64483549867105,27.166508285762042',
      locationLabel: 'Asukoht',
      hoursLabel: 'Lahtiolekuajad',
      hours: 'Avatud aastaringselt',
      phone: '+372 56 955 758',
      email: 'willipu.willipu@gmail.com',
      cta: 'Saada e-kiri',
      legal: {
        reg: '10972974',
        vat: 'EE100878462',
        legalAddress: 'Villipu, Pusi küla, 60217 Peipsiääre vald, Tartu maakond',
      },
    },
    footer: {
      tagline: 'Peipsi järve ääres alates 2010.',
      rights: 'Kõik õigused kaitstud',
    },
  },
  en: {
    nav: {
      about: 'About',
      stay: 'Stay',
      amenities: 'Activities',
      pricing: 'Pricing',
      gallery: 'Gallery',
      contact: 'Contact',
    },
    hero: {
      eyebrow: 'On the shore of Lake Peipus',
      title: 'Willipu Guesthouse and Caravan Park',
      subtitle:
        'A quiet place by the water — for gatherings, getaways and good food. In Pusi village, southern Estonia.',
      cta: 'Book a stay at the caravan park',
      ctaAlt: 'See pricing',
      ctaNote: 'Room and cottage bookings by email.',
    },
    about: {
      kicker: 'Welcome',
      title: 'Over 20 years of experience',
      body:
        'Willipu sits in Tartu county, Alatskivi commune, Pusi village — right on the shore of Lake Peipus. The nearest town Kallaste is 2 km away, Tartu is 50 km, Tallinn 200 km. We offer rooms in the main house, summer cottages, a banquet hall for events and a full caravan park.',
      stats: [
        { value: '10', label: 'beds in main house' },
        { value: '30', label: 'seats in banquet hall' },
        { value: '41', label: 'caravan spots' },
        { value: '2 km', label: 'to Kallaste' },
        { value: '16', label: 'beds in cottages' },
        { value: 'up to 5', label: 'extra beds' },
        { value: '🏖', label: 'child-friendly sandy beach' },
        { value: '🌿', label: 'large lawn for outdoor events' },
      ],
    },
    stay: {
      kicker: 'Stay',
      title: 'Find the right place to sleep',
      cards: [
        {
          name: 'Main house',
          tagline: 'Rooms for 2–3, up to 10 guests',
          desc:
            'Three rooms have TV, WiFi, shower and toilet. One room has shower and toilet in the hall. The ground floor holds our banquet hall for up to 30 people.',
          price: 'from €25 / person',
        },
        {
          name: 'Family cottage',
          tagline: '5 beds, kitchen, shower, toilet',
          desc:
            'Two bedrooms, full bathroom and kitchen. Air conditioning. Comfortable for a family or small group.',
          price: '€110 / night',
        },
        {
          name: 'Small cottage',
          tagline: '2 beds, heated, year-round',
          desc:
            'Insulated for winter use, with hot water and toilet. A cosy spot for couples or overflow guests.',
          price: '€40 / night',
        },
        {
          name: 'Caravan park',
          tagline: 'Power, water, showers, WC',
          desc:
            'Up to 41 caravan spots with electric, water and sewage hookups. Tent camping welcome.',
          price: 'from €14 / night',
        },
      ],
    },
    amenities: {
      kicker: 'Things to do',
      title: 'Life by the lake',
      items: [
        { icon: 'wave', title: 'Swim and surf', body: 'Sandy beach, also great for windsurfers.' },
        { icon: 'ball', title: 'Volleyball and games', body: 'Outdoor courts and open lawns.' },
        { icon: 'fire', title: 'Bonfire and sauna', body: 'Fire pit and sauna for groups.' },
        { icon: 'hall', title: 'Banquet hall for 30', body: 'Conferences, parties, trainings.' },
        { icon: 'wifi', title: 'WiFi throughout', body: 'Free coverage in the main house.' },
      ],
    },
    pricing: {
      kicker: 'Pricing',
      title: 'Affordable prices, all comforts included',
      note:
        'A 50% deposit confirms your booking. Cancellations within 14 days of arrival forfeit the deposit.',
      groups: [
        {
          label: 'Large Camping Cottage',
          icon: '🏡',
          amenities: [
            { icon: 'wc', label: 'WC' },
            { icon: 'shower', label: 'Shower' },
            { icon: 'wifi', label: 'WiFi' },
            { icon: 'kitchen', label: 'Kitchen' },
            { icon: 'grill', label: 'BBQ' },
          ],
          rows: [
            { item: '5 persons', price: '€110 / night' },
            { item: '4 persons', price: '€100 / night' },
            { item: '2–3 persons', price: '€85 / night' },
          ],
        },
        {
          label: 'Small Camping Cottage',
          icon: '🛖',
          amenities: [
            { icon: 'wc', label: 'WC' },
            { icon: 'wifi', label: 'WiFi' },
            { icon: 'grill', label: 'BBQ' },
          ],
          rows: [
            { item: '2 persons', price: '€55 / night' },
            { item: '1 person', price: '€35 / night' },
          ],
        },
        {
          label: 'Double Room',
          icon: '🛏',
          amenities: [
            { icon: 'wc', label: 'WC' },
            { icon: 'shower', label: 'Shower' },
            { icon: 'wifi', label: 'WiFi' },
            { icon: 'kitchen', label: 'Shared kitchen' },
            { icon: 'grill', label: 'BBQ' },
          ],
          rows: [
            { item: '2 persons', price: '€55 / night' },
            { item: '1 person', price: '€35 / night' },
          ],
        },
        {
          label: 'Triple Room',
          icon: '🛏',
          amenities: [
            { icon: 'wc', label: 'WC' },
            { icon: 'shower', label: 'Shower' },
            { icon: 'wifi', label: 'WiFi' },
            { icon: 'kitchen', label: 'Shared kitchen' },
            { icon: 'grill', label: 'BBQ' },
          ],
          rows: [
            { item: '3 persons', price: '€80 / night' },
            { item: '2 persons', price: '€60 / night' },
          ],
        },
        {
          label: 'Caravan Park',
          icon: '🚐',
          amenities: [
            { icon: 'checkin', label: 'Check-in 24/7', tooltip: 'Self-service check-in' },
            { icon: 'electric', label: 'Electric' },
            { icon: 'shower', label: 'Shower' },
            { icon: 'wifi', label: 'WiFi' },
            { icon: 'water', label: 'Fresh water' },
            { icon: 'dump', label: 'Waste dump' },
            { icon: 'chemical', label: 'Chemical WC' },
            { icon: 'kitchen', label: 'Kitchen' },
            { icon: 'washer', label: 'Washer' },
            { icon: 'trash', label: 'Waste disposal' },
            { icon: 'pets', label: 'Pets welcome' },
          ],
          rows: [
            { item: 'Caravan without power', price: '€20 / night', note: 'includes 2 persons' },
            { item: 'Caravan with power', price: '€25 / night', note: 'includes 2 persons' },
            { item: 'Tent camping', price: '€7 / person' },
            { item: 'Extra person', price: '€3 / person' },
          ],
        },
        {
          label: 'Other',
          icon: '❄️',
          rows: [
            { item: 'Winter lake transport', price: 'ask for price' },
          ],
        },
      ],
    },
    contact: {
      kicker: 'Contact',
      title: 'Come visit or get in touch',
      address: 'Pusi village, Alatskivi parish, Tartu county',
      mapUrl: 'https://www.google.com/maps/search/?api=1&query=58.64483549867105,27.166508285762042',
      locationLabel: 'Location',
      hoursLabel: 'Opening hours',
      hours: 'Open year-round',
      phone: '+372 56 955 758',
      email: 'willipu.willipu@gmail.com',
      cta: 'Send an email',
      legal: {
        reg: '10972974',
        vat: 'EE100878462',
        legalAddress: 'Villipu, Pusi küla, 60217 Peipsiääre vald, Tartu maakond',
      },
    },
    footer: {
      tagline: 'On Lake Peipus since 2010.',
      rights: 'All rights reserved',
    },
  },
  de: {
    nav: {
      about: 'Über uns',
      stay: 'Unterkunft',
      amenities: 'Aktivitäten',
      pricing: 'Preise',
      gallery: 'Galerie',
      contact: 'Kontakt',
    },
    hero: {
      eyebrow: 'Am Ufer des Peipussees',
      title: 'Willipu Gästehaus und Campingpark',
      subtitle: 'Ein ruhiger Ort am Wasser — zum Treffen, Erholen und Feiern. Im Dorf Pusi, Südestland.',
      cta: 'Stellplatz im Campingpark buchen',
      ctaAlt: 'Preise ansehen',
      ctaNote: 'Zimmer- und Hüttenbuchungen per E-Mail.',
    },
    about: {
      kicker: 'Willkommen',
      title: 'Über 20 Jahre Erfahrung',
      body: 'Willipu liegt im Kreis Tartu, Gemeinde Alatskivi, Dorf Pusi — direkt am Ufer des Peipussees. Die nächste Stadt Kallaste ist 2 km entfernt, Tartu 50 km und Tallinn 200 km. Wir bieten Zimmer im Haupthaus, Sommerhütten, einen Festsaal für Veranstaltungen und einen vollständigen Campingpark.',
      stats: [
        { value: '10', label: 'Betten im Haupthaus' },
        { value: '30', label: 'Plätze im Festsaal' },
        { value: '41', label: 'Campingstellplätze' },
        { value: '2 km', label: 'bis Kallaste' },
        { value: '16', label: 'Betten in Hütten' },
        { value: 'bis 5', label: 'Zusatzbetten' },
        { value: '🏖', label: 'kinderfreundlicher Sandstrand' },
        { value: '🌿', label: 'großer Rasen für Freiluftveranstaltungen' },
      ],
    },
    amenities: {
      kicker: 'Aktivitäten',
      title: 'Freizeitangebote am See',
      items: [
        { icon: 'wave', title: 'Schwimmen und Surfen', body: 'Sandstrand, ideal auch für Windsurfer.' },
        { icon: 'ball', title: 'Volleyball und Spiele', body: 'Außenplätze und offene Rasenflächen.' },
        { icon: 'fire', title: 'Lagerfeuer und Sauna', body: 'Feuerstelle und Sauna für Gruppen.' },
        { icon: 'hall', title: 'Festsaal für 30', body: 'Konferenzen, Feiern, Schulungen.' },
        { icon: 'wifi', title: 'WiFi überall', body: 'Kostenloses WLAN im Haupthaus.' },
      ],
    },
    pricing: {
      kicker: 'Preise',
      title: 'Günstige Preise, alle Annehmlichkeiten inklusive',
      note: 'Eine Anzahlung von 50 % bestätigt Ihre Buchung. Bei Stornierung innerhalb von 14 Tagen vor Anreise verfällt die Anzahlung.',
      groups: [
        {
          label: 'Großes Campinghaus',
          icon: '🏡',
          photos: [
            { url: 'https://images.unsplash.com/photo-1518780664697-55e3ad937233?w=1200&q=80', alt: 'Großes Campinghaus' },
            { url: 'https://images.unsplash.com/photo-1499696010180-025ef6e1a8f9?w=1200&q=80', alt: 'Innenansicht' },
          ],
          amenities: [
            { icon: 'wc', label: 'WC' },
            { icon: 'shower', label: 'Dusche' },
            { icon: 'wifi', label: 'WiFi' },
            { icon: 'kitchen', label: 'Küche' },
            { icon: 'grill', label: 'Grill' },
          ],
          rows: [
            { item: '5 Personen', price: '110 € / Nacht' },
            { item: '4 Personen', price: '100 € / Nacht' },
            { item: '2–3 Personen', price: '85 € / Nacht' },
          ],
        },
        {
          label: 'Kleines Campinghaus',
          icon: '🛖',
          photos: [
            { url: 'https://images.unsplash.com/photo-1518780664697-55e3ad937233?w=1200&q=80', alt: 'Kleines Campinghaus' },
            { url: 'https://images.unsplash.com/photo-1464822759023-fed622ff2c3b?w=1200&q=80', alt: 'Umgebung' },
          ],
          amenities: [
            { icon: 'wc', label: 'WC' },
            { icon: 'wifi', label: 'WiFi' },
            { icon: 'grill', label: 'Grill' },
          ],
          rows: [
            { item: '2 Personen', price: '55 € / Nacht' },
            { item: '1 Person', price: '35 € / Nacht' },
          ],
        },
        {
          label: 'Doppelzimmer',
          icon: '🛏',
          photos: [
            { url: 'https://images.unsplash.com/photo-1499696010180-025ef6e1a8f9?w=1200&q=80', alt: 'Doppelzimmer' },
            { url: 'https://images.unsplash.com/photo-1500530855697-b586d89ba3ee?w=1200&q=80', alt: 'Blick auf den See' },
          ],
          amenities: [
            { icon: 'wc', label: 'WC' },
            { icon: 'shower', label: 'Dusche' },
            { icon: 'wifi', label: 'WiFi' },
            { icon: 'kitchen', label: 'Gemeinschaftsküche' },
            { icon: 'grill', label: 'Grill' },
          ],
          rows: [
            { item: '2 Personen', price: '55 € / Nacht' },
            { item: '1 Person', price: '35 € / Nacht' },
          ],
        },
        {
          label: 'Dreibettzimmer',
          icon: '🛏',
          photos: [
            { url: 'https://images.unsplash.com/photo-1499696010180-025ef6e1a8f9?w=1200&q=80', alt: 'Dreibettzimmer' },
            { url: 'https://images.unsplash.com/photo-1505765050516-f72dcac9c60e?w=1200&q=80', alt: 'Strand' },
          ],
          amenities: [
            { icon: 'wc', label: 'WC' },
            { icon: 'shower', label: 'Dusche' },
            { icon: 'wifi', label: 'WiFi' },
            { icon: 'kitchen', label: 'Gemeinschaftsküche' },
            { icon: 'grill', label: 'Grill' },
          ],
          rows: [
            { item: '3 Personen', price: '80 € / Nacht' },
            { item: '2 Personen', price: '60 € / Nacht' },
          ],
        },
        {
          label: 'Campingpark',
          icon: '🚐',
          photos: [
            { url: 'https://images.unsplash.com/photo-1500530855697-b586d89ba3ee?w=1200&q=80', alt: 'See' },
            { url: 'https://images.unsplash.com/photo-1470770841072-f978cf4d019e?w=1200&q=80', alt: 'Kiefernwald am Wasser' },
            { url: 'https://images.unsplash.com/photo-1505765050516-f72dcac9c60e?w=1200&q=80', alt: 'Strand in der goldenen Stunde' },
          ],
          amenities: [
            { icon: 'checkin', label: 'Check-in 24/7', tooltip: 'Selbstbedienung Check-in' },
            { icon: 'electric', label: 'Strom' },
            { icon: 'shower', label: 'Dusche' },
            { icon: 'wifi', label: 'WiFi' },
            { icon: 'water', label: 'Frischwasser' },
            { icon: 'dump', label: 'Abwasserentsorgung' },
            { icon: 'chemical', label: 'Chemie-WC' },
            { icon: 'kitchen', label: 'Küche' },
            { icon: 'washer', label: 'Waschmaschine' },
            { icon: 'trash', label: 'Müllentsorgung' },
            { icon: 'pets', label: 'Haustiere erlaubt' },
          ],
          rows: [
            { item: 'Wohnwagen ohne Strom', price: '20 € / Nacht', note: 'inkl. 2 Personen' },
            { item: 'Wohnwagen mit Strom', price: '25 € / Nacht', note: 'inkl. 2 Personen' },
            { item: 'Zelten', price: '7 € / Person' },
            { item: 'Zusatzperson', price: '3 € / Person' },
          ],
        },
        {
          label: 'Sonstiges',
          icon: '❄️',
          rows: [
            { item: 'Winter-Seetransport', price: 'Preis auf Anfrage' },
          ],
        },
      ],
    },
    contact: {
      kicker: 'Kontakt',
      title: 'Besuchen Sie uns oder nehmen Sie Kontakt auf',
      address: 'Dorf Pusi, Gemeinde Alatskivi, Kreis Tartu',
      mapUrl: 'https://www.google.com/maps/search/?api=1&query=58.64483549867105,27.166508285762042',
      locationLabel: 'Standort',
      hoursLabel: 'Öffnungszeiten',
      hours: 'Ganzjährig geöffnet',
      phone: '+372 56 955 758',
      email: 'willipu.willipu@gmail.com',
      cta: 'E-Mail senden',
      legal: {
        reg: '10972974',
        vat: 'EE100878462',
        legalAddress: 'Villipu, Pusi küla, 60217 Peipsiääre vald, Tartu maakond',
      },
    },
    footer: {
      tagline: 'Am Peipussee seit 2010.',
      rights: 'Alle Rechte vorbehalten',
    },
  },
  fi: {
    nav: {
      about: 'Meistä',
      stay: 'Majoitus',
      amenities: 'Aktiviteetit',
      pricing: 'Hinnat',
      gallery: 'Galleria',
      contact: 'Yhteystiedot',
    },
    hero: {
      eyebrow: 'Peipsijärven rannalla',
      title: 'Willipu vierastalo ja asuntovaunupuisto',
      subtitle: 'Rauhallinen paikka veden äärellä — kokoontumisiin, lomailuun ja juhliin. Pusin kylässä, Etelä-Virossa.',
      cta: 'Varaa paikka asuntovaunupuistosta',
      ctaAlt: 'Katso hinnat',
      ctaNote: 'Huoneiden ja mökkien varaukset sähköpostitse.',
    },
    about: {
      kicker: 'Tervetuloa',
      title: 'Yli 20 vuoden kokemus',
      body: 'Willipu sijaitsee Tarton maakunnassa, Alatskivin kunnassa, Pusin kylässä – suoraan Peipsijärven rannalla. Lähin kaupunki Kallaste on 2 km päässä, Tartu 50 km ja Tallinn 200 km. Tarjoamme huoneita päätalossa, kesämökkejä, juhlatilan tapahtumia varten sekä täyden asuntovaunualueen.',
      stats: [
        { value: '10', label: 'paikkaa päätalossa' },
        { value: '30', label: 'paikkaa juhlatilassa' },
        { value: '41', label: 'asuntovaunupaikkaa' },
        { value: '2 km', label: 'Kallasteen kaupunkiin' },
        { value: '16', label: 'paikkaa mökeissä' },
        { value: 'enint. 5', label: 'lisäpaikkaa' },
        { value: '🏖', label: 'lapsiystävällinen hiekkaranta' },
        { value: '🌿', label: 'suuri nurmialue ulkotapahtumia varten' },
      ],
    },
    amenities: {
      kicker: 'Aktiviteetit',
      title: 'Tekemistä järven rannalla',
      items: [
        { icon: 'wave', title: 'Uinti ja surffaus', body: 'Hiekkaranta, sopii myös purjelautailijoille.' },
        { icon: 'ball', title: 'Lentopallo ja pelit', body: 'Ulkokentät ja avoimet nurmikenttät.' },
        { icon: 'fire', title: 'Nuotio ja sauna', body: 'Nuotiopaikka ja sauna ryhmille.' },
        { icon: 'hall', title: 'Juhlatila 30 hengelle', body: 'Kokoukset, juhlat, koulutukset.' },
        { icon: 'wifi', title: 'WiFi kaikkialla', body: 'Ilmainen yhteys päätalossa.' },
      ],
    },
    pricing: {
      kicker: 'Hinnat',
      title: 'Edulliset hinnat, kaikki mukavuudet mukana',
      note: '50 %:n ennakkomaksu vahvistaa varauksen. Peruutuksista alle 14 päivää ennen saapumista ennakkomaksua ei palauteta.',
      groups: [
        {
          label: 'Suuri leirintämökki',
          icon: '🏡',
          photos: [
            { url: 'https://images.unsplash.com/photo-1518780664697-55e3ad937233?w=1200&q=80', alt: 'Suuri leirintämökki' },
            { url: 'https://images.unsplash.com/photo-1499696010180-025ef6e1a8f9?w=1200&q=80', alt: 'Sisänäkymä' },
          ],
          amenities: [
            { icon: 'wc', label: 'WC' },
            { icon: 'shower', label: 'Suihku' },
            { icon: 'wifi', label: 'WiFi' },
            { icon: 'kitchen', label: 'Keittiö' },
            { icon: 'grill', label: 'Grilli' },
          ],
          rows: [
            { item: '5 henkilöä', price: '110 € / yö' },
            { item: '4 henkilöä', price: '100 € / yö' },
            { item: '2–3 henkilöä', price: '85 € / yö' },
          ],
        },
        {
          label: 'Pieni leirintämökki',
          icon: '🛖',
          photos: [
            { url: 'https://images.unsplash.com/photo-1518780664697-55e3ad937233?w=1200&q=80', alt: 'Pieni leirintämökki' },
            { url: 'https://images.unsplash.com/photo-1464822759023-fed622ff2c3b?w=1200&q=80', alt: 'Ympäristö' },
          ],
          amenities: [
            { icon: 'wc', label: 'WC' },
            { icon: 'wifi', label: 'WiFi' },
            { icon: 'grill', label: 'Grilli' },
          ],
          rows: [
            { item: '2 henkilöä', price: '55 € / yö' },
            { item: '1 henkilö', price: '35 € / yö' },
          ],
        },
        {
          label: 'Kahden hengen huone',
          icon: '🛏',
          photos: [
            { url: 'https://images.unsplash.com/photo-1499696010180-025ef6e1a8f9?w=1200&q=80', alt: 'Kahden hengen huone' },
            { url: 'https://images.unsplash.com/photo-1500530855697-b586d89ba3ee?w=1200&q=80', alt: 'Näkymä järvelle' },
          ],
          amenities: [
            { icon: 'wc', label: 'WC' },
            { icon: 'shower', label: 'Suihku' },
            { icon: 'wifi', label: 'WiFi' },
            { icon: 'kitchen', label: 'Yhteiskeittiö' },
            { icon: 'grill', label: 'Grilli' },
          ],
          rows: [
            { item: '2 henkilöä', price: '55 € / yö' },
            { item: '1 henkilö', price: '35 € / yö' },
          ],
        },
        {
          label: 'Kolmen hengen huone',
          icon: '🛏',
          photos: [
            { url: 'https://images.unsplash.com/photo-1499696010180-025ef6e1a8f9?w=1200&q=80', alt: 'Kolmen hengen huone' },
            { url: 'https://images.unsplash.com/photo-1505765050516-f72dcac9c60e?w=1200&q=80', alt: 'Ranta' },
          ],
          amenities: [
            { icon: 'wc', label: 'WC' },
            { icon: 'shower', label: 'Suihku' },
            { icon: 'wifi', label: 'WiFi' },
            { icon: 'kitchen', label: 'Yhteiskeittiö' },
            { icon: 'grill', label: 'Grilli' },
          ],
          rows: [
            { item: '3 henkilöä', price: '80 € / yö' },
            { item: '2 henkilöä', price: '60 € / yö' },
          ],
        },
        {
          label: 'Asuntovaunupuisto',
          icon: '🚐',
          photos: [
            { url: 'https://images.unsplash.com/photo-1500530855697-b586d89ba3ee?w=1200&q=80', alt: 'Järvi' },
            { url: 'https://images.unsplash.com/photo-1470770841072-f978cf4d019e?w=1200&q=80', alt: 'Mäntymetsä veden äärellä' },
            { url: 'https://images.unsplash.com/photo-1505765050516-f72dcac9c60e?w=1200&q=80', alt: 'Ranta kultaisella hetkellä' },
          ],
          amenities: [
            { icon: 'checkin', label: 'Check-in 24/7', tooltip: 'Itsepalvelu check-in' },
            { icon: 'electric', label: 'Sähkö' },
            { icon: 'shower', label: 'Suihku' },
            { icon: 'wifi', label: 'WiFi' },
            { icon: 'water', label: 'Puhdas vesi' },
            { icon: 'dump', label: 'Jäteveden tyhjennys' },
            { icon: 'chemical', label: 'Kemiallinen WC' },
            { icon: 'kitchen', label: 'Keittiö' },
            { icon: 'washer', label: 'Pesukone' },
            { icon: 'trash', label: 'Jätteiden käsittely' },
            { icon: 'pets', label: 'Lemmikit sallittu' },
          ],
          rows: [
            { item: 'Asuntovaunu ilman sähköä', price: '20 € / yö', note: 'sis. 2 henkilöä' },
            { item: 'Asuntovaunu sähköllä', price: '25 € / yö', note: 'sis. 2 henkilöä' },
            { item: 'Telttailu', price: '7 € / henkilö' },
            { item: 'Lisähenkilö', price: '3 € / henkilö' },
          ],
        },
        {
          label: 'Muut',
          icon: '❄️',
          rows: [
            { item: 'Talvinen järvikuljetus', price: 'kysy hinta' },
          ],
        },
      ],
    },
    contact: {
      kicker: 'Yhteystiedot',
      title: 'Tule vierailulle tai ota yhteyttä',
      address: 'Pusin kylä, Alatskivin kunta, Tarton maakunta',
      mapUrl: 'https://www.google.com/maps/search/?api=1&query=58.64483549867105,27.166508285762042',
      locationLabel: 'Sijainti',
      hoursLabel: 'Aukioloajat',
      hours: 'Auki ympäri vuoden',
      phone: '+372 56 955 758',
      email: 'willipu.willipu@gmail.com',
      cta: 'Lähetä sähköposti',
      legal: {
        reg: '10972974',
        vat: 'EE100878462',
        legalAddress: 'Villipu, Pusi küla, 60217 Peipsiääre vald, Tartu maakond',
      },
    },
    footer: {
      tagline: 'Peipsijärven rannalla vuodesta 2010.',
      rights: 'Kaikki oikeudet pidätetään',
    },
  },
}

export const gallery = [
  {
    url: 'https://images.unsplash.com/photo-1500530855697-b586d89ba3ee?w=1200&q=80',
    alt: 'Lake at sunrise',
  },
  {
    url: 'https://images.unsplash.com/photo-1518780664697-55e3ad937233?w=1200&q=80',
    alt: 'Wooden cottage in trees',
  },
  {
    url: 'https://images.unsplash.com/photo-1464822759023-fed622ff2c3b?w=1200&q=80',
    alt: 'Misty forest morning',
  },
  {
    url: 'https://images.unsplash.com/photo-1499696010180-025ef6e1a8f9?w=1200&q=80',
    alt: 'Cabin interior with wood',
  },
  {
    url: 'https://images.unsplash.com/photo-1470770841072-f978cf4d019e?w=1200&q=80',
    alt: 'Pine forest by water',
  },
  {
    url: 'https://images.unsplash.com/photo-1505765050516-f72dcac9c60e?w=1200&q=80',
    alt: 'Boat dock at golden hour',
  },
]

export const heroImage = '/52c0d4c0-7aea-429a-b0f0-0f4a1ca2155d.jpg'
