---
title: "Baseflow Separation Using the Lyne-Hollick Filter — A Python Implementation"
date: 2026-04-11
categories: [insights]
tags: [python, tutorial, hydrology, flood-modelling, urbs]
excerpt: "The standard Australian baseflow separation method exists only in R. This post provides the Python translation, applied to a BOM gauge record with a sensitivity analysis on the filter parameter α."
header:
  overlay_color: "#0f172a"
  overlay_filter: 0.7
  overlay_image: /images/pano1.jpg
read_time: true
---

<!-- COMPANION NOTEBOOK: notebooks/01_baseflow_lyne_hollick/baseflow_lyne_hollick.ipynb -->
<!-- STATUS: draft — notebook not yet written -->

## Why baseflow separation matters

Before you calibrate any runoff-routing model — URBS, RORB, or WBNM — you need to strip baseflow from the gauged record. The direct runoff volume you use to calibrate loss parameters depends entirely on how you make that separation. Get it wrong and every calibrated parameter downstream is biased.

The standard Australian approach is the Lyne-Hollick recursive digital filter, formalised by Ladson et al. (2013) in the Australian Journal of Water Resources. The Ladson implementation exists in R. There is no equivalent Python implementation. This post provides one.

## The Lyne-Hollick filter

_[Explain the recursive digital filter equation here]_

## Python implementation

_[Short code block — 20–30 lines. Full implementation in notebook.]_

## Applied to a BOM gauge record

_[Figure: observed streamflow, separated baseflow, direct runoff]_

## Sensitivity analysis: effect of α

_[Figure: baseflow index vs α for the sample gauge]_

## Comparison with the Ladson R implementation

_[Tabulated comparison of results]_

## Limitations

_[What this does not do. What practitioners should check before using in production.]_

---

**Companion notebook:** The full implementation, with all figures reproducible, is in [`notebooks/01_baseflow_lyne_hollick/baseflow_lyne_hollick.ipynb`](https://github.com/lmillard79/lmillard79.github.io/tree/main/notebooks/01_baseflow_lyne_hollick).

**Reference:** Ladson, A.R., Brown, R., Neal, B. and Nathan, R. (2013). A standard approach to baseflow separation using the Lyne and Hollick filter. *Australian Journal of Water Resources* 17(1): 25–34.
