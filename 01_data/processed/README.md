# Processed data

Cleaned, reprojected, clipped, and analysis-ready layers. All files here derived from raw inputs.
All layers in EPSG:2157 (ITM).

## Expected files (in workflow order)

| File | Description |
|---|---|
| `study_area.gpkg` | Study area polygon: ~400m × 300m centred on O'Connell St / Henry St junction |
| `nDSM_clipped.tif` | DSM minus DTM, clipped to study area: above-ground height raster |
| `osm_buildings_clipped.gpkg` | OSM building footprints clipped to study area, cleaned |
| `osm_poi_clipped.gpkg` | OSM POIs clipped to study area |
| `oconnell_buildings.gpkg` | **Main analysis layer**: buildings with height, floor count, ground use, upper floor area attributes |

## Key attribute fields (oconnell_buildings.gpkg)
- `height_m`: zonal max from nDSM (or OSM building:height if present)
- `osm_levels`: building:levels tag from OSM (where present)
- `estimated_floors`: ROUND(height_m / 3.5); use osm_levels if available
- `footprint_area_m2`: polygon area in m²
- `gross_floor_area_m2`: footprint_area_m2 × estimated_floors
- `upper_floor_area_m2`: footprint_area_m2 × (estimated_floors − 1)
- `gf_use`: ground floor use category (retail_active, retail_vacant, food_bev, office, civic, unknown)
- `missing_floors_flag`: boolean; True where upper floor area is large and gf_use suggests low activity
