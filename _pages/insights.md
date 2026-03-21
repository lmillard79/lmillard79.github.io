---
layout: archive
title: "Insights & Thought Leadership"
permalink: /insights/
author_profile: true
header:
  overlay_color: "#0f172a"
  overlay_filter: 0.7
  overlay_image: /images/pano1.jpg
  caption: "Perspectives on water engineering and data science"
classes: wide
---

<div class="intro text-center" style="max-width: 800px; margin: 0 auto 3rem auto; font-size: 1.15rem; color: #cbd5e1;">
  <p>
    Professional commentary and analysis on flood modelling, hydrological data science, and engineering practice in Australia.
    Originally published across LinkedIn and expanded here.
  </p>
  <p style="margin-top: 1rem;">
    <a href="https://www.linkedin.com/in/lindsaymillard" class="btn btn--inverse" target="_blank" rel="noopener">
      <i class="fab fa-linkedin"></i> Follow on LinkedIn
    </a>
  </p>
</div>

{% assign insights_posts = site.posts | where_exp: "post", "post.categories contains 'insights'" %}

{% if insights_posts.size > 0 %}
  <div class="grid__wrapper">
    {% for post in insights_posts %}
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
    <p>Articles are coming soon. In the meantime, connect on <a href="https://www.linkedin.com/in/lindsaymillard" target="_blank" rel="noopener">LinkedIn</a> for regular updates on flood modelling and water data science.</p>
  </div>
{% endif %}
