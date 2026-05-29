#!/usr/bin/env python3
"""
⚙️ Systems Core: Documentation Generator
Refactored for Robustness, Scalability, and OCP.

WHAT:
This script generates the static Markdown documentation site structure in the `docs/` directory.
It scans all prompts and workflows, organizes them by category (metadata-driven), and builds
category index pages and individual workflow documentation pages.

WHY:
It treats documentation as a first-class build artifact, keeping the `docs/` site in perfect
sync with the actual source code (`prompts/` and `workflows/`). By automating this process,
we eliminate "Documentation Debt" and ensure developers always have an accurate, up-to-date
reference for the system.

HOW TO USE:
Run this script from the root of the repository:

    python3 tools/scripts/generate_docs.py

> [!NOTE]
> This script is automatically executed as part of the master validation suite (`test_all.py`).
> It relies on `tools/scripts/docs_config.json` for directory configuration and structural mappings.
"""

import sys
import yaml
import json
import re
import os # Needed for relpath calculation in strict paths
from pathlib import Path
from dataclasses import dataclass, field
from typing import List, Dict, Optional, Any
from utils import load_yaml, derive_prompt_category

# --- Configuration Loading (Extracted) ---
def load_config() -> Dict[str, Any]:
    config_path = Path(__file__).parent / "docs_config.json"
    try:
        with config_path.open('r', encoding='utf-8') as f:
            config = json.load(f)
            # Convert dir strings to Path objects
            if "dirs" in config:
                for k, v in config["dirs"].items():
                    config["dirs"][k] = Path(v)
            return config
    except Exception as e:
        print(f"❌ Error: Failed to load config from {config_path}: {e}")
        sys.exit(1)

CONFIG = load_config()

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
    def derive_category(path: Path, root_dir: Path, data: Optional[Dict[str, Any]] = None) -> str:
        """
        Derives prompt/workflow category.
        Prompts: metadata/tags-first, with directory fallback.
        Workflows: directory-based.
        """
        # Prompt scans pass parsed YAML data; workflow scan callers explicitly pass data=None.
        # Workflows remain directory-grouped for now because they don't use prompt tag taxonomy.
        if data is not None:
            return derive_prompt_category(path, root_dir, data)

        try:
            relative = path.relative_to(root_dir)
            # If in root (e.g., prompts/README.md), it's Uncategorized
            if len(relative.parts) < 2:
                return "Uncategorized"

            return relative.parts[0].replace('_', ' ').title()
        except ValueError:
            return "Uncategorized"

class WorkflowGrapher:
    """Specialized logic for Mermaid graph generation."""
    RE_STEPS = re.compile(r'steps\.([a-zA-Z0-9_-]+)\.(?:output|history)')
    RE_INPUTS = re.compile(r'inputs\.([a-zA-Z0-9_-]+)')
    
    @staticmethod
    def generate(data: Dict[str, Any]) -> str:
        if 'steps' not in data and 'inputs' not in data:
            return ""
            
        graph = ["graph TD"]
        
        # Inputs
        for inp in data.get('inputs', []):
            name = inp.get('name', 'Unknown')
            graph.append(f"    Input_{name}[Input: {name}] -.-> Steps")

        steps = data.get('steps', [])
        
        # Step Nodes & Control Flow
        for i, step in enumerate(steps):
            step_id = step.get('step_id', 'unknown')
            graph.append(f"    {step_id}[Step: {step_id}]")
            
            next_prop = step.get('next')
            if next_prop is not None:
                if isinstance(next_prop, str):
                    graph.append(f"    {step_id} --> {next_prop}")
                elif isinstance(next_prop, list):
                    for edge in next_prop:
                        if isinstance(edge, str):
                            graph.append(f"    {step_id} --> {edge}")
                        elif isinstance(edge, dict):
                            target = edge.get('target', 'unknown')
                            condition = edge.get('condition')
                            if condition:
                                cond_text = str(condition).replace('"', "'")
                                graph.append(f"    {step_id} -->|\"{cond_text}\"| {target}")
                            else:
                                graph.append(f"    {step_id} --> {target}")
            else:
                if i + 1 < len(steps):
                    next_step = steps[i+1].get('step_id', 'unknown')
                    graph.append(f"    {step_id} --> {next_step}")

        # Data Dependencies
        for step in steps:
            step_id = step.get('step_id', 'unknown')
            inputs_map = step.get('map_inputs', {})
            for val in inputs_map.values():
                if isinstance(val, str):
                    # Dependency on other steps
                    for match in WorkflowGrapher.RE_STEPS.findall(val):
                        graph.append(f"    {match} -.->|data| {step_id}")
                    # Dependency on global inputs
                    for match in WorkflowGrapher.RE_INPUTS.findall(val):
                        graph.append(f"    Input_{match} -.->|data| {step_id}")
                        
        return "\n".join(graph) if len(graph) > 1 else ""

class DocumentationGenerator:
    def __init__(self, root: Path):
        self.root = root
        self.items: List[DocItem] = []
        self.prompt_to_workflows: Dict[Path, List[Dict[str, Any]]] = {}

    def _build_relational_index(self):
        wf_dir = self.root / CONFIG['dirs']['workflows']
        if not wf_dir.exists():
            return
        for path in wf_dir.rglob("*"):
            if path.name.startswith("._") or path.suffix not in {'.yaml', '.yml'} or '.workflow' not in path.name:
                continue
            data = load_yaml(path)
            wf_title = FileParser.derive_title(path, data)
            wf_rel_path = path.relative_to(self.root)
            for step in data.get('steps', []):
                prompt_file = step.get('prompt_file') or step.get('prompt')
                if prompt_file:
                    full_prompt_path = (self.root / prompt_file).resolve()
                    if full_prompt_path not in self.prompt_to_workflows:
                        self.prompt_to_workflows[full_prompt_path] = []
                    self.prompt_to_workflows[full_prompt_path].append({'title': wf_title, 'path': wf_rel_path})

    def scan_prompts(self, check_mode: bool = False) -> bool:
        """
        Scans the prompts directory for YAML files, generating a Markdown page for each.

        Args:
            check_mode: If True, checks if pages exist and match expected content without writing.

        Returns:
            bool: True if changes were detected or written, False otherwise.
        """
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
                data = load_yaml(path)

                # Render the individual prompt page
                page_path, page_changed = self._render_prompt_page(path, data, check_mode)
                if page_changed:
                    changes_detected = True

                item = DocItem(
                    title=FileParser.derive_title(path, data),
                    path=page_path,
                    category=FileParser.derive_category(path, prompts_dir, data),
                    item_type='prompt'
                )
                self.items.append(item)
        return changes_detected

    def _render_prompt_page(self, source_path: Path, data: Dict[str, Any], check_mode: bool = False) -> tuple[Path, bool]:
        """
        Generates or checks the Markdown page for a single prompt.

        Args:
            source_path: The filesystem path to the source `.prompt.yaml` file.
            data: The parsed YAML data dictionary.
            check_mode: If True, only checks if the generated content matches the existing file.

        Returns:
            tuple[Path, bool]: A tuple containing the output Path and a boolean indicating if changes occurred.
        """
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

        used_in_block = ""
        resolved_source = source_path.resolve()
        if resolved_source in self.prompt_to_workflows:
            used_in_block = "## Used In\n\n"
            for wf in sorted(self.prompt_to_workflows[resolved_source], key=lambda x: x['title']):
                # Find the relative path from output docs page to the workflow docs page
                wf_doc_path = self.root / CONFIG['dirs']['workflow_docs'] / wf['path'].stem.replace('.workflow', '')
                wf_doc_path = wf_doc_path.with_suffix(".md")
                rel_wf_doc = os.path.relpath(wf_doc_path, output_path.parent)
                used_in_block += f"- [{wf['title']}]({rel_wf_doc})\n"

        content = f"""---
title: {title}
---

# {title}

{desc}

{used_in_block}

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
        """
        Scans the workflows directory for YAML files, generating a Markdown page for each.

        Args:
            check_mode: If True, checks if pages exist and match expected content without writing.

        Returns:
            bool: True if changes were detected or written, False otherwise.
        """
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
                data = load_yaml(path)
                
                # Check/Render the individual workflow page
                page_path, page_changed = self._render_workflow_page(path, data, check_mode)
                if page_changed:
                    changes_detected = True
                
                item = DocItem(
                    title=FileParser.derive_title(path, data),
                    path=page_path, # Link to the generated MD, not the source YAML
                    category=FileParser.derive_category(path, wf_dir, data),
                    item_type='workflow'
                )
                self.items.append(item)
        return changes_detected

    def _render_workflow_page(self, source_path: Path, data: Dict[str, Any], check_mode: bool = False) -> tuple[Path, bool]:
        """
        Generates or checks the Markdown page for a single workflow, including Mermaid graphs.

        Args:
            source_path: The filesystem path to the source `.workflow.yaml` file.
            data: The parsed YAML data dictionary.
            check_mode: If True, only checks if the generated content matches the existing file.

        Returns:
            tuple[Path, bool]: A tuple containing the output Path and a boolean indicating if changes occurred.
        """
        title = FileParser.derive_title(source_path, data)
        desc = data.get('description', 'No description provided.')
        mermaid = WorkflowGrapher.generate(data)
        
        filename = source_path.stem.replace('.workflow', '') + ".md"
        output_path = self.root / CONFIG['dirs']['workflow_docs'] / filename
        
        # Link to GitHub source for the button
        rel_path_from_root = source_path.relative_to(self.root)
        github_url = f"https://github.com/fderuiter/proompts/blob/main/{rel_path_from_root}"

        mermaid_block = f"## Workflow Diagram\n\n```mermaid\n{mermaid}\n```\n" if mermaid else ""

        dependencies_block = ""
        prompts_used = []
        for step in data.get('steps', []):
            prompt_ref = step.get('prompt_file') or step.get('prompt')
            if prompt_ref:
                # Resolve relative path from workflow docs page to prompt docs page
                full_prompt_path = (self.root / prompt_ref).resolve()
                try:
                    rel_to_prompts = full_prompt_path.relative_to(self.root / CONFIG['dirs']['prompts'])
                    prompt_doc_path = self.root / CONFIG['dirs']['docs'] / "prompts" / rel_to_prompts.with_suffix(".md")
                    rel_prompt_doc = os.path.relpath(prompt_doc_path, output_path.parent)
                    prompts_used.append(f"[{full_prompt_path.stem}]({rel_prompt_doc})")
                except ValueError:
                    prompts_used.append(f"`{prompt_ref}`")
        if prompts_used:
            dependencies_block = "## Dependencies\n\n" + "\n".join(f"- {p}" for p in prompts_used) + "\n\n"

        content = f"""---
title: {title}
---

# {title}

{desc}

{dependencies_block}{mermaid_block}
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
        """
        Groups all discovered items by category and generates the index Markdown pages.

        Args:
            check_mode: If True, only checks if the generated indices match the existing files.

        Returns:
            bool: True if changes were detected or written, False otherwise.
        """
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

def main() -> None:
    """
    Main entrypoint for the documentation generator script.
    Parses arguments, initializes the generator, and runs scans.
    """
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

    gen._build_relational_index()

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
