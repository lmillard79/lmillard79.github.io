# Lindsay Millard - Professional Portfolio Website

[![GitHub Pages](https://img.shields.io/badge/GitHub%20Pages-222222?style=for-the-badge&logo=github&logoColor=white)](https://lmillard79.github.io/)
[![Jekyll](https://img.shields.io/badge/Jekyll-CC0000?style=for-the-badge&logo=jekyll&logoColor=white)](https://jekyllrb.com/)
[![Cayman Theme](https://img.shields.io/badge/Theme-Cayman-159818?style=for-the-badge)](https://pages-themes.github.io/cayman/)

This is the repository for my professional portfolio website showcasing my expertise in hydrology, water resources engineering, and data science.

## 🚀 Features

- **Modern & Responsive Design**: Built with Jekyll and the Cayman theme for optimal viewing on all devices
- **Fast Performance**: Optimized for quick loading and smooth navigation
- **SEO Optimized**: Built-in search engine optimization features
- **Blog Ready**: Easy-to-use blog system for sharing technical articles and insights
- **Project Showcase**: Clean, organized display of professional projects and case studies

## 🏗️ Project Structure

```
.
├── _includes/      # Reusable components (header, footer, etc.)
├── _layouts/       # Page templates
├── _pages/         # Main content pages
│   ├── about/      # About me section
│   ├── projects/   # Project portfolio
│   ├── blog/       # Blog posts
│   └── resources/  # Technical resources and cheatsheets
├── assets/         # Static assets (CSS, JS, images)
└── _config.yml     # Site configuration
```

## 🛠️ Technical Stack

- **Static Site Generator**: [Jekyll](https://jekyllrb.com/)
- **Theme**: [Cayman](https://pages-themes.github.io/cayman/)
- **Hosting**: [GitHub Pages](https://pages.github.com/)
- **CI/CD**: GitHub Actions

## 🚀 Getting Started

### Prerequisites

- Ruby (recommended: 2.5.0 or higher)
- Bundler (`gem install bundler`)
- Jekyll (`gem install jekyll`)

### Local Development

1. Clone the repository:
   ```bash
   git clone https://github.com/lmillard79/lmillard79.github.io.git
   cd lmillard79.github.io
   ```

2. Install dependencies:
   ```bash
   bundle install
   ```

3. Start the development server:
   ```bash
   bundle exec jekyll serve
   ```

4. Open your browser to `http://localhost:4000`

## 🚀 Deployment

This site is configured to be automatically deployed to GitHub Pages. Simply push your changes to the `main` branch, and GitHub Pages will automatically build and deploy the site.

```bash
git add .
git commit -m "Update site content and structure"
git push origin main
```

The site will be available at: https://lmillard79.github.io

### Manual Build (Optional)

If you need to build the site manually:

```bash
bundle exec jekyll build
```

The built site will be available in the `_site` directory.

## 📝 Adding New Content

### Create a New Blog Post

```bash
./_scripts/new_post.sh "Your Post Title"
```

Or manually create a new markdown file in `_posts/` with the following front matter:

```yaml
---
layout: post
title: "Your Post Title"
date: YYYY-MM-DD HH:MM:SS +1000
categories: [category1, category2]
tags: [tag1, tag2]
---
```

### Add a New Project

Create a new markdown file in `_pages/projects/` with the following front matter:

```yaml
---
layout: page
title: "Project Name"
description: "Brief description of the project"
image: /path/to/image.jpg
---
```

## License

This project is open source and available under the [MIT License](LICENSE).

## Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the [issues page](https://github.com/lmillard79/lmillard79.github.io/issues).

## 📬 Contact

- GitHub: [@lmillard79](https://github.com/lmillard79)
- LinkedIn: [Lindsay Millard](https://www.linkedin.com/in/lindsaymillard)
- Email: [lindsay.millard@example.com](mailto:lindsay.millard@example.com)

---

<p align="center">
  <i>Built with Jekyll</i>
</p>
- GIS and spatial analysis (QGIS, ArcGIS)
- Project management and client relations

### Professional Experience

With over 15 years of experience in water resources engineering, I have successfully delivered projects across multiple sectors including:

- Transport infrastructure (road and rail drainage design)
- Mining (water management for large-scale operations)
- Civil infrastructure (urban development and water sensitive design)
- Water utilities (strategic water resource planning)

## Technical Implementation

The website uses:

- Jekyll static site generator
- Minimal Mistakes theme
- Responsive design for all devices
- Structured navigation for easy content discovery
- Blog functionality for technical articles
- Portfolio showcase for key projects

## Deployment

The website is automatically deployed to GitHub Pages from the `main` branch.

## Maintenance

To update the website:

1. Make changes to the relevant Markdown files in the `_pages` directory
2. Update blog posts in the `_posts` directory
3. Modify styling in the `_sass` directory if needed
4. Push changes to GitHub for automatic deployment

For any inquiries, please contact lindsay.milard79@gmail.com
