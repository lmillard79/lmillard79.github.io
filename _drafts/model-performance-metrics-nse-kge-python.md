---
title: "Is Nash-Sutcliffe Efficiency Enough? A Python Comparison of Calibration Metrics for Australian Flood Models"
date: 2026-04-11
categories: [insights]
tags: [python, tutorial, hydrology, flood-modelling, urbs, statistics]
excerpt: "Automated calibration routinely produces high NSE values on models that are physically unrealistic. This post implements NSE, KGE, PBIAS, and peak flow bias in Python and shows how the same model run looks good on one metric and poor on another."
header:
  overlay_color: "#0f172a"
  overlay_filter: 0.7
  overlay_image: /images/pano1.jpg
read_time: true
---

<!-- COMPANION NOTEBOOK: notebooks/05_model_performance_metrics/model_performance_metrics.ipynb -->
<!-- STATUS: draft — notebook not yet written -->

## The legacy problem

_[Why NSE dominates despite its well-documented limitations — the Chiew and McMahon (1993) survey legacy]_

## Four metrics and what they each measure

_[NSE, KGE, PBIAS, peak flow bias — formulas and the engineering intuition behind each one]_

## Python implementation

_[Short code block — all four metrics. Full implementation in notebook.]_

## Applied to synthetic URBS outputs

_[Figure: four hydrograph scenarios, each with a different deficiency, scored by all four metrics]_

_[Table: which metric catches which problem?]_

## Recommended metric set for ARR 2019 calibration reporting

_[Practical recommendation: NSE + KGE + peak flow bias as a minimum set]_

## Limitations

_[What this does not do. Calibration objective functions vs diagnostic metrics. What practitioners should check.]_

---

**Companion notebook:** Full implementation at [`notebooks/05_model_performance_metrics/model_performance_metrics.ipynb`](https://github.com/lmillard79/lmillard79.github.io/tree/main/notebooks/05_model_performance_metrics).

**References:**
- Gupta, H.V., Kling, H., Yilmaz, K.K. and Martinez, G.F. (2009). Decomposition of the mean squared error and NSE: Implications for improving hydrological modelling. *Journal of Hydrology* 377(1–2): 80–91.
- Chiew, F.H.S. and McMahon, T.A. (1993). Assessing the adequacy of catchment streamflow yield estimates. *Australian Journal of Soil Research* 31(5): 665–680.
