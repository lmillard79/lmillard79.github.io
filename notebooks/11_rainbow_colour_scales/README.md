# Notebook 11 — Rainbow Colour Scales: Measuring Why They Mislead

> **Related article:** [Why Rainbow Colour Scales Mislead — a Python Follow-up to Tony Ladson's Post](https://lmillard79.github.io/insights/2026/09/01/rainbow-colour-scales-python.html)
>
> **Original source:** [Rainbow colour scales in hydrologic maps and charts](https://tonyladson.wordpress.com/2016/05/06/rainbow-colour-scales/) — Tony Ladson, drawing on Ed Hawkins' [Scrap rainbow colour scales](https://www.nature.com/articles/519291d) (*Nature*, 2015) and his [#ShowYourStripes](https://showyourstripes.info/) project.

## What this notebook does

Measures, rather than just asserts, why jet/rainbow colourmaps mislead: converts colourmaps to CIE L\*a\*b\* space (`colorspacious` — the same library used to justify the design of matplotlib's `viridis`) and checks whether perceptual lightness changes monotonically across the scale. `jet` doesn't (5 direction changes); `viridis` and `cividis` do (0). Then shows what that measurable property looks like on a smooth synthetic field with no real edges anywhere.

## Why it matters

"Don't use rainbow colourmaps" is good, common advice that's usually delivered as an assertion. This notebook is the same advice with the receipts — a concrete, checkable reason, not just a style preference.

## Contents

```
11_rainbow_colour_scales/
├── README.md
├── rainbow_colour_scales.ipynb   # main notebook
└── data/                          # empty — synthetic field only, no external data
```

## Dependencies

```
numpy
matplotlib
colorspacious   # pip install colorspacious -- not in the standard scientific stack
```

## Data note

No real dataset is used anywhere in this notebook — the point is a property of colourmaps themselves. Ed Hawkins' warming stripes are discussed and linked to, not reproduced; recreating them properly needs the real global temperature record, which wasn't fetchable in this environment.

## Status

- [x] Notebook written
- [x] Lightness monotonicity measured quantitatively (not just asserted)
- [x] Smooth-field false-banding demonstration rendered
- [x] Figures exported to /images/
- [x] Article published
