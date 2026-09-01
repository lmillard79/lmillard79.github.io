---
title: "Automating Flood Model Post-Processing with Python"
date: 2025-03-01
categories: [insights]
tags: [python, automation, flood-modelling, tuflow]
excerpt: "Post-processing TUFLOW results used to take hours. Here's how a few Python scripts changed that — and what I learned building them."
header:
  overlay_color: "#0f172a"
  overlay_filter: 0.7
  overlay_image: /images/pano1.jpg
read_time: true
---

Anyone who has delivered a TUFLOW flood study knows the post-processing grind. Hundreds of scenarios, dozens of output variables, regulatory tables that need to be formatted just so. For years this was manual — open SMS/QGIS, extract levels, paste into Excel, repeat.

Python changed that for me. This post covers what I built and why.

## The Pattern That Makes This Work

The fundamental insight is that TUFLOW output files are structured. Once you understand the format — `.dat` check files, `.csv` time series, NetCDF grids — you can write code that is completely reusable across projects.

My standard workflow uses three layers:

1. **Extraction**: `tuflow_utils` / `floodmodeller_api` / direct NetCDF parsing with `xarray` to pull raw results
2. **Transformation**: `pandas` for the heavy lifting — joining scenarios, calculating afflux, finding peak levels at points of interest
3. **Reporting**: `openpyxl` or `Jinja2` templates to generate formatted tables and figures directly into report-ready outputs

## The Afflux Calculation Example

A classic regulatory deliverable is an afflux table: peak water level at nominated points under existing vs. proposed conditions, across multiple AEP events.

With a manual workflow this might take half a day. With automation:

```python
import pandas as pd
import numpy as np

def calculate_afflux(existing_df, proposed_df, poi_ids):
    """
    Calculate afflux at points of interest across all scenarios.

    existing_df / proposed_df: columns = [scenario, poi_id, peak_wl]
    Returns: pivot table of afflux values
    """
    merged = existing_df.merge(proposed_df, on=["scenario", "poi_id"], suffixes=("_ex", "_prop"))
    merged["afflux"] = merged["peak_wl_prop"] - merged["peak_wl_ex"]
    return merged.pivot_table(index="poi_id", columns="scenario", values="afflux")
```

The actual result extraction takes a few more lines, but the principle is the same. The key is that **the logic is written once** and tested once — after that it's just a matter of pointing it at new data.

## What I Learned Building These Tools

**Start with the output format.** It's tempting to build a general-purpose extraction tool, but the regulatory reporting format is your real constraint. Work backwards from the table your client needs and build the extraction logic to feed it.

**Version control everything.** Scripts that live in a project folder get copied, modified, and diverge. Keeping these in a shared repository (even a private one) means improvements propagate to future projects.

**Don't automate the QA judgment.** Automation is great for mechanical tasks. Flag anomalies — unexpected negatives, suspiciously large afflux values, scenarios that didn't converge — but keep a human in the loop for sign-off. Clients are paying for your engineering judgment, not just your efficiency.

## The Time Savings Are Real

A post-processing workflow that used to take 2 days for a typical study now takes 2–3 hours of script execution and review. That's time that goes back into model review, sensitivity testing, and actually understanding what the results are telling you.

---

*I'm happy to share code snippets or discuss specific post-processing challenges. Reach out via [LinkedIn](https://www.linkedin.com/in/lindsaymillard) or [email](mailto:lindsay.millard@outlook.com.au).*
