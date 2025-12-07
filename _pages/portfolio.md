---
title: "Project Portfolio"
layout: archive
permalink: /portfolio/
author_profile: true
header:
  overlay_color: "#0f172a"
  overlay_filter: 0.7
  overlay_image: /images/beach.jpg
  caption: "Engineering & Data Science in Action"
---

<div class="intro text-center" style="margin-bottom: 3rem;">
  <p>A selection of case studies demonstrating technical excellence in flood modelling, software development, and complex data analysis.</p>
</div>

<!-- This loop will automatically find any post with the category 'portfolio' -->
<div class="feature__wrapper">
  {% assign projects = site.categories.portfolio %}
  {% if projects.size > 0 %}
    {% for post in projects %}
      <div class="feature__item">
        <div class="feature__item-teaser">
          {% if post.header.image %}
            <img src="{{ post.header.image }}" alt="{{ post.title }}">
          {% else %}
            <img src="{{ post.header.overlay_image | default: '/images/pano1.jpg' }}" alt="{{ post.title }}">
          {% endif %}
        </div>
        <h3 class="archive__item-title">{{ post.title }}</h3>
        <p class="archive__item-excerpt">{{ post.excerpt | strip_html | truncate: 100 }}</p>
        <a href="{{ post.url }}" class="btn--primary">View Case Study</a>
      </div>
    {% endfor %}
  {% else %}
    <div class="notice--warning">
      <p>No project showcases found yet. Add posts with <code>category: portfolio</code> to populate this gallery.</p>
    </div>
  {% endif %}
</div>

<h2 style="margin-top: 4rem; border-top: 1px solid rgba(255,255,255,0.1); padding-top: 2rem;">Technical Capabilities</h2>

<div class="grid__wrapper">
    <div class="grid__item">
        <h3><i class="fas fa-laptop-code"></i> Hydraulic Modelling</h3>
        <ul>
            <li><strong>TUFLOW:</strong> Classic & HPC, GPU acceleration, Advection-Dispersion</li>
            <li><strong>HEC-RAS:</strong> 1D/2D unsteady flow, dam breach</li>
            <li><strong>InfoWorks ICM:</strong> Integrated urban drainage</li>
        </ul>
    </div>
    <div class="grid__item">
        <h3><i class="fas fa-chart-line"></i> Data Science</h3>
        <ul>
            <li><strong>Python:</strong> Pandas, NumPy, Scikit-learn, GeoPandas</li>
            <li><strong>R:</strong> Tidyverse, ggplot2, Shiny</li>
            <li><strong>Statistics:</strong> Bayesian Inference, Extreme Value Analysis (EVA)</li>
        </ul>
    </div>
</div>
