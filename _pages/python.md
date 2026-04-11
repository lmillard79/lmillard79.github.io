---
layout: archive
title: "Python for Hydrology"
permalink: /python/
author_profile: true
header:
  overlay_color: "#0f172a"
  overlay_filter: 0.7
  overlay_image: /images/pano1.jpg
  caption: "Reproducible Python workflows for Australian hydrology practice"
classes: wide
---

<div class="intro text-center" style="max-width: 800px; margin: 0 auto 3rem auto; font-size: 1.15rem; color: #cbd5e1;">
  <p>
    Reproducible Python workflows for Australian flood hydrology, grounded in ARR 2019 and calibrated against established Australian methods.
    Each post links to a companion Jupyter notebook you can run on your own data.
  </p>
  <p style="margin-top: 1rem;">
    <a href="https://github.com/lmillard79/lmillard79.github.io/tree/main/notebooks" class="btn btn--inverse" target="_blank" rel="noopener">
      <i class="fab fa-github"></i> All Notebooks on GitHub
    </a>
  </p>
</div>

{% assign python_posts = site.posts | where_exp: "post", "post.tags contains 'tutorial'" %}

{% if python_posts.size > 0 %}
  <div class="grid__wrapper">
    {% for post in python_posts %}
      <div class="grid__item">
        <article class="archive__item">
          <h3 class="archive__item-title no_toc">
            <a href="{{ post.url | relative_url }}">{{ post.title }}</a>
          </h3>
          <p class="page__meta" style="font-size: 0.8rem; color: #94a3b8; margin-bottom: 0.5rem;">
            <i class="far fa-calendar-alt"></i>
            {{ post.date | date: "%B %-d, %Y" }}
            {% if post.tags.size > 0 %}
              &nbsp;&mdash;&nbsp;
              {% for tag in post.tags limit:3 %}
                <span style="background: rgba(255,255,255,0.1); border-radius: 3px; padding: 2px 7px; margin-right: 4px; font-size: 0.75rem;">{{ tag }}</span>
              {% endfor %}
            {% endif %}
          </p>
          <p class="archive__item-excerpt">{{ post.excerpt | strip_html | truncate: 160 }}</p>
          <a href="{{ post.url | relative_url }}" class="btn btn--primary btn--small">Read More</a>
        </article>
      </div>
    {% endfor %}
  </div>
{% else %}
  <div class="notice--info">
    <p>The first tutorials are in progress. In the meantime, browse the <a href="https://github.com/lmillard79/lmillard79.github.io/tree/main/notebooks" target="_blank" rel="noopener">notebooks on GitHub</a> to see what is coming.</p>
  </div>
{% endif %}

---

<div style="margin-top: 2rem; color: #94a3b8; font-size: 0.95rem;">
  <h3 style="color: #cbd5e1;">The series</h3>
  <p>Five starter posts covering the Python tools that Australian flood hydrology practitioners need but do not yet have in one place:</p>
  <ol>
    <li><strong>Baseflow Separation</strong> — Lyne-Hollick filter, Python translation of Ladson et al. (2013)</li>
    <li><strong>ARR Temporal Pattern QA</strong> — screen for embedded burst errors before ensemble runs</li>
    <li><strong>ARF Calculator</strong> — ARR 2019 Book 2 equations, all 11 regions, importable module</li>
    <li><strong>Monte Carlo Loss Sampling</strong> — ARR 2019 IL/CL distributions, URBS pre-processor output</li>
    <li><strong>Model Performance Metrics</strong> — NSE, KGE, PBIAS, and peak flow bias compared</li>
  </ol>
</div>
