#!/usr/bin/env python3
"""Migrate existing prompts to the new schema."""

import re
import yaml
from pathlib import Path

try:
    from utils import iter_prompt_files, ROOT
except ImportError:
    import sys
    sys.path.append(str(Path(__file__).parent))
    from utils import iter_prompt_files, ROOT

def extract_variables(messages) -> set:
    found_vars = set()
    for msg in messages:
        if isinstance(msg, dict) and 'content' in msg:
            # Matches {{ var }} or {{var}}
            found_vars.update(re.findall(r'\{\{\s*([^}]+?)\s*\}\}', msg['content']))
    return found_vars

def generate_new_fields(variables: set) -> str:
    lines = []
    lines.append('version: "0.1.0"')
    lines.append('metadata:')
    lines.append('  domain: unknown')
    lines.append('  complexity: medium')
    lines.append('  tags: []')
    lines.append('  requires_context: false')
    if not variables:
        lines.append('variables: []')
    else:
        lines.append('variables:')
        for var in sorted(variables):
            lines.append(f'  - name: {var}')
            lines.append(f'    description: ""')
            lines.append(f'    required: true')
            lines.append(f'    default: null') # Explicitly add default for now
    return '\n'.join(lines) + '\n'

def migrate_file(file_path: Path):
    try:
        content = file_path.read_text()

        # Check if already migrated
        if 'metadata:' in content and 'variables:' in content:
            return

        # Find insertion point (after description)
        match = re.search(r'^description:.*$', content, re.MULTILINE)
        if not match:
            # Fallback: try inserting after 'name:'
            match = re.search(r'^name:.*$', content, re.MULTILINE)

        if not match:
             print(f"Warning: No description or name found in {file_path.name}, skipping.")
             return

        # Parse YAML just to extract variables accurately from messages
        data = yaml.safe_load(content)
        messages = data.get('messages', [])
        found_vars = extract_variables(messages)

        # Generate the new block text
        new_block = generate_new_fields(found_vars)

        # Insert into original content
        prefix = content[:match.end()]
        suffix = content[match.end():]

        new_content = prefix + '\n' + new_block + suffix

        file_path.write_text(new_content)
        print(f"Migrated {file_path.name}")

    except Exception as e:
        print(f"Error processing {file_path.name}: {e}")

def main():
    print("Starting migration...")
    # Manually exclude template from automatic migration as we handled it separately
    template_path = Path('docs/template_prompt.prompt.yaml').resolve()

    for file_path in iter_prompt_files(ROOT):
        if file_path.resolve() == template_path:
             continue
        migrate_file(file_path)
    print("Migration complete.")

if __name__ == "__main__":
    main()
