export const SITE = {
  name: 'BestBusinessLoans',
  domain: 'bestbusinessloans.co.uk',
  url: 'https://bestbusinessloans.co.uk',
  tagline: 'Independent UK reviews of business loans, lenders and finance products.',
  parentOrganization: undefined as { name: string; url: string } | undefined,
  twitter: undefined as string | undefined,
  defaultAuthorSlug: 'editorial-team',
  // BBL never hosts application forms — it cross-links to FundBiz for the application funnel.
  fundbizUrl: 'https://fundbiz.co.uk',
} as const;
