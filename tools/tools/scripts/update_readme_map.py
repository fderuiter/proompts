import os
import re
from pathlib import Path

def get_script_info(filepath):
    """Extracts description from docstring or file header."""
    with open(filepath, 'r') as f:
        content = f.read()
    
    # Try to find WHAT: section in docstring
    what_match = re.search(r'WHAT:\s*(.*?)\n\s*(?:WHY:|HOW TO USE:|$)', content, re.DOTALL)
    if what_match:
        desc = what_match.group(1).strip().replace('\n', ' ')
        return desc
    
    # Try to find first docstring
    docstring_match = re.search(r'"""(.*?)"""', content, re.DOTALL)
    if docstring_match:
        lines = docstring_match.group(1).strip().split('\n')
        # Skip filename line if it exists
        for line in lines:
            line = line.strip()
            if line and not line.endswith('.py:') and not line.startswith('WHAT:'):
                return line
    return "No description provided."

def get_detailed_usage(filepath):
    with open(filepath, 'r') as f:
        content = f.read()
    how_match = re.search(r'HOW TO USE:\s*(.*?)\n\s*(?:"""|$)', content, re.DOTALL)
    if how_match:
        return how_match.group(1).strip()
    return None

def main():
    scripts_dir = Path('/app/tools/tools/scripts')
    readme_path = scripts_dir / 'README.md'
    
    scripts = []
    for f in os.listdir(scripts_dir):
        if f.endswith('.py') or f.endswith('.sh'):
            if f in ['update_readme_map.py', '__init__.py']:
                continue
            scripts.append(f)
            
    scripts.sort()
    
    table_lines = [
        "| Path | Type | Description |",
        "| :--- | :--- | :--- |"
    ]
    
    core_scripts = ['run_workflow.py', 'governance_manifest_generator.py']
    detailed_docs = []
    
    for script in scripts:
        script_path = scripts_dir / script
        desc = get_script_info(script_path)
        ext = script.split('.')[-1]
        type_str = "🐍 Python" if ext == 'py' else "🐚 Shell"
        
        # Clean up description (truncate if too long or just keep it single line)
        desc_clean = re.sub(r'\s+', ' ', desc)
        
        table_lines.append(f"| **`{script}`** | {type_str} | {desc_clean} |")
        
        if script in core_scripts:
            usage = get_detailed_usage(script_path)
            if usage:
                detailed_docs.append(f"### `{script}`\n\n**Description:** {desc_clean}\n\n**Usage Example:**\n```bash\n{usage}\n```\n")
    
    # Read existing README.md
    with open(readme_path, 'r') as f:
        readme_content = f.read()
    
    # We will replace everything from "## Validation & Testing" to the end (excluding the Return link)
    # with our auto-generated Directory Map and Core Scripts sections.
    
    parts = re.split(r'## 🗺️ Directory Map|## Table of Contents', readme_content)
    if len(parts) > 1:
        base_content = parts[0]
    else:
        base_content = readme_content
        
    # Generate the new sections
    new_sections = "## 🗺️ Directory Map\n\n" + "\n".join(table_lines) + "\n\n"
    
    new_sections += "## Core Simulation & Governance Scripts\n\n"
    new_sections += "".join(detailed_docs)
    
    new_sections += "---\n\n[Return to Documentation Index](../../docs/index.md)\n"
    
    with open(readme_path, 'w') as f:
        f.write(base_content + new_sections)

if __name__ == '__main__':
    main()
