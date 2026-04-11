# Notebook 03 — ARF Calculator (ARR 2019)

> **Related article:** _Areal Reduction Factors in Python — ARR 2019 Compliant_ (coming soon)

## What this notebook does

Implements the ARR 2019 Book 2 Areal Reduction Factor (ARF) equations for all 11 Australian regions, with `scipy.interpolate` handling the duration interpolation between short and long duration equations.

Includes a standalone importable module (`arr_arf_functions.py`) for use in automated design rainfall workflows.

## Why it matters

ARFs are required whenever design rainfall depths need to be converted from point estimates to catchment-average estimates. Automated URBS/RORB pre-processing workflows need ARF calculations without opening a spreadsheet. This notebook provides a documented, validated Python implementation of the ARR Book 2 equations.

## Contents

```
03_arf_calculator/
├── README.md
├── arf_calculator.ipynb            # main notebook (to be created)
├── arr_arf_functions.py            # standalone importable module (to be created)
└── data/
    └── README.md
```

## Dependencies

```
numpy
scipy
pandas
matplotlib
```

## Validation

Validated against the 11 test cases in ARR Book 2 Chapter 6.5.3. Results are tabulated in the notebook.

## Importable module

`arr_arf_functions.py` can be imported directly into other scripts:

```python
from arr_arf_functions import calculate_arf
arf = calculate_arf(area_km2=150, duration_min=360, region='East_Coast')
```

## Status

- [ ] Notebook written
- [ ] `arr_arf_functions.py` written
- [ ] Validated against ARR Book 2 Chapter 6.5.3 test cases
- [ ] Figures exported to /images/
- [ ] Article published
