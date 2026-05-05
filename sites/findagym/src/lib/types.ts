// Shared types across the gym data + components + pages.

export type Tier = 'budget' | 'mid' | 'premium' | 'luxury' | 'boutique' | 'council';

export type DemographicProfile = {
  gender_split_estimate: { male: number; female: number; other: number };
  age_bands_estimate: { '18_25': number; '26_40': number; '41_55': number; '56_plus': number };
  skill_split_estimate: { beginner: number; intermediate: number; advanced: number };
  intimidation_factor_1_5: number;
  music_volume_1_5: number;
  atmosphere_notes: string;
};

export type EquipmentAudit = {
  treadmill_count: number;
  bike_count: number;
  rower_count: number;
  ski_erg_count: number;
  dumbbell_ceiling_kg: number;
  kettlebell_range_kg: string;
  barbell_count: number;
  squat_rack_count: number;
  deadlift_platform_count: number;
  power_cage_count: number;
  cable_station_count: number;
  functional_zone: string;
  pool: boolean;
  sauna: boolean;
  steam: boolean;
  broken_or_worn: string[];
};

export type ClassEntry = {
  name: string;
  instructor?: string;
  day?: string;
  time?: string;
  popularity?: number;
};

export type Gym = {
  gym_id: string;
  name: string;
  brand: string;
  brand_slug: string;
  tier: Tier;
  tier_label: string;
  address: string;
  postcode: string;
  lat: number;
  lng: number;
  phone: string | null;
  website: string;
  open_24_7: boolean;
  open_hours_summary: string;
  monthly_price_2026_gbp: number;
  joining_fee_2026_gbp: number;
  no_contract: boolean;
  facilities: string[];
  specialisms: string[];
  demographic_profile: DemographicProfile;
  popular_times_summary: string;
  equipment_audit: EquipmentAudit;
  class_roster: ClassEntry[];
  best_for: string[];
  underrated_for: string[];
  worst_for: string[];
  honest_pros: string[];
  honest_cons: string[];
  review_count_google: number;
  review_avg_google: number;
  review_count_trustpilot: number;
  review_avg_trustpilot: number;
  last_visit_date: string | null;
};

export type SpecialismStudio = {
  studio_id: string;
  name: string;
  specialism: string;
  specialism_slug: string;
  tier: Tier;
  tier_label: string;
  address: string;
  postcode: string;
  lat: number;
  lng: number;
  monthly_price_2026_gbp: number;
  drop_in_2026_gbp: number;
  best_for: string[];
  underrated_for: string[];
  worst_for: string[];
  class_roster_summary: string;
};

export type TownGymData = {
  _town: string;
  _county: string;
  _lat: number;
  _lng: number;
  _last_data_refresh: string;
  gyms: Gym[];
  specialism_studios: SpecialismStudio[];
};

export type FAQ = {
  q: string;
  a: string;
};
