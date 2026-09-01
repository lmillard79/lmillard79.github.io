---
title: "AI Doesn't Remove the Judgment Calls in Climate Science — It Just Makes Them Easier to Miss"
date: 2026-09-01
categories: [insights]
tags: [machine-learning, climate-change, open-science]
excerpt: "A benchmark of AI rainfall-downscaling models found no single model performed best across every metric or region — a precise, checkable illustration of a bigger point: AI doesn't invent scientific judgment calls, it just makes them more numerous, less visible, and easier to propagate unexamined."
header:
  overlay_color: "#0f172a"
  overlay_filter: 0.7
  overlay_image: /images/pano1.jpg
read_time: true
---

A paper crossed my feed this week benchmarking AI methods for precipitation downscaling over Australia — refining coarse climate model output down to a resolution useful for local planning. The finding that stuck with me: model performance rankings changed depending on which metric you evaluated against — total rainfall, spatial pattern, seasonal cycle, or long-term trend — and depending on which region of Australia you looked at. No model won across the board.

That's not a failure. It's the same lesson I landed on writing up [pyraingen](/insights/2026/09/01/pyraingen-stochastic-rainfall-evaluation.html) a few days ago, from a completely different angle: whether a tool is "good" isn't a yes/no question. It depends what you actually need it to get right, at what scale, for what decision. A downscaling model tuned to reproduce seasonal totals isn't automatically the right choice for someone who needs trend fidelity, and neither of those is wrong — they're answering different questions.

## The actual argument, which isn't "AI bad"

I found that paper via a piece from the ARC Centre of Excellence for 21st Century Weather, by Taimoor Sohail (University of Melbourne) and Sanaa Hobeichi (UNSW Sydney) — ["A wave of AI slop is coming for climate science"](https://21centuryweather.org.au/a-wave-of-ai-slop-is-coming-for-climate-science-the-best-defence-is-to-retain-and-upskill-our-scientists). The title reads more alarmist than the piece actually is. Their real argument is more precise than "AI produces bad science," and worth taking on its own terms rather than the headline: every quantitative study already involves judgment calls — which data to include, how to handle missing values, what baseline to use, how to aggregate results. None of that is new to AI. What changes is that these choices become more numerous, less visible, and easier to propagate once a pipeline involves a trained model — sitting in a preprocessing step, a resampling choice, a default setting, discoverable only in a script, if documented at all.

Their own example is the honest version of this: quality-checking Antarctic Ocean salinity data with a neural network, they found a genuine result — seal-mounted sensors carry a consistent salty bias that survives existing quality control. Getting there required building a synthetic dataset from a high-resolution ocean model to reconcile ship, float and seal data collected in different places and seasons, and that process ended up duplicating somewhere between 7% and 17% of synthetic profiles, depending on source. They caught it, checked whether it distorted the result, and reported it themselves in the paper. That's not a cautionary tale about a mistake — it's what the discipline they're arguing for actually looks like in practice.

The downscaling paper (the one I opened with) is their second example — and it turns out to be their own work: Sanaa Hobeichi is the corresponding author on both the paper and the piece that pointed me to it. Three ML models (a generative diffusion model, a vision transformer, and a recurrent neural network) were benchmarked against 24 regional climate model simulations across four fundamental rainfall characteristics — totals, spatial pattern, seasonal cycle, trend — using pre-defined minimum skill thresholds rather than just ranking whatever came out on top. All three ML models cleared the bar; so did 10 of the 24 RCMs. The paper doesn't claim "AI wins" — it publishes the benchmark methodology and the raw model outputs alongside the RCM scores, specifically so other researchers can check the claim rather than take it on trust. That's the provenance argument made concrete, not asserted as a slogan.

## Where this lands for me

I don't have a horse in the AI-and-climate-science-jobs debate — that's not my field, and the piece raises a real point about timing that's above my pay grade to weigh in on (they note this is landing in the same year as real job losses across the climate and environmental sector, which is its own separate problem). What I do have an opinion on, from direct experience this week, is the mechanics of the actual argument: judgment calls don't disappear because a tool is faster. They just get easier to leave unexamined if nobody's checking.

That's the whole reason the pyraingen write-up turned into a bug report instead of a tutorial — I went in expecting to demonstrate a working pipeline, and instead found a dependency pin that breaks on install, a compiled binary that only runs on one platform, and a helper function whose own return shape doesn't match its documentation. None of that was hidden maliciously. It's exactly the "competent, well-intentioned team that didn't happen to look closely enough at one particular step" failure mode Sohail and Hobeichi describe — just in a small open-source package instead of a published dataset. The [Mann-Kendall self-check](/insights/2026/09/01/ffa-nonstationarity-outlier-diagnostic-python.html) in the FFA post the same week was the same instinct from the other direction: before trusting a statistical test on anything real, prove it can tell a known answer from a known non-answer.

None of that requires being an AI researcher. It requires treating "the tool produced an output" and "the output is right for what I need" as two separate questions, and being willing to actually check the gap between them — logging what you tried, what you checked, and what you're still unsure about, rather than presenting a clean result and hoping nobody asks. That's a fairly old engineering habit wearing a new hat. AI just raises the stakes on keeping it, because it's now cheap enough to skip.

---

**References:**
- Sohail, T. & Hobeichi, S. (2026). [A wave of AI slop is coming for climate science — the best defence is to retain and upskill our scientists](https://21centuryweather.org.au/a-wave-of-ai-slop-is-coming-for-climate-science-the-best-defence-is-to-retain-and-upskill-our-scientists). ARC Centre of Excellence for 21st Century Weather.
- [Applying a Standardized Benchmarking Framework to Evaluate AI Methods for Precipitation Downscaling over Australia](https://doi.org/10.1175/AIES-D-25-0048.1). *Artificial Intelligence for the Earth Systems*, 5(1), 2026.
