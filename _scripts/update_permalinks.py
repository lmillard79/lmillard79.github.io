import os
import frontmatter

def update_permalinks(directory):
    for filename in os.listdir(directory):
        if filename.endswith('.md') and filename != 'index.md':
            filepath = os.path.join(directory, filename)
            with open(filepath, 'r', encoding='utf-8') as f:
                post = frontmatter.load(f)
            
            # Get the base name without extension
            base_name = os.path.splitext(filename)[0]
            
            # Update permalink to match the filename with capital first letter
            new_permalink = f'/{base_name}/'
            if 'permalink' in post.metadata and post.metadata['permalink'] != new_permalink:
                print(f'Updating {filename} permalink from {post.metadata["permalink"]} to {new_permalink}')
                post.metadata['permalink'] = new_permalink
                
                # Write the updated content back to the file
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(frontmatter.dumps(post))

if __name__ == "__main__":
    projects_dir = os.path.join(os.path.dirname(__file__), '..', '_pages', 'projects')
    update_permalinks(projects_dir)
