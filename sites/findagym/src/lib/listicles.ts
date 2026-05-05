// Listicle configuration — defines every "best gyms for X in Colchester" page.
// Each entry filters/sorts the gym list and supplies the page copy.

import type { Gym } from './types';
import { colchester } from './data';

export type ListicleConfig = {
  slug: string;
  title: string;
  metaDescription: string;
  h1: string;
  intro: string;
  bottomNote?: string;
  filter: (g: Gym) => boolean;
  sort?: (a: Gym, b: Gym) => number;
  takeTopN?: number;
};

export const listicles: ListicleConfig[] = [
  // BEST + tiers
  {
    slug: 'best-gyms-colchester',
    title: 'Best Gyms in Colchester 2026 — Honest Review by FindAGym',
    metaDescription: 'The best gyms in Colchester ranked honestly across budget, equipment, hours, and crowd. Quiet times, demographic profile, equipment audit per gym.',
    h1: 'Best gyms in Colchester (2026)',
    intro: 'Ranking the gyms in Colchester on what actually matters: equipment quality, busy times, atmosphere, and what each gym is genuinely best at. Not just price.',
    filter: () => true,
    sort: (a, b) => (a.demographic_profile.intimidation_factor_1_5 - b.demographic_profile.intimidation_factor_1_5) || (a.monthly_price_2026_gbp - b.monthly_price_2026_gbp),
  },
  {
    slug: 'cheap-gyms-colchester',
    title: 'Cheap Gyms in Colchester 2026 — Under £25/month | FindAGym',
    metaDescription: 'The cheapest gyms in Colchester for under £25/month. No-contract, 24/7 access, honest review of what each one is genuinely best for.',
    h1: 'Cheap gyms in Colchester (under £25/month)',
    intro: 'The cheapest UK gym chains run £19.99–£24.99 in Colchester in 2026. Here\'s which one suits which kind of training — based on equipment, hours and crowd, not just headline price.',
    filter: (g) => g.monthly_price_2026_gbp < 25,
    sort: (a, b) => a.monthly_price_2026_gbp - b.monthly_price_2026_gbp,
  },
  {
    slug: 'luxury-gyms-colchester',
    title: 'Luxury Gyms in Colchester 2026 — Premium & Members-Only | FindAGym',
    metaDescription: 'Premium and members-only gym options in Colchester. Honest comparison of pool/sauna/steam, equipment, and what each is genuinely best for.',
    h1: 'Luxury gyms in Colchester (premium tier)',
    intro: 'Premium and members-only gym options in Colchester. Smaller floor-plates, more recovery facilities, less peak-hour congestion. What you\'re actually paying for.',
    filter: (g) => g.tier === 'premium' || g.tier === 'luxury' || g.monthly_price_2026_gbp >= 60,
    bottomNote: 'Colchester\'s premium-gym market is smaller than London or Manchester — the strongest "luxury" option locally is often Leisure World Colchester for the pool/sauna combo plus a budget chain for kit. Worth thinking about.',
  },
  // HOURS / ACCESS
  {
    slug: '24-hour-gyms-colchester',
    title: '24-Hour Gyms in Colchester 2026 — Always Open | FindAGym',
    metaDescription: 'Every 24-hour gym in Colchester. When each is genuinely quiet at night, what equipment is left running, and which one is best for early-morning lifters.',
    h1: '24-hour gyms in Colchester',
    intro: 'Open 24/7 doesn\'t mean staffed 24/7. Here\'s which Colchester gyms are genuinely usable at 6am or 10pm, with a real read on overnight crowd, equipment access and safety.',
    filter: (g) => g.open_24_7,
    sort: (a, b) => a.monthly_price_2026_gbp - b.monthly_price_2026_gbp,
  },
  {
    slug: 'gym-day-pass-colchester',
    title: 'Gym Day Passes in Colchester 2026 — No Contract | FindAGym',
    metaDescription: 'Day passes and no-contract gym options in Colchester. Drop-in pricing, what each gym lets you in for the day, and which one suits visitors.',
    h1: 'Gym day passes in Colchester (drop-in)',
    intro: 'Visiting Colchester or trialling before you commit? Here are the gyms with day passes or true no-contract memberships, with honest reads on what each gives you for the day.',
    filter: (g) => g.no_contract,
    sort: (a, b) => a.monthly_price_2026_gbp - b.monthly_price_2026_gbp,
  },
  // AUDIENCE
  {
    slug: 'womens-gym-colchester',
    title: "Women's Gyms in Colchester 2026 — Female-Friendly | FindAGym",
    metaDescription: 'Female-friendly gyms in Colchester. Genuine demographic mix, women-only hours, atmosphere read — not marketing copy.',
    h1: "Women's gyms in Colchester (genuinely female-friendly)",
    intro: 'No gym in Colchester is women-only, but several have genuine female-friendly atmospheres, women-only hours, or a balanced demographic. Here\'s the real read.',
    filter: (g) => g.demographic_profile.gender_split_estimate.female >= 38,
    sort: (a, b) => b.demographic_profile.gender_split_estimate.female - a.demographic_profile.gender_split_estimate.female,
    bottomNote: 'Estimated splits — refreshed at every visit. None of these are women-only; we are flagging where the actual member mix and atmosphere skew female or balanced.',
  },
  {
    slug: 'student-gym-colchester',
    title: 'Student Gyms in Colchester 2026 — University of Essex | FindAGym',
    metaDescription: 'Best student gyms in Colchester. Cheapest options, term-time deals, atmosphere reads. Made for University of Essex undergrads.',
    h1: 'Student gyms in Colchester (University of Essex)',
    intro: 'University of Essex students get a clear set of options in Colchester. Here\'s what each delivers on cost, hours, and crowd — including which ones go quiet during reading week.',
    filter: (g) => g.demographic_profile.age_bands_estimate['18_25'] >= 25,
    sort: (a, b) => a.monthly_price_2026_gbp - b.monthly_price_2026_gbp,
  },
  {
    slug: 'over-50s-gym-colchester',
    title: 'Over-50s Gyms in Colchester 2026 — Active Retirement | FindAGym',
    metaDescription: 'Best gyms in Colchester for the over-50s. Calm atmosphere, low intimidation, classes that suit active retirement.',
    h1: 'Over-50s gyms in Colchester',
    intro: 'For active retirement, the right gym is the one with low intimidation, good daytime hours, and a community of regulars in the same age band. Here\'s what each Colchester gym offers.',
    filter: (g) => g.demographic_profile.age_bands_estimate['56_plus'] >= 7 || g.demographic_profile.intimidation_factor_1_5 <= 2,
    sort: (a, b) => a.demographic_profile.intimidation_factor_1_5 - b.demographic_profile.intimidation_factor_1_5,
  },
  // GOAL
  {
    slug: 'best-gym-weight-loss-colchester',
    title: 'Best Gym for Weight Loss in Colchester 2026 | FindAGym',
    metaDescription: 'Which Colchester gym is best for weight loss? Honest read on cardio capacity, classes, atmosphere — and which to avoid if you\'re self-conscious.',
    h1: 'Best gym for weight loss in Colchester',
    intro: 'Weight-loss progress depends on consistency more than gym choice — but the right gym makes consistency easier. Here\'s what each Colchester option offers for cardio, classes, and a non-intimidating atmosphere.',
    filter: (g) => g.equipment_audit.treadmill_count >= 8 || g.equipment_audit.bike_count >= 6,
    sort: (a, b) => a.demographic_profile.intimidation_factor_1_5 - b.demographic_profile.intimidation_factor_1_5,
  },
  {
    slug: 'best-gym-marathon-training-colchester',
    title: 'Best Gym for Marathon Training in Colchester 2026 | FindAGym',
    metaDescription: 'Best gyms in Colchester for marathon and half-marathon training. Treadmill quality, ski erg / rower availability, recovery facilities.',
    h1: 'Best gym for marathon training in Colchester',
    intro: 'Marathon prep needs reliable treadmills, working clocks, recovery options and ideally a pool or sauna. Here\'s how Colchester\'s gyms stack up.',
    filter: (g) => g.equipment_audit.treadmill_count >= 10,
    sort: (a, b) => b.equipment_audit.treadmill_count - a.equipment_audit.treadmill_count,
  },
  {
    slug: 'best-gym-postnatal-colchester',
    title: 'Best Gym for Postnatal Recovery in Colchester 2026 | FindAGym',
    metaDescription: 'Best Colchester gym for postnatal recovery. Quiet midday hours, supportive atmosphere, classes appropriate for new mothers.',
    h1: 'Best gym for postnatal recovery in Colchester',
    intro: 'Postnatal recovery needs a quiet, low-intimidation environment with classes that recognise the difference. Here\'s what Colchester offers.',
    filter: (g) => g.demographic_profile.intimidation_factor_1_5 <= 2,
    sort: (a, b) => a.demographic_profile.intimidation_factor_1_5 - b.demographic_profile.intimidation_factor_1_5,
  },
  // UNDER-SERVED ANGLE PAGES — THE DIFFERENTIATOR
  {
    slug: 'quietest-gyms-colchester',
    title: 'Quietest Gyms in Colchester 2026 — When Each One Is Empty | FindAGym',
    metaDescription: 'Which Colchester gym is genuinely quiet — and when. Hour-by-hour breakdown for every chain. Avoid the queues for squat racks and treadmills.',
    h1: 'Quietest gyms in Colchester (when each one is empty)',
    intro: 'No gym is "quiet" — they\'re quiet at specific hours. Here\'s the real hour-by-hour read on every Colchester gym, so you can plan a session that doesn\'t involve waiting 20 minutes for a squat rack.',
    filter: () => true,
    sort: (a, b) => a.popular_times_summary.localeCompare(b.popular_times_summary),
    bottomNote: 'Quiet windows are observational and from Google Maps Popular Times. Refreshed at every revisit.',
  },
  {
    slug: 'least-intimidating-gym-colchester',
    title: 'Least Intimidating Gym in Colchester 2026 — For Absolute Beginners | FindAGym',
    metaDescription: 'Which Colchester gym is least intimidating for absolute beginners? Honest atmosphere reads, no peacocking, supportive crowd.',
    h1: 'Least intimidating gym in Colchester (for absolute beginners)',
    intro: "For your first gym, the equipment matters less than whether you'll go back. Here's the honest atmosphere read on every Colchester option, ranked by intimidation factor.",
    filter: () => true,
    sort: (a, b) => a.demographic_profile.intimidation_factor_1_5 - b.demographic_profile.intimidation_factor_1_5,
    bottomNote: 'Intimidation factor is observational on a 1–5 scale, where 1 = walking in feels like nothing, 5 = lots of mirror work and serious lifters watching the door.',
  },
  {
    slug: 'best-equipped-gym-colchester',
    title: 'Best-Equipped Gym in Colchester 2026 — Real Equipment Audit | FindAGym',
    metaDescription: 'Best-equipped Colchester gym? Real equipment audits — squat racks, deadlift platforms, dumbbell ceilings, recovery facilities — for every chain.',
    h1: 'Best-equipped gym in Colchester (real equipment audit)',
    intro: 'Counting cardio machines and free-weight ceilings, station by station. Here\'s the real equipment audit for every Colchester gym so you can pick one that suits your training.',
    filter: () => true,
    sort: (a, b) => (b.equipment_audit.squat_rack_count + b.equipment_audit.deadlift_platform_count) - (a.equipment_audit.squat_rack_count + a.equipment_audit.deadlift_platform_count),
  },
  {
    slug: 'best-gym-classes-colchester',
    title: 'Best Gym Classes in Colchester 2026 — Class Roster Compared | FindAGym',
    metaDescription: 'Which Colchester gym has the best classes? Compared by roster, named instructors and popularity. HIIT, spin, body pump, yoga.',
    h1: 'Best gym classes in Colchester (compared by roster)',
    intro: 'Class quality depends on the instructor. Here\'s what each Colchester gym offers and where the genuinely good classes are.',
    filter: (g) => g.facilities.includes('free_classes') || g.facilities.includes('fiit_studio'),
  },
];

export function getListicle(slug: string): ListicleConfig | undefined {
  return listicles.find((l) => l.slug === slug);
}

export function getListicleGyms(cfg: ListicleConfig): Gym[] {
  let gyms = colchester.gyms.filter(cfg.filter);
  if (cfg.sort) gyms = [...gyms].sort(cfg.sort);
  if (cfg.takeTopN) gyms = gyms.slice(0, cfg.takeTopN);
  return gyms;
}
