# Python Hydrology Notebooks

Companion Jupyter notebooks for the Python hydrology series on [lmillard79.github.io](https://lmillard79.github.io).

Each notebook is self-contained. Clone just the subdirectory you need and run it without understanding the rest of the repository.

## Series overview

| # | Notebook | Article | Status |
|---|----------|---------|--------|
| 01 | [Baseflow Separation — Lyne-Hollick Filter](01_baseflow_lyne_hollick/) | [published](https://lmillard79.github.io/insights/2026/04/11/baseflow-separation-lyne-hollick-python.html) | done |
| 02 | [ARR Temporal Pattern QA](02_arr_temporal_pattern_qa/) | [published](https://lmillard79.github.io/insights/2026/09/01/arr-temporal-pattern-embedded-burst-screening.html) | mostly done (API integration open) |
| 03 | [ARF Calculator — ARR 2019](03_arf_calculator/) | _coming soon_ | draft |
| 04 | [Monte Carlo Loss Sampling](04_monte_carlo_loss_sampling/) | [published](https://lmillard79.github.io/insights/2026/04/25/monte-carlo-loss-sampling-arr2019-python.html) | done |
| 05 | [Model Performance Metrics](05_model_performance_metrics/) | [published](https://lmillard79.github.io/insights/2026/04/18/model-performance-metrics-nse-kge-python.html) | done |
| 06 | [FFA Non-Stationarity Diagnostic](06_ffa_nonstationarity_diagnostic/) | [published](https://lmillard79.github.io/insights/2026/09/01/ffa-nonstationarity-outlier-diagnostic-python.html) | done |
| 07 | [pyraingen Evaluation](07_pyraingen_evaluation/) | [published](https://lmillard79.github.io/insights/2026/09/01/pyraingen-stochastic-rainfall-evaluation.html) | done |
| 08 | [POT Exponential Fit](08_pot_exponential_fit/) | [published](https://lmillard79.github.io/insights/2026/09/01/pot-exponential-fit-python.html) | done |
| 09 | [Water Balance Waterfall Chart](09_water_balance_waterfall/) | [published](https://lmillard79.github.io/insights/2026/09/01/water-balance-waterfall-python.html) | done |
| 10 | [Better Line Graphs](10_better_line_graphs/) | [published](https://lmillard79.github.io/insights/2026/09/01/better-line-graphs-python.html) | done |
| 11 | [Rainbow Colour Scales](11_rainbow_colour_scales/) | [published](https://lmillard79.github.io/insights/2026/09/01/rainbow-colour-scales-python.html) | done |
| 12 | [Nonlinear Model Fitting](12_nonlinear_model_fitting/) | [published](https://lmillard79.github.io/insights/2026/09/01/nonlinear-model-fitting-python.html) | done |

## Requirements

Each notebook lists its own dependencies. Common stack:

```
numpy
pandas
matplotlib
scipy
```

Install with:

```bash
pip install numpy pandas matplotlib scipy
```

For notebook 02 only, `requests` is also required (ARR Data Hub API).

## Data

Sample input data is provided in each notebook's `data/` subdirectory. BOM gauge data used in these notebooks is sourced from the [Bureau of Meteorology Water Data](http://www.bom.gov.au/waterdata/) portal.

## Licence

Code is MIT licensed. Sample data files retain their original source conditions.
