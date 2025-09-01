import os
import glob
import frontmatter

# Define common front matter for project pages
PROJECT_FRONTMATTER = """---
title: "{title}"
permalink: /{slug}/
layout: single
header:
  image: "/images/pano1.jpg"
  caption: "{caption}"
author_profile: true
---
"""

# Define project metadata
PROJECTS = {
    'Breach.md': {
        'title': 'Breach Analysis',
        'caption': 'Advanced breach modelling and analysis',
        'slug': 'breach'
    },
    'GIS.md': {
        'title': 'GIS & Spatial Analysis',
        'caption': 'Geographic Information Systems and spatial data analysis',
        'slug': 'gis'
    },
    'Hydraulic.md': {
        'title': 'Hydraulic Modelling',
        'caption': 'Advanced hydraulic modelling and analysis',
        'slug': 'hydraulic'
    },
    'Hydrology.md': {
        'title': 'Hydrological Modelling',
        'caption': 'Advanced hydrological analysis and modelling',
        'slug': 'hydrology'
    },
    'Monte.md': {
        'title': 'Monte Carlo Analysis',
        'caption': 'Probabilistic analysis and risk assessment',
        'slug': 'monte-carlo'
    },
    'Post-processing.md': {
        'title': 'Post-processing & Analysis',
        'caption': 'Advanced data processing and visualization',
        'slug': 'post-processing'
    }
}

def update_project_pages():
    """Update project pages with consistent front matter."""
    projects_dir = os.path.join('_pages', 'projects')
    
    for filename, meta in PROJECTS.items():
        filepath = os.path.join(projects_dir, filename)
        if os.path.exists(filepath):
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Extract existing content after front matter
            if '---' in content:
                _, _, content = content.split('---', 2)
            
            # Create new content with updated front matter
            new_frontmatter = PROJECT_FRONTMATTER.format(
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
    print("Updating project pages with consistent front matter...")
    update_project_pages()
    print("\nFront matter update complete!")

if __name__ == "__main__":
    main()
