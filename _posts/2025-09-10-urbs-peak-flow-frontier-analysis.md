---
title: "Exploring Frontier Relationships in 16,437 Calibrated Australian URBS Models"
date: 2025-09-10
categories: [insights]
tags: [hydrology, flood-modelling, continuous-simulation]
excerpt: "What happens when you plot rainfall, catchment area and peak flow for 55,000 print locations from Terry Malone's calibrated Australian URBS dataset? A frontier emerges — and it aligns with the TMR QRT relationship."
header:
  overlay_color: "#0f172a"
  overlay_filter: 0.7
  overlay_image: /images/pano1.jpg
read_time: true
---

One of the underappreciated assets in Australian hydrology is the calibrated URBS model dataset compiled by Terry Malone — a collection of models spanning catchments across the continent, each with peak ratios (PR) derived from PQH files comparing gauge observations to modelled outputs.

At around 55,000 print locations, this is a substantial cross-section of Australian hydrology. I wanted to see what the data said if you looked at it differently: not model-by-model, but as a cloud of observations from which a **frontier relationship** might emerge.

## The Question

When you plot rainfall, catchment area and peak flow together across 16,437 calibrated URBS locations, does a physically meaningful envelope appear? And if so, does it correspond to known regional flood estimation relationships?

<figure>
  <img src="/images/2023_urbs_peak-flow-frontier-analysis-australia.png" alt="URBS peak flow frontier analysis — 16,437 Australian calibrated models">
  <figcaption>Four-panel figure. <strong>Top left:</strong> Excess Rainfall vs Peak Flow scatter (16,437 URBS locations), coloured by total rainfall. <strong>Top right:</strong> Area vs Peak Flow log-log scatter — frontier ORT relationship 7×Area<sup>0.644</sup> overlaid. <strong>Bottom panels:</strong> Histograms of Peak Flow and Excess Rainfall distributions across the dataset. Source: Terry Malone URBS calibrated dataset. Analysis: WRM Water &amp; Environment — Lindsay Millard, 2023.</figcaption>
</figure>

## What the Frontier Shows

The log-log scatter of area versus peak flow does produce a frontier — a bounding envelope that the dataset approaches but doesn't exceed. The form of this frontier is:

**ORT relationship: Q = 7 × Area^0.644**

This aligns closely with the Queensland Regional Flood Estimation (QRT) relationship published by TMR, which is reassuring — it suggests the frontier is capturing a physically real upper bound on peak flow per unit catchment area, not a statistical artefact.

## What This Might Mean

As we approach the frontier, the implication is that catchments are approaching the maximum runoff efficiency — close to a runoff coefficient of 1.0 for the design event. Events near or on the frontier correspond to conditions where:

- Soils are fully saturated (antecedent moisture at maximum)
- Rainfall intensity is high relative to catchment storage capacity
- The relationship between area and peak flow holds most cleanly

The corollary is that data points well below the frontier indicate either: sub-saturated antecedent conditions, significant attenuation through storage or floodplain routing, or lower rainfall intensity relative to capacity.

## Where to Take This Analysis

This was exploratory work in progress. Some directions worth pursuing:

1. **Climate zone stratification** — does the frontier coefficient vary systematically by Köppen classification or BOM climate zone? The Monsoonal North versus the southeast coastal zone should behave differently.

2. **Event conditioning** — selecting only events with high antecedent moisture (soil moisture > 90th percentile from AWRA-L) should push points closer to the frontier.

3. **Regional calibration** — can the frontier be used as a sanity check on new URBS calibrations? A model producing peak flows well above the regional frontier for a given area warrants scrutiny.

4. **Comparison to RFFE** — how does the frontier relationship compare to the ARR Regional Flood Frequency Estimation outputs for the same catchments?

The dataset exists and is well-curated. The analysis is straightforward. It's the kind of investigation that rarely gets done because it sits between individual project deliverables rather than within them.

---

*Dataset: Terry Malone's calibrated Australian URBS models (PQH output files).*
*Analysis: WRM Water &amp; Environment — Lindsay Millard, 2023.*
*Originally shared on [LinkedIn](https://www.linkedin.com/in/lindsaymillard/) — 75 reactions.*
