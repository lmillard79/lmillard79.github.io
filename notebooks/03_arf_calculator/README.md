# Notebook 03 — ARR 2019 Areal Reduction Factors (Python port of Tony Ladson's R method)

> **Related article:** [Areal Reduction Factors in Python — a Port of Tony Ladson's ARR 2019 Method](https://lmillard79.github.io/insights/2026/09/01/arf-calculator-arr2019-python.html)
>
> **Original source:** [ARR2019 – Areal Reduction Factors](https://tonyladson.wordpress.com/2020/04/05/arr2019-areal-reduction-factors/) and [Areal reduction factors – some edge cases](https://tonyladson.wordpress.com/2020/04/14/arr2019-areal-reduction-factors-some-edge-cases/) — Tony Ladson, April 2020. R source: [gist.github.com/TonyLadson/fc870cf7ebfe39ea3d1a812bcc53c8fb](https://gist.github.com/TonyLadson/fc870cf7ebfe39ea3d1a812bcc53c8fb), [gist.github.com/TonyLadson/b8baac6c450fe7f32f5020eb496e8b62](https://gist.github.com/TonyLadson/b8baac6c450fe7f32f5020eb496e8b62)

## What this notebook does

A Python port of Ladson's complete ARR 2019 Book 2 Areal Reduction Factor implementation: both equations (short duration <=12h; long duration 24-168h across 10 climatological regions), the small-catchment (<10 km²) interpolation rule, the 12-24h interpolation logic, and full input validation. Checked directly against two exact values Ladson prints in his own script (`arf_short(26, 720, 0.0005) = 0.9377527`, `arf_long(26, 1440, 0.0005, 'Tasmania') = 0.9322746`) — both match to 7 decimal places.

## Why it matters

This resolves a previously stalled draft. An earlier attempt at this post had the short-duration equation reconstructed (unverified) from a third-party spreadsheet vendor, and an explicit TODO for the long-duration equation, its 10 regional coefficients, and the interpolation logic, because the ARR 2019 PDF wasn't directly accessible when that draft was written. Finding Ladson's real, working implementation (with two independently useful gists — the main calculator and a documented edge case) resolved all of it at once, including a real ARR 2019 quirk that isn't obvious from the standard alone: for some catchments, the short-duration ARF at 12h is briefly *larger* than the long-duration ARF at 24h.

## Contents

```
03_arf_calculator/
├── README.md
├── arf_calculator.ipynb   # main notebook
└── data/                   # empty — all coefficients are embedded in-notebook
```

## Dependencies

```
numpy
matplotlib
```

## Validation

- Both core equations checked against Ladson's own published output (exact match to 7 decimal places).
- Continuity across the 12h and 24h duration boundaries checked numerically (no discontinuity).
- Small-area (<10 km²) interpolation and area<=1 km² edge cases checked.
- Input validation (area, AEP, duration ranges; short-duration area>1000km² constraint) checked to raise correctly.
- The documented non-monotonic "downhill segment" edge case reproduced exactly.

## Status

- [x] Notebook written
- [x] Validated against Ladson's published R output (exact match)
- [x] Continuity, small-area, and validity-range edge cases checked
- [x] Figure exported to /images/
- [x] Article published
