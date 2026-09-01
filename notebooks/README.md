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
