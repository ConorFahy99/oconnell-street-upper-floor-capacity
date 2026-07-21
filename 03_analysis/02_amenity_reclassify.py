"""
02_amenity_reclassify.py

Spatially joins OSM amenity points to building polygons and reclassifies
buildings with use_class = 'unknown' where a matching amenity point falls
within the footprint.

Inputs:
    01_data/processed/oconnell_buildings.gpkg     -- master buildings layer
    01_data/raw/osm/osm_amenity_clipped.gpkg      -- OSM amenity points

Output:
    01_data/processed/oconnell_buildings.gpkg     -- updated in place
    (use_class field updated for matched buildings)
"""

import geopandas as gpd
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
PROCESSED    = PROJECT_ROOT / "01_data/processed"
RAW_OSM      = PROJECT_ROOT / "01_data/raw/osm"

AMENITY_TO_CLASS = {
    # Retail / food & drink
    "restaurant":    "retail",
    "cafe":          "retail",
    "fast_food":     "retail",
    "pub":           "retail",
    "bar":           "retail",
    "marketplace":   "retail",
    "casino":        "retail",
    "pharmacy":      "retail",
    "internet_cafe": "retail",
    # Civic / community
    "college":         "civic",
    "school":          "civic",
    "language_school": "civic",
    "music_school":    "civic",
    "theatre":         "civic",
    "police":          "civic",
    "post_office":     "civic",
    "social_facility": "civic",
    "doctors":         "civic",
    "dentist":         "civic",
    # Religious
    "place_of_worship": "religious",
}

# Amenity values that are street furniture / not building uses
EXCLUDE_AMENITIES = {
    "bench", "waste_basket", "recycling", "bicycle_parking",
    "parking", "parking_entrance", "atm", "post_box",
    "vending_machine", "telephone", "drinking_water",
}


def reclassify():
    buildings = gpd.read_file(PROCESSED / "oconnell_buildings.gpkg")
    amenities = gpd.read_file(RAW_OSM / "osm_amenity_clipped.gpkg")

    print(f"Buildings loaded: {len(buildings)}")
    print(f"Amenity points loaded: {len(amenities)}")

    # Drop street furniture
    amenities = amenities[~amenities["amenity"].isin(EXCLUDE_AMENITIES)].copy()
    print(f"Amenity points after excluding street furniture: {len(amenities)}")

    # Ensure matching CRS
    if amenities.crs != buildings.crs:
        amenities = amenities.to_crs(buildings.crs)

    # Spatial join: amenity points within building polygons
    joined = gpd.sjoin(amenities, buildings, how="inner", predicate="within")
    print(f"Amenity points matched to buildings: {len(joined)}")

    # For each matched building, take the first amenity hit
    matched = joined.groupby("index_right").first().reset_index()
    matched = matched.rename(columns={"index_right": "building_idx"})

    reclassified = 0
    for _, row in matched.iterrows():
        idx = row["building_idx"]
        amenity_val = row["amenity"]
        new_class = AMENITY_TO_CLASS.get(amenity_val)

        # Only update buildings that are currently 'unknown'
        if new_class and buildings.at[idx, "use_class"] == "unknown":
            buildings.at[idx, "use_class"] = new_class
            reclassified += 1

    print(f"Buildings reclassified: {reclassified}")
    print(f"use_class distribution after reclassification:")
    print(buildings["use_class"].value_counts().to_string())

    buildings.to_file(PROCESSED / "oconnell_buildings.gpkg", driver="GPKG")
    print(f"\nUpdated layer written: {PROCESSED / 'oconnell_buildings.gpkg'}")


if __name__ == "__main__":
    reclassify()
