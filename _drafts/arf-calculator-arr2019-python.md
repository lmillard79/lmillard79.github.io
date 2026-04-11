---
title: "Areal Reduction Factors in Python — ARR 2019 Compliant"
date: 2026-04-11
categories: [insights]
tags: [python, tutorial, arr2019, hydrology, flood-modelling]
excerpt: "Automated design rainfall workflows need ARF calculations without opening a spreadsheet. This post provides a documented Python implementation of the ARR Book 2 ARF equations, with ARR-compliant duration interpolation."
header:
  overlay_color: "#0f172a"
  overlay_filter: 0.7
  overlay_image: /images/pano1.jpg
read_time: true
---

<!-- COMPANION NOTEBOOK: notebooks/03_arf_calculator/arf_calculator.ipynb -->
<!-- STANDALONE MODULE: notebooks/03_arf_calculator/arr_arf_functions.py -->
<!-- STATUS: draft — notebook not yet written -->

## What ARFs are and where they sit in the design rainfall workflow

_[Point rainfall → catchment-average rainfall. Where ARFs fit in the URBS/RORB pre-processing chain.]_

## ARR Book 2 ARF equations

_[Overview of the 11 Australian regions and the short/long duration equation structure]_

## Python implementation

_[Short code block — the core calculate_arf() function. Full implementation in notebook and module.]_

## Validation against ARR Book 2 test cases

_[Table: calculated vs ARR Book 2 Chapter 6.5.3 test cases for all 11 regions]_

## Usage: generating an ARF matrix for URBS

_[Example: loop over durations and areas to produce a URBS-ready ARF table]_

## Limitations

_[What this does not do. Regional applicability. What practitioners should check before using in production.]_

---

**Companion notebook:** Full implementation at [`notebooks/03_arf_calculator/arf_calculator.ipynb`](https://github.com/lmillard79/lmillard79.github.io/tree/main/notebooks/03_arf_calculator).

**Standalone module:** Import `arr_arf_functions.py` directly into your own scripts — see the [notebook directory](https://github.com/lmillard79/lmillard79.github.io/tree/main/notebooks/03_arf_calculator) for usage instructions.

**Reference:** Ball, J., Babister, M., Nathan, R., Weeks, W., Weinmann, E., Retallick, M. and Testoni, I. (Editors) (2019). *Australian Rainfall and Runoff: A Guide to Flood Estimation.* Commonwealth of Australia. Book 2, Chapter 6.
