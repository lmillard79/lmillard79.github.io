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
    &nbsp;
    <a href="/python/" class="btn btn--inverse">
      <i class="fab fa-python"></i> Python Tutorials
    </a>
  </p>
</div>

{% assign insights_posts = site.posts | where_exp: "post", "post.categories contains 'insights'" %}
{% assign tutorial_posts = insights_posts | where_exp: "post", "post.tags contains 'tutorial'" %}
{% assign commentary_posts = insights_posts | where_exp: "post", "post.tags != 'tutorial'" %}

{% if tutorial_posts.size > 0 %}
<h2 style="color: #cbd5e1; border-bottom: 1px solid rgba(255,255,255,0.1); padding-bottom: 0.5rem; margin-bottom: 1.5rem;">
  Python Tutorials
  <a href="/python/" style="font-size: 0.75rem; font-weight: normal; margin-left: 1rem; color: #94a3b8;">View all →</a>
</h2>

  <div class="grid__wrapper" style="margin-bottom: 3rem;">
    {% for post in tutorial_posts %}
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

<h2 style="color: #cbd5e1; border-bottom: 1px solid rgba(255,255,255,0.1); padding-bottom: 0.5rem; margin-bottom: 1.5rem;">Commentary</h2>
{% endif %}

{% if insights_posts.size > 0 %}
  <div class="grid__wrapper">
    {% for post in insights_posts %}
      {% unless post.tags contains 'tutorial' %}
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
      {% endunless %}
    {% endfor %}
  </div>
{% else %}
  <div class="notice--info">
    <p>Articles are coming soon. In the meantime, connect on <a href="https://www.linkedin.com/in/lindsaymillard" target="_blank" rel="noopener">LinkedIn</a> for regular updates on flood modelling and water data science.</p>
  </div>
{% endif %}
