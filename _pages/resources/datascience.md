---
title: "Data Science Blog & Projects"
permalink: /datascience/
header:
  image: "/images/pano1.jpg"
  caption: "Data-Driven Solutions for Water Resources Challenges"
---

# Data Science & Hydrological Projects

Explore my work at the intersection of hydrology, environmental science, and data analysis. These projects demonstrate how modern data science techniques can be applied to solve complex water resources engineering problems.

## Blog Posts

{% for post in site.posts %}
  <article class="archive__item" itemscope itemtype="https://schema.org/CreativeWork">
    <h2 class="archive__item-title" itemprop="headline">
      <a href="{{ post.url | relative_url }}" rel="permalink">{{ post.title }}</a>
    </h2>
    <p class="page__meta">
      <i class="far fa-calendar-alt" aria-hidden="true"></i> {{ post.date | date: "%B %d, %Y" }}
    </p>
    <p class="archive__item-excerpt" itemprop="description">{{ post.excerpt | markdownify | strip_html | truncate: 160 }}</p>
  </article>
{% endfor %}

## Technical Expertise

### Programming & Data Analysis
- **Python:** Pandas, NumPy, SciPy, Matplotlib, Seaborn
- **R:** Statistical modeling and data visualization
- **Database Technologies:** SQL, Data warehousing concepts

### Hydrological Modeling
- **Continuous Simulation:** GoldSim, WaterRIDE
- **Event-Based Modeling:** TUFLOW, MIKE FLOOD, HEC-RAS
- **Conceptual Models:** RORB, URBS

### Data Visualization
- Interactive dashboards with Tableau
- Custom visualizations with Python and R
- GIS mapping and spatial analysis

## Publications & Presentations

- *"Python the lingua franca of FEWS"* - Presentation at Delft FEWS User Day Melbourne 2019
- Technical reports on flood risk assessment methodologies
- Internal documentation on innovative modeling approaches

## Open Source Contributions

I contribute to the water resources engineering community through:
- Code repositories for model adapters and utilities
- Technical documentation and tutorials
- Participation in professional forums and discussions

[View GitHub Profile](https://github.com/lmillard79){: .btn .btn--success}

---

*For consulting opportunities or collaboration on water resources projects, please [contact me](mailto:lindsay.milard79@gmail.com).*
