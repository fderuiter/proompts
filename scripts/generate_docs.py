#!/usr/bin/env python3
"""
⚙️ Systems Core: Documentation Generator
Refactored for Robustness, Scalability, and OCP.
"""

import sys
import yaml
import re
import os
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
        clean_name = re.sub(r'^\d+_', '', stem)
        return clean_name.replace('_', ' ').title()

    @staticmethod
    def derive_category(path: Path, root_dir: Path, data: Dict[str, Any] = None) -> str:
        """
        Derives category from directory structure or metadata.
        Pattern: root / category / subfolder / file
        """
        if data:
            if category := data.get('category'):
                return str(category).strip()
            # Check nested metadata too
            if metadata := data.get('metadata'):
                if isinstance(metadata, dict) and (cat := metadata.get('category')):
                    return str(cat).strip()

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
                    for match in re.findall(r'steps\.(\w+)\.output', val):
                        graph.append(f"    {match} --> {step_id}")
                    # Dependency on global inputs
                    for match in re.findall(r'inputs\.(\w+)', val):
                        graph.append(f"    Input_{match} --> {step_id}")

        return "\n".join(graph) if len(graph) > 1 else ""

class DocumentationGenerator:
    def __init__(self, root: Path):
        self.root = root
        self.items: List[DocItem] = []

    def scan_prompts(self):
        prompts_dir = self.root / CONFIG['dirs']['prompts']
        if not prompts_dir.exists():
            return

        print(f"🔍 Scanning Prompts in {prompts_dir}...")
        for path in prompts_dir.rglob("*"):
            if path.suffix in {'.yaml', '.yml'} and '.prompt' in path.name:
                data = FileParser.load_yaml(path)
                item = DocItem(
                    title=FileParser.derive_title(path, data),
                    path=path,
                    category=FileParser.derive_category(path, prompts_dir, data),
                    item_type='prompt'
                )
                self.items.append(item)

    def scan_workflows(self):
        wf_dir = self.root / CONFIG['dirs']['workflows']
        if not wf_dir.exists():
            return

        print(f"🔍 Scanning Workflows in {wf_dir}...")
        # Ensure output dir exists
        (self.root / CONFIG['dirs']['workflow_docs']).mkdir(parents=True, exist_ok=True)

        for path in wf_dir.rglob("*"):
            if path.suffix in {'.yaml', '.yml'} and '.workflow' in path.name:
                data = FileParser.load_yaml(path)

                # Render the individual workflow page immediately (Side Effect)
                page_path = self._render_workflow_page(path, data)

                item = DocItem(
                    title=FileParser.derive_title(path, data),
                    path=page_path, # Link to the generated MD, not the source YAML
                    category=FileParser.derive_category(path, wf_dir, data),
                    item_type='workflow'
                )
                self.items.append(item)

    def _render_workflow_page(self, source_path: Path, data: Dict[str, Any]) -> Path:
        """Generates the Markdown page for a single workflow."""
        title = FileParser.derive_title(source_path, data)
        desc = data.get('description', 'No description provided.')
        mermaid = WorkflowGrapher.generate(data)
        
        filename = source_path.stem.replace('.workflow', '') + ".md"
        output_path = self.root / CONFIG['dirs']['workflow_docs'] / filename
        
        # Relative link to source for the button
        rel_source = os.path.relpath(source_path, output_path.parent)

        content = f"""---
layout: default
title: {title}
parent: Workflows
nav_order: 99
---

# {title}

{desc}

{f'## Workflow Diagram\n\n<div class="mermaid">\n{mermaid}\n</div>\n' if mermaid else ''}
[View Source YAML]({rel_source})
"""
        output_path.write_text(content, encoding='utf-8')
        return output_path

    def build_indices(self):
        """Groups items by category and writes index pages."""
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
        for category, types in registry.items():
            if not any(types.values()):
                continue

            filename = category.lower().replace(" ", "_") + ".md"
            out_path = docs_dir / filename
            nav = CONFIG['nav_order'].get(category, 99)
            
            md = [
                "---",
                "layout: default",
                f"title: {category}",
                f"nav_order: {nav}",
                "has_children: false",
                "---",
                "",
                f"# {category}",
                ""
            ]

            if types['prompt'] and category != "Workflows":
                md.append("## Prompts")
                md.append("")
                for p in sorted(types['prompt'], key=lambda x: x.title):
                    # Calculate relative path from docs/category.md to prompts/file.yaml
                    rel = os.path.relpath(p.path, docs_dir)
                    md.append(f"- [{p.title}]({rel})")
                md.append("")

            if types['workflow']:
                header = "## Workflows" if category != "Workflows" else ""
                if header:
                    md.append(header)
                    md.append("")
                for w in sorted(types['workflow'], key=lambda x: x.title):
                    # For workflows, path is already pointing to docs/workflows/file.md
                    # We need relative path from docs/category.md to docs/workflows/file.md
                    rel = os.path.relpath(w.path, docs_dir)
                    md.append(f"- [{w.title}]({rel})")

            out_path.write_text("\n".join(md), encoding='utf-8')
            print(f"✅ Updated {out_path}")

def main():
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
    gen.scan_prompts()
    gen.scan_workflows()
    gen.build_indices()
    print("✨ Documentation generation complete.")

if __name__ == "__main__":
    main()
