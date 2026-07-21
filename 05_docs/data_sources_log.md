# Data sources log

Record each dataset as you download it.

| Dataset | Source | URL | Date downloaded | Format | CRS | Notes |
|---|---|---|---|---|---|---|
| OSM building footprints | OpenStreetMap / QuickOSM | - | | .gpkg | EPSG:4326 → reproject to 2157 | Query: `building=*` |
| OSM POIs | OpenStreetMap / QuickOSM | - | | .gpkg | EPSG:4326 → reproject to 2157 | Query: `shop=*`, `amenity=*`, `office=*` |
| EPA LiDAR DSM | EPA National LiDAR Programme | https://www.epa.ie/... | | .tif | Check on download | Dublin tile |
| EPA LiDAR DTM | EPA National LiDAR Programme | https://www.epa.ie/... | | .tif | Check on download | Dublin tile |
| DCC commercial data | data.gov.ie | https://data.gov.ie/organization/dublin-city-council | | | | |
| CSO SAPS 2022 | CSO | https://www.cso.ie | | .csv | - | Small area population statistics |
| CSO Small Area boundaries | CSO | https://www.cso.ie | | .gpkg/.shp | EPSG:2157 | 2022 boundaries |
