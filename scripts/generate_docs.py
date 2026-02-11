#!/usr/bin/env python3
import os
import yaml
import re

# Configuration
PROMPTS_DIR = "prompts"
WORKFLOWS_DIR = "workflows"
DOCS_DIR = "docs"

# Category Mapping: Order Matters!
# We check for these prefixes in order.
CATEGORY_MAP_LIST = [
    ("technical/architecture", "Architecture"),
    ("technical/languages", "Languages"),
    ("technical/software_engineering", "Software Engineering"),
    ("technical/testing", "Testing"),
    ("technical", "Technical"), # General Technical
    ("business", "Business"),
    ("clinical", "Clinical"),
    ("communication", "Communication"),
    ("management", "Management"),
    ("meta", "Meta"),
    ("regulatory", "Regulatory"),
    ("scientific", "Scientific"),
]

NAV_ORDER = {
    "Architecture": 1,
    "Business": 2,
    "Clinical": 3,
    "Communication": 4,
    "Languages": 5,
    "Management": 6,
    "Meta": 7,
    "Regulatory": 8,
    "Scientific": 9,
    "Software Engineering": 10,
    "Technical": 11,
    "Testing": 12,
    "Workflows": 13 
}

def get_title(filepath):
    """Extracts the title from a prompt or workflow file."""
    try:
        with open(filepath, 'r') as f:
            data = yaml.safe_load(f)
            if data and isinstance(data, dict):
                if 'name' in data:
                    return data['name']
                # Workflows might use 'title' or just prompt names, let's check for 'name' first
    except Exception as e:
        pass
    
    # Fallback: Use filename converted to title case
    filename = os.path.basename(filepath)
    name = os.path.splitext(filename)[0]
    # Remove numbering if present
    name = re.sub(r'^\d+_', '', name)
    # Remove extension if double extension (like .workflow.yaml -> .workflow -> name)
    if name.endswith('.workflow'):
        name = name[:-9]
        
    return name.replace('_', ' ').title()

def main():
    # Find project root
    current_dir = os.getcwd()
    if os.path.exists(os.path.join(current_dir, PROMPTS_DIR)):
        base_dir = current_dir
    else:
        # Try one up
        base_dir = os.path.dirname(current_dir)
        if not os.path.exists(os.path.join(base_dir, PROMPTS_DIR)):
             # Fallback to script location
             base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    prompts_abs = os.path.join(base_dir, PROMPTS_DIR)
    workflows_abs = os.path.join(base_dir, WORKFLOWS_DIR)
    docs_abs = os.path.join(base_dir, DOCS_DIR)

    categories = {cat_name: [] for _, cat_name in CATEGORY_MAP_LIST}
    categories["Uncategorized"] = []
    
    # --- Process Prompts ---
    print(f"Scanning {prompts_abs}...")
    for root, dirs, files in os.walk(prompts_abs):
        for file in files:
            if file.endswith('.prompt.yaml') or file.endswith('.prompt.yml'):
                full_path = os.path.join(root, file)
                rel_path_from_prompts = os.path.relpath(full_path, prompts_abs)
                
                category = "Uncategorized"
                rel_path_check = rel_path_from_prompts.replace("\\", "/")
                
                for prefix, cat_name in CATEGORY_MAP_LIST:
                    if rel_path_check.startswith(prefix):
                        category = cat_name
                        break
                
                title = get_title(full_path)
                link_path = os.path.join("..", PROMPTS_DIR, rel_path_from_prompts)
                
                categories[category].append({'title': title, 'path': link_path})

    # --- Process Workflows ---
    workflows = []
    if os.path.exists(workflows_abs):
        print(f"Scanning {workflows_abs}...")
        for root, dirs, files in os.walk(workflows_abs):
            for file in files:
                if file.endswith('.workflow.yaml') or file.endswith('.workflow.yml'):
                    full_path = os.path.join(root, file)
                    rel_path_from_workflows = os.path.relpath(full_path, workflows_abs)
                    
                    title = get_title(full_path)
                    link_path = os.path.join("..", WORKFLOWS_DIR, rel_path_from_workflows)
                    
                    workflows.append({'title': title, 'path': link_path})
    
    # Add Workflows to categories if we want a separate page
    if workflows:
        categories["Workflows"] = workflows

    # --- Generate Docs ---
    print("Generating documentation files...")
    for category, items in categories.items():
        if not items:
            continue
            
        filename = category.lower().replace(" ", "_") + ".md"
        output_path = os.path.join(docs_abs, filename)
        
        sorted_items = sorted(items, key=lambda x: x['title'])
        nav_order = NAV_ORDER.get(category, 99)
        
        content = f"---\nlayout: default\ntitle: {category}\nnav_order: {nav_order}\nhas_children: false\n---\n\n"
        content += f"# {category}\n\n"
        
        for item in sorted_items:
             content += f"- [{item['title']}]({item['path']})\n"
        
        with open(output_path, 'w') as f:
            f.write(content)
        print(f"Updated {output_path}")

    print("Done.")

if __name__ == "__main__":
    main()


