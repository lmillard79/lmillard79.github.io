# Notebook 09 — Water Balance Waterfall Chart (Python port of Tony Ladson's R method)

> **Related article:** [Graphing a Water Balance — a Python Port of Tony Ladson's R Method](https://lmillard79.github.io/insights/2026/09/01/water-balance-waterfall-python.html)
>
> **Original source:** [Graphing a water balance](https://tonyladson.wordpress.com/2017/08/15/graphing-a-water-balance/) — Tony Ladson, 15 August 2017. R source: [gist.github.com/TonyLadson/4d42e2cedc20aa1ff04a06631af88551](https://gist.github.com/TonyLadson/4d42e2cedc20aa1ff04a06631af88551)

## What this notebook does

A Python port of Ladson's waterfall-chart construction for an urban catchment water balance, using the same real published data (Mitchell et al. 2003) for a driest and a wettest example period.

## Why it matters

Waterfall charts are the clearest way to show a sequential accounting of ins, outs, and a residual/storage term. This notebook also checks something the original R script doesn't: whether the reported "change in storage" actually equals what the other terms sum to. It does for the wettest period; it doesn't for the driest (a real 24mm gap) — a useful reminder that a waterfall chart's visual closure is a drawing convention, not proof the underlying accounting reconciles.

## Contents

```
09_water_balance_waterfall/
├── README.md
├── water_balance_waterfall.ipynb   # main notebook
└── data/                            # empty — the two example datasets are embedded in-notebook
```

## Dependencies

```
numpy
matplotlib
```

## Validation

Bar geometry logic reproduces Ladson's R (`cumsum` + forced zero-close on the final bar). The closure discrepancy check (Section 3) is original to this notebook, not present in the source R script.

## Status

- [x] Notebook written
- [x] Waterfall geometry matches Ladson's R construction
- [x] Closure discrepancy independently checked and reported
- [x] Figure exported to /images/
- [x] Article published
