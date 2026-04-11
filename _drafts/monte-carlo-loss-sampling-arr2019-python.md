---
title: "Sampling ARR 2019 Loss Distributions in Python — A URBS Pre-Processor"
date: 2026-04-11
categories: [insights]
tags: [python, tutorial, arr2019, urbs, flood-modelling, monte-carlo]
excerpt: "ARR 2019 recommends Monte Carlo simulation treating initial loss as a random variable. Most practitioners still use fixed median values because the sampling machinery isn't in their model front-ends. This post provides the missing pre-processor."
header:
  overlay_color: "#0f172a"
  overlay_filter: 0.7
  overlay_image: /images/pano1.jpg
read_time: true
---

<!-- COMPANION NOTEBOOK: notebooks/04_monte_carlo_loss_sampling/monte_carlo_loss_sampling.ipynb -->
<!-- STATUS: draft — notebook not yet written -->

## The ARR 2019 joint probability framework

_[What ARR 2019 actually asks us to do — treat IL as a random variable, not a fixed median]_

## The empirical IL distribution

_[ARR Table 5.3.13 — what the data says about IL variability across Australian catchments]_

## Python sampler

_[Short code block — draw N IL/CL pairs from the ARR distributions. Full implementation in notebook.]_

## Output format for URBS batch input

_[CSV structure. How to wire it into a URBS pre-processor.]_

## How many ensemble members do you actually need?

_[Figure: convergence of flood peak statistics with ensemble size N]_

## Monte Carlo sampling vs sensitivity testing

_[They are not the same thing. What each tells you and what each doesn't.]_

## Limitations

_[What this does not do. Regional vs national distributions. What practitioners should check before using in production.]_

---

**Companion notebook:** Full implementation at [`notebooks/04_monte_carlo_loss_sampling/monte_carlo_loss_sampling.ipynb`](https://github.com/lmillard79/lmillard79.github.io/tree/main/notebooks/04_monte_carlo_loss_sampling).

**Reference:** Ball et al. (2019). *Australian Rainfall and Runoff.* Book 5, Chapter 3.
