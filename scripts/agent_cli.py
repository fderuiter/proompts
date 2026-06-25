#!/usr/bin/env python3
import argparse
import sys
import os
import json
import re
import hashlib
from pathlib import Path

# Add project root to path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "promptops"))

from promptops.utils import iter_prompt_files, load_yaml, iter_skill_manifests, parse_skill_manifest

def get_tool_name(path: Path, content: dict) -> tuple[str, str]:
    name = content.get('name')
    if not name:
        name = path.name.replace(".prompt.yaml", "")
        
    original_name = name
    name = re.sub(r'[^a-zA-Z0-9_-]', '_', name)
    name = re.sub(r'_+', '_', name)
    name = name.strip('_')
    
    if len(name) > 64:
        h = hashlib.md5(str(path).encode()).hexdigest()[:6]
        name = name[:57] + "_" + h
        
    return original_name, name

def get_tools_info(prompts_dir):
    prompts_dir_path = Path(prompts_dir)
    manifested_tool_stems = set()
    manifests = []
    
    for path in iter_skill_manifests(prompts_dir):
        try:
            manifest = parse_skill_manifest(path)
            domain = manifest["metadata"].get("domain") or path.parent.name
            manifests.append({"path": path, "domain": domain, "skills": manifest["skills"]})
            for skill in manifest["skills"]:
                stem = re.sub(r'[^a-zA-Z0-9_-]', '_', skill["name"]).lower().strip('_')
                manifested_tool_stems.add(stem)
        except Exception:
            pass

    tools_info = []
    for path in iter_prompt_files(prompts_dir):
        try:
            content = load_yaml(path)
        except Exception:
            continue
        original_name, tool_name = get_tool_name(path, content)
        
        overridden = False
        overriding_manifest = None
        if tool_name.lower() in manifested_tool_stems and (path.parent / "skills.md").exists():
            overridden = True
            overriding_manifest = str(path.parent / "skills.md")
            
        tools_info.append({
            "path": str(path),
            "original_name": original_name,
            "tool_name": tool_name,
            "truncated": len(original_name) > 64,
            "overridden": overridden,
            "overriding_manifest": overriding_manifest
        })
    
    return tools_info, manifests

def generate_config():
    python_path = sys.executable
    script_path = str(Path(__file__).resolve().parent.parent / "mcp_server.py")
    cwd = str(Path(__file__).resolve().parent.parent)
    
    config = {
        "mcpServers": {
            "proompts": {
                "command": python_path,
                "args": [script_path],
                "env": {
                    "PYTHONPATH": cwd
                }
            }
        }
    }
    print(json.dumps(config, indent=2))

def discovery_report():
    cwd = str(Path(__file__).resolve().parent.parent)
    prompts_dir = Path(cwd) / "prompts"
    tools_info, manifests = get_tools_info(prompts_dir)
    
    print("=== Discovery Report ===")
    print("\n--- Tool Name Transformations ---")
    for t in tools_info:
        if t["tool_name"] != t["original_name"]:
            print(f"- {t['original_name']} -> {t['tool_name']}")

    print("\n--- Overridden Tools ---")
    for t in tools_info:
        if t["overridden"]:
            print(f"- {t['path']} is overridden by {t['overriding_manifest']}")

def main():
    parser = argparse.ArgumentParser(description="Agent Setup CLI")
    subparsers = parser.add_subparsers(dest="command", required=True)
    
    config_parser = subparsers.add_parser("config", help="Generate Claude Desktop JSON configuration")
    discovery_parser = subparsers.add_parser("discovery", help="Show discovery report")
    
    args = parser.parse_args()
    if args.command == "config":
        generate_config()
    elif args.command == "discovery":
        discovery_report()

if __name__ == "__main__":
    main()
