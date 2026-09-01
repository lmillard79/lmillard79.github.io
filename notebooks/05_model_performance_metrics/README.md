# Notebook 05 — Model Performance Metrics Beyond NSE

> **Related article:** [Is Nash-Sutcliffe Efficiency Enough? A Python Comparison of Calibration Metrics for Australian Flood Models](https://lmillard79.github.io/insights/2026/04/18/model-performance-metrics-nse-kge-python.html)

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
└── model_performance_metrics.ipynb # main notebook
```

Section 10 of the notebook (LYR RORB calibration application) is an intentional
placeholder for a specific client project's real data and is not part of the
published article -- see the notebook itself for what's needed to complete it.

## Dependencies

```
numpy
pandas
matplotlib
```

## Validation

Applied to synthetic URBS outputs with known deficiencies — volume error, timing error, and peak bias — to demonstrate the diagnostic power of each metric.

## Status

- [x] Notebook written
- [x] Synthetic URBS outputs generated
- [x] Figures exported to /images/
- [x] Article published
- [ ] LYR RORB calibration application (Section 10) — needs real project data, out of scope for the article
