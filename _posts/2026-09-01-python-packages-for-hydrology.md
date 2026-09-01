---
title: "Python Packages for Hydrology — a Companion to Tony Ladson's R Roundup"
date: 2026-09-01
categories: [insights]
tags: [python, tutorial, hydrology, open-source]
excerpt: "Tony Ladson's 2017 roundup of R packages for hydrology is a genuinely useful map of that ecosystem. This is the Python-side equivalent — independently researched and checked against each package's actual current status, not a translation of his list."
header:
  overlay_color: "#0f172a"
  overlay_filter: 0.7
  overlay_image: /images/pano1.jpg
read_time: true
---

Last in this batch drawing on [Tony Ladson's blog](https://tonyladson.wordpress.com/) — and the one entry in the series that isn't a translation of his work, because there's nothing to translate. His [R Packages for Hydrology](https://tonyladson.wordpress.com/2017/12/30/r-packages-for-hydrology/) (30 December 2017) is a reference list, not a method. The useful companion isn't a Python port of his list — it's an independently-researched Python-side equivalent, checked against each package's actual current status rather than assumed from memory.

## Flood frequency and extreme value analysis

- **[pyextremes](https://github.com/georgebv/pyextremes)** — block-maxima and peaks-over-threshold extreme value analysis. My own [fork](/insights/2026/03/22/pyextremes-arr2019-flood-frequency-python.html) adds LP3, Multiple Grubbs-Beck, TCEV and LH-moments for ARR 2019 compliance.
- **[lmoments3](https://github.com/OpenHydrology/lmoments3)** (PyPI, v1.0.8) — L-moment parameter estimation for statistical distributions, a Python port of Hosking's original `lmoments.f`. Directly relevant to LP3/GEV fitting.

## Model performance and calibration

- **[hydroeval](https://github.com/ThibHlln/hydroeval)** (PyPI) — vectorised NSE, KGE (and its α/β/γ or r/α/β components), and non-parametric KGE. Covers the same ground as the [metrics I built from scratch](/insights/2026/04/18/model-performance-metrics-nse-kge-python.html) earlier in this series, if you'd rather use a maintained package than your own implementation.
- **[HydroErr](https://pypi.org/project/HydroErr/)** (PyPI) — a broader library of 70+ error metrics, with explicit handling of NaN/Inf/negative/zero values.
- **[SPOTPY](https://github.com/thouska/spotpy)** (PyPI; Houska et al., *PLOS ONE*, 2015) — calibration, sensitivity and uncertainty analysis for environmental models generally, not hydrology-specific but heavily used in the field. Eight sampling algorithms, eleven objective functions, MPI-parallel.

## Groundwater

- **[Pastas](https://github.com/pastas/pastas)** (PyPI, v1.13.2 as of Feb 2026) — time series analysis of groundwater levels: response functions for rainfall, pumping and other stresses, trend and outlier detection. Actively maintained at TU Delft.

## Terrain and catchment analysis

- **[pysheds](https://github.com/mdbartos/pysheds)** (PyPI) — DEM-based catchment delineation and flow accumulation, D8 routing by default. Built on the standard geospatial Python stack (numpy, rasterio, scikit-image).

## General scientific stack

Not hydrology-specific, but where most of the actual work happens: `numpy`/`scipy` for the numerical core, `pandas` for time series handling, `xarray` (plus `rioxarray` for georeferencing) for gridded/NetCDF climate and model output — the same stack every notebook in this series has been built on.

## For more

[raoulcollenteur/Python-Hydrology-Tools](https://github.com/raoulcollenteur/Python-Hydrology-Tools) is a maintained, community-curated list that goes considerably wider than what's above — worth bookmarking rather than something I'd try to duplicate here.

---

**Source:** Ladson, A.R. (2017). [R Packages for Hydrology](https://tonyladson.wordpress.com/2017/12/30/r-packages-for-hydrology/) — the R-side original this post is a companion to, not a translation of.
