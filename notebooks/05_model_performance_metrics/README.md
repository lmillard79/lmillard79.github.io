# Notebook 05 — Model Performance Metrics Beyond NSE

> **Related article:** _Is Nash-Sutcliffe Efficiency Enough? A Python Comparison of Calibration Metrics for Australian Flood Models_ (coming soon)

## What this notebook does

Implements NSE, KGE (Kling-Gupta Efficiency), PBIAS, and peak flow bias in Python. Applies all four metrics to synthetic URBS-style outputs and demonstrates how the same model run can look good on one metric and poor on another.

Key reference:

> Gupta, H.V., Kling, H., Yilmaz, K.K. and Martinez, G.F. (2009). Decomposition of the mean squared error and NSE: Implications for improving hydrological modelling. *Journal of Hydrology* 377(1–2): 80–91.

## Why it matters

High NSE values are routinely produced by automated calibration on models that are physically unrealistic. NSE is dominated by high flows and insensitive to timing and volume errors in the low-to-medium flow range. This notebook shows what each metric measures and which combination is most diagnostic for ARR 2019 calibration reporting.

## Contents

```
05_model_performance_metrics/
├── README.md
├── model_performance_metrics.ipynb # main notebook (to be created)
└── data/
    └── README.md
```

## Dependencies

```
numpy
pandas
matplotlib
```

## Validation

Applied to synthetic URBS outputs with known deficiencies — volume error, timing error, and peak bias — to demonstrate the diagnostic power of each metric.

## Status

- [ ] Notebook written
- [ ] Synthetic URBS outputs generated
- [ ] Figures exported to /images/
- [ ] Article published
