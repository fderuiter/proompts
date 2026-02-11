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
    workflow_docs_dir = os.path.join(docs_abs, "workflows")
    os.makedirs(workflow_docs_dir, exist_ok=True)

    if os.path.exists(workflows_abs):
        print(f"Scanning {workflows_abs}...")
        for root, dirs, files in os.walk(workflows_abs):
            for file in files:
                if file.endswith('.workflow.yaml') or file.endswith('.workflow.yml'):
                    full_path = os.path.join(root, file)
                    title = get_title(full_path)
                    
                    # Generate individual workflow page content with Mermaid
                    mermaid_graph = "graph TD\n"
                    
                    try:
                        with open(full_path, 'r') as f:
                            data = yaml.safe_load(f)
                            
                            # Inputs node
                            if 'inputs' in data:
                                for inp in data['inputs']:
                                    inp_name = inp['name']
                                    mermaid_graph += f"    Input_{inp_name}[Input: {inp_name}] --> Steps\n"
                            
                            previous_step = None
                            if 'steps' in data:
                                for step in data['steps']:
                                    step_id = step['step_id']
                                    mermaid_graph += f"    {step_id}[Step: {step_id}]\n"
                                    
                                    # Try to infer dependencies from map_inputs
                                    if 'map_inputs' in data:
                                        # This is too complex to parse perfectly without a real parser
                                        # But we can check if {{steps.PREV.output}} is used
                                        pass
                                    
                                    # Simple sequential linking for now if no explicit dependencies found?
                                    # Or just list them.
                                    # Let's try to find dependencies in map_inputs values
                                    if 'map_inputs' in step:
                                        for key, val in step['map_inputs'].items():
                                            if isinstance(val, str):
                                                # Look for {{steps.STEP_ID.output}}
                                                matches = re.findall(r'steps\.(\w+)\.output', val)
                                                for match in matches:
                                                    mermaid_graph += f"    {match} --> {step_id}\n"
                                                
                                                # Look for {{inputs.INPUT_NAME}}
                                                matches_input = re.findall(r'inputs\.(\w+)', val)
                                                for match in matches_input:
                                                    mermaid_graph += f"    Input_{match} --> {step_id}\n"

                    except Exception as e:
                        print(f"Error parsing workflow {file}: {e}")
                        mermaid_graph = ""

                    # Create individual page
                    workflow_filename = re.sub(r'\.workflow\.ya?ml$', '', file) + ".md"
                    workflow_page_path = os.path.join(workflow_docs_dir, workflow_filename)
                    
                    description = data.get('description', 'No description provided.') if data else ''
                    
                    page_content = f"---\nlayout: default\ntitle: {title}\nparent: Workflows\nnav_order: 99\n---\n\n"
                    page_content += f"# {title}\n\n"
                    page_content += f"{description}\n\n"
                    
                    if mermaid_graph.strip() != "graph TD":
                         page_content += "## Workflow Diagram\n\n"
                         page_content += "<div class=\"mermaid\">\n"
                         page_content += mermaid_graph
                         page_content += "</div>\n\n"
                    
                    # Link to source
                    rel_path_source = os.path.relpath(full_path, workflow_docs_dir)
                    page_content += f"[View Source YAML]({rel_path_source})\n"

                    with open(workflow_page_path, 'w') as f:
                        f.write(page_content)
                    print(f"Generated workflow page: {workflow_page_path}")

                    # Add to main list (link to the generated doc, NOT the yaml)
                    # The link in docs/workflows.md should be relative to docs/workflows.md
                    # Target: docs/workflows/filename.md
                    link_path = os.path.join("workflows", workflow_filename)
                    workflows.append({'title': title, 'path': link_path})
    
    # Add Workflows to categories if we want a separate page
    if workflows:
        categories["Workflows"] = workflows # This will generate the index page


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


