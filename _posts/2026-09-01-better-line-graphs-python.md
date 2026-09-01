---
title: "Better Line Graphs for Hydrologic Data — a Python Port of Tony Ladson's R Method"
date: 2026-09-01
categories: [insights]
tags: [python, tutorial, hydrology, data-visualisation, open-source]
excerpt: "A sequential colour palette is the wrong tool for distinguishing unrelated categories — it implies a ranking that isn't there and gives the least contrast exactly where you need the most. A Python port of Tony Ladson's before/after example, plus direct line labelling instead of a legend."
header:
  overlay_color: "#0f172a"
  overlay_filter: 0.7
  overlay_image: /images/pano1.jpg
read_time: true
---

Third in an occasional series porting specific methods from [Tony Ladson's blog](https://tonyladson.wordpress.com/) to Python — his explanation and the underlying method are his; I'm just providing a translation for readers who know Python better than R. Sources: [Visualising Hydrologic Data](https://tonyladson.wordpress.com/2018/12/02/visualising-hydrologic-data/) and the concrete worked example, [Better line graphs for hydrologic data](https://tonyladson.wordpress.com/2018/08/06/better-line-graphs-for-hydrologic-data/), R in his [gist](https://gist.github.com/TonyLadson/732e3dbcb8aeaf76fd25c04f6ff246b7).

Six creeks, six unrelated peak-flow-vs-duration lines on one chart. Ladson's example (invented creek names, made-up numbers — a teaching example, not a real gauge record) makes two points at once.

## Point one: sequential palettes are for ordered data

```python
blues = plt.cm.Blues(np.linspace(0.35, 0.95, len(creeks)))  # mimics brewer.pal(8,'Blues')[3:8]

fig, ax = plt.subplots(figsize=(7, 5))
for (name, flows), color in zip(creeks.items(), blues):
    ax.plot(durations, flows, marker='o', color=color, label=name)
ax.legend(fontsize=8)
```

<figure>
  <img src="/images/2026-09_line-graphs-v1-avoid.png" alt="Line graph of six unrelated creeks using a sequential Blues colour palette, showing poor contrast between similarly-valued lines">
  <figcaption>Sequential palette on unordered categories. Rocky, Reedy and Waterhole Creeks — the three lines closest together in value, exactly where the reader most needs contrast — are also the three closest together in colour.</figcaption>
</figure>

A sequential palette encodes *order* — light to dark implies low to high. These six creeks have no natural order; picking a sequential palette to tell them apart imports a ranking that isn't there, and (worse, practically) the mid-range blues used for the middle of the palette are genuinely hard to tell apart at a glance.

## Point two: a legend makes the reader do the work

The fix is two changes at once: a qualitative palette built for categorical data (`Dark2` — matplotlib ships the identical ColorBrewer palette Ladson uses in R), and labelling each line directly instead of routing identification through a legend the reader has to look back and forth to.

```python
dark2 = plt.cm.Dark2(np.linspace(0, 1, len(creeks)))

fig, ax = plt.subplots(figsize=(8, 5.5))
for (name, flows), color in zip(creeks.items(), dark2):
    ax.plot(durations, flows, marker='o', color=color)
    ax.annotate(name, xy=(durations[0], flows[0]), xytext=(-8, 0),
                textcoords='offset points', ha='right', va='center', fontsize=8, color=color)
    ax.annotate(name, xy=(durations[-1], flows[-1]), xytext=(8, 0),
                textcoords='offset points', ha='left', va='center', fontsize=8, color=color)
for spine in ['top', 'right']:
    ax.spines[spine].set_visible(False)
```

<figure>
  <img src="/images/2026-09_line-graphs-v2-better.png" alt="The same six creeks using a qualitative Dark2 colour palette with direct line labels instead of a legend">
  <figcaption>Qualitative palette, labelled directly at both ends, minimal frame. No legend to decode; each creek reads as itself.</figcaption>
</figure>

Not perfect — where lines start close together (Reedy, Rocky and Waterhole Creeks all begin within about 150 units of each other), the left-hand labels still sit tight against one another. That's an honest limitation of direct labelling when the data itself is genuinely bunched, not something the technique fixes for free — it shows up in Ladson's original R version too, for the same reason.

---

**Companion notebook:** [`notebooks/10_better_line_graphs/`](https://github.com/lmillard79/lmillard79.github.io/tree/main/notebooks/10_better_line_graphs)

**Source:** Ladson, A.R. (2018). [Better line graphs for hydrologic data](https://tonyladson.wordpress.com/2018/08/06/better-line-graphs-for-hydrologic-data/); companion page [Visualising Hydrologic Data](https://tonyladson.wordpress.com/2018/12/02/visualising-hydrologic-data/). R source: [gist.github.com/TonyLadson/732e3dbcb8aeaf76fd25c04f6ff246b7](https://gist.github.com/TonyLadson/732e3dbcb8aeaf76fd25c04f6ff246b7).
