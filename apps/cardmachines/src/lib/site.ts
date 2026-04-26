// CardMachines site-wide constants. Imported wherever needed for schema,
// canonical URLs, and copy.
export const SITE = {
  name: 'CardMachines',
  domain: 'cardmachines.co.uk',
  url: 'https://cardmachines.co.uk',
  tagline: 'UK card terminals, merchant accounts and payment processing — independently reviewed.',
  // Set when the cross-site Organization schema decision is locked.
  parentOrganization: undefined as { name: string; url: string } | undefined,
  twitter: undefined as string | undefined,
  defaultAuthorSlug: 'editorial-team',
} as const;
