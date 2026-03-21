---
title: "Visualising 130 Years of Australian Rainfall Intensity Change in Python"
date: 2026-02-15
categories: [insights]
tags: [python, hydrology, climate-change]
excerpt: "I replicated Ed Hawkins' climate stripes style using the Simple Daily Intensity Index and the SILO Patched Point Dataset to show how rainfall intensity is shifting in Brisbane, Sydney, and regional Australia."
header:
  overlay_color: "#0f172a"
  overlay_filter: 0.7
  overlay_image: /images/pano1.jpg
read_time: true
---

Professor Ed Hawkins (University of Reading) created the [Climate Stripes](https://showyourstripes.info/) — one of the most effective climate communication tools ever made. His tagline captures the rainfall story precisely: *"When it rains, it now rains more."*

I wanted to test whether that signal was visible in Australian data, and whether I could replicate the visual style using local station records. Here's the methodology.

## The Metric: Simple Daily Intensity Index (SDII)

The key to this analysis is **not** total annual rainfall — that's dominated by El Niño/La Niña variability and obscures long-term trends.

Instead, I used the **Simple Daily Intensity Index (SDII)**:

```
SDII = Total annual rainfall ÷ Number of wet days
```

The critical detail: **only days with >1mm count as "wet days."** This removes dew, trace showers, and instrument noise that would otherwise dilute the average, leaving a clean signal of *how hard it rains when it rains.*

## The Data: SILO Patched Point Dataset

You can't detect a century-long trend with gaps in the record. I used the **SILO Patched Point Dataset** from the Queensland Government's [Long Paddock project](https://www.longpaddock.qld.gov.au/silo/).

SILO creates a continuous daily rainfall record from 1889 to the present day by scientifically merging historical Post Office records with modern automatic weather station data. It's one of the most underutilised resources in Australian hydrology.

## The Visualisation: Anomaly, Not Raw Values

Rather than plotting raw SDII values — which vary enormously by location — the plot shows the **anomaly against the 1961–1990 standard climate baseline:**

- **Blue bars** = years where rainfall was more intense than the 1961–1990 average
- **Orange bars** = years where rainfall was less intense
- **Colour saturation** scales with the magnitude — deep navy = exceptionally intense wet year

This approach cuts through ENSO noise and isolates the underlying decadal signal in storm intensity.

## The Code

The Python script pulls live SILO data via API for any Australian station and generates the plot automatically. The key libraries are `pandas`, `matplotlib`, and `requests`.

```python
import requests
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import numpy as np

def get_silo_data(station_id, start_year=1889):
    """Pull daily rainfall from SILO Patched Point Dataset."""
    url = f"https://www.longpaddock.qld.gov.au/cgi-bin/silo/PatchedPointDataset.php"
    params = {
        "station": station_id,
        "start": f"{start_year}0101",
        "finish": "20261231",
        "format": "csv",
        "username": "your_email@example.com",  # register free at longpaddock.qld.gov.au
        "password": "apirequest"
    }
    # Parse daily rainfall, calculate SDII, compute anomaly vs 1961-1990 baseline
    ...

def plot_intensity_stripes(sdii_anomaly, station_name):
    """Render climate-stripes style bar chart of SDII anomaly."""
    ...
```

The full script is available as a GitHub gist — drop a comment on the [LinkedIn post](https://www.linkedin.com/in/lindsaymillard/) or [email me](mailto:lindsay.milard@outlook.com.au) and I'll share it. If you'd like to see your town's data, let me know in the comments.

## What the Data Shows

Across Brisbane, Sydney, Bundaberg and several regional locations, the signal is consistent: **the intensity of rainfall on wet days has increased**, particularly from the 1990s onward, even in years where total annual rainfall was average or below average.

This has direct implications for urban stormwater design and IFD curve validity — a topic worth a separate post.

---

*Inspired by Professor Ed Hawkins' [Climate Stripes](https://showyourstripes.info/) and the work of the Climate Lab Book.*
*Originally shared on [LinkedIn](https://www.linkedin.com/in/lindsaymillard/) — 3,536 impressions.*
