import os
import yaml
import glob

# Define required fields
REQUIRED_FIELDS = ['title', 'permalink', 'layout']

# Define UK English spellings to check
UK_ENGLISH = {
    'organisation', 'organisations', 'analyse', 'analysed', 'analysing',
    'behaviour', 'behaviours', 'catalogue', 'centre', 'colour', 'customise',
    'customised', 'favour', 'favourite', 'honour', 'labour', 'licence',
    'maximise', 'minimise', 'modelling', 'offence', 'organisation', 'organise',
    'organised', 'practise', 'programme', 'realise', 'recognise', 'speciality',
    'standardise', 'summarise', 'theatre', 'travelled', 'traveller', 'travelling',
    'utilisation', 'utilise', 'utilised', 'whilst', 'yoghurt'
}

def check_frontmatter(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Extract front matter
    if not content.startswith('---'):
        return False, "Missing front matter delimiter (---)"
    
    parts = content.split('---')
    if len(parts) < 3:
        return False, "Incomplete front matter"
    
    try:
        frontmatter = yaml.safe_load(parts[1])
    except yaml.YAMLError as e:
        return False, f"YAML parsing error: {str(e)}"
    
    # Check required fields
    missing_fields = [field for field in REQUIRED_FIELDS if field not in frontmatter]
    if missing_fields:
        return False, f"Missing required fields: {', '.join(missing_fields)}"
    
    # Check permalink format
    permalink = frontmatter.get('permalink', '')
    if not permalink.startswith('/') or not permalink.endswith('/'):
        return False, f"Permalink should start and end with '/': {permalink}"
    
    # Check for UK English in title and description
    if 'title' in frontmatter:
        words = set(frontmatter['title'].lower().split())
        us_spellings = words.intersection(UK_ENGLISH)
        if us_spellings:
            return False, f"Possible US English in title: {', '.join(us_spellings)}"
    
    return True, "OK"

def main():
    root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    md_files = glob.glob(os.path.join(root_dir, '**', '*.md'), recursive=True)
    
    print("Checking markdown files for front matter consistency...\n")
    
    all_ok = True
    for md_file in sorted(md_files):
        if any(skip in md_file for skip in ['_site', 'node_modules', 'vendor']):
            continue
            
        rel_path = os.path.relpath(md_file, root_dir)
        is_ok, message = check_frontmatter(md_file)
        
        status = "[OK]" if is_ok else "[ERROR]"
        try:
            print(f"{status} {rel_path}: {message}")
        except UnicodeEncodeError:
            print(f"{rel_path}: {message}".encode('utf-8').decode('ascii', 'ignore'))
        
        if not is_ok:
            all_ok = False
    
    if all_ok:
        print("\nAll files have valid front matter!")
    else:
        print("\nSome files have issues that need to be addressed.")

if __name__ == "__main__":
    main()
