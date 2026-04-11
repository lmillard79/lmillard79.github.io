# Notebook 01 — Baseflow Separation Using the Lyne-Hollick Filter

> **Related article:** _Baseflow Separation Using the Lyne-Hollick Filter — A Python Implementation_ (coming soon)

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
├── baseflow_lyne_hollick.ipynb     # main notebook (to be created)
└── data/
    └── README.md                   # data source instructions
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

- [ ] Notebook written
- [ ] Validated against Ladson R reference
- [ ] Figures exported to /images/
- [ ] Article published
