// Data loaders. Astro can import JSON natively at build time so these are simple wrappers
// that give us typed access throughout the templates.

import districtsData from '@data/geo/districts.json';
import gasSafeData from '@data/registers/gas-safe.json';
import niceicData from '@data/registers/niceic.json';
import oftecData from '@data/registers/oftec.json';
import mcsData from '@data/registers/mcs.json';
import plumberPricingData from '@data/pricing/plumber.json';
import electricianPricingData from '@data/pricing/electrician.json';
import boilerPricingData from '@data/pricing/boiler.json';
import type {
  District,
  GasSafeRegister,
  PlumberPricing,
  ElectricianPricing,
  BoilerPricing,
} from './types';

export const districts: District[] = districtsData as District[];

export const gasSafe = gasSafeData as GasSafeRegister;
export const niceic = niceicData as GasSafeRegister; // shape is identical for our purposes
export const oftec = oftecData as GasSafeRegister;
export const mcs = mcsData as GasSafeRegister;

export const plumberPricing = plumberPricingData as {
  districts: Record<string, PlumberPricing>;
};
export const electricianPricing = electricianPricingData as {
  districts: Record<string, ElectricianPricing>;
};
export const boilerPricing = boilerPricingData as {
  districts: Record<string, BoilerPricing>;
};

// Helper: get a district by slug.
export function getDistrictBySlug(slug: string): District | undefined {
  return districts.find((d) => d.slug === slug);
}

// Helper: get all districts grouped by county.
export function getDistrictsByCounty(): Record<string, District[]> {
  return districts.reduce<Record<string, District[]>>((acc, d) => {
    if (!acc[d.county_slug]) acc[d.county_slug] = [];
    acc[d.county_slug].push(d);
    return acc;
  }, {});
}

// Helper: get neighbouring districts (those that exist in our dataset).
export function getNeighbouringDistricts(district: District): District[] {
  return district.neighbouring_districts
    .map((pc) => districts.find((d) => d.postcode_district === pc))
    .filter((d): d is District => d !== undefined);
}

// Helper: pretty-print a postcode district (e.g. "Colchester (CO1)").
export function districtLabel(d: District): string {
  return `${d.town} (${d.postcode_district})`;
}

// Helper: build the URL slug used in dynamic pages.
export function districtSlugFromRecord(d: District): string {
  return d.slug;
}

// All eight district slugs for getStaticPaths.
export function getAllDistrictParams() {
  return districts.map((d) => ({
    params: { district: d.slug },
    props: { district: d },
  }));
}
