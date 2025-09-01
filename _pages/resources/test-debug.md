---
title: "Testing & Debugging"
permalink: /resources/testing-debugging/
layout: single
header:
  image: "/images/pano1.jpg"
  caption: "Best practices for testing and debugging"
author_profile: true
---
# Debug Test Page

This is a test page to verify Jekyll permalink functionality with the Cayman theme.

## Page Information

- **Current time:** {{ site.time | date: "%Y-%m-%d %H:%M:%S %z" }}
- **Page URL:** {{ page.url }}
- **Site URL:** {{ site.url }}
- **Base URL:** {{ site.baseurl }}
- **Permalink:** {{ page.permalink }}

## Navigation

[Back to Home]({{ site.url }}{{ site.baseurl }}/) | 
[About]({{ site.url }}{{ site.baseurl }}/about/) | 
[Portfolio]({{ site.url }}{{ site.baseurl }}/portfolio/)

## Debug Information

- **Jekyll Environment:** {{ jekyll.environment }}
- **Site Title:** {{ site.title }}
- **Page Title:** {{ page.title }}