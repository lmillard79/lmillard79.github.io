---
layout: archive
title: "Climate Risk & Non-Stationarity"
permalink: /climate-risk/
author_profile: true
header:
  overlay_color: "#0f172a"
  overlay_filter: 0.7
  overlay_image: /images/pano1.jpg
  caption: "Reading the evidence for a flood and water-security practice, without overreaching it"
classes: wide
---

<div class="intro text-center" style="max-width: 800px; margin: 0 auto 3rem auto; font-size: 1.15rem; color: #cbd5e1;">
  <p>
    Design flood and water-security assessments run on an assumption: that the historical record still represents the system being designed for. These posts sit at the edge of that assumption — reporting what specific events, records, and datasets show, and what that might mean for practice, without overstating what a single event or dataset can prove.
  </p>
  <p style="margin-top: 1rem;">
    Formal climate attribution is its own discipline, with its own methods and its own experts. What follows here is a flood engineer's read of the evidence in front of them, written to inform rather than to pronounce.
  </p>
</div>

{% assign climate_posts = site.posts | where_exp: "post", "post.tags contains 'climate-change'" %}

{% if climate_posts.size > 0 %}
  <div class="grid__wrapper">
    {% for post in climate_posts %}
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
    <p>New posts in this series are in progress.</p>
  </div>
{% endif %}
