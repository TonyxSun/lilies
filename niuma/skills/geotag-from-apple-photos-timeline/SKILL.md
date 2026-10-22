---
name: Geotag from Apple Photos + Timeline
description: >-
  Use when geotagging Sony/camera JPGs with Apple Photos (iCloud) GPS as
  priority and Google Timeline as fallback — including ±2 min matches,
  same-place dwell/sticky rules, dry-run first, required post-tag report, no RAW
  edits.
---
# Geotag Sony photos: Apple Photos (iCloud) first, Google Timeline fallback

Assign GPS to camera JPGs (default: not RAW) using **two sources**, with a strict priority. **Do not write GPS until the user approves** after a dry-run report, unless they explicitly say to apply.

After every **apply** (and after every dry-run), deliver the **Post-tag report** below. That report is required — not optional.

## Priority (highest first)

1. **Apple Photos / iCloud geotagged media** (iPhone photos *and* videos with location)
2. **Google Maps Timeline** track
3. Leave unmarked / report if neither can place the shot

## Inputs

| Input | Required | Notes |
|-------|----------|-------|
| **Sony photo folder** | Yes | JPGs to label; exclude `._*` |
| **Camera timezone** | Yes | For EXIF times with no TZ (e.g. `-04:00` EDT) |
| **Apple Photos library** | Yes for priority path | Photos automation (JXA) on Mac; or Photos.sqlite if Full Disk Access allows |
| **Timeline export** | Yes for fallback | `Timeline.json` / `location-history.json` |
| **Rule parameters** | No | Defaults below |

## Outputs (dry-run vs apply)

| Output | Dry-run (default first) | Apply |
|--------|-------------------------|-------|
| Anchor CSV from Photos | `{time, lat, lon, filename}` in trip window | same |
| Timeline GPX | derived track | same |
| Assignment CSV | per Sony file: rule, source, lat/lon, delta | same |
| **Post-tag report** | projected counts + spot-checks | verified counts + spot-checks (**required in chat**) |
| Summary file on disk | optional | write `geotag_apply_summary.txt` next to work files |
| Photo GPS tags | **not written** | written in place on JPGs; set `GPSProcessingMethod` to the rule id |

## Post-tag report (required)

Always send this to the user in chat after tagging (and the dry-run version before apply).

### 1. Headline result
- Folder path (short)
- **N / N** JPGs with GPS · **M** missing · RAW untouched (yes/no)
- Whether previous GPS was stripped first (if applicable)
- Camera timezone used

### 2. Counts by rule (table)

| Rule | Count |
|------|------:|
| `icloud_near_2min` | … |
| `icloud_dwell_interp` | … |
| `icloud_sticky_prev` | … |
| `icloud_sticky_next` | … |
| `timeline_fallback` | … |
| `unlocated` | … |

Also state **% iCloud-priority** vs Timeline (Rules A–D vs E).

### 3. Spot checks (3–6 rows)
Spread early / mid / late, plus one sticky example if any. Verify with `exiftool` **after** write.

### 4. Failures / caveats
- `unlocated` or failed writes
- AppleDouble `._*` ignored
- Access limits only if they affected the run

### 5. Artifacts
Assignment CSV, summary txt, Timeline GPX / Photos anchor CSV.

## Rules for each Sony photo at time `T`

Normalize `T` with the camera timezone. Build sorted **anchors** from Photos: geotagged items in `[trip_start, trip_end]`.

### Rule A — `icloud_near_2min` (highest)
If any anchor has `|t − T| ≤ 120 seconds` → use the **nearest** anchor’s lat/lon.

### Rule B — `icloud_dwell_interp`
`prev` = latest anchor `t ≤ T`, `next` = earliest `t ≥ T`.
If both exist **and** distance(prev, next) ≤ **200 m** **and** `(next.t − prev.t) ≤ 3 hours` → time-interpolate between prev and next.

### Rule C — `icloud_sticky_prev`
If A/B miss and `prev` exists and `(T − prev.t) ≤ 90 minutes` → use **prev**.
Tighten with Timeline when available: only sticky if Timeline displacement from `prev` to `T` ≤ **150 m**.

### Rule D — `icloud_sticky_next`
If still unmatched and `next` exists and `(next.t − T) ≤ 30 minutes` → use **next** (optional Timeline gate ≤ 150 m).

### Rule E — `timeline_fallback`
Else assign from Google Timeline at `T`.

### Rule F — `unlocated`
Neither source works → report; do not invent coordinates.

## Suggested defaults

| Parameter | Default |
|-----------|---------|
| near window | ±2 min |
| dwell max separation | 200 m |
| dwell max span | 3 h |
| sticky after prev | 90 min |
| sticky before next | 30 min |
| Timeline sticky gate | 150 m |
| GeoMaxIntSecs (Timeline) | 7200 |
| GeoMaxExtSecs (Timeline) | 1800 |

## Precision and safety (extras)
- Aim for the most specific pin (street, trail, overlook), never a city-center default.
- A reverse-geocoded place name can be a municipality, not a downtown (e.g. "Bar Harbor" covers Sand Beach / Thunder Hole).
- Clean the Timeline track first: drop teleport edges (>5 km in <20 min) before using it.
- Don't replace a coherent phone + Timeline block with a guessed landmark.
- City legs after the trip (e.g. Boston) get the same rules; refine to neighborhoods/streets, not one city pin.
- Back up EXIF before any write. Add a short `reason` per file in the assignment CSV.
- Photos access: JXA usually works; `Photos.sqlite` is readable once Full Disk Access is granted.

## Workflow

1. Inventory Sony JPGs (`DateTimeOriginal` min/max).
2. Export Photos anchors for that window.
3. Build Timeline track/GPX for the same window.
4. Assign every JPG → CSV + rule counts.
5. Dry-run Post-tag report; wait for apply unless already ordered.
6. Apply — optionally strip previous GPS; write GPS + `GPSProcessingMethod=<rule>`; leave RAW untouched; skip `._*`.
7. Verify on disk; Post-tag report in chat + summary file.

## What not to do
- Do not skip the Post-tag report.
- Do not write during planning unless apply was ordered.
- Do not prefer Timeline when Rule A–D matches.
- Do not use non-geotagged Photos as anchors.
- Do not trust `mdfind` alone for iCloud coverage.
- Do not modify `._*` or RAW by default.
