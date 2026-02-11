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

# Workflow to Category Mapping
WORKFLOW_MAPPING = {
    "adjudication": "Clinical",
    "agentic_coding": "Software Engineering",
    "bioskills": "Scientific",
    "biological_safety": "Scientific",
    "cfo": "Business",
    "cra": "Clinical",
    "chemical_characterization": "Scientific",
    "clinical_data": "Clinical",
    "data_management_etl": "Clinical",
    "clinical_monitoring": "Clinical",
    "clinical_prompts": "Clinical",
    "clinical_safety": "Clinical",
    "imaging": "Clinical",
    "learning_development": "Management",
    "market_research": "Business",
    "meta_prompt_chain": "Meta",
    "microbiology": "Scientific",
    "pathology_study": "Scientific",
    "project_management": "Management",
    "protocol": "Clinical",
    "rtsm": "Clinical",
    "site_acquisition": "Clinical",
    "sterility": "Scientific",
    "study_director": "Management",
    "technical_writer": "Technical",
    "testing": "Testing",
    "vp_statistics": "Scientific",
    "eclinical_integration": "Clinical",
    "epro": "Clinical"
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

    # Categories now hold both prompts and workflows
    categories = {cat_name: {'prompts': [], 'workflows': []} for _, cat_name in CATEGORY_MAP_LIST}
    categories["Uncategorized"] = {'prompts': [], 'workflows': []}
    categories["Workflows"] = {'prompts': [], 'workflows': []} # Keep master list
    
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
                
                categories[category]['prompts'].append({'title': title, 'path': link_path})

    # --- Process Workflows ---
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

                    # Determine Workflow Category
                    workflow_basename = re.sub(r'\.workflow\.ya?ml$', '', file)
                    # Handle double extensions if any
                    if workflow_basename.endswith('.workflow'):
                        workflow_basename = workflow_basename[:-9]
                        
                    category = WORKFLOW_MAPPING.get(workflow_basename, "Uncategorized")
                    
                    # Link paths are slightly different depending on if we are in docs/workflows.md or docs/category.md
                    # But actually we are linking to the *generated* docs/workflows/file.md
                    # In docs/category.md -> workflows/file.md
                    # In docs/workflows.md -> workflows/file.md
                    
                    link_path = os.path.join("workflows", workflow_filename)
                    
                    # Add to specific category
                    if category in categories:
                        categories[category]['workflows'].append({'title': title, 'path': link_path})
                    
                    # Add to master list
                    categories["Workflows"]['workflows'].append({'title': title, 'path': link_path})
    

    # --- Generate Docs ---
    print("Generating documentation files...")
    for category, content_data in categories.items():
        prompts = content_data['prompts']
        workflows = content_data['workflows']
        
        if not prompts and not workflows:
            continue
            
        filename = category.lower().replace(" ", "_") + ".md"
        output_path = os.path.join(docs_abs, filename)
        
        nav_order = NAV_ORDER.get(category, 99)
        
        page_content = f"---\nlayout: default\ntitle: {category}\nnav_order: {nav_order}\nhas_children: false\n---\n\n"
        page_content += f"# {category}\n\n"
        
        if prompts and category != "Workflows":
            page_content += "## Prompts\n\n"
            sorted_prompts = sorted(prompts, key=lambda x: x['title'])
            for prompt in sorted_prompts:
                page_content += f"- [{prompt['title']}]({prompt['path']})\n"
            page_content += "\n"

        if workflows:
            if category != "Workflows":
                 page_content += "## Workflows\n\n"
            
            sorted_workflows = sorted(workflows, key=lambda x: x['title'])
            for wf in sorted_workflows:
                page_content += f"- [{wf['title']}]({wf['path']})\n"
        
        with open(output_path, 'w') as f:
            f.write(page_content)
        print(f"Updated {output_path}")

    print("Done.")

if __name__ == "__main__":
    main()


