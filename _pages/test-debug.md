---
title: "Debug Test Page"
permalink: /test-debug/
layout: single
author_profile: true
---

# Debug Test Page

This is a test page to verify Jekyll permalink functionality.

**Current time:** {{ site.time }}

**Page URL:** {{ page.url }}

**Site URL:** {{ site.url }}

**Base URL:** {{ site.baseurl }}

**Permalink:** {{ page.permalink }}

## Navigation Test

- [Back to Home]({{ site.url }}{{ site.baseurl }}/)
- [About Page]({{ site.url }}{{ site.baseurl }}/about/)
- [Portfolio Page]({{ site.url }}{{ site.baseurl }}/portfolio/)

## Debug Info

- **Jekyll Environment:** {{ jekyll.environment }}
- **Site Title:** {{ site.title }}
- **Page Title:** {{ page.title }}
