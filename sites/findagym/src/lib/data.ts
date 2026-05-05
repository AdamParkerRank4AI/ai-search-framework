// Data loaders. Town datasets live in data/gyms/<town>.json. Astro imports JSON natively at build time.

import colchesterData from '@data/gyms/colchester.json';
import type { Gym, SpecialismStudio, TownGymData } from './types';

export const colchester = colchesterData as TownGymData;

// Future towns: import + register here as they're added.
export const allTowns = ['colchester'] as const;
export type TownSlug = typeof allTowns[number];

const townMap: Record<TownSlug, TownGymData> = {
  colchester,
};

export function getTownData(slug: TownSlug): TownGymData {
  return townMap[slug];
}

export function getColchesterGyms(): Gym[] {
  return colchester.gyms;
}

export function getColchesterStudios(): SpecialismStudio[] {
  return colchester.specialism_studios;
}

export function getGymById(id: string): Gym | undefined {
  return colchester.gyms.find((g) => g.gym_id === id);
}

export function getGymsByBrandSlug(brandSlug: string): Gym[] {
  return colchester.gyms.filter((g) => g.brand_slug === brandSlug);
}

// Tier filters for category pages.
export function getGymsByTier(tier: string): Gym[] {
  return colchester.gyms.filter((g) => g.tier === tier);
}

export function getGymsBy24_7(): Gym[] {
  return colchester.gyms.filter((g) => g.open_24_7);
}

export function getGymsByNoContract(): Gym[] {
  return colchester.gyms.filter((g) => g.no_contract);
}

export function getGymsByPool(): Gym[] {
  return colchester.gyms.filter((g) => g.equipment_audit.pool);
}

export function getStudioBySpecialismSlug(slug: string): SpecialismStudio | undefined {
  return colchester.specialism_studios.find((s) => s.specialism_slug === slug);
}

// Format helpers.
export function fmtMoney(n: number): string {
  return `£${n.toLocaleString('en-GB')}`;
}
