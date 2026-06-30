import sys
import json
import re
import hashlib
from pathlib import Path
from typing import Tuple, List, Dict, Any

from promptops.utils import iter_prompt_files, load_yaml, iter_skill_manifests, parse_skill_manifest

def get_tool_name(path: Path, content: dict) -> Tuple[str, str]:
    name = content.get('name')
    if not name:
        name = path.name.replace(".prompt.md", "")
        
    original_name = name
    name = re.sub(r'[^a-zA-Z0-9_-]', '_', name)
    name = re.sub(r'_+', '_', name)
    name = name.strip('_')
    
    if len(name) > 64:
        h = hashlib.md5(str(path).encode()).hexdigest()[:6]
        name = name[:57] + "_" + h
        
    return original_name, name

def get_tools_info(prompts_dir: Path) -> Tuple[List[Dict[str, Any]], List[Dict[str, Any]]]:
    manifested_tool_stems = set()
    manifests = []
    
    for path in iter_skill_manifests(str(prompts_dir)):
        try:
            manifest = parse_skill_manifest(path)
            domain = manifest["metadata"].get("domain") or path.parent.name
            manifests.append({"path": str(path), "domain": domain, "skills": manifest["skills"]})
            for skill in manifest["skills"]:
                stem = re.sub(r'[^a-zA-Z0-9_-]', '_', skill["name"]).lower().strip('_')
                manifested_tool_stems.add(stem)
        except Exception:
            pass

    tools_info = []
    for path in iter_prompt_files(str(prompts_dir)):
        try:
            content = load_yaml(str(path))
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

def generate_config(prompts_dir: str):
    root = Path(prompts_dir).resolve().parent
    python_path = sys.executable
    script_path = str(root / "mcp_server.py")
    cwd = str(root)
    
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

def discovery_report(prompts_dir: str):
    prompts_dir_path = Path(prompts_dir).resolve()
    tools_info, manifests = get_tools_info(prompts_dir_path)
    
    print("=== Discovery Report ===")
    print("\n--- Tool Name Transformations ---")
    for t in sorted(tools_info, key=lambda x: x["original_name"]):
        if t["tool_name"] != t["original_name"]:
            print(f"- {t['original_name']} -> {t['tool_name']}")

    print("\n--- Overridden Tools ---")
    for t in sorted(tools_info, key=lambda x: x["path"]):
        if t["overridden"]:
            try:
                rel_path = str(Path(t["path"]).relative_to(prompts_dir_path.parent))
                rel_manifest = str(Path(t["overriding_manifest"]).relative_to(prompts_dir_path.parent))
            except ValueError:
                rel_path = t["path"]
                rel_manifest = t["overriding_manifest"]
            print(f"- {rel_path} is overridden by {rel_manifest}")
