# Notebook 12 — Nonlinear Model Fitting: Confidence vs. Prediction Intervals

> **Related article:** [Fitting Non-linear Models in Python: Confidence vs. Prediction Intervals](https://lmillard79.github.io/insights/2026/09/01/nonlinear-model-fitting-python.html)
>
> **Topic inspiration:** [Fitting non-linear models](https://tonyladson.wordpress.com/2016/06/20/fitting-non-linear-models/) — Tony Ladson, 20 June 2016.

## Important note on this one

Unlike the other notebooks in this series (POT fit, water balance, line graphs, rainbow colour scales), **this is not a port of Ladson's actual R code**. The tool used to fetch his gist for this post declined to reproduce it verbatim, citing the original research dataset it's built on (Antecedent Precipitation Index vs. Initial Loss). So this notebook is an original Python demonstration of the *same general method* — fitting a nonlinear model and getting properly propagated confidence and prediction intervals — applied to a different, standard hydrological example (a stage-discharge rating curve) with clearly synthetic data, rather than reconstructing his dataset secondhand.

## What this notebook does

Fits a power-law rating curve (`Q = C(h-h0)^n`) to synthetic gauging data via `scipy.optimize.curve_fit`, then propagates the fitted parameter covariance through the model's own gradient (the delta method) to get a 95% confidence interval on the fitted curve and a 95% prediction interval on a new observation — explicitly, so the mechanics are visible rather than hidden behind a library call the way R's `propagate::predictNLS` would hide them.

## Why it matters

R's `nls()` doesn't give confidence/prediction intervals out of the box; Ladson's post flags this as the genuinely tricky part. It's just as true in Python if you reach only for the point estimate `curve_fit` returns — this notebook shows the actual propagation.

## A real gotcha surfaced along the way

The three fitted rating-curve parameters (C, h0, n) turn out to be highly correlated with each other (|r| > 0.9 for every pair) — a well-known feature of power-law rating curves, where several different parameter combinations trace out nearly the same curve. The individual parameter estimates land noticeably off their "true" synthetic values even though the *fitted curve itself* tracks the data well. Worth checking curve fit quality separately from individual parameter recovery.

## Contents

```
12_nonlinear_model_fitting/
├── README.md
├── nonlinear_model_fitting.ipynb   # main notebook
└── data/                            # empty — synthetic gaugings generated in-notebook
```

## Dependencies

```
numpy
scipy
matplotlib
```

## Status

- [x] Notebook written
- [x] PI-wider-than-CI relationship asserted, not just plotted
- [x] Parameter correlation noted and shown explicitly
- [x] Figure exported to /images/
- [x] Article published
