# Notebook 02 — ARR Temporal Pattern QA

> **Related article:** [Screening ARR 2019 Temporal Patterns for Embedded Burst Errors](https://lmillard79.github.io/insights/2026/09/01/arr-temporal-pattern-embedded-burst-screening.html)

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
└── arr_temporal_pattern_qa.ipynb   # main notebook
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

- [x] Notebook written -- screening function complete, unit-tested on synthetic patterns
- [x] Figures exported to /images/
- [x] Article published
- [ ] **API integration** (`fetch_arr_temporal_patterns`, see the TODO cell at the end of the notebook) -- per the note above, no API key should be needed, but the exact endpoint/response schema still needs confirming and wiring up
- [ ] Validated against Ladson (2021)'s own flagged pattern list, once real patterns are pulled in via the API
