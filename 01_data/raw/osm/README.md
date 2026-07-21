# OSM raw data

Source: OpenStreetMap via QGIS QuickOSM plugin.

## Queries to run
- `building=*` within study area bounding box → building footprints
- `shop=*`, `amenity=*`, `office=*` within study area → ground floor POIs

## Export format
GeoPackage (.gpkg), EPSG:2157 (ITM).

## Files expected here
- `osm_buildings_raw.gpkg`
- `osm_poi_raw.gpkg`
