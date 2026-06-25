#!/usr/bin/env python3
import sys
import os
from pathlib import Path
from ruamel.yaml import YAML

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'tools', 'tools')))
from scripts.enrich_prompts import infer_domain, infer_tags, infer_complexity, infer_requires_context, _path_parts

ROOT = Path(__file__).parent.parent

TAG_ALIASES = {
    "bioskills": "skill",
}

def normalize_tags(tags):
    if not tags:
        return ["skill"]
    normalized = []
    for tag in tags:
        if tag in TAG_ALIASES:
            normalized.append(TAG_ALIASES[tag])
        else:
            normalized.append(tag)
    if "skill" not in normalized:
        normalized.append("skill")
    # preserve order but deduplicate
    seen = set()
    result = []
    for t in normalized:
        if t not in seen:
            seen.add(t)
            result.append(t)
    return result

def main():
    yaml = YAML()
    yaml.preserve_quotes = True
    yaml.indent(mapping=2, sequence=4, offset=2)
    
    updated_files = 0
    total_files = 0
    
    for root, dirs, files in os.walk(ROOT):
        # Don't walk into .git, site, venv, etc
        parts = set(root.split(os.sep))
        if {'.git', 'site', 'venv', '.venv'}.intersection(parts):
            continue
        for file in files:
            if file.endswith('.prompt.yaml') or file.endswith('.prompt.yml'):
                total_files += 1
                path = Path(root) / file
                
                try:
                    with open(path, 'r', encoding='utf-8') as f:
                        content = yaml.load(f)
                except Exception as e:
                    print(f"Error loading {path}: {e}")
                    continue
                    
                if not isinstance(content, dict):
                    continue
                    
                modified = False
                # compute parts relative to prompts/ if it's in prompts
                prompts_dir = ROOT / "prompts"
                try:
                    rel = path.resolve().relative_to(prompts_dir.resolve())
                    parts = list(rel.parts[:-1])
                except ValueError:
                    parts = []
                    
                prompt_name = content.get("name", "")
                
                if "metadata" not in content or content["metadata"] is None:
                    keys = list(content.keys())
                    if "description" in keys:
                        content.insert(keys.index("description") + 1, "metadata", {})
                    else:
                        content["metadata"] = {}
                    modified = True
                
                metadata = content["metadata"]
                
                if "domain" not in metadata:
                    metadata["domain"] = infer_domain(parts)
                    modified = True
                
                if "complexity" not in metadata:
                    metadata["complexity"] = infer_complexity(content)
                    modified = True
                    
                if "tags" not in metadata:
                    inferred = infer_tags(parts, prompt_name)
                    metadata["tags"] = normalize_tags(inferred)
                    modified = True
                else:
                    new_tags = normalize_tags(metadata["tags"])
                    if new_tags != metadata["tags"]:
                        metadata["tags"] = new_tags
                        modified = True
                        
                if "requires_context" not in metadata:
                    metadata["requires_context"] = infer_requires_context(content)
                    modified = True
                    
                if modified:
                    try:
                        with open(path, 'w', encoding='utf-8') as f:
                            yaml.dump(content, f)
                        updated_files += 1
                    except Exception as e:
                        print(f"Error saving {path}: {e}")
                        
    print(f"Total prompt files: {total_files}")
    print(f"Updated prompt files: {updated_files}")

if __name__ == "__main__":
    main()
