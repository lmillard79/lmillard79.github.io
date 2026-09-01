# Lindsay Millard — Professional Portfolio Website

[![GitHub Pages](https://img.shields.io/badge/GitHub%20Pages-222222?style=for-the-badge&logo=github&logoColor=white)](https://lmillard79.github.io/)
[![Jekyll](https://img.shields.io/badge/Jekyll-CC0000?style=for-the-badge&logo=jekyll&logoColor=white)](https://jekyllrb.com/)
[![Minimal Mistakes](https://img.shields.io/badge/Theme-Minimal%20Mistakes-159957?style=for-the-badge)](https://mmistakes.github.io/minimal-mistakes/)

This is the repository for my professional portfolio website, showcasing my work in hydrology, water resources engineering, and data science.

## Features

- **Dark, minimal-mistakes-based theme** for a clean, professional feel on any device
- **SEO optimised** via `jekyll-seo-tag`
- **Blog** for technical articles, insights, and Python tutorials
- **Project showcase** of open-source tools and technical work

## Project Structure

```
.
├── _includes/      # Reusable components (custom head, feature rows)
├── _layouts/       # Page templates (falls through to the remote theme
│                     where no local override is defined)
├── _pages/         # Main content pages (About, Expertise, Projects,
│                     Publications, Python, Blog resources)
├── _posts/         # Blog posts and technical write-ups
├── notebooks/      # Companion Jupyter notebooks for the Python series
├── assets/         # Static assets (CSS, JS, images)
└── _config.yml     # Site configuration
```

**Note:** `_pages/` starts with an underscore, so it is not picked up by Jekyll automatically — it's force-included via `include: [_pages]` in `_config.yml`. Keep that in mind if you ever rename or restructure it.

## Technical Stack

- **Static Site Generator**: [Jekyll](https://jekyllrb.com/)
- **Theme**: [Minimal Mistakes](https://mmistakes.github.io/minimal-mistakes/) (dark skin), loaded via `remote_theme`
- **Hosting**: [GitHub Pages](https://pages.github.com/)
- **CI/CD**: GitHub Actions (`.github/workflows/jekyll.yml`)

## Local Development

1. **Install prerequisites**
   - [Ruby](https://www.ruby-lang.org/en/documentation/installation/) 2.7+
   - [Bundler](https://bundler.io/): `gem install bundler`

2. **Clone the repository**
   ```bash
   git clone https://github.com/lmillard79/lmillard79.github.io.git
   cd lmillard79.github.io
   ```

3. **Install dependencies**
   ```bash
   bundle install
   ```

4. **Run the site locally**
   ```bash
   bundle exec jekyll serve
   ```
   The site will be available at `http://localhost:4000`.

## Deployment

The site deploys automatically to GitHub Pages via GitHub Actions whenever changes are pushed to `main`.

## Adding New Content

### Add a blog post

```bash
./_scripts/new_post.sh "Your Post Title"              # commentary/insights post
./_scripts/new_post.sh "Your Post Title" --tutorial    # Python tutorial post
```

Or create a file in `_posts/` manually. This is the actual pattern every current post follows — copy it, don't improvise a new one:

```yaml
---
title: "Your Post Title"
date: YYYY-MM-DD
categories: [insights]
tags: [python, tutorial, hydrology]   # include "tutorial" only for the Python how-to series
excerpt: "One or two sentences. Shown on the homepage 'Latest Insights' cards and /insights/."
header:
  overlay_color: "#0f172a"
  overlay_filter: 0.7
  overlay_image: /images/pano1.jpg     # or a topical image from /images/
read_time: true
---
```

A few conventions worth knowing before you write:

- **Don't set `layout:`.** It defaults to `single` via `_config.yml`, which is what every real post relies on for the theme's masthead/sidebar/hero rendering. Setting `layout: post` (the old default in this script, now fixed) breaks that.
- **`tags` containing `tutorial`** is what routes a post onto the `/python/` page as well as `/insights/` — see `_pages/python.md` and `_pages/insights.md`, both of which filter on it. Nothing else about a tutorial post is structurally different.
- **Images** go in `/images/` named `YYYY-MM_short-topic-slug.png` (or `.jpg`), matching the post's date. Reference in-post with a `<figure>`/`<figcaption>` block — see any recent post's markdown for the pattern.
- **Code-heavy posts** get a companion notebook under `notebooks/NN_slug/` (see the Python tutorial series). Not required for commentary posts.
- **A post claiming a specific technical standard is correct** (ARR 2019 tables, code validated against a reference implementation, etc.) should actually be validated before publishing — run the code, check the numbers, don't take a draft's claim on faith. `_drafts/` is scaffolding, not content; treat any bracketed `_[placeholder text]_` as unwritten, not "mostly done."

### Content backlog

`_pages/resources/content-ideas.md` (excluded from the build, so it's a private working note) tracks source material for future posts — currently the unused LinkedIn material from a September 2026 content audit. Check there before starting from a blank page.

### Add a page

Create a markdown file under `_pages/` with front matter, e.g.:

```yaml
---
layout: single
title: "Page Name"
permalink: /page-name/
author_profile: true
---
```

## License

This project is open source and available under the [MIT License](LICENSE.txt).

## Contact

- GitHub: [@lmillard79](https://github.com/lmillard79)
- LinkedIn: [Lindsay Millard](https://www.linkedin.com/in/lindsaymillard)
- Email: [lindsay.millard@outlook.com.au](mailto:lindsay.millard@outlook.com.au)

---

<p align="center">
  <i>Built with Jekyll</i>
</p>
