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
./_scripts/new_post.sh "Your Post Title"
```

Or create a file in `_posts/` manually with front matter:

```yaml
---
layout: single
title: "Your Post Title"
date: YYYY-MM-DD HH:MM:SS +1000
categories: [insights]
tags: [tag1, tag2]
---
```

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
