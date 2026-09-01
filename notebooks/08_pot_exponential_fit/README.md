# Notebook 08 — POT Exponential Fit (Python port of Tony Ladson's R method)

> **Related article:** [Fitting a Probability Model to POT Data — a Python Port of Tony Ladson's R Method](https://lmillard79.github.io/insights/2026/09/01/pot-exponential-fit-python.html)
>
> **Original source:** [Fitting a probability model to POT data](https://tonyladson.wordpress.com/2019/03/25/fitting-a-probability-model-to-pot-data/) — Tony Ladson, 25 March 2019. R source: [gist.github.com/TonyLadson/5b01838fef1140293397e23eebe12079](https://gist.github.com/TonyLadson/5b01838fef1140293397e23eebe12079)

## What this notebook does

A line-for-line Python port of Ladson's R script for fitting an exponential distribution to Partial Duration Series (POT) flood data via L-moments, run on his own published example (Styx River at Jeogla, 47 peaks) and checked against his published output at every step: L-moments, fitted parameters, all 9 standard-EY flood quantiles, and bootstrap confidence intervals.

## Why it matters

POT/PDS series use more of a short record than annual maxima do, but the AEP conversion is different — a plotting-position formula alone isn't valid when more than one exceedance can occur per year. Ladson's post is the clearest explanation of the correct EY-based conversion available for Australian practice; this notebook makes the same method available in Python, validated rather than just translated.

## Contents

```
08_pot_exponential_fit/
├── README.md
├── pot_exponential_fit.ipynb   # main notebook
└── data/                        # empty — the Styx River series is embedded in-notebook
```

## Dependencies

```
numpy
scipy
matplotlib
```

## Validation

Every checkable number is checked against Ladson's own published R output in the notebook itself (asserted, not just printed): L1, L2, beta, q_star, all 9 quantiles in the standard-EY table, and his explicit `EY=0.01 -> 796.8394` check value. Bootstrap CIs use `scipy.stats.bootstrap(method='BCa')` and land in the same range as his `boot::boot.ci` output, as expected for independent resampling runs of the same method.

## Status

- [x] Notebook written
- [x] Validated against Ladson's published R output (L-moments, parameters, quantile table, explicit check value)
- [x] Bootstrap CI cross-checked against his reported range
- [x] Figure exported to /images/
- [x] Article published
