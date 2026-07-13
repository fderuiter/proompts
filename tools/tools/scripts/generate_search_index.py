#!/usr/bin/env python3
"""
Generate Search Index Script

## What is this?
This script generates a `search.json` index file for the static documentation site.

## Why use it?
- **Enables Searchability:** Allows the documentation frontend to provide real-time search across prompts and workflows.
- **Aggregates Metadata:** Extracts titles, descriptions, and tags from YAML files into a single, optimized JSON payload.

## How to use it?
```bash
python3 tools/tools/scripts/generate_search_index.py
```
"""

import json
import sys
from pathlib import Path


from promptops.utils import ROOT, iter_prompt_files, iter_workflow_files, load_yaml, iter_skill_manifests, parse_skill_manifest

def generate_index(output_path: str = "search.json"):
    search_data = []

    # Track which directories have skill manifests
    manifested_dirs = set()

    prompts_dir = ROOT / "prompts"

    # Iterate through all skill manifest files
    for path in iter_skill_manifests(prompts_dir):
        try:
            manifest = parse_skill_manifest(path)
            rel_path = path.relative_to(ROOT)
            manifested_dirs.add(path.parent)

            tags = manifest["metadata"].get("tags", [])
            tags_str = ", ".join(tags) if isinstance(tags, list) else str(tags)

            for skill in manifest["skills"]:
                entry = {
                    "title": skill["name"],
                    "description": skill.get("description", ""),
                    "tags": tags_str,
                    "url": f"{rel_path}#skill-{skill['name'].lower().replace(' ', '-')}",
                    "type": "skill"
                }
                search_data.append(entry)
        except Exception as e:
             print(f"Error indexing manifest {path}: {e}")

    # Iterate through all prompt files using the utility
    for path in iter_prompt_files(prompts_dir):
        # Skip prompts that are covered by skill manifests
        if path.parent in manifested_dirs:
            continue

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
        for path in iter_workflow_files(workflows_dir):
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
