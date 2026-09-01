# Notebook 01 — Baseflow Separation Using the Lyne-Hollick Filter

> **Related article:** [Baseflow Separation Using the Lyne-Hollick Filter — A Python Implementation](https://lmillard79.github.io/insights/2026/04/11/baseflow-separation-lyne-hollick-python.html)

## What this notebook does

Implements the Lyne-Hollick recursive digital filter for baseflow separation from daily streamflow records. Applies the method to a BOM gauge record and conducts a sensitivity analysis on the filter parameter α.

This is the Python translation of the standard Australian method described in:

> Ladson, A.R., Brown, R., Neal, B. and Nathan, R. (2013). A standard approach to baseflow separation using the Lyne and Hollick filter. *Australian Journal of Water Resources* 17(1): 25–34.

## Why it matters

Accurate baseflow separation is a prerequisite for URBS/RORB model calibration. The direct runoff volume used to calibrate loss parameters depends entirely on how baseflow is removed from the gauged record. The Ladson et al. (2013) method is the Australian standard; this notebook provides the Python implementation.

## Contents

```
01_baseflow_lyne_hollick/
├── README.md
└── baseflow_lyne_hollick.ipynb     # main notebook
```

## Dependencies

```
numpy
pandas
matplotlib
```

## Validation

Results are validated against the Ladson R implementation. Expected outputs for the sample gauge are documented in the notebook.

## Status

- [x] Notebook written
- [x] Validated against Ladson R reference (BFI = 0.3875 vs. reference 0.3879)
- [x] Figures exported to /images/
- [x] Article published
