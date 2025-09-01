---
layout: cayman
title: Data Science Blog
permalink: /datascience/
---

# Data Science Blog

## Categories

{% for category in site.categories %}
  <h2>{{ category[0] | capitalize }}</h2>
  <ul>
    {% for post in category[1] %}
      <li>
        <a href="{{ post.url | relative_url }}">{{ post.title }}</a>
        <small>{{ post.date | date: "%b %-d, %Y" }}</small>
      </li>
    {% endfor %}
  </ul>
{% endfor %}

## All Posts

{% for post in site.posts %}
  <h3>
    <a href="{{ post.url | relative_url }}">
      {{ post.title }}
    </a>
  </h3>
  <p>
    <small>{{ post.date | date: "%b %-d, %Y" }}</small>
    {% if post.tags.size > 0 %}
      <br>
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