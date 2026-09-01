---
title: "Stochastic Rainfall Generation with pyraingen: A Practitioner's Evaluation"
date: 2026-09-01
categories: [insights]
tags: [python, tutorial, stochastic-rainfall, open-source, climate-change]
excerpt: "pyraingen promises stochastic daily/subdaily rainfall generation with IFD constraining — a genuinely useful way to explore rainfall behaviour beyond a single historical record. Here's what I found actually trying to run it: a real dependency-pin conflict, a Windows-only compiled core, and a helper function whose own author left a '?' in the logic."
header:
  overlay_color: "#0f172a"
  overlay_filter: 0.7
  overlay_image: /images/pano1.jpg
read_time: true
---

A single historical rainfall record is one realisation of what the climate at a site could produce — not the only one, and not necessarily the most extreme one. Stochastic rainfall generation addresses that directly: instead of one 50-year record, produce many statistically plausible 50-year records with the same broad statistical properties, and see how design rainfall at different durations and AEPs behaves across the whole set. That's a genuinely useful tool for probing how much a design estimate depends on which particular sequence of years happened to get recorded — a different and more modest question than asking how a warming climate will change future rainfall, but a useful one on its own terms.

`pyraingen` is one of the few Python packages attempting this for Australian conditions, so I wanted to actually use it — not just describe it — for the [Climate Risk series](/climate-risk/). This post is what I found doing that.

## What it promises

From the package's own documentation: `pyraingen` "can be used to stochastically generate regionalised daily rainfall, disaggregate daily rainfall to subdaily fragments and constrain generated rainfall to observed or predicted Intensity Frequency Duration (IFD) relationships," via three main functions — `regionaliseddailysim`, `regionalisedsubdailysim`, and `ifdcond`. The subdaily disaggregation step implements the method from Westra et al. (2012), "Continuous rainfall simulation 1: A regionalised subdaily disaggregation approach" (cited directly in the package's own docstrings); the IFD-conditioning step implements "Algorithm from Fitsum et al. (2016) for Constraining continuous rainfall simulations for derived design flood estimation" — also per its own docstring. Both are legitimate, real methods. The question was whether the current release actually runs.

```bash
pip install pyraingen
```

## Problem 1: a dependency pin that doesn't work today

`pyraingen` 1.0.0's own package metadata declares:

```
Requires-Dist: numpy (>=1.23.5)
Requires-Dist: pandas (==1.5.3)
Requires-Dist: xarray (==2023.01.0)
```

No upper bound on numpy, but `pandas` and `xarray` hard-pinned to versions that predate numpy 2.0 (released mid-2024) — and whose compiled C extensions are ABI-incompatible with it. I confirmed this isn't an artifact of one messy environment: in a completely clean virtualenv, `pip install pyraingen` resolves numpy 2.x (nothing stops it), and importing anything that touches pandas fails:

```
ValueError: numpy.dtype size changed, may indicate binary incompatibility.
Expected 96 from C header, got 88 from PyObject
```

**The fix**, if you want to use this package today: pin numpy yourself before installing.

```bash
pip install "numpy<2" pyraingen
```

With that pin, `pandas==1.5.3` and `xarray==2023.01.0` both import cleanly.

## Problem 2: the core generator doesn't run on Linux at all

With the numpy pin fixed, the package's actual daily rainfall generator still fails:

```
>>> from pyraingen.regionaliseddailysim import regionaliseddailysim
...
ImportError: cannot import name 'regionalised_dailyT4' from 'pyraingen.fortran_daily'
```

The installed package's own file listing explains why — `pyraingen/fortran_daily/` contains:

```
regionalised_dailyT.cp38-win_amd64.pyd
regionalised_dailyT4.cp38-win_amd64.pyd
regionalised_dailyT.for
regionalised_dailyT4.for
```

`.pyd` files are compiled Windows extension modules, and these are built specifically for CPython 3.8 on 64-bit Windows. There's no Linux (`.so`) or macOS build anywhere in the package, and no automatic source-compilation fallback. The Fortran source is there, so compiling it yourself with `f2py` is possible in principle — I didn't attempt it here.

In practice: **`regionaliseddailysim` — the actual stochastic daily rainfall generator, the core of what the package does — is not runnable via a plain `pip install pyraingen` on Linux or macOS.** That matters because Linux is where most cloud, CI, and HPC-based hydrology computation happens today. `regionalisedsubdailysim` has code paths that can work from existing daily data without touching the Fortran generator, but its "generate everything from scratch" option hits the same wall.

## What does run: computeIFD, and a shape that doesn't match its own docstring

One piece has no compiled or pinned-package dependency at all: `computeIFD`, described in its own docstring as an internal helper "designed to be used inside the IFD Conditioning code" rather than something meant for direct use. It takes a pre-built 6-minute rainfall array and is meant to return an annual-maximum table by duration. I fed it a small, deliberately synthetic 6-minute series — random sparse bursts, not real rainfall — purely to exercise the function's contract:

```python
import numpy as np
from pyraingen.computeifd import computeIFD

rng = np.random.default_rng(20260901)
n_days, n_sims, n_records_per_day = 365 * 10, 3, 240

rainfall = np.zeros((n_records_per_day, n_days, n_sims))
for sim in range(n_sims):
    n_bursts = 300
    burst_days = rng.integers(0, n_days, n_bursts)
    burst_starts = rng.integers(0, n_records_per_day - 10, n_bursts)
    burst_depths = rng.gamma(shape=2.0, scale=3.0, size=n_bursts)
    for d, s, depth in zip(burst_days, burst_starts, burst_depths):
        dur = rng.integers(1, 8)
        rainfall[s:s+dur, d, sim] += depth / dur

years_vector = np.repeat(np.arange(2016, 2026), 365)
ifd_durations = [6, 30, 60, 360, 1440]  # minutes

IFD = computeIFD(rainfall, years_vector, ifd_durations)
print(f'Output shape: {IFD.shape}')
```

```
Output shape: (10, 240, 5)
```

I'd asked for 3 simulations. The docstring says the output should be `(nYears, nSimulations, nIFDDurations)` — `(10, 3, 5)`. What came back has 240 in the middle slot, not 3. Reading the source explains why: the output array is allocated with `np.size(rainfallSeries, axis=0)`, which is the 240 six-minute-slots-per-day count, not the simulations axis. The fill loop then collapses across both the simulation axis and the within-year day axis before assigning into that 240-long slot — which doesn't produce a per-simulation annual-maximum-by-duration table.

The function's own source has a comment that reads like the original author flagged this themselves:

```python
# The general process for each simulation is:
#   -) Aggregate up from 6 minute if required.
#   -) Extract the annual maximum series
#   -) ?
```

I wouldn't trust this specific function's return values for a real project without independently re-deriving the annual maxima myself — the trailing `?` is in the package's own source, not something I've added for effect.

## What I'd actually tell a colleague

The underlying methods — Westra et al.'s subdaily disaggregation, Fitsum et al.'s IFD conditioning — are legitimate and exactly the right tools for the question "how much does design rainfall at different durations and AEPs depend on the particular 50 years we happened to record." `pyraingen` is a genuine, serious attempt at packaging that for Australian conditions in Python, and I'd rather see it exist, with rough edges, than not exist at all.

But as released today (1.0.0), I wouldn't build a real project workflow on it without addressing all three of the above first: pin `numpy<2` yourself, either work on Windows/Python 3.8 or compile the bundled Fortran source for your platform, and independently verify `computeIFD`'s output rather than trusting the shape the docstring promises. For a Linux-based team, that's currently closer to "a well-documented methodology worth reimplementing the disaggregation and conditioning steps around" than "a package you `pip install` and use."

## Limitations of this evaluation

- I did not attempt to compile the bundled Fortran source with `f2py` — that may well resolve the Linux blocker; I'm reporting what the released PyPI package does out of the box, not what's theoretically achievable with more effort.
- I have not run this on Windows/Python 3.8, where the shipped binaries are presumably functional.
- The `computeIFD` finding is based on reading the source and one test run, not an exhaustive test suite — I'd want to see the package's own tests (if any exist) before stating definitively that it's wrong rather than differently-intentioned than its docstring suggests.

---

**Companion notebook:** [`notebooks/07_pyraingen_evaluation/`](https://github.com/lmillard79/lmillard79.github.io/tree/main/notebooks/07_pyraingen_evaluation)

**Related:** [Was That Flood an Outlier? A Python Diagnostic for Non-Stationarity in Flood Frequency Analysis](/insights/2026/09/01/ffa-nonstationarity-outlier-diagnostic-python.html) · [more on the Climate Risk page](/climate-risk/)

**References:**
- Dykman, C. `pyraingen` 1.0.0. [pypi.org/project/pyraingen](https://pypi.org/project/pyraingen/), docs at [pyraingen.readthedocs.io](https://pyraingen.readthedocs.io).
- Westra, S. et al. (2012). Continuous rainfall simulation: 1. A regionalised subdaily disaggregation approach — as cited in the package's own docstrings.
- Fitsum, et al. (2016). Constraining continuous rainfall simulations for derived design flood estimation — as cited in the package's own docstrings.
