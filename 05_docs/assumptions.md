# Modelling assumptions

Document assumptions here so they can be stated clearly in the pitch.

## Floor height
- **Value used:** 3.5m per floor (floor-to-floor)
- **Rationale:** Standard assumption for mixed commercial/historic stock. Residential is typically 2.8–3.0m; commercial ground floors and civic buildings often 4–5m. 3.5m is a conservative middle estimate for this building stock.
- **Risk:** Double-height ground floors (e.g. GPO, banks) will cause overestimation of floor count. The GPO's main hall is significantly taller than 3.5m, so `estimated_floors` there may overcount usable residential floors.
- **Mitigation:** Use OSM `building:levels` tag where available; treat LiDAR-derived counts as estimates.

## Apartment size benchmark
- **Value used:** 75m² per unit
- **Rationale:** Approximate average for a 2-bed apartment. Consistent with Irish apartment design standards.
- **Risk:** O'Connell Street floor plates are wide and deep: actual unit mix would depend on subdivision. 75m² may underestimate unit yield if efficient layouts are used.

## Upper floor use
- **Assumption:** Where no data on upper floor use exists in OSM or DCC data, the floor is classified as "unknown": NOT confirmed vacant.
- **Rationale:** Avoids overclaiming. Some buildings may have active office use not captured in open data.
- **Mitigation:** Ground-truth survey or DCC rates data would reduce unknowns.

## OSM completeness
- **Assumption:** OSM building coverage in central Dublin is reasonable but not complete.
- **Action:** Manual check against aerial imagery (QuickMapServices in QGIS) recommended before finalising.
