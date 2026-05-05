// Schema.org JSON-LD generators. Each returns a plain object that templates JSON-stringify into a <script type="application/ld+json"> tag.

import type { District, FAQ } from './types';

export function organisationSchema() {
  return {
    '@context': 'https://schema.org',
    '@type': 'Organization',
    name: 'FindATradey',
    url: 'https://findatradey.co.uk',
    description:
      'UK trade-finder matching homeowners with verified Gas Safe / NICEIC / OFTEC / MCS engineers. Three vetted local engineers per job, no spam.',
    foundingDate: '2026',
  };
}

export function websiteSchema() {
  return {
    '@context': 'https://schema.org',
    '@type': 'WebSite',
    name: 'FindATradey',
    url: 'https://findatradey.co.uk',
  };
}

export function placeSchema(d: District) {
  return {
    '@context': 'https://schema.org',
    '@type': 'Place',
    name: `${d.town}, ${d.county}`,
    geo: {
      '@type': 'GeoCoordinates',
      latitude: d.lat,
      longitude: d.lng,
    },
    address: {
      '@type': 'PostalAddress',
      addressRegion: d.county,
      addressCountry: d.country,
    },
  };
}

export function serviceSchema(args: {
  serviceName: string;
  serviceType: string;
  district: District;
  description: string;
  averagePrice?: number;
}) {
  return {
    '@context': 'https://schema.org',
    '@type': 'Service',
    name: args.serviceName,
    serviceType: args.serviceType,
    areaServed: {
      '@type': 'Place',
      name: `${args.district.town} (${args.district.postcode_district})`,
    },
    provider: {
      '@type': 'Organization',
      name: 'FindATradey',
      url: 'https://findatradey.co.uk',
    },
    description: args.description,
    ...(args.averagePrice
      ? {
          offers: {
            '@type': 'Offer',
            priceCurrency: 'GBP',
            price: args.averagePrice,
          },
        }
      : {}),
  };
}

export function faqSchema(faqs: FAQ[]) {
  return {
    '@context': 'https://schema.org',
    '@type': 'FAQPage',
    mainEntity: faqs.map((f) => ({
      '@type': 'Question',
      name: f.q,
      acceptedAnswer: {
        '@type': 'Answer',
        text: f.a,
      },
    })),
  };
}

export function breadcrumbSchema(items: Array<{ name: string; url: string }>) {
  return {
    '@context': 'https://schema.org',
    '@type': 'BreadcrumbList',
    itemListElement: items.map((it, idx) => ({
      '@type': 'ListItem',
      position: idx + 1,
      name: it.name,
      item: it.url,
    })),
  };
}
