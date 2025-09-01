---
layout: default
title: "Data Science Blog"
permalink: /datascience/
author_profile: true
header:
  overlay_color: "#000"
  overlay_filter: "0.5"
  overlay_image: /images/pano1.jpg
  caption: "Data Science and Analytics"
---

<div class="blog-container">
  <h1 class="page-title">Data Science Blog</h1>
  
  <div class="intro-text">
    <p>Insights, tutorials, and case studies on data science, machine learning, and statistical analysis in water resources engineering.</p>
  </div>

  <div class="categories-grid">
    {% for category in site.categories %}
      <div class="category-card">
        <h2 class="category-title">{{ category[0] | capitalize }}</h2>
        <ul class="post-list">
          {% for post in category[1] %}
            <li class="post-item">
              <a href="{{ post.url | relative_url }}" class="post-link">
                <span class="post-title">{{ post.title }}</span>
                <span class="post-date">{{ post.date | date: "%b %-d, %Y" }}</span>
              </a>
            </li>
          {% endfor %}
        </ul>
      </div>
    {% endfor %}
  </div>

  <div class="all-posts">
    <h2>All Posts</h2>
    <ul class="post-list">
      {% for post in site.posts %}
        <li class="post-item">
          <a href="{{ post.url | relative_url }}" class="post-link">
            <span class="post-title">{{ post.title }}</span>
            <span class="post-date">{{ post.date | date: "%b %-d, %Y" }}</span>
          </a>
          {% if post.tags.size > 0 %}
            <div class="post-tags">
              {% for tag in post.tags %}
                <span class="tag">{{ tag }}</span>
              {% endfor %}
            </div>
          {% endif %}
        </li>
      {% endfor %}
    </ul>
  </div>
</div>
      {% for tag in post.tags %}
        <span class="tag">{{ tag }}</span>
      {% endfor %}
    {% endif %}
  </p>
  {% if post.excerpt %}
    <p>{{ post.excerpt | strip_html | truncatewords: 30 }}</p>
  {% endif %}
  <hr>
{% endfor %}