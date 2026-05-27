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
      ctaNote: 'Tubade ja kämpingute broneerimine hetkel võimalik vaid e-maili teel.',
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
      hours: 'Avatud aastaringselt',
      phone: '+372 56 955 758',
      email: 'willipu.willipu@gmail.com',
      cta: 'Saada e-kiri',
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
      ctaNote: 'Room and cottage bookings currently available by email only.',
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
      hours: 'Open year-round',
      phone: '+372 56 955 758',
      email: 'willipu.willipu@gmail.com',
      cta: 'Send an email',
    },
    footer: {
      tagline: 'On Lake Peipus since 2010.',
      rights: 'All rights reserved',
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
