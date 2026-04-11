# Notebook 02 — ARR Temporal Pattern QA

> **Related article:** _Screening ARR 2019 Temporal Patterns for Embedded Burst Errors_ (coming soon)

## What this notebook does

Screens ARR 2019 temporal patterns for embedded burst errors — cases where two large rainfall increments are separated by approximately 24 hours, producing physically unrealistic flood peaks in ensemble runs.

Implements the Python equivalent of the screening approach described in:

> Ladson, A.R. (2021). Review of temporal patterns from Australian Rainfall and Runoff 2019. *39th Hydrology and Water Resources Symposium.*

## Why it matters

ARR 2019 recommends running an ensemble of 10 temporal patterns for design flood estimation. Some patterns contain errors that inflate peak flows. Running this screen before ensemble runs avoids wasted model runs and catches problems before they propagate into design flood estimates.

## Contents

```
02_arr_temporal_pattern_qa/
├── README.md
├── arr_temporal_pattern_qa.ipynb   # main notebook (to be created)
└── data/
    └── README.md                   # ARR Data Hub API instructions
```

## Dependencies

```
numpy
pandas
matplotlib
requests
```

Note: `requests` is required for the ARR Data Hub API calls.

## API access

This notebook retrieves temporal patterns from the ARR Data Hub API. No API key is required — the endpoint is publicly accessible.

## Status

- [ ] Notebook written
- [ ] API integration tested
- [ ] Validated against Ladson (2021) flagged pattern list
- [ ] Figures exported to /images/
- [ ] Article published
