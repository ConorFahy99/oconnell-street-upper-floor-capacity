# Project spec: The missing floors

**Working title:** The missing floors: vertical underutilisation on the O'Connell Street corridor  
**Pitch target:** David McRedmond, outgoing CEO, An Post  
**Format:** Building-level map with supporting analysis; deliverable as a print-ready A3 layout and a short written summary

---

## Objective

Map the gap between what the buildings on O'Connell Street *could* contain and what they actually contain. The argument: the housing opportunity McRedmond is calling for isn't a future construction project, it's already built, in the form of upper floors above retail units that are unused, underused, or entirely unoccupied. This analysis makes that visible at building level.

The GPO is the headline example McRedmond raised in the podcast. This project scales that observation across the entire O'Connell Street corridor.

---

## Core argument

O'Connell Street is lined with wide, multi-storey buildings. Ground floors are occupied by retail, fast food, or vacant units. Above them sit floors, in some cases four or five storeys, that are not residential, not clearly in active office use, and in many cases effectively dark. The total "missing" floorspace above ground level on this single street is likely significant. Making that number visible and spatial is the point.

---

## Study area

O'Connell Street and immediate surroundings: O'Connell Street Upper and Lower, Henry Street, Earl Street, Cathedral Street, Parnell Street (western end), and the GPO block. Approximately 400m × 300m area centred on the O'Connell Street / Henry Street junction.

This is intentionally tight. A focused, building-level analysis of one street is more persuasive than a coarse city-wide picture.

---

## Data sources

### Building footprints
| Source | Dataset | Notes |
|---|---|---|
| OpenStreetMap | Building footprints | Via QGIS QuickOSM plugin. Query: `building=*` within study area bounding box. Export as GeoPackage. |

OSM building coverage for central Dublin is good. Each polygon represents one building footprint. Some will already have `building:levels` or `building:height` tags, use these where present, fill gaps with LiDAR.

### Building heights
| Source | Dataset | Notes |
|---|---|---|
| EPA | National LiDAR Programme: Dublin tiles | Free download at [epa.ie/our-services/monitoring--assessment/assessment/mapping/national-lidar-programme](https://www.epa.ie/our-services/monitoring--assessment/assessment/mapping/national-lidar-programme/). Download both DSM (Digital Surface Model) and DTM (Digital Terrain Model) rasters for the Dublin tile. |

The EPA LiDAR programme provides 1m resolution DSM and DTM rasters for Ireland. Subtracting DTM from DSM gives a normalised DSM (nDSM), effectively a raster of above-ground heights. Buildings read as elevated areas; ground reads as zero. This is the source of building height data for footprints that don't have OSM tags.

### Ground floor use
| Source | Dataset | Notes |
|---|---|---|
| OpenStreetMap | POI / land use tags | OSM `shop=*`, `amenity=*`, `office=*` etc. within study area. Captures what's on the ground floor. Coverage in central Dublin is reasonable but will need manual checking. |
| Dublin City Council | Commercial rates / planning data | [data.gov.ie](https://data.gov.ie/organization/dublin-city-council): some vacancy and land use data available. Supplement OSM where possible. |

### Residential population
| Source | Dataset | Notes |
|---|---|---|
| CSO | SAPS 2022, Small Area boundaries | Confirms near-zero residential population in the study area. Used to frame the contrast: buildings tall enough for many residents, currently housing almost none. |

---

## Workflow

### Phase 1, Data preparation
1. Define study area as a polygon in QGIS. Use this to clip all subsequent layers.
2. Run QuickOSM query for `building=*` within the bounding box. Inspect results, check coverage, remove any obvious errors (very small slivers, duplicate polygons).
3. Download EPA LiDAR DSM and DTM tiles for Dublin. Load into QGIS. Use the **Raster Calculator** to compute:  
   `nDSM = DSM − DTM`  
   This gives above-ground height as a raster. Reproject to EPSG:2157 (ITM) if not already.
4. Clip nDSM to study area.

**CRS note:** Use EPSG:2157 (ITM) throughout. Reproject all inputs on import. The EPA LiDAR tiles may be in ITM already: check before proceeding.

### Phase 2, Building height and floor count
5. Run **Zonal Statistics** (Raster → Zonal Statistics) on the nDSM raster using the OSM building footprints as zones. Statistic: **maximum** (the highest point above ground within each building footprint). This gives `height_m` per building.
6. For buildings that already have `building:levels` in OSM, use that value directly. For all others, estimate floor count:  
   `estimated_floors = ROUND(height_m / 3.5)`  
   3.5m is a reasonable floor-to-floor height for the mixed commercial/historic stock on O'Connell Street. Flag this as an assumption.
7. Calculate gross floor area per building:  
   `gross_floor_area_m2 = footprint_area_m2 × estimated_floors`
8. Calculate upper floor area (everything above ground floor):  
   `upper_floor_area_m2 = footprint_area_m2 × (estimated_floors − 1)`

### Phase 3, Ground floor use classification
9. Join OSM POI/land use data to building footprints by spatial location. Classify each building's ground floor use into categories: retail (active), retail (vacant / charity shop / bookmaker), food & beverage, office, civic/institutional (GPO, banks), other.
10. Vacant or low-value ground floor use combined with multiple upper floors = highest priority "missing floors" buildings. Flag these.

### Phase 4, Analysis
11. Calculate total upper floor area across the study area. Express in m² and as an equivalent number of apartments (assume ~75m² per unit as a benchmark). This is the headline number for the pitch.
12. Identify the top 10 buildings by upper floor area that have no clear active upper-floor use. The GPO should feature prominently.
13. Join CSO small area population data to confirm near-zero residential population in the study area. Use as a framing stat: X,000m² of upper floor space, Y residents.

### Phase 5, Visualisation
14. Main map: building footprints coloured by estimated floor count, with ground floor use shown by a border or symbol. Study area at large scale, individual buildings legible.
15. Secondary map or chart: bar chart of upper floor area by building, top 20. GPO highlighted.
16. Inset: location map showing study area within Dublin.
17. Key stats panel: total upper floor area, equivalent apartment count, current residential population.
18. Compose A3 print layout in QGIS.

---

## Key outputs

- `oconnell_buildings.gpkg`: building footprints with height, floor count, ground use, and upper floor area attributes
- Main map (A3 PDF)
- Bar chart of upper floor area by building (PNG or embedded)
- 1-page written summary

---

## Stated limitations (include in pitch)

- **Floor count is estimated:** The 3.5m floor-to-floor assumption is reasonable but approximate. Buildings with mezzanines, double-height ground floors (like the GPO), or irregular floor plates will have errors. This is flagged as a modelling assumption, not a measured survey.
- **Upper floor use is partially inferred:** Where a building has no OSM or DCC data on upper floor use, it is classified as unknown: not confirmed vacant. Some buildings may have active office use that isn't captured in open data. A follow-up ground-truth survey (or DCC rates data) would improve this.
- **OSM completeness:** OSM building coverage in central Dublin is good but not perfect. Some buildings may be missing or have incorrect footprint geometry. A manual check against aerial imagery (available in QGIS via the QuickMapServices plugin) is recommended before finalising.

---

## Pitch framing

Three points:

1. **The housing is already built:** The upper floors of O'Connell Street represent a significant quantum of floorspace, estimated X,000m², equivalent to approximately Y apartments, that is not in residential use and in many cases not in any clearly active use.
2. **The GPO is the headline but not the only case:** Show the top 10 buildings. McRedmond knows the GPO argument; showing him that the same logic applies to a dozen other buildings on the same street extends his own argument.
3. **This is the fastest path to city centre housing:** Conversion of existing upper floors requires no new construction footprint, no greenfield land, and in many cases the structural shell already exists. Planning and political will are the constraints, not physical capacity.

---

## Suggested timeline

| Week | Work |
|---|---|
| 1 | Download EPA LiDAR tiles; load DSM/DTM; compute nDSM; download OSM building footprints |
| 2 | Zonal statistics for building heights; estimate floor counts; calculate floor areas |
| 3 | Ground floor use classification; identify top buildings; calculate headline stats |
| 4 | Map layout, bar chart, written summary, pitch document |
