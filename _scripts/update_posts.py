import os
import glob
from datetime import datetime

# Define common front matter for blog posts
POST_FRONTMATTER = """---
title: "{title}"
date: {date}
permalink: /blog/{slug}/
layout: single
header:
  image: "/images/pano1.jpg"
  caption: "{caption}"
author_profile: true
tags: {tags}
categories: {categories}
---
"""

# Define blog post metadata
POSTS = {
    '2019-05-12-BayesianCoinToss.md': {
        'title': 'Bayesian Inference Example - Using Python',
        'caption': 'A practical guide to Bayesian inference with Python',
        'slug': 'bayesian-coin-toss',
        'tags': ['Bayesian', 'Python', 'Statistics'],
        'categories': ['Data Science']
    },
    '2019-05-12-FirstPost.md': {
        'title': 'First Blog Post',
        'caption': 'Welcome to my technical blog',
        'slug': 'first-post',
        'tags': ['Introduction'],
        'categories': ['General']
    },
    '2019-05-12-PeakOverThreshold.md': {
        'title': 'Peak Over Threshold Analysis',
        'caption': 'Implementing POT analysis in Python',
        'slug': 'peak-over-threshold',
        'tags': ['Hydrology', 'Statistics', 'Python'],
        'categories': ['Hydrology', 'Data Analysis']
    },
    '2019-05-31-DFUDA-FEWSAdapter.md': {
        'title': 'Delft-FEWS Model Adapter Development',
        'caption': 'Creating custom model adapters for Delft-FEWS',
        'slug': 'delft-fews-adapter',
        'tags': ['Delft-FEWS', 'Hydrology', 'Python'],
        'categories': ['Hydrology', 'Software Development']
    }
}

def update_blog_posts():
    """Update blog posts with consistent front matter."""
    posts_dir = '_posts'
    
    for filename, meta in POSTS.items():
        filepath = os.path.join(posts_dir, filename)
        if os.path.exists(filepath):
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Extract existing content after front matter if it exists
            if '---' in content:
                parts = content.split('---', 2)
                if len(parts) > 2:
                    content = parts[2].strip()
                else:
                    content = ''
            
            # Create new content with updated front matter
            new_frontmatter = POST_FRONTMATTER.format(
                title=meta['title'],
                date=filename[:10],
                slug=meta['slug'],
                caption=meta['caption'],
                tags=meta['tags'],
                categories=meta['categories']
            )
            new_content = f"{new_frontmatter}{content}"
            
            # Write back to file
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            
            print(f"Updated: {filepath}")

def main():
    print("Updating blog posts with consistent front matter...")
    update_blog_posts()
    print("\nBlog posts update complete!")

if __name__ == "__main__":
    main()
