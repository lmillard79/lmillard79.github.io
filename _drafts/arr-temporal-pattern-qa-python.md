---
title: "Screening ARR 2019 Temporal Patterns for Embedded Burst Errors"
date: 2026-04-11
categories: [insights]
tags: [python, tutorial, arr2019, flood-modelling, hydrology]
excerpt: "Running 10 ARR temporal patterns is standard practice. Some contain errors that produce physically unrealistic flood peaks. This post provides a Python screening tool you can run on your own model inputs."
header:
  overlay_color: "#0f172a"
  overlay_filter: 0.7
  overlay_image: /images/pano1.jpg
read_time: true
---

<!-- COMPANION NOTEBOOK: notebooks/02_arr_temporal_pattern_qa/arr_temporal_pattern_qa.ipynb -->
<!-- STATUS: draft — notebook not yet written -->

## The problem with embedded bursts

_[What embedded bursts are and why they matter for design flood estimation]_

## Accessing ARR temporal patterns

_[ARR Data Hub API — how to retrieve patterns programmatically]_

## The screening algorithm

_[Short code block — flag patterns where the two largest increments are ~24 hours apart]_

## Visualisation: suspect versus clean patterns

_[Figure: side-by-side comparison of a flagged pattern and a clean pattern]_

## Recommended workflow

_[Screen before ensemble runs, not after]_

## Limitations

_[What this does not do. What practitioners should check before using in production.]_

---

**Companion notebook:** Full implementation at [`notebooks/02_arr_temporal_pattern_qa/arr_temporal_pattern_qa.ipynb`](https://github.com/lmillard79/lmillard79.github.io/tree/main/notebooks/02_arr_temporal_pattern_qa).

**Reference:** Ladson, A.R. (2021). Review of temporal patterns from Australian Rainfall and Runoff 2019. *39th Hydrology and Water Resources Symposium.*
