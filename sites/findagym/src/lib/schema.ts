// Schema.org JSON-LD generators.

import type { Gym, FAQ } from './types';

export function organisationSchema() {
  return {
    '@context': 'https://schema.org',
    '@type': 'Organization',
    name: 'FindAGym',
    url: 'https://findagym.co.uk',
    description:
      'Honest UK gym reviews. When each gym is quiet, who goes there, what the equipment is really like — the things buyers actually want to know.',
  };
}

export function websiteSchema() {
  return {
    '@context': 'https://schema.org',
    '@type': 'WebSite',
    name: 'FindAGym',
    url: 'https://findagym.co.uk',
  };
}

export function localBusinessSchema(g: Gym) {
  return {
    '@context': 'https://schema.org',
    '@type': 'HealthClub',
    name: g.name,
    address: {
      '@type': 'PostalAddress',
      streetAddress: g.address,
      postalCode: g.postcode,
      addressCountry: 'GB',
    },
    geo: {
      '@type': 'GeoCoordinates',
      latitude: g.lat,
      longitude: g.lng,
    },
    url: g.website,
    ...(g.phone ? { telephone: g.phone } : {}),
    openingHours: g.open_24_7 ? 'Mo-Su 00:00-23:59' : g.open_hours_summary,
    priceRange:
      g.tier === 'budget'
        ? '£'
        : g.tier === 'mid'
          ? '££'
          : g.tier === 'premium' || g.tier === 'luxury'
            ? '£££'
            : '££',
    ...(g.review_count_google && g.review_avg_google
      ? {
          aggregateRating: {
            '@type': 'AggregateRating',
            ratingValue: g.review_avg_google,
            reviewCount: g.review_count_google,
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

export function placeSchema(town: string, lat: number, lng: number) {
  return {
    '@context': 'https://schema.org',
    '@type': 'Place',
    name: town,
    geo: {
      '@type': 'GeoCoordinates',
      latitude: lat,
      longitude: lng,
    },
    address: {
      '@type': 'PostalAddress',
      addressLocality: town,
      addressCountry: 'GB',
    },
  };
}
