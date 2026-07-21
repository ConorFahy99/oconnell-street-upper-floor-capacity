# O'Connell Street Upper Floor Capacity

**How much space is sitting unused above Dublin's most famous street?**

This project uses LiDAR height data and building footprints to estimate the total upper floor area across every building on the O'Connell Street corridor, and what it could theoretically accommodate if converted to residential use.

**[View the interactive map](https://conorfahy99.github.io/oconnell-street-upper-floor-capacity/04_outputs/deliverables/oconnell_missing_floors_interactive.html)**: click any building to see its height, floor count, upper floor area, and equivalent apartment count.

---

## The idea

Dublin has a housing crisis. It also has a city centre full of buildings where the ground floor is active retail or commercial use, and the floors above are either empty or in unknown use. The question this project tries to answer is: at the scale of O'Connell Street, how big is that opportunity?

Rather than relying on planning documents or vacancy surveys (which don't exist at building level for this area), the analysis works from first principles: LiDAR gives us building heights, heights give us estimated floor counts, floor counts give us upper floor area.

---

## Findings

| | |
|---|---|
| **206** | Opportunity buildings |
| **234,254 m²** | Total upper floor area |
| **3,028** | Equivalent 2-bed apartments (at 75 m² each) |

Buildings in hotel, civic, religious, office, or residential use are excluded. The 206 figure covers retail, commercial, and unclassified buildings where the upper floors exist in the LiDAR data but aren't attributed to any active use.

3,028 equivalent units is roughly 12% of Dublin City Council's annual housing target for the entire city, on a single corridor, in buildings that already exist.

---

## Maps

![The Missing Floors: O'Connell Street Corridor](04_outputs/deliverables/oconnell_missing_floors_A3.png)

*Each building is coloured by the number of equivalent 2-bed apartments its upper floors could accommodate. Grey buildings are excluded use classes (hotels, offices, civic, religious, residential).*

**[View the interactive map →](https://conorfahy99.github.io/oconnell-street-upper-floor-capacity/04_outputs/deliverables/oconnell_missing_floors_interactive.html)**

Click any building to see its height, estimated floor count, upper floor area, and equivalent apartment count.

---

## How it works

**Height data** comes from the GSI National LiDAR Programme (two DSM tiles covering Dublin city centre). A constant 4m ground elevation is subtracted to get above-ground heights. O'Connell Street is extremely flat, so this introduces minimal error.

**Floor counts** are estimated at one floor per 3.5m of above-ground height, cross-referenced against OSM `building:levels` tags where available.

**Upper floor area** = footprint area × (floors − 1). The ground floor is excluded on the assumption it's in active use.

**Use classification** comes from OSM building and amenity tags, supplemented by a spatial join of amenity POI data to reclassify buildings tagged as unknown.

The 234,254 m² figure is a ceiling: structural capacity, not confirmed vacancy. It doesn't distinguish empty floors from floors in active non-residential use.

---

## Tools

- **QGIS** for map styling, zonal statistics, and print layout
- **Python** (GeoPandas, Rasterio, Shapely) for LiDAR processing, data cleaning, and interactive map generation
- **Leaflet.js** for the interactive map
- **OpenStreetMap / Overpass API** for building footprints and amenity data
- **GSI National LiDAR Programme** for DSM source data

---

## Project structure

```
├── 01_data/
│   ├── raw/osm/                          # OSM building and amenity data
│   └── processed/
│       ├── oconnell_buildings.gpkg        # Master analysis layer (269 buildings)
│       └── study_area.gpkg
├── 02_qgis/                              # QGIS project file
├── 03_analysis/
│   ├── 01_prepare_lidar.py               # DSM merge, CRS fix, nDSM generation
│   └── 02_amenity_reclassify.py          # Spatial join reclassification
├── 04_outputs/deliverables/
│   ├── oconnell_missing_floors_A3.pdf    # Print map
│   └── oconnell_missing_floors_interactive.html
└── 05_docs/
    └── pitch_summary.md                  # Written analysis summary
```

---

## Author

**Conor Fahy**  
MSc Geospatial Data Analysis, University College Dublin  
[conorbrianfahy@gmail.com](mailto:conorbrianfahy@gmail.com)
