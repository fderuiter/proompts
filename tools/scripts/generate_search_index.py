#!/usr/bin/env python3
"""Generates a search.json index for the static site."""

import json
import sys
from pathlib import Path

# Add the script's directory to sys.path to ensure utils can be imported
sys.path.append(str(Path(__file__).parent))

try:
    from utils import ROOT, iter_prompt_files, load_yaml
except ImportError:
    # Fallback if run from a different location without setting PYTHONPATH
    print("Error: Could not import utils. Please run from the repository root or tools/scripts directory.")
    sys.exit(1)

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

        entry = {
            "title": content.get('name', str(rel_path)),
            "description": content.get('description', ''),
            "tags": ", ".join(content.get('tags', [])),
            # URL relative to the site root (repo root)
            "url": str(rel_path)
        }
        search_data.append(entry)

    # Output to the specified path (defaults to repo root if just filename)
    out_file = ROOT / output_path
    with open(out_file, 'w', encoding='utf-8') as f:
        json.dump(search_data, f, indent=2)

    print(f"Generated {out_file} with {len(search_data)} entries.")

if __name__ == "__main__":
    generate_index("search.json")
