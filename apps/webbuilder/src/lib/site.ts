// WebBuilder is the SERVICE site in the network.
// Unlike BBL / FundBiz / CardMachines / MarketInvoice / AINews / Fleet,
// WebBuilder doesn't earn affiliate commission — we provide the service
// directly. Lead capture funnels to our own delivery team.
//
// Positioning: AI-search-optimised website builds and audits for UK
// businesses, drawing on the Rank4AI methodology already documented
// in this repo's framework PDF.

export const SITE = {
  name: 'WebBuilder',
  domain: 'webbuilder.uk', // placeholder — confirm
  url: 'https://webbuilder.uk',
  tagline: 'Websites built to be cited by AI search.',
  parentOrganization: undefined as { name: string; url: string } | undefined,
  defaultAuthorSlug: 'editorial-team',
  // Service tiers — placeholder pricing until commercial decision
  tiers: [
    { slug: 'audit', name: 'AI Search Audit', priceFromGBP: 0, summary: 'Free baseline scan of your current site\'s AI-search visibility.' },
    { slug: 'build', name: 'AI-Ready Site Build', priceFromGBP: null, summary: 'Full site build engineered for citation by ChatGPT, Perplexity, Claude, Gemini, AI Overviews.' },
    { slug: 'managed', name: 'Managed AI Search', priceFromGBP: null, summary: 'Monthly programme — content, schema, entity work, citation tracking.' },
  ],
} as const;
