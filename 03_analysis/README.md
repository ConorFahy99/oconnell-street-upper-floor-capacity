# Analysis outputs

Intermediate analysis results: tables, stats, exported attribute data.
Not final deliverables, those go in 04_outputs/.

## Expected files

| File | Description |
|---|---|
| `building_stats.csv` | Per-building table: name/OSM ID, footprint area, floors, upper floor area, gf use |
| `top20_upper_floor_area.csv` | Top 20 buildings ranked by upper_floor_area_m2 |
| `headline_stats.md` | Total upper floor area (m²), equivalent apartment count (@75m²/unit), current residential population |
| `ground_use_summary.csv` | Building count and total upper floor area by ground floor use category |

## Key numbers to calculate
- Total upper floor area (m²) across study area
- Equivalent apartment count: total_upper_floor_area_m2 / 75
- Residential population from CSO SAPS (expected: near zero)
