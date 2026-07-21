"""
01_prepare_lidar.py

Merges two DSM tiles from the GSI National LiDAR Programme, assigns EPSG:2157,
masks fill values, and writes a clean nDSM (above-ground heights) clipped to
the study area.

Inputs:
    01_data/raw/lidar/DSM_30795.tif
    01_data/raw/lidar/DSM_31019.tif
    01_data/processed/study_area.gpkg

Output:
    01_data/raw/lidar/DSM_merged_fixed.tif   -- merged, CRS-corrected DSM
    01_data/processed/nDSM_clipped.tif       -- nDSM clipped to study area
"""

import numpy as np
import rasterio
from rasterio.merge import merge
from rasterio.mask import mask
from rasterio.crs import CRS
import geopandas as gpd
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
RAW_LIDAR    = PROJECT_ROOT / "01_data/raw/lidar"
PROCESSED    = PROJECT_ROOT / "01_data/processed"

GROUND_ELEVATION_M = 4.0   # constant ground level for O'Connell Street (m above Malin Head)
NODATA_VALUE       = -9999
MIN_VALID_HEIGHT   = 0.5   # pixels below this are treated as fill/ground


def merge_and_fix_dsm():
    tile_paths = [RAW_LIDAR / "DSM_30795.tif", RAW_LIDAR / "DSM_31019.tif"]
    datasets = [rasterio.open(p) for p in tile_paths]

    merged, transform = merge(datasets)
    meta = datasets[0].meta.copy()
    meta.update({
        "driver": "GTiff",
        "height": merged.shape[1],
        "width":  merged.shape[2],
        "transform": transform,
        "crs": CRS.from_epsg(2157),
        "nodata": NODATA_VALUE,
        "compress": "lzw",
    })

    # Mask fill values (stored as 0 in source tiles — no NoData set)
    data = merged[0].astype(np.float32)
    data[data < MIN_VALID_HEIGHT] = NODATA_VALUE

    out_path = RAW_LIDAR / "DSM_merged_fixed.tif"
    with rasterio.open(out_path, "w", **meta) as dst:
        dst.write(data, 1)

    for ds in datasets:
        ds.close()

    print(f"Merged DSM written: {out_path}")
    valid = data[data != NODATA_VALUE]
    print(f"  Valid pixels: {len(valid):,} ({len(valid)/data.size*100:.1f}%)")
    print(f"  Height range: {valid.min():.1f} – {valid.max():.1f} m")
    return out_path


def create_ndsm(dsm_path):
    study_area = gpd.read_file(PROCESSED / "study_area.gpkg")
    shapes = [geom.__geo_interface__ for geom in study_area.geometry]

    with rasterio.open(dsm_path) as src:
        clipped, transform = mask(src, shapes, crop=True, nodata=NODATA_VALUE)
        meta = src.meta.copy()

    data = clipped[0].astype(np.float32)

    # Subtract constant ground elevation to get above-ground heights
    valid_mask = data != NODATA_VALUE
    data[valid_mask] -= GROUND_ELEVATION_M
    data[data < 0] = NODATA_VALUE   # clip any sub-zero artefacts

    meta.update({
        "height": data.shape[0],
        "width":  data.shape[1],
        "transform": transform,
        "nodata": NODATA_VALUE,
        "compress": "lzw",
    })

    out_path = PROCESSED / "nDSM_clipped.tif"
    with rasterio.open(out_path, "w", **meta) as dst:
        dst.write(data, 1)

    print(f"nDSM written: {out_path}")
    valid = data[data != NODATA_VALUE]
    print(f"  Above-ground height range: {valid.min():.1f} – {valid.max():.1f} m")
    return out_path


if __name__ == "__main__":
    dsm_path = merge_and_fix_dsm()
    create_ndsm(dsm_path)
