#!/usr/bin/env python3
"""Generates a search.json index for the static site."""

import json
import sys
from pathlib import Path


from promptops.utils import ROOT, iter_prompt_files, load_yaml

def generate_index(output_path: str = "search.json"):
    search_data = []

    # Iterate through all prompt files using the utility
    for path in iter_prompt_files(ROOT):
        content = load_yaml(path)

        # Calculate the web-accessible path relative to the repository root
        try:
            rel_path = path.relative_to(ROOT)
        except ValueError:
            # Should not happen if iter_prompt_files uses ROOT/prompts
            continue

        from promptops.tags import extract_tags
        tags = extract_tags(content)
                
        entry = {
            "title": content.get('name', str(rel_path)),
            "description": content.get('description', ''),
            "tags": ", ".join(tags),
            "url": str(rel_path),
            "type": "prompt"
        }
        search_data.append(entry)

    # Iterate through all workflow files
    workflows_dir = ROOT / "workflows"
    if workflows_dir.exists():
        for path in workflows_dir.rglob("*.workflow.yaml"):
            if path.name.startswith("._"):
                continue
            content = load_yaml(path)
            try:
                rel_path = path.relative_to(ROOT)
            except ValueError:
                continue

            from promptops.tags import extract_tags
            tags = extract_tags(content)

            entry = {
                "title": content.get('name', str(rel_path)),
                "description": content.get('description', ''),
                "tags": ", ".join(tags),
                "url": str(rel_path),
                "type": "workflow"
            }
            search_data.append(entry)

    # Output to the specified path (defaults to repo root if just filename)
    out_file = ROOT / output_path
    with open(out_file, 'w', encoding='utf-8') as f:
        json.dump(search_data, f, indent=2)

    print(f"Generated {out_file} with {len(search_data)} entries.")

if __name__ == "__main__":
    generate_index("search.json")
