// AINews — slot reserved for the AI-search news / publication property.
// Positioning, monetisation and audience NOT YET DECIDED.
// Placeholder kept in the network so the dashboard sees the slot
// and we don't lose the idea.

export const SITE = {
  name: 'AI Search News',
  domain: 'aisearchnews.uk', // placeholder — confirm
  url: 'https://aisearchnews.uk',
  tagline: 'Coverage, analysis and updates for AI search — TBD.',
  parentOrganization: undefined as { name: string; url: string } | undefined,
  defaultAuthorSlug: 'editorial-team',
  status: 'tbd' as const,
} as const;
