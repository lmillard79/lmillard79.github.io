import os

# Define common front matter for resource pages
RESOURCE_FRONTMATTER = """---
title: "{title}"
permalink: /resources/{slug}/
layout: single
header:
  image: "/images/pano1.jpg"
  caption: "{caption}"
author_profile: true
---
"""

# Define resource metadata
RESOURCES = {
    'CS_Markdown.md': {
        'title': 'Markdown Cheat Sheet',
        'caption': 'Quick reference for Markdown syntax',
        'slug': 'markdown-cheat-sheet'
    },
    'CS_Wrangle.md': {
        'title': 'Data Wrangling Cheat Sheet',
        'caption': 'Data manipulation and cleaning techniques',
        'slug': 'data-wrangling'
    },
    'CS_visualisation.md': {
        'title': 'Data Visualization Guide',
        'caption': 'Effective data visualization techniques',
        'slug': 'data-visualization'
    },
    'cheatsheets.md': {
        'title': 'Technical Cheat Sheets',
        'caption': 'Collection of technical references',
        'slug': 'cheat-sheets'
    },
    'datascience.md': {
        'title': 'Data Science Resources',
        'caption': 'Tools and resources for data science',
        'slug': 'data-science'
    },
    'links.md': {
        'title': 'Useful Links',
        'caption': 'Collection of useful resources and references',
        'slug': 'links'
    },
    'test-debug.md': {
        'title': 'Testing & Debugging',
        'caption': 'Best practices for testing and debugging',
        'slug': 'testing-debugging'
    }
}

def update_resource_pages():
    """Update resource pages with consistent front matter."""
    resources_dir = os.path.join('_pages', 'resources')
    
    for filename, meta in RESOURCES.items():
        filepath = os.path.join(resources_dir, filename)
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
            new_frontmatter = RESOURCE_FRONTMATTER.format(
                title=meta['title'],
                slug=meta['slug'],
                caption=meta['caption']
            )
            new_content = f"{new_frontmatter}{content}"
            
            # Write back to file
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            
            print(f"Updated: {filepath}")

def main():
    print("Updating resource pages with consistent front matter...")
    update_resource_pages()
    print("\nResource pages update complete!")

if __name__ == "__main__":
    main()
