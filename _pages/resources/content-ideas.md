---
title: "Content Ideas Backlog"
permalink: /resources/content-ideas/
layout: single
---

Internal working note — excluded from the build (see `_config.yml` exclude list), not a published page.

## Source

Full LinkedIn post history (`Shares.csv`, 681 rows) lives in Google Drive at the
`LinkedIn_HISTORY` folder referenced in `README_Content_Sources.md` (also in
Drive). A September 2026 pass filtered that down to 83 substantive original
posts (not reposts, >300 characters) spanning 2021–2025. What follows is a
curated subset — genuinely good raw material, not an exhaustive list. Grep
the full CSV by date if you want a post not listed here.

## Already written up as full posts

- Baseflow separation (Lyne-Hollick) — `2026-04-11-baseflow-separation-lyne-hollick-python.md`
- Model performance metrics (NSE/KGE/PBIAS) — `2026-04-18-model-performance-metrics-nse-kge-python.md`
- Joy Division / ridge plot rainfall (2025-01-13) — published
- Gabba cricket rainfall (2024-12-17) — published
- Ingham cumulative rainfall (2025-02-03, 2025-02-16) — published
- Kedron Brook flood study read (2025-03-15 area) — published
- pyextremes ARR2019 fork — published

## Strong candidates — data/code angle, not yet written

- **BARRA-R2 hourly reanalysis dataset** (2025-01-02, 2024-12-24 ×3, 2024-12-18) — BOM's new hourly dataset back to 1979; wettest-month animations already drafted in the LinkedIn posts. Novel, nobody else covering this from a practitioner angle.
- **AI in flood forecasting, compared** (2024-12-18 Google Floodhub, 2023-10-02 GraphCast) — practitioner's-eye view of what's actually useful vs. hype in the two highest-profile ML weather/flood tools.
- **The AEP/probability order-of-magnitude misunderstanding** (2025-01-21, 1,379 chars — the single longest post in the archive) — a misconception you say you explain to clients and regulators constantly. Pure expertise, no data pull needed, probably the single best "explainer" candidate in the backlog.
- **Skew-T / aerological diagrams** (2024-01-29) — BOM weather balloon data explainer, visual and technical, nothing like it currently on the site.
- **SILO spaghetti plots** (2023-12-19) — technique piece, fits the existing joyplot/heatmap data-viz aesthetic.
- **Terry Malone's calibrated URBS datasets** (2025-07-17) — directly extends the existing peak-flow frontier analysis post rather than starting fresh.
- **Uncertainty communication in FFA** (2023-12-18, 1,217 chars) — pairs naturally with the AEP misunderstanding post above; consider merging.
- **1974 floods, 50th anniversary roundup** (2024-01-22) — timely historical hook, technical work compilation, ties to existing Brisbane River content.
- **Dec 2024 Brisbane rain event** — Norman Creek flooded cars (2024-12-01) + "epic/unprecedented" media-terminology critique (2024-12-01, same day) — personal observation + technical read, could merge into one post.
- **Continuous simulation IFD comparison** (2024-05-22) — draft output comparing rainfall-derived vs. gauge-derived IFD, responding to a Peter Coombes post. Needs checking whether the underlying plot/data is still available.

## Also found: reusable visual assets

`WebsiteLinkedin` Drive folder has custom NotebookLM-generated infographics comparing TCEV vs. traditional LP3/GEV flood frequency models, citing Totaro/Kuczera/Iacobellis papers — connects directly to the TCEV support already in the pyextremes fork on `/projects/`. "Why I added TCEV" is a strong post with visuals largely built already.

## Lower priority (commentary/reshare-heavy, weaker fit for the site's data/code bar)

Energy storage vs. dams policy commentary (2023-11-27), Panama Canal/Hong Kong/California flood news commentary (2023-11-01, 2023-11-22, 2024-02-07), Warwick/Stanthorpe family holiday reflection (2024-09-09 — good personality piece if a lighter/personal post is ever wanted, just not a technical one), various conference shout-outs and link-shares without much original analysis attached.

## Notes on tone

Everything above is genuinely yours (own analysis, own charts, own words) — filtered specifically to exclude reposts of others' content per the earlier LinkedIn audit. Still worth a read-through before publishing verbatim; LinkedIn posts are written for a feed, not a blog, and most will want restructuring (a real intro/conclusion, code you can actually run, a citation instead of an in-line link) rather than a straight copy-paste.
