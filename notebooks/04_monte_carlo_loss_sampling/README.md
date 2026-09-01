# Notebook 04 — Monte Carlo Loss Sampling for ARR 2019

> **Related article:** [Sampling ARR 2019 Loss Distributions in Python — A URBS Pre-Processor](https://lmillard79.github.io/insights/2026/04/25/monte-carlo-loss-sampling-arr2019-python.html)

## What this notebook does

Implements a standalone Python sampler for drawing Initial Loss / Continuing Loss pairs from the ARR 2019 empirical distributions (ARR Book 5, Table 5.3.13). Outputs IL/CL pairs in a CSV format compatible with URBS batch input files.

## Why it matters

ARR 2019 recommends Monte Carlo simulation treating initial loss as a random variable, but most practitioners still use fixed median values because the sampling machinery is not built into URBS or RORB front-ends. This notebook provides the missing pre-processor. It is the highest-value post in the series for practitioners running ARR 2019-compliant ensemble flood studies.

## Contents

```
04_monte_carlo_loss_sampling/
├── README.md
├── monte_carlo_loss_sampling.ipynb # main notebook
└── data/
    ├── README.md
    └── il_cl_samples_N{0100,0500,1000}.csv  # example export output
```

## Dependencies

```
numpy
scipy
pandas
matplotlib
```

## Output format

The sampler generates a CSV with N rows, one per ensemble member:

```csv
member,IL_mm,CL_mm_hr
1,23.5,2.1
2,31.2,1.8
...
```

This CSV is designed to be directly consumed by a URBS batch input pre-processor.

## Validation

Results are compared against the Ladson R implementation of the same ARR distributions.

## Status

- [x] Notebook written
- [x] Validated against Ladson R reference (IL mean 1.162 vs ~1.15, CL mean 1.241 vs ~1.24 -- within Monte Carlo noise at N=10,000)
- [x] URBS CSV output format implemented (N=100/500/1000 example exports in data/)
- [x] Figures exported to /images/
- [x] Article published
- [ ] LYR RORB application (Section 10 of the notebook) -- needs real project median IL/CL from the ARR Data Hub, out of scope for the article
