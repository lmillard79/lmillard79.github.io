# Notebook 06 — FFA Non-Stationarity Diagnostic

> **Related article:** [Was That Flood an Outlier? A Python Diagnostic for Non-Stationarity in Flood Frequency Analysis](https://lmillard79.github.io/insights/2026/09/01/ffa-nonstationarity-outlier-diagnostic-python.html)

## What this notebook does

Three diagnostics for the "is this event actually unusual, or does it just feel that way" question in flood frequency analysis:

1. A stationary Log-Pearson III fit (`scipy.stats.pearson3` on log10-transformed annual maxima — the standard ARR 2019 / Bulletin 17C at-site approach).
2. A from-scratch Mann-Kendall trend test, validated against a known-stationary and a known-trended synthetic series before being trusted for anything else.
3. A percentile/AEP diagnostic: what annual exceedance probability would a *stationary*, historical-only model assign to a new or recent event?

**Data note:** every series here is synthetically generated, not an observed gauge record — see the notebook's own opening cell for why, and what that does and doesn't mean for the results. This validates the methods; it doesn't make a claim about any specific real catchment. The motivating real-world example — the 2024 Kedron Brook Flood Study's sensitivity analysis around the 2022 Brisbane flood events — is discussed and linked in the notebook and companion article, but its underlying gauge data was not available to reproduce here.

## Why it matters

"Unprecedented" gets used loosely in flood risk communication. This notebook is the Python mechanics behind turning that into an actual, checkable number — and behind being honest about what such a number can and can't establish, particularly the line between a non-stationarity diagnostic and formal climate attribution (a different discipline, with different tools).

## Contents

```
06_ffa_nonstationarity_diagnostic/
├── README.md
├── ffa_nonstationarity_diagnostic.ipynb   # main notebook
└── data/                                   # empty — no external data; series are generated in-notebook
```

## Dependencies

```
numpy
scipy
matplotlib
```

## Validation

The Mann-Kendall implementation is self-validated in the notebook: it's run against a known-stationary control series (must NOT show a significant trend) and a known-trended series (must show one), with both checks asserted in-notebook rather than just eyeballed.

## Status

- [x] Notebook written
- [x] Mann-Kendall implementation self-validated (correctly distinguishes control vs. trended series)
- [x] Figures exported to /images/
- [x] Article published
