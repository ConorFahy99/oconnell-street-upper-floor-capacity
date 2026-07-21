# The Missing Floors: Vertical Underutilisation on the O'Connell Street Corridor

**Prepared by:** Conor Fahy  
**Date:** June 2026  
**Data sources:** OSM building footprints, GSI National LiDAR Programme  

---

## The problem

Dublin's housing crisis shows up in planning applications and rental listings. It's less visible from the street. Walk the length of O'Connell Street and you see a grand civic boulevard lined with commercial frontages. What you don't see is floor after floor of empty space above those shopfronts, in the middle of the city, on a street with good transport links and building structure already in place.

This analysis puts numbers on that for the first time, at building level, using LiDAR height data and OSM building footprints.

---

## What the data shows

Across the O'Connell Street corridor (Parnell Square to O'Connell Bridge, including Henry Street and the surrounding block) the analysis identifies:

| Metric | Value |
|---|---|
| Opportunity buildings | **206** |
| Total upper floor area | **234,254 m²** |
| Equivalent 2-bed apartments (at 75 m²) | **3,028** |

Hotels, civic buildings, churches, offices, and residential buildings are excluded. The 206 are in retail, commercial, or unclassified use, with upper floors that the LiDAR data shows exist but that aren't attributed to any active use.

The largest buildings each carry upper floor area equivalent to 234 to 333 two-bed units. Even the smallest in the 0 to 25 range represent meaningful infill at city-centre land values.

---

## Methodology

Building heights came from the GSI National LiDAR Programme DSM (Digital Surface Model), processed to remove ground elevation and clipped to the study area. Floor counts were estimated at one floor per 3.5 metres of above-ground height, cross-referenced against OSM `building:levels` tags where available. Upper floor area is:

> *footprint area × (estimated floors − 1)*

The analysis doesn't distinguish between vacant upper floors and upper floors in active non-residential use. The 234,254 m² figure is a ceiling: the total upper floor area across opportunity buildings, not a directly developable quantum. It measures what's structurally there.

---

## Why this matters

3,028 equivalent units is roughly 12% of Dublin City Council's annual housing target for the entire city, on a single corridor, in buildings that already exist. Converting or intensifying existing stock costs less than new build. Planning and infrastructure barriers are lower. Timeframes are shorter.

The corridor already has development interest and several buildings have live planning applications. What's missing is a view of the aggregate picture: what is the total scale of what's sitting unused, and where is it? Individual planning decisions get made without that context.

---

## The ask

Three things would sharpen this analysis considerably:

1. **Vacancy data.** Dublin City Council's GeoDirectory or Tailored Business Statistics could confirm which upper floors are genuinely vacant versus in active non-residential use.
2. **Planning history.** Cross-referencing against live and historical planning applications would show where permission already exists or has been refused.
3. **Ownership data.** Land Registry polygons would identify public, institutional, and fragmented private holdings, and therefore which intervention points are realistic.

The map with this summary shows the building-level picture. The orange buildings are not a planning aspiration. They are an evidence base.

---

*Analysis conducted in QGIS using Python (GeoPandas, Rasterio). All data open-source. Full methodology available on request.*
