---
title: "A Practitioner's Primer on Bayesian Flood Frequency Analysis"
date: 2024-11-01
categories: [insights]
tags: [bayesian, flood-frequency, statistics, hydrology]
excerpt: "Bayesian methods for flood frequency analysis are no longer academic curiosities. Here's what they offer and when they're worth the extra effort."
header:
  overlay_color: "#0f172a"
  overlay_filter: 0.7
  overlay_image: /images/pano1.jpg
read_time: true
related: true
---

The standard approach to flood frequency analysis — fit a log-Pearson III, read off the quantiles, report confidence intervals — is familiar to every practitioner. It works. But it carries assumptions that Bayesian methods handle more honestly.

This post is a practitioner-level introduction: what Bayesian FFA offers, when it matters, and what the workflow looks like.

## The Classical FFA Problem

Given a record of annual maximum flows, we want to estimate the magnitude of the 1% AEP (100-year) flood. The classical (frequentist) approach:

1. Fit a parametric distribution (LP3 in Australia per ARR)
2. Estimate parameters using method of moments or MLE
3. Derive confidence intervals from the parameter covariance matrix

The fundamental limitation is **data scarcity**. A 30-year record is considered good for Australian catchments. But we're extrapolating to the 0.1% or even 0.01% AEP — events with return periods 10–100x longer than our record. The uncertainty in those estimates is enormous, and classical confidence intervals tend to understate it.

## What Bayesian FFA Adds

Bayesian methods treat the distribution parameters as random variables with probability distributions rather than fixed unknowns. This has two practical consequences:

**1. Prior information can be formally incorporated.** Regional flood frequency data, paleoflood evidence, or expert judgment about likely parameter ranges can be encoded as prior distributions. The posterior combines this with your gauged record.

**2. Uncertainty propagates correctly.** Because you're sampling from a joint posterior distribution over all parameters, the uncertainty in your quantile estimates naturally reflects both record length and extrapolation distance.

The result is quantile estimates with **credible intervals** — not confidence intervals. The distinction matters: a 90% credible interval means "there is a 90% probability the true value lies here, given the data and priors," which is actually what practitioners and planners want to know.

## A Simple Example in R

```r
library(nsRFA)
library(rstan)

# Fit LP3 via Bayesian MCMC (using Stan or JAGS)
# This sketch uses the log-space GEV for illustration

annual_max <- c(240, 380, 195, 440, 310, ...)  # your data

# Stan model would encode:
# mu ~ Normal(prior_mean, prior_sd)
# sigma ~ Half-Normal(0, prior_scale)
# xi ~ Normal(0, 0.2)  # shape — informative prior from regional data
# y ~ GEV(mu, sigma, xi)

# Posterior samples give you the full distribution over quantiles
```

I've written more detail on this in my [Bayesian Coin Toss post](/2019/05/12/BayesianCoinToss/) which walks through the mechanics of Bayesian updating — a useful foundation before tackling flood frequency.

## When Is It Worth It?

Bayesian FFA is most valuable when:

- **Record length is short** (< 20 years) and regional prior information is available
- **Extrapolation is extreme** (estimating 0.01% AEP events for dam safety)
- **Uncertainty communication matters** (clients or regulators need to understand risk, not just a point estimate)
- **Multiple data sources exist** — historic floods, botanical evidence, paleoflood records that can't be incorporated in classical methods

For routine flood impact assessments with adequate records, the added complexity is usually not warranted.

## The Regulatory Landscape

ARR 2019 acknowledges Bayesian methods but stops short of prescribing them. In Queensland, PFRA guidelines are increasingly receptive to uncertainty-aware approaches, particularly for infrastructure design. The practical constraint is that regulators need to review and accept the method — which means documentation and plain-language explanation are as important as the statistics themselves.

---

*More detail on my flood frequency analysis work is in the [Data Science section](/datascience/). For questions on specific applications, connect via [LinkedIn](https://www.linkedin.com/in/lindsaymillard).*
