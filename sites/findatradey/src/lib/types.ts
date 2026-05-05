// Shared types used across data + components + pages.

export type District = {
  postcode_district: string;
  slug: string;
  town: string;
  town_slug: string;
  borough_council: string;
  constituency: string;
  county: string;
  county_slug: string;
  region: string;
  country: string;
  lat: number;
  lng: number;
  population_2021: number;
  households_2021: number;
  housing_stock_dominant: string;
  median_property_year: number;
  neighbouring_districts: string[];
};

export type RegisterEntry = {
  name: string;
  registration_id: string;
  phone?: string;
  postcode?: string;
  lat?: number;
  lng?: number;
};

export type RegisterDistrict = {
  registered_count: number;
  top_3?: RegisterEntry[];
  niceic_count?: number;
  napit_count?: number;
  elecsa_count?: number;
  heat_pump_count?: number;
  solar_count?: number;
};

export type GasSafeRegister = {
  _comment?: string;
  _refresh_frequency?: string;
  _last_refresh?: string | null;
  districts: Record<string, RegisterDistrict>;
};

export type PlumberPricing = {
  average_emergency_callout_2026_gbp: number;
  median_hourly_rate_2026_gbp: number;
  leak_detection_average_gbp: number;
  drain_unblocking_average_gbp: number;
  regional_premium_pct: number;
};

export type ElectricianPricing = {
  average_emergency_callout_2026_gbp: number;
  median_hourly_rate_2026_gbp: number;
  eicr_3bed_average_gbp: number;
  rewire_3bed_average_gbp: number;
  consumer_unit_replacement_average_gbp: number;
  regional_premium_pct: number;
};

export type BoilerPricing = {
  average_emergency_callout_2026_gbp: number;
  median_hourly_rate_2026_gbp: number;
  annual_service_average_gbp: number;
  boiler_repair_average_gbp: number;
  new_combi_install_average_gbp: number;
  heat_pump_install_average_gbp: number;
  regional_premium_pct: number;
};

export type Trade = 'plumber' | 'electrician' | 'boiler';

export type FAQ = {
  q: string;
  a: string;
};
