# Sitemap Submission Guide for Google Search Console

## Prerequisites

1. Ensure your website is built and deployed to GitHub Pages
2. Verify you have a Google account

## Steps to Submit Your Sitemap

### 1. Access Google Search Console
- Go to [Google Search Console](https://search.google.com/search-console/)
- Sign in with your Google account
- Add your property (https://lmillard79.github.io/)
- Verify ownership (GitHub Pages makes this easy with automatic verification)

### 2. Locate Your Sitemap
- After your Jekyll site is built, your sitemap will be available at:
  `https://lmillard79.github.io/sitemap.xml`
- The jekyll-sitemap plugin automatically generates this file

### 3. Submit Your Sitemap
- In Google Search Console, click on your property
- In the left sidebar, click "Sitemaps" under "Index"
- In the "Add a new sitemap" field, enter: `sitemap.xml`
- Click "Submit"

### 4. Monitor Performance
- Check back regularly to see indexing status
- Look for any crawl errors that need to be addressed
- Monitor which pages are being indexed

## Troubleshooting

If your sitemap isn't found:
- Ensure the jekyll-sitemap gem is in your Gemfile
- Verify the plugin is listed in your _config.yml
- Check that your site builds successfully

## Next Steps

After submitting your sitemap:
- Set up Google Analytics (if not already done)
- Monitor search performance
- Submit your site to Bing Webmaster Tools as well
