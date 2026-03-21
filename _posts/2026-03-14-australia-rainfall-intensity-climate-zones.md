---
title: "Australia's Rainfall Is Getting More Intense — And the Regional Variation Matters"
date: 2026-03-14
categories: [insights]
tags: [hydrology, climate-change, flood-modelling]
excerpt: "A 7.2% per °C average increase in extreme rainfall intensity across Australia conceals enormous regional variation — from 21.3% in the monsoonal north to 1.4% in winter-dominant southern regions. The implications for design flood estimation are not uniform."
header:
  overlay_color: "#0f172a"
  overlay_filter: 0.7
  overlay_image: /images/pano1.jpg
read_time: true
---

The headline number is striking: Australia is experiencing a **7.20% per °C increase in extreme rainfall intensity** (R²=0.96). But that national average conceals a regional story that matters enormously for design flood estimation in practice.

This analysis, produced by Nicholas Deeks (Technical Director — Hydrology, GHD), applies a rigorous statistical framework to station-level Australian rainfall data and deserves wide attention in the flood hydrology profession.

## The Methodology

The approach is technically sound:

- **Peaks Over Threshold (POT)** extraction with Generalised Pareto Distribution (GPD) fitting
- Dynamic thresholds to account for changing record characteristics
- Block bootstrap confidence intervals to quantify uncertainty
- Fixed-effects regression to derive **Clausius-Clapeyron scaling coefficients (α)** by climate region
- Regional violin plots showing the *distribution* of change within zones — not just a headline mean

## The Regional Picture

| Climate Region | Scaling Coefficient (α) | R² |
|---|---|---|
| Australia (national) | 7.20% per °C | 0.96 |
| Monsoonal North | 21.3% per °C | 0.84 |
| Winter-dominant South | 1.42% per °C | 0.93 |

The divergence is physically meaningful. In tropical and monsoonal regions, convective enhancement mechanisms exceed simple thermodynamic expectations — warming amplifies extreme rainfall through both moisture availability and convective organisation. The Clausius-Clapeyron relationship (roughly 7% per °C) understates the risk in these regions.

In winter-dominant southern regions, large-scale frontal systems dominate and the temperature-intensity relationship is weaker.

## What This Means for Practitioners

This is exactly the kind of independent, transparent analysis the profession needs as we grapple with non-stationarity in design flood estimation.

The practical implication is that **IFD curve adjustments for climate change should not use a single national scaling factor**. A flat 10% uplift applied uniformly across Australia overstates the risk in southern Victoria and significantly understates it in northern Queensland, the NT Top End, and monsoonal Western Australia.

For dam safety and major infrastructure assessments in tropical regions particularly, the 21.3% per °C scaling coefficient deserves serious consideration when selecting design climate change factors.

The Clausius-Clapeyron framing is physically grounded. The limitations are honestly stated in the original analysis. It's the kind of work that should be informing the next revision of Australian Rainfall and Runoff guidance on climate change.

---

*Analysis by Nicholas Deeks, GHD. Data: Bureau of Meteorology station network.*
*Originally shared on [LinkedIn](https://www.linkedin.com/in/lindsaymillard/) with commentary — 1,804 impressions.*
