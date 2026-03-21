---
title: "Visualising 130 Years of Australian Rainfall Intensity Change in Python"
date: 2026-02-15
categories: [insights]
tags: [python, hydrology, climate-change]
excerpt: "I replicated Ed Hawkins' climate stripes style using the Simple Daily Intensity Index and the SILO Patched Point Dataset to show how rainfall intensity is shifting across Australian cities — results range from -3.9% in Bundaberg to +21.0% in Toowoomba."
header:
  overlay_color: "#0f172a"
  overlay_filter: 0.7
  overlay_image: /images/pano1.jpg
read_time: true
---

Professor Ed Hawkins (University of Reading) created the [Climate Stripes](https://showyourstripes.info/) — one of the most effective climate communication tools ever made. His tagline captures the rainfall story precisely: *"When it rains, it now rains more."*

I wanted to test whether that signal was visible in Australian data, and whether I could replicate the visual style using local station records. Here's the methodology and what I found.

## The Metric: Simple Daily Intensity Index (SDII)

The key to this analysis is **not** total annual rainfall — that's dominated by El Niño/La Niña variability and obscures long-term trends.

Instead, I used the **Simple Daily Intensity Index (SDII)**:

```
SDII = Total annual rainfall ÷ Number of wet days
```

The critical detail: **only days with >1mm count as "wet days."** This removes dew, trace showers, and instrument noise that would otherwise dilute the average, leaving a clean signal of *how hard it rains when it rains.*

## The Data: SILO Patched Point Dataset

You can't detect a century-long trend with gaps in the record. I used the **SILO Patched Point Dataset** from the Queensland Government's [Long Paddock project](https://www.longpaddock.qld.gov.au/silo/).

SILO creates a continuous daily rainfall record from 1889 to the present day by merging historical Post Office records with modern automatic weather station data. It's one of the most underutilised resources in Australian hydrology.

## The Visualisation: Anomaly, Not Raw Values

Rather than plotting raw SDII values — which vary enormously by location — the plots show the **anomaly against the 1961–1990 standard climate baseline:**

- **Blue bars** = years where rainfall was more intense than average
- **Orange bars** = years where rainfall was less intense
- **Colour saturation** scales with magnitude — deep navy = exceptionally intense wet year

This approach cuts through ENSO noise and isolates the underlying decadal signal in storm intensity.

## Results: Four Australian Locations

<figure>
  <img src="/images/2026-02_sdii-rainfall-intensity-chart-1.jpg" alt="SDII rainfall intensity anomaly chart — Australian location 1889-2024">
  <figcaption>Annual rainfall intensity anomaly (SDII), 1889–2024. Blue bars = years more intense than the 1961–90 baseline; orange = less intense. Data: SILO Patched Point Dataset. Analysis: Lindsay Millard.</figcaption>
</figure>

<figure>
  <img src="/images/2026-02_sdii-rainfall-intensity-chart-2.jpg" alt="SDII rainfall intensity anomaly chart — Australian location 1889-2024">
  <figcaption>Annual rainfall intensity anomaly (SDII), 1889–2024 — second location. Data: SILO Patched Point Dataset. Analysis: Lindsay Millard.</figcaption>
</figure>

*The full set of four location charts (Bundaberg -3.9%, Townsville +16.5%, Sydney +11.8%, Toowoomba +21.0%) is available on the [original LinkedIn post](https://www.linkedin.com/in/lindsaymillard/).*

## What the Pattern Shows

The results are not uniform — and that's the point. Bundaberg's -3.9% sits alongside Toowoomba's +21.0%. This is consistent with Nicholas Deeks' recent regional analysis showing national-average scaling coefficients (7.2% per °C) that mask enormous regional variation — from 21.3% per °C in the Monsoonal North to 1.4% in winter-dominant southern regions.

The southeast Queensland and coastal NSW stations are showing the strongest intensification signal. For infrastructure design in these regions, the assumption that historical IFD curves remain valid is increasingly difficult to defend.

## The Code

The Python script pulls live SILO data via API for any Australian station and generates the plot automatically. Key libraries: `pandas`, `matplotlib`, `requests`.

Drop a comment on the [LinkedIn post](https://www.linkedin.com/in/lindsaymillard/) or [email me](mailto:lindsay.milard@outlook.com.au) and I'll share the code for your location.

---

*Inspired by Professor Ed Hawkins' [Climate Stripes](https://showyourstripes.info/). Data: SILO Patched Point Dataset, Queensland Government Long Paddock project.*
*Originally shared on [LinkedIn](https://www.linkedin.com/in/lindsaymillard/) — 3,536 impressions.*
