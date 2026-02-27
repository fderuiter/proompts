#!/usr/bin/env python3
"""
⚙️ Systems Core: Documentation Generator
Refactored for Robustness, Scalability, and OCP.
"""

import sys
import yaml
import re
import os # Needed for relpath calculation in strict paths
from pathlib import Path
from dataclasses import dataclass, field
from typing import List, Dict, Optional, Any

# --- Configuration Constants (Centralized) ---
CONFIG = {
    "dirs": {
        "prompts": Path("prompts"),
        "workflows": Path("workflows"),
        "docs": Path("docs"),
        "workflow_docs": Path("docs/workflows"),
    },
    "nav_order": {
        "Architecture": 1, "Business": 2, "Clinical": 3, "Communication": 4,
        "Languages": 5, "Management": 6, "Meta": 7, "Regulatory": 8,
        "Scientific": 9, "Software Engineering": 10, "Technical": 11,
        "Testing": 12, "Workflows": 13
    }
}

@dataclass(frozen=True)
class DocItem:
    """Immutable data carrier for documentation items."""
    title: str
    path: Path
    category: str
    item_type: str  # 'prompt' or 'workflow'
    description: str = ""
    graph_mermaid: Optional[str] = None

class FileParser:
    """Encapsulates logic for extracting metadata from files."""
    RE_NUMERIC_PREFIX = re.compile(r'^\d+_')
    
    @staticmethod
    def load_yaml(path: Path) -> Dict[str, Any]:
        try:
            with path.open('r', encoding='utf-8') as f:
                return yaml.safe_load(f) or {}
        except Exception as e:
            print(f"⚠️ Warning: Failed to parse {path}: {e}")
            return {}

    @staticmethod
    def derive_title(path: Path, data: Dict[str, Any]) -> str:
        """Derives title from metadata or strictly formatted filename."""
        if name := data.get('name') or data.get('title'):
            return str(name).strip()
        
        # Fallback: Robust filename parsing
        stem = path.stem.replace('.workflow', '')
        # Remove leading numbers (e.g., 01_filename -> filename)
        clean_name = FileParser.RE_NUMERIC_PREFIX.sub('', stem)
        return clean_name.replace('_', ' ').title()

    @staticmethod
    def derive_category(path: Path, root_dir: Path) -> str:
        """
        Derives category from directory structure. 
        Pattern: root / category / subfolder / file
        """
        try:
            relative = path.relative_to(root_dir)
            # If in root (e.g., prompts/README.md), it's Uncategorized
            if len(relative.parts) < 2:
                return "Uncategorized"
            
            # Map top-level technical folders to cleaner names if needed
            category_raw = relative.parts[0]
            if category_raw == "technical" and len(relative.parts) > 1:
                # Handle technical/architecture -> Architecture
                sub = relative.parts[1]
                if sub in ["architecture", "languages", "software_engineering", "testing"]:
                    return sub.replace('_', ' ').title()
                return "Technical"
                
            return category_raw.replace('_', ' ').title()
        except ValueError:
            return "Uncategorized"

class WorkflowGrapher:
    """Specialized logic for Mermaid graph generation."""
    RE_STEPS = re.compile(r'steps\.(\w+)\.output')
    RE_INPUTS = re.compile(r'inputs\.(\w+)')
    
    @staticmethod
    def generate(data: Dict[str, Any]) -> str:
        if 'steps' not in data and 'inputs' not in data:
            return ""
            
        graph = ["graph TD"]
        
        # Inputs
        for inp in data.get('inputs', []):
            name = inp.get('name', 'Unknown')
            graph.append(f"    Input_{name}[Input: {name}] --> Steps")

        # Steps & Dependencies
        for step in data.get('steps', []):
            step_id = step.get('step_id', 'unknown')
            graph.append(f"    {step_id}[Step: {step_id}]")
            
            inputs_map = step.get('map_inputs', {})
            for val in inputs_map.values():
                if isinstance(val, str):
                    # Dependency on other steps
                    for match in WorkflowGrapher.RE_STEPS.findall(val):
                        graph.append(f"    {match} --> {step_id}")
                    # Dependency on global inputs
                    for match in WorkflowGrapher.RE_INPUTS.findall(val):
                        graph.append(f"    Input_{match} --> {step_id}")
                        
        return "\n".join(graph) if len(graph) > 1 else ""

class DocumentationGenerator:
    def __init__(self, root: Path):
        self.root = root
        self.items: List[DocItem] = []

    def scan_prompts(self, check_mode: bool = False) -> bool:
        prompts_dir = self.root / CONFIG['dirs']['prompts']
        if not prompts_dir.exists():
            return False

        print(f"🔍 Scanning Prompts in {prompts_dir}...")
        changes_detected = False

        # Ensure output dir exists
        (self.root / CONFIG['dirs']['docs'] / "prompts").mkdir(parents=True, exist_ok=True)

        for path in prompts_dir.rglob("*"):
            if path.name.startswith("._"):
                continue
            if path.suffix in {'.yaml', '.yml'} and '.prompt' in path.name:
                data = FileParser.load_yaml(path)

                # Render the individual prompt page
                page_path, page_changed = self._render_prompt_page(path, data, check_mode)
                if page_changed:
                    changes_detected = True

                item = DocItem(
                    title=FileParser.derive_title(path, data),
                    path=page_path,
                    category=FileParser.derive_category(path, prompts_dir),
                    item_type='prompt'
                )
                self.items.append(item)
        return changes_detected

    def _render_prompt_page(self, source_path: Path, data: Dict[str, Any], check_mode: bool = False) -> tuple[Path, bool]:
        """Generates the Markdown page for a single prompt."""
        title = FileParser.derive_title(source_path, data)
        desc = data.get('description', 'No description provided.')

        # Calculate output path: docs/prompts/category/filename.md
        # relative_path = source_path.relative_to(self.root / CONFIG['dirs']['prompts'])
        # Actually, let's just mirror the structure under prompts/
        # source: prompts/A/B/foo.prompt.yaml
        # output: docs/prompts/A/B/foo.md

        rel_to_prompts = source_path.relative_to(self.root / CONFIG['dirs']['prompts'])
        output_path = self.root / CONFIG['dirs']['docs'] / "prompts" / rel_to_prompts.with_suffix(".md")

        output_path.parent.mkdir(parents=True, exist_ok=True)

        # Link to GitHub source for the button
        rel_path_from_root = source_path.relative_to(self.root)
        github_url = f"https://github.com/fderuiter/proompts/blob/main/{rel_path_from_root}"

        try:
            raw_content = source_path.read_text(encoding='utf-8')
        except Exception as e:
            raw_content = f"# Error reading source file: {e}"

        content = f"""---
title: {title}
---

# {title}

{desc}

[View Source YAML]({github_url})

```yaml
{raw_content}
```
"""
        if check_mode:
            if not output_path.exists():
                print(f"❌ Missing prompt page: {output_path}")
                return output_path, True
            elif output_path.read_text(encoding='utf-8') != content:
                print(f"❌ Content mismatch: {output_path}")
                return output_path, True
            return output_path, False
        else:
            output_path.write_text(content, encoding='utf-8')
            return output_path, False

    def scan_workflows(self, check_mode: bool = False) -> bool:
        wf_dir = self.root / CONFIG['dirs']['workflows']
        if not wf_dir.exists():
            return False

        print(f"🔍 Scanning Workflows in {wf_dir}...")
        # Ensure output dir exists
        (self.root / CONFIG['dirs']['workflow_docs']).mkdir(parents=True, exist_ok=True)
        
        changes_detected = False

        for path in wf_dir.rglob("*"):
            if path.name.startswith("._"):
                continue
            if path.suffix in {'.yaml', '.yml'} and '.workflow' in path.name:
                data = FileParser.load_yaml(path)
                
                # Check/Render the individual workflow page
                page_path, page_changed = self._render_workflow_page(path, data, check_mode)
                if page_changed:
                    changes_detected = True
                
                item = DocItem(
                    title=FileParser.derive_title(path, data),
                    path=page_path, # Link to the generated MD, not the source YAML
                    category=FileParser.derive_category(path, wf_dir),
                    item_type='workflow'
                )
                self.items.append(item)
        return changes_detected

    def _render_workflow_page(self, source_path: Path, data: Dict[str, Any], check_mode: bool = False) -> tuple[Path, bool]:
        """Generates the Markdown page for a single workflow. Returns (path, changed_bool)."""
        title = FileParser.derive_title(source_path, data)
        desc = data.get('description', 'No description provided.')
        mermaid = WorkflowGrapher.generate(data)
        
        filename = source_path.stem.replace('.workflow', '') + ".md"
        output_path = self.root / CONFIG['dirs']['workflow_docs'] / filename
        
        # Link to GitHub source for the button
        rel_path_from_root = source_path.relative_to(self.root)
        github_url = f"https://github.com/fderuiter/proompts/blob/main/{rel_path_from_root}"

        mermaid_block = f"## Workflow Diagram\n\n```mermaid\n{mermaid}\n```\n" if mermaid else ""

        content = f"""---
title: {title}
---

# {title}

{desc}

{mermaid_block}
[View Source YAML]({github_url})
"""
        if check_mode:
            if not output_path.exists():
                print(f"❌ Missing workflow page: {output_path}")
                return output_path, True
            elif output_path.read_text(encoding='utf-8') != content:
                print(f"❌ Content mismatch: {output_path}")
                return output_path, True
            return output_path, False
        else:
            output_path.write_text(content, encoding='utf-8')
            return output_path, False

    def build_indices(self, check_mode: bool = False) -> bool:
        """Groups items by category and writes index pages. Returns True if changes detected in check mode."""
        print("📝 Generating Category Indices...")
        
        # Grouping
        registry: Dict[str, Dict[str, List[DocItem]]] = {}
        
        for item in self.items:
            if item.category not in registry:
                registry[item.category] = {'prompt': [], 'workflow': []}
            registry[item.category][item.item_type].append(item)
            
            # Add all workflows to a Master "Workflows" category as well
            if item.item_type == 'workflow':
                if "Workflows" not in registry:
                    registry["Workflows"] = {'prompt': [], 'workflow': []}
                registry["Workflows"]['workflow'].append(item)

        # Rendering
        docs_dir = self.root / CONFIG['dirs']['docs']
        changes_detected = False
        
        for category, types in registry.items():
            if not any(types.values()): 
                continue
                
            filename = category.lower().replace(" ", "_") + ".md"
            out_path = docs_dir / filename
            nav = CONFIG['nav_order'].get(category, 99)
            
            md = [
                "---",
                f"title: {category}",
                "---",
                "",
                f"# {category}",
                ""
            ]

            if category == "Workflows":
                md.append("For a comprehensive guide on creating and running workflows, see the [Workflow Guide](workflow_guide.md).")
                md.append("")

            if types['prompt'] and category != "Workflows":
                md.append("## Prompts")
                # Sort prompts by title (case insensitive)
                for p in sorted(types['prompt'], key=lambda x: x.title.lower()):
                    # Calculate relative path from docs/category.md to prompts/file.yaml
                    # Note: p.path is absolute
                    rel = os.path.relpath(p.path, docs_dir)
                    md.append(f"- [{p.title}]({rel})")
                md.append("")

            if types['workflow']:
                header = "## Workflows" if category != "Workflows" else ""
                if header: md.append(header)
                # Sort workflows by title (case insensitive)
                for w in sorted(types['workflow'], key=lambda x: x.title.lower()):
                    # For workflows, p.path is absolute path to docs/workflows/file.md
                    # We need relative path from docs/category.md to docs/workflows/file.md
                    rel = os.path.relpath(w.path, docs_dir)
                    md.append(f"- [{w.title}]({rel})")
            
            content = "\n".join(md)
            
            if check_mode:
                if not out_path.exists():
                    print(f"❌ Missing file: {out_path}")
                    changes_detected = True
                elif out_path.read_text(encoding='utf-8') != content:
                    print(f"❌ Content mismatch: {out_path}")
                    changes_detected = True
            else:
                out_path.write_text(content, encoding='utf-8')
                print(f"✅ Updated {out_path}")
                
        return changes_detected

import argparse

def main():
    parser = argparse.ArgumentParser(description="Generate documentation site structure.")
    parser.add_argument("--check", action="store_true", help="Check if docs are up-to-date without writing.")
    args = parser.parse_args()

    # Detect root (where script is run from)
    root = Path.cwd()
    if not (root / CONFIG['dirs']['prompts']).exists():
        # Try one level up if run from scripts/
        if (root.parent / CONFIG['dirs']['prompts']).exists():
            root = root.parent
        else:
            print("❌ Error: Could not locate project root.")
            sys.exit(1)

    gen = DocumentationGenerator(root)

    if args.check:
        print("🔍 Checking documentation status...")

    changes = gen.scan_prompts(check_mode=args.check)
    changes |= gen.scan_workflows(check_mode=args.check)
    changes |= gen.build_indices(check_mode=args.check)
    
    if args.check:
        if changes:
             print("❌ Documentation is out of date. Run 'tools/scripts/generate_docs.py' to update.")
             sys.exit(1)
        else:
             print("✅ Documentation is up-to-date.")
             sys.exit(0)
    
    print("✨ Documentation generation complete.")

if __name__ == "__main__":
    main()
