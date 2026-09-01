# Notebook 07 — pyraingen Evaluation

> **Related article:** [Stochastic Rainfall Generation with pyraingen: A Practitioner's Evaluation](https://lmillard79.github.io/insights/2026/09/01/pyraingen-stochastic-rainfall-evaluation.html)

## What this notebook does

A real, evidence-based evaluation of [pyraingen](https://pypi.org/project/pyraingen/) 1.0.0 — a stochastic daily/subdaily rainfall generation package with IFD constraining. Not a tutorial: this documents what actually happened trying to install and run it on Linux, including a dependency-pin conflict, a Windows-only compiled core that blocks the main daily/subdaily generator entirely on Linux/macOS, and an internal-helper function (`computeIFD`) whose return shape looks inconsistent with its own docstring.

## Why it matters

Stochastic rainfall generation is a genuinely useful way to explore a much larger sample of plausible rainfall behaviour — at different durations and AEPs — than a single historical record provides. `pyraingen` is one of the only Python packages attempting this for Australian conditions. Anyone considering it for real project work should know what this notebook found before building a workflow around it.

## Contents

```
07_pyraingen_evaluation/
├── README.md
├── pyraingen_evaluation.ipynb   # main notebook
└── data/                         # empty — no external data
```

## Dependencies

```
numpy
pyraingen
```

For the parts of `pyraingen` beyond `computeIFD` (see the notebook and article), a working install additionally needs `numpy<2` pinned manually, and — for the core daily/subdaily simulator — either a Windows/CPython 3.8 environment or compiling the bundled Fortran source yourself.

## Status

- [x] Notebook written
- [x] Dependency-pin conflict reproduced in a clean virtualenv (not an artifact of one messy environment)
- [x] Windows-only compiled binary confirmed via package file listing
- [x] `computeIFD` return-shape issue reproduced with real executed code
- [x] Article published
- [ ] Full daily-sim -> subdaily disaggregation -> IFD conditioning pipeline — not achievable on Linux with the current PyPI release; would need either a Windows environment or compiling the bundled `.for` source locally
