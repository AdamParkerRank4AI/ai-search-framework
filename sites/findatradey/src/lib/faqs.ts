// Templated FAQ generators. Each takes the district + relevant pricing and returns
// a list of FAQ entries with district-specific facts swapped in.

import type { District, FAQ } from './types';

const fmtMoney = (n: number) => `£${n.toLocaleString('en-GB')}`;

export function emergencyPlumberFAQs(args: {
  d: District;
  callout: number;
  hourly: number;
}): FAQ[] {
  return [
    {
      q: `How much does an emergency plumber cost in ${args.d.town}?`,
      a: `In ${args.d.town} (${args.d.postcode_district}) the typical 2026 emergency plumber callout is around ${fmtMoney(args.callout)}, with an hourly rate of ${fmtMoney(args.hourly)} once on site. Out-of-hours and weekend rates can be 50–100% higher.`,
    },
    {
      q: `How quickly can a plumber get to me in ${args.d.postcode_district}?`,
      a: `Most ${args.d.town} plumbers aim to reach an emergency callout within 60–120 minutes. Lead times stretch on weekends, public holidays, and during cold-snap weeks when demand spikes.`,
    },
    {
      q: `Should I turn the water off before the plumber arrives?`,
      a: `Yes. Turn off the water at the stopcock (usually under the kitchen sink). Then turn off the boiler. This contains damage and lowers what the plumber needs to do once on site, often reducing the bill.`,
    },
    {
      q: `Are emergency plumbers in ${args.d.town} on the WaterSafe register?`,
      a: `Plumbers handling mains water work should be WaterSafe-registered, which signals competence under the Water Supply Regulations. Gas Safe is required separately for any gas appliance work.`,
    },
    {
      q: `Will my home insurance cover an emergency plumber?`,
      a: `Many home insurance policies include a 24-hour emergency line, but excesses and per-incident caps apply. Check your policy before paying out of pocket.`,
    },
  ];
}

export function leakDetectionFAQs(args: {
  d: District;
  averagePrice: number;
}): FAQ[] {
  return [
    {
      q: `How much does leak detection cost in ${args.d.town}?`,
      a: `Specialist non-invasive leak detection in ${args.d.town} typically costs ${fmtMoney(args.averagePrice)} in 2026, depending on the equipment used (acoustic, thermal imaging, tracer gas) and how long the search takes.`,
    },
    {
      q: `What's the difference between a plumber and a leak detection specialist?`,
      a: `A general plumber will usually only locate visible leaks. A specialist uses thermal cameras, acoustic listening sticks and tracer gas to find leaks under floors, in walls and beneath driveways without breaking surfaces.`,
    },
    {
      q: `Can I claim leak detection on my home insurance?`,
      a: `Most UK home insurance policies cover the cost of "trace and access" once a water-damage claim is open. The work usually has to be quoted before the insurer authorises it.`,
    },
    {
      q: `How does a thermal imaging leak detection work?`,
      a: `Thermal imaging spots temperature differences between leaking water and the surrounding floor or wall. A small differential — sometimes less than 1°C — shows up clearly on a camera, letting the engineer mark the leak point without lifting tiles or cutting walls.`,
    },
  ];
}

export function drainUnblockingFAQs(args: {
  d: District;
  averagePrice: number;
}): FAQ[] {
  return [
    {
      q: `How much does drain unblocking cost in ${args.d.town}?`,
      a: `In ${args.d.town} a standard drain unblock costs around ${fmtMoney(args.averagePrice)} in 2026 for a single household connection. Major blockages, root ingress and CCTV surveys cost more.`,
    },
    {
      q: `Whose responsibility is the blocked drain — mine or the water company?`,
      a: `Drains within your property boundary are usually your responsibility. Sewers (the shared pipe outside your boundary) are the water company's. Anglian Water, Thames Water and Southern Water all run no-cost emergency unblocks for shared sewers — call them before paying a private contractor.`,
    },
    {
      q: `Will a high-pressure jet damage my pipes?`,
      a: `Modern jetting machines run at variable pressure. A competent operator dials it down for cast iron, lead and old clay pipes. Always ask if your pipework is over 60 years old before jetting starts.`,
    },
    {
      q: `Do I need a CCTV survey?`,
      a: `Only if the same drain blocks repeatedly, or if you suspect roots, collapse or misconnections. A one-off blockage rarely needs a survey.`,
    },
  ];
}

export function eicrFAQs(args: {
  d: District;
  eicrPrice: number;
}): FAQ[] {
  return [
    {
      q: `How much does an EICR cost in ${args.d.town}?`,
      a: `An EICR (Electrical Installation Condition Report) for a 3-bed home in ${args.d.town} typically costs around ${fmtMoney(args.eicrPrice)} in 2026. Larger properties cost more, simple flats less.`,
    },
    {
      q: `Is an EICR a legal requirement for landlords?`,
      a: `Yes. Since 2020, all private rented properties in England must have a current EICR (renewed every 5 years). Wales, Scotland and Northern Ireland have similar regulations. Failure to provide a valid EICR exposes the landlord to fines up to £30,000 per property.`,
    },
    {
      q: `What does a C1, C2, C3 or FI mean on an EICR?`,
      a: `C1 = danger present, requires immediate action. C2 = potentially dangerous, requires urgent remedial work. C3 = improvement recommended (not a fail). FI = further investigation required. C1 and C2 mark the report Unsatisfactory.`,
    },
    {
      q: `Who can perform an EICR in ${args.d.town}?`,
      a: `Any electrician registered with NICEIC, NAPIT or ELECSA. Always ask for their registration number and verify it on the relevant register before booking.`,
    },
  ];
}

export function rewireFAQs(args: {
  d: District;
  rewirePrice: number;
}): FAQ[] {
  return [
    {
      q: `How much does a full house rewire cost in ${args.d.town}?`,
      a: `A 3-bed property rewire in ${args.d.town} typically costs ${fmtMoney(args.rewirePrice)} in 2026, depending on the property's age, accessibility, and whether floors and ceilings need lifting. Older Victorian and Edwardian homes can run 15–25% over this baseline.`,
    },
    {
      q: `How long does a rewire take?`,
      a: `A 3-bed rewire usually takes 5–10 working days. The first 2–3 days are first-fix (cables in walls), then plastering / making good, then second-fix (sockets, switches, light fittings). You can typically remain in the home, though kitchen and bathroom days are disruptive.`,
    },
    {
      q: `When does a property need rewiring?`,
      a: `Common triggers: rubber, lead or fabric-insulated cabling (pre-1965); a fuse box with rewireable fuses rather than MCBs; round-pin sockets; a previous EICR returning C1 or multiple C2 codes; or major refurbishment. Many ${args.d.town} properties built before 1980 are due rewiring.`,
    },
    {
      q: `Do I need a building regulations notification for a rewire?`,
      a: `Yes. Major electrical work in a UK home is notifiable under Part P. A registered electrician (NICEIC / NAPIT / ELECSA) can self-certify and lodge the notification with the local authority for you.`,
    },
  ];
}

export function emergencyElectricianFAQs(args: {
  d: District;
  callout: number;
}): FAQ[] {
  return [
    {
      q: `How much does an emergency electrician cost in ${args.d.town}?`,
      a: `In ${args.d.town} the typical emergency electrician callout in 2026 is around ${fmtMoney(args.callout)}, plus an hourly rate once on site. Out-of-hours rates apply 18:00–07:00 and at weekends.`,
    },
    {
      q: `My fuse box keeps tripping — what should I do first?`,
      a: `Switch off everything plugged in, then reset the breaker once. If it trips again immediately, that suggests a hard fault — stop and call an electrician. If it holds, plug appliances back in one at a time until it trips; the last one connected is the likely fault.`,
    },
    {
      q: `Is the power cut a job for the electrician or the network operator?`,
      a: `If your whole street is dark, it's the local Distribution Network Operator (e.g. UK Power Networks, SSEN, National Grid Electricity Distribution). Call 105 free from any phone. If only your home is dark, that's an electrician's job.`,
    },
    {
      q: `Will an emergency electrician issue a certificate for the work?`,
      a: `Yes. After any notifiable work an electrician must issue a Minor Works or Electrical Installation Certificate. Keep these for the property file — landlords need them, future buyers' surveyors will ask.`,
    },
  ];
}

export function consumerUnitFAQs(args: {
  d: District;
  cuPrice: number;
}): FAQ[] {
  return [
    {
      q: `How much does a new fuse box cost in ${args.d.town}?`,
      a: `A consumer unit (modern fuse box) replacement in ${args.d.town} typically costs ${fmtMoney(args.cuPrice)} in 2026. The variation depends on existing earthing, RCBO vs RCD specification, and whether SPD (surge protection) is added.`,
    },
    {
      q: `When does a fuse box need replacing?`,
      a: `Common triggers: wooden-backed fuse boxes (pre-1980), units without RCDs, units that lack the 18th Edition update (pre-2018), or a property having a major rewire. Insurance and EICR reports flag these.`,
    },
    {
      q: `RCBOs vs RCDs — which is better?`,
      a: `RCBOs (one per circuit) isolate only the faulty circuit when there's an issue. RCDs cover multiple circuits at once, so one fault knocks out half the house. RCBOs cost more but are now the default in modern installs.`,
    },
    {
      q: `Will I be without power for the whole day?`,
      a: `Most fuse box swaps take 4–6 hours. The electrician usually phases the work to keep the fridge running where possible.`,
    },
  ];
}

export function boilerServiceFAQs(args: {
  d: District;
  servicePrice: number;
}): FAQ[] {
  return [
    {
      q: `How much does a boiler service cost in ${args.d.town}?`,
      a: `A standard annual boiler service in ${args.d.town} costs around ${fmtMoney(args.servicePrice)} in 2026. Combi services cost less than system or regular boilers (more components to test).`,
    },
    {
      q: `Do I really need a boiler service every year?`,
      a: `Manufacturers' warranties usually require an annual service to remain valid. Beyond the warranty, a service catches scale, blocked condensate traps and worn parts before they become emergency callouts in winter.`,
    },
    {
      q: `Who is qualified to service a boiler in ${args.d.town}?`,
      a: `Anyone working on gas appliances must be Gas Safe registered. Always ask to see the engineer's Gas Safe ID card on the day. The card lists which appliance categories they're qualified to work on.`,
    },
    {
      q: `What does a boiler service actually involve?`,
      a: `A proper service includes a flue gas analysis, condensate trap clean, internal seal and electrode check, water pressure check, and confirmation of the gas inlet pressure. Anything shorter than 30 minutes is unlikely to be thorough.`,
    },
  ];
}

export function boilerRepairFAQs(args: {
  d: District;
  repairPrice: number;
  callout: number;
}): FAQ[] {
  return [
    {
      q: `How much does a boiler repair cost in ${args.d.town}?`,
      a: `A typical boiler repair in ${args.d.town} costs ${fmtMoney(args.repairPrice)} in 2026, including the callout (around ${fmtMoney(args.callout)}) and parts. Major repairs (heat exchanger, PCB) cost considerably more.`,
    },
    {
      q: `When is it cheaper to replace than repair?`,
      a: `Rule of thumb: if the repair quote is more than half the cost of a new boiler, and the existing boiler is over 10 years old, replacement is usually the better economic choice.`,
    },
    {
      q: `My boiler error code says F22 / F75 / F1 — what does it mean?`,
      a: `Codes vary by brand. Common ones: F22/F1 = low water pressure, top up via the filling loop. F75 = pump or pressure sensor (Worcester / Vaillant). E168 = generic fault, needs an engineer. Always cross-check the code with the manufacturer's manual before paying for a callout.`,
    },
    {
      q: `Should I claim on my home insurance for the boiler repair?`,
      a: `Standard contents/buildings insurance rarely covers boiler breakdown. A separate Home Emergency policy or boiler service plan (British Gas, HomeServe, Hometree) does — but check the per-incident excess.`,
    },
  ];
}

export function newBoilerInstallFAQs(args: {
  d: District;
  combiPrice: number;
}): FAQ[] {
  return [
    {
      q: `How much does a new boiler cost in ${args.d.town}?`,
      a: `A new combi boiler installation in ${args.d.town} typically costs ${fmtMoney(args.combiPrice)} in 2026 fitted, depending on brand (Worcester / Vaillant / Ideal), output (24 / 30 / 42 kW) and whether the flue / pipework needs reconfiguring.`,
    },
    {
      q: `Combi vs system vs regular — which do I need?`,
      a: `Combi: 1 bathroom, no hot-water cylinder, hot water on demand. System: 2+ bathrooms, hot-water cylinder, mains-pressure showers. Regular (heat-only): older homes with cold-water tank in loft. Most ${args.d.town} 2-3 bed homes do well on a combi.`,
    },
    {
      q: `What warranty should a new boiler come with?`,
      a: `8–10 years is now standard for top brands when installed by an accredited installer (Worcester Accredited, Vaillant Advance, Ideal Max). Use a non-accredited installer and that drops to 5–7 years.`,
    },
    {
      q: `Are there grants towards a new boiler in ${args.d.town}?`,
      a: `For a like-for-like gas boiler, no — the BUS scheme funds heat pumps and biomass only. If you're switching from gas to a heat pump, you can claim £7,500 (or £9,000 from July 2026 if replacing oil/LPG).`,
    },
  ];
}

export function heatPumpInstallerFAQs(args: {
  d: District;
  hpPrice: number;
}): FAQ[] {
  return [
    {
      q: `How much does a heat pump installation cost in ${args.d.town}?`,
      a: `A typical air source heat pump installation in ${args.d.town} costs around ${fmtMoney(args.hpPrice)} in 2026 before grants. After the £7,500 Boiler Upgrade Scheme grant — or £9,000 from July 2026 for oil/LPG replacement — the net cost falls accordingly.`,
    },
    {
      q: `Do I need an MCS-certified installer to claim the BUS grant?`,
      a: `Yes. The BUS application is installer-led and only MCS-certified installers can lodge the claim. Choose an MCS installer in ${args.d.town} or your installer applies on your behalf — either way, MCS certification is mandatory.`,
    },
    {
      q: `Will my house need new radiators?`,
      a: `Often yes. Heat pumps run at lower flow temperatures than gas boilers, so existing radiators may not output enough heat at 45–55°C. A heat-loss survey establishes which rooms need bigger radiators or underfloor heating.`,
    },
    {
      q: `How long does a heat pump install take?`,
      a: `Typical installs run 2–5 days for a 3-bed home, plus an upfront site survey week or two before. Larger jobs with substantial radiator upgrades or new pipework can stretch to 7–10 days.`,
    },
  ];
}
