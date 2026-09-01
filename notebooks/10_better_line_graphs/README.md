# Notebook 10 — Better Line Graphs for Hydrologic Data (Python port of Tony Ladson's R method)

> **Related article:** [Better Line Graphs for Hydrologic Data — a Python Port of Tony Ladson's R Method](https://lmillard79.github.io/insights/2026/09/01/better-line-graphs-python.html)
>
> **Original source:** [Visualising Hydrologic Data](https://tonyladson.wordpress.com/2018/12/02/visualising-hydrologic-data/) / [Better line graphs for hydrologic data](https://tonyladson.wordpress.com/2018/08/06/better-line-graphs-for-hydrologic-data/) — Tony Ladson. R source: [gist.github.com/TonyLadson/732e3dbcb8aeaf76fd25c04f6ff246b7](https://gist.github.com/TonyLadson/732e3dbcb8aeaf76fd25c04f6ff246b7)

## What this notebook does

Ports Ladson's before/after example: a sequential ("Blues") colour palette used to distinguish six unrelated creeks (wrong tool — implies a false ranking, poor contrast between similar-valued lines) versus a qualitative palette (Dark2 — matplotlib ships the identical ColorBrewer palette) with direct end-of-line labelling instead of a legend.

## Why it matters

Colour palette choice is not a matter of taste — sequential and qualitative palettes are built for different jobs, and using the wrong one actively works against the reader for exactly the data that most needs to be distinguished. This is a small, mechanical fix worth having as a habit.

## Contents

```
10_better_line_graphs/
├── README.md
├── better_line_graphs.ipynb   # main notebook
└── data/                       # empty — Ladson's illustrative example data is embedded in-notebook
```

## Dependencies

```
numpy
matplotlib
```

## Data note

The six-creek dataset is Ladson's own invented illustrative example (made-up creek names, made-up numbers) — not a real gauge record.

## Status

- [x] Notebook written
- [x] Both versions (sequential-palette-and-legend vs. qualitative-palette-and-direct-labels) rendered and compared
- [x] Figures exported to /images/
- [x] Article published
