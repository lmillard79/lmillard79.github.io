---
title: "Areal Reduction Factors in Python — ARR 2019 Compliant"
date: 2026-09-01
categories: [insights]
tags: [python, tutorial, arr2019, hydrology, flood-modelling]
excerpt: "Automated design rainfall workflows need ARF calculations without opening a spreadsheet. This post provides a documented Python implementation of the ARR Book 2 ARF equations, with ARR-compliant duration interpolation."
header:
  overlay_color: "#0f172a"
  overlay_filter: 0.7
  overlay_image: /images/pano1.jpg
read_time: true
---

<!--
STATUS: SCAFFOLD, NOT PUBLISHABLE YET -- read this block before touching anything below.

What's confirmed (cross-checked across multiple independent sources, Sept 2026):
- ARR 2019 gives TWO ARF equations: short duration (<12h, one equation for
  all of Australia) and long duration (24-168h, 10 regional coefficient sets).
  12-24h is interpolated between the two. Source: ARR Book 2 S2.4 (per
  Tony Ladson's ARR2019 ARF blog series -- he has at least 3 posts on this
  exact topic, including one specifically on the short/long interpolation
  edge cases, all worth reading before finalising this: search
  "tonyladson.wordpress.com ARR2019 Areal Reduction Factors").
- Valid AEP range for both equations: 0.5 to 0.0005 (50% to 0.05%).
- The short-duration equation below is a RECONSTRUCTION from a third-party
  spreadsheet vendor's (CivilWeb) published Excel formula, not read directly
  from the ARR2019 PDF. It has NOT been validated against the ARR Book 2
  worked examples. Treat every coefficient in it as needing a check against
  the primary source before this goes anywhere near real design work.

What's still missing (I could not access the ARR2019 PDF directly or your
Drive copies of the specific books in this environment):
1. The long-duration ARF equation and its 10 regional coefficient sets
   (region names/boundaries AND the a/b/c/d-style coefficients per region).
   ARR Book 2, Section 2.4 (also referenced as Chapter 4.3 in some
   secondary sources -- worth confirming the actual section number when
   you have the PDF open).
2. Validation against the ARR Book 2 worked examples (Section 6.5.3 per
   the original outline for this post -- confirm the section number).
3. Confirmation/correction of the short-duration formula below against
   the primary source.

Fill in the TODO-marked sections, delete this comment block, and this is
ready to test and publish.
-->

## What ARFs are and where they sit in the design rainfall workflow

Point rainfall — an IFD estimate at a single location — systematically overstates the rainfall actually falling, on average, over a large catchment at any given moment, because storm cells don't cover a whole large catchment with uniform intensity simultaneously. Areal Reduction Factors correct for this: multiply a point rainfall depth by the appropriate ARF (always ≤ 1) to get a catchment-average design rainfall, before that value goes into a URBS, RORB, or WBNM hydrologic model as a design storm input.

Skipping this step — running a design storm using point rainfall directly on anything but a very small catchment — systematically overestimates design flood peaks, more severely as catchment area increases.

## ARR Book 2 ARF equations

Two equations, by duration:

- **Short duration (< 12 hours):** a single national equation, derived from data-rich regions around Sydney, Brisbane and Melbourne, applied Australia-wide.
- **Long duration (24–168 hours):** different coefficients for each of 10 regions, delineated by climatology (Podger et al. 2015 methodology, adopted into ARR 2019).
- **12–24 hours:** interpolated between the short- and long-duration results — see Ladson's blog post on this specific edge case before implementing it; the interpolation isn't simply linear-in-duration and is easy to get subtly wrong.
- Both equations are valid for AEP between 0.5 and 0.0005 (50% to 0.05%) — outside that range, ARR doesn't provide guidance and neither should this function (raise, don't silently extrapolate).

## Python implementation

```python
import numpy as np

def arf_short_duration(area_km2, duration_min, aep):
    """ARR 2019 short-duration (<12h) Areal Reduction Factor.

    UNVERIFIED -- reconstructed from a third-party spreadsheet vendor's
    published formula, not read directly from ARR 2019 Book 2. Check every
    coefficient against the primary source before relying on this.

    Parameters
    ----------
    area_km2 : float
        Catchment area, km^2.
    duration_min : float
        Storm duration, minutes (valid < 720 min / 12h).
    aep : float
        Annual Exceedance Probability as a decimal (valid 0.5 to 0.0005).
    """
    if not (0.0005 <= aep <= 0.5):
        raise ValueError("aep outside ARR 2019 ARF validity range (0.0005-0.5)")
    if duration_min >= 720:
        raise ValueError("duration_min >= 720 (12h) -- use the long-duration equation")

    A, D, P = area_km2, duration_min, aep
    arf = (
        1
        - 0.287 * (A**0.265 - 0.439 * np.log10(D)) * D**-0.36
        + 2.26e-3 * A**0.226 * D**0.125 * (0.3 + np.log10(P))
        + 0.0141 * A**0.213 * 10 ** (-0.021 * (D - 180) ** 2 / 1440) * (0.3 + np.log10(P))
    )
    return arf


def arf_long_duration(area_km2, duration_hr, aep, region):
    """ARR 2019 long-duration (24-168h) Areal Reduction Factor.

    TODO: needs the actual ARR Book 2 long-duration equation form and the
    10 regional coefficient sets. Structure below is a placeholder -- the
    equation form itself (not just the coefficients) needs confirming
    against the primary source, don't assume it mirrors the short-duration
    form.
    """
    # TODO: replace with the real region -> coefficient mapping from
    # ARR 2019 Book 2. Region names below are placeholders, not the
    # actual ARR region names/boundaries.
    REGIONAL_COEFFICIENTS = {
        "region_1": {},  # TODO
        "region_2": {},  # TODO
        # ... 10 regions total
    }
    if region not in REGIONAL_COEFFICIENTS:
        raise ValueError(f"Unknown region '{region}'. Valid: {list(REGIONAL_COEFFICIENTS)}")
    raise NotImplementedError("Long-duration ARF equation not yet implemented -- see TODO above")


def arf(area_km2, duration_min, aep, region=None):
    """Dispatch to short/long/interpolated ARF depending on duration."""
    if duration_min < 720:
        return arf_short_duration(area_km2, duration_min, aep)
    elif duration_min > 1440:
        if region is None:
            raise ValueError("region is required for long-duration ARFs")
        return arf_long_duration(area_km2, duration_min / 60, aep, region)
    else:
        # TODO: 12-24h interpolation -- see Ladson's blog post on this
        # specific edge case before implementing. Not simply linear in
        # duration between the two endpoint values.
        raise NotImplementedError("12-24h interpolation not yet implemented")
```

## Validation against ARR Book 2 test cases

```python
# TODO: populate with the actual ARR Book 2 worked examples (original
# outline for this post referenced Section 6.5.3 -- confirm section number
# against the current PDF) for all 10 regions, and assert the Python output
# matches within a sensible tolerance. Don't publish this post until this
# section has real, passing assertions -- an untested "ARR2019 compliant"
# claim is worse than no claim at all.

TEST_CASES = [
    # (area_km2, duration_min, aep, region, expected_arf),
]

for area, duration, aep, region, expected in TEST_CASES:
    result = arf(area, duration, aep, region)
    assert abs(result - expected) < 0.01, f"Mismatch: got {result}, expected {expected}"
print(f"All {len(TEST_CASES)} test cases passed." if TEST_CASES else "No test cases yet -- add from ARR Book 2 before publishing.")
```

## Usage: generating an ARF matrix for URBS

_Straightforward to write once the above is real: loop `arf()` over the durations and areas your URBS model needs, write to a CSV. Not worth drafting until the underlying calculation is verified._

## Limitations

- Regional applicability: ARF regions are climatological, not administrative — don't assume a catchment near a region boundary behaves like the interior of either region without checking.
- These equations apply to a nominally circular/compact catchment shape assumption typical of ARF derivation methodology; check ARR guidance on elongated or irregular catchments before applying without adjustment.
- Valid only within the stated AEP range (0.0005–0.5) — the function should raise outside that range, not extrapolate.

---

**Standalone module:** _once complete, extract into `arr_arf_functions.py` for direct import — see the [notebook directory](https://github.com/lmillard79/lmillard79.github.io/tree/main/notebooks/03_arf_calculator)._

**Reference:** Ball, J., Babister, M., Nathan, R., Weeks, W., Weinmann, E., Retallick, M. and Testoni, I. (Editors) (2019). *Australian Rainfall and Runoff: A Guide to Flood Estimation.* Commonwealth of Australia. Book 2.
