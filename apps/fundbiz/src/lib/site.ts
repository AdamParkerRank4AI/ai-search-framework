export const SITE = {
  name: 'FundBiz',
  domain: 'fundbiz.co.uk',
  url: 'https://fundbiz.co.uk',
  tagline: 'UK business loan matching for limited companies, LLPs and partnerships of 4+. Post-decline help and sector-specific lenders.',
  parentOrganization: undefined as { name: string; url: string } | undefined,
  twitter: undefined as string | undefined,
  defaultAuthorSlug: 'editorial-team',
  // FundBiz operating rule: B2B / Ltd / LLP / partnership 4+ only.
  // See docs/regulatory-notes.md.
  eligibleStructures: ['Ltd', 'PLC', 'LLP', 'Partnership 4+'],
  bblUrl: 'https://bestbusinessloans.co.uk',
} as const;
