#!/usr/bin/env python3
"""Generate a search index for the prompts."""

import json
from pathlib import Path
from typing import List, Dict, Any

try:
    from utils import ROOT, iter_prompt_files, load_yaml
except ImportError:
    import sys
    sys.path.append(str(Path(__file__).parent))
    from utils import ROOT, iter_prompt_files, load_yaml

def generate_index() -> None:
    """Generate search.json from prompt files."""
    index: List[Dict[str, str]] = []

    for file_path in iter_prompt_files(ROOT):
        content = load_yaml(file_path)
        if not content:
            continue

        # Extract fields
        name = content.get('name', file_path.stem)
        description = content.get('description', '')
        messages = content.get('messages', [])
        tags = content.get('tags', [])

        # Flatten messages for content search
        message_content = " ".join([m.get('content', '') for m in messages if isinstance(m, dict)])

        # Determine URL (relative path from root)
        url = str(file_path.relative_to(ROOT).as_posix())

        # Category (parent directory name)
        category = file_path.parent.name

        item = {
            "title": name,
            "url": url,
            "category": category,
            "tags": ", ".join(tags) if isinstance(tags, list) else str(tags),
            "description": description,
            "content": message_content
        }
        index.append(item)

    output_path = ROOT / "search.json"
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(index, f, indent=2)

    print(f"Generated search index with {len(index)} items at {output_path}")

if __name__ == "__main__":
    generate_index()
