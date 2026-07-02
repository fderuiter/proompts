#!/usr/bin/env python3
"""
Systems Core: Documentation Generator

## What is this?
This script generates the static Markdown documentation site structure in the `docs/` directory.
It scans all prompts and workflows, organizes them by category (metadata-driven), and builds
category index pages and individual workflow documentation pages.

## Why use it?
It treats documentation as a first-class build artifact, keeping the `docs/` site in perfect
sync with the actual source code (`prompts/` and `workflows/`). By automating this process,
we eliminate "Documentation Debt" and ensure developers always have an accurate, up-to-date
reference for the system.

## How to use it?
Run this script from the root of the repository:
```bash
python3 tools/tools/scripts/generate_docs.py
```

> [!NOTE]
> This script is automatically executed as part of the master validation suite (`validate_prompts.sh`).
> It relies on `tools/tools/scripts/docs_config.json` for directory configuration and structural mappings.
"""

import sys
import yaml
import json
import re
import os # Needed for relpath calculation in strict paths
from pathlib import Path
from dataclasses import dataclass
from typing import List, Dict, Optional, Any
from promptops.utils import load_yaml, derive_prompt_category

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
    def _escape_mermaid_string(text: str) -> str:
        if not text:
            return ""
        text = str(text)
        text = text.replace('\\', '\\\\')
        text = text.replace('"', '&quot;').replace("'", "&#39;")
        text = text.replace('<', '&lt;').replace('>', '&gt;')
        text = text.replace('\n', ' ').replace('\r', '')
        return text.strip()

    @staticmethod
    def generate(data: Dict[str, Any]) -> str:
        if 'steps' not in data and 'inputs' not in data:
            return ""
            
        graph = ["graph TD"]
        
        # Accessibility Metadata
        name = WorkflowGrapher._escape_mermaid_string(data.get('name') or 'Workflow')
        desc = WorkflowGrapher._escape_mermaid_string(data.get('description') or '')
        
        metadata = data.get('metadata') or {}
        meta_parts = []
        for key in ['domain', 'topic', 'tags']:
            val = metadata.get(key)
            if val:
                if isinstance(val, list):
                    val = f"[{', '.join(str(v) for v in val)}]"
                meta_parts.append(f"{key.capitalize()}: {val}")
        
        if meta_parts:
            meta_str = " | ".join(meta_parts)
            desc = f"{desc} | {meta_str}" if desc else meta_str
            
        graph.append(f"    accTitle: {name}")
        if desc:
            graph.append(f"    accDescr: {desc}")
        
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

    def build_maturity_dashboard(self, check_mode: bool = False) -> bool:
        print("📊 Generating Maturity Dashboard...")
        prompts_dir = self.root / CONFIG['dirs']['prompts']
        docs_dir = self.root / CONFIG['dirs']['docs']
        
        from promptops.utils import iter_skill_manifests, parse_skill_manifest, iter_prompt_files
        
        total_prompts = 0
        l5_count = 0
        autonomy_counts = {}
        maturity_counts = {}
        
        # Process skills.md manifests
        for path in iter_skill_manifests(str(prompts_dir)):
            try:
                manifest = parse_skill_manifest(path)
                for skill in manifest.get("skills", []):
                    total_prompts += 1
                    meta = skill.get("metadata", {})
                    autonomy = meta.get("autonomy", "Unknown")
                    maturity = meta.get("maturity", "Unknown")
                    
                    autonomy_counts[autonomy] = autonomy_counts.get(autonomy, 0) + 1
                    maturity_counts[maturity] = maturity_counts.get(maturity, 0) + 1
                    if autonomy == "L5":
                        l5_count += 1
            except Exception:
                pass
                
        # Process individual .prompt files
        for path in iter_prompt_files(str(prompts_dir)):
            try:
                content = load_yaml(str(path))
            except Exception:
                continue
                
            total_prompts += 1
            meta = content.get("metadata", {})
            autonomy = meta.get("autonomy", "Unknown")
            maturity = meta.get("maturity", "Unknown")
            
            autonomy_counts[autonomy] = autonomy_counts.get(autonomy, 0) + 1
            maturity_counts[maturity] = maturity_counts.get(maturity, 0) + 1
            if autonomy == "L5":
                l5_count += 1
                
        percentage_l5 = (l5_count / total_prompts * 100) if total_prompts > 0 else 0
        
        md = [
            "---",
            "title: Maturity Dashboard",
            "---",
            "",
            "# 📊 Maturity Dashboard",
            "",
            "This dashboard provides an aggregate view of prompt and skill compliance across the library.",
            "",
            "## Compliance Summary",
            "",
            f"- **Total Prompts:** {total_prompts}",
            f"- **L5-Compliant Prompts:** {l5_count} ({percentage_l5:.1f}%)",
            "",
            "## Autonomy Levels",
            "",
            "| Level | Count |",
            "|-------|-------|"
        ]
        
        for k, v in sorted(autonomy_counts.items()):
            md.append(f"| {k} | {v} |")
            
        md.extend([
            "",
            "## Maturity Status",
            "",
            "| Status | Count |",
            "|--------|-------|"
        ])
        
        for k, v in sorted(maturity_counts.items()):
            md.append(f"| {k} | {v} |")
            
        # Mermaid pie charts for visualization
        md.extend([
            "",
            "## Visualizations",
            "",
            "### Autonomy Distribution",
            "```mermaid",
            "pie title Autonomy Levels"
        ])
        for k, v in sorted(autonomy_counts.items()):
            md.append(f'    "{k}" : {v}')
        md.append("```")
        
        md.extend([
            "",
            "### Maturity Distribution",
            "```mermaid",
            "pie title Maturity Status"
        ])
        for k, v in sorted(maturity_counts.items()):
            md.append(f'    "{k}" : {v}')
        md.append("```\n")
        
        out_path = docs_dir / "maturity_dashboard.md"
        content = "\n".join(md)
        
        if check_mode:
            if not out_path.exists():
                print(f"❌ Missing file: {out_path}")
                return True
            elif out_path.read_text(encoding='utf-8') != content:
                print(f"❌ Content mismatch: {out_path}")
                return True
            return False
        else:
            out_path.write_text(content, encoding='utf-8')
            print(f"✅ Updated {out_path}")
            return False

    def build_tool_registry(self, check_mode: bool = False) -> bool:
        prompts_dir = self.root / CONFIG['dirs']['prompts']
        docs_dir = self.root / CONFIG['dirs']['docs']
        
        manifested_tool_stems = set()
        
        from promptops.utils import iter_skill_manifests, parse_skill_manifest, iter_prompt_files, iter_workflow_files, extract_template_vars
        import hashlib
        
        skills_info = []
        prompts_info = []
        workflows_info = []
        
        for p in iter_skill_manifests(str(prompts_dir)):
            try:
                manifest = parse_skill_manifest(p)
                for skill in manifest["skills"]:
                    stem = re.sub(r'[^a-zA-Z0-9_-]', '_', skill["name"]).lower().strip('_')
                    manifested_tool_stems.add(stem)
                    
                    tool_name = skill["name"]
                    tool_name = re.sub(r'[^a-zA-Z0-9_-]', '_', tool_name)
                    tool_name = re.sub(r'_+', '_', tool_name).strip('_')
                    
                    vars_list = skill.get("variables", [])
                    vars_str = ", ".join(v.get("name", v) if isinstance(v, dict) else str(v) for v in vars_list) if vars_list else "None"
                    
                    desc = skill.get("description", "Agent Skill")
                    desc = desc.replace("\n", " ").strip() if desc else "Agent Skill"
                    
                    skills_info.append({
                        "name": tool_name,
                        "desc": desc[:100],
                        "inputs": vars_str
                    })
            except Exception:
                pass

        for p in iter_prompt_files(str(prompts_dir)):
            try:
                content_yaml = load_yaml(str(p))
            except Exception:
                continue
            
            name = content_yaml.get('name')
            if not name:
                name = p.name.replace(".prompt.md", "")
                
            original_name = name
            name = re.sub(r'[^a-zA-Z0-9_-]', '_', name)
            name = re.sub(r'_+', '_', name)
            name = name.strip('_')
            
            if len(name) > 64:
                h = hashlib.md5(str(p).encode()).hexdigest()[:6]
                name = name[:57] + "_" + h
                
            tool_name = name
            
            if tool_name.lower() in manifested_tool_stems and (p.parent / "skills.md").exists():
                continue
                
            vars_list = content_yaml.get("variables") or content_yaml.get("vars") or content_yaml.get("inputs")
            if not vars_list:
                try:
                    vars_list = extract_template_vars(content_yaml)
                except Exception:
                    vars_list = []
            
            if isinstance(vars_list, list):
                vars_str = ", ".join(v.get("name", v) if isinstance(v, dict) else str(v) for v in vars_list)
            elif isinstance(vars_list, dict):
                vars_str = ", ".join(vars_list.keys())
            else:
                vars_str = "None"
                
            if not vars_str:
                vars_str = "None"
                
            desc = content_yaml.get("description", "Prompt Tool")
            desc = desc.replace("\n", " ").strip() if desc else "Prompt Tool"
                
            prompts_info.append({
                "name": tool_name,
                "desc": desc[:100],
                "inputs": vars_str
            })
            
        workflows_dir = self.root / CONFIG['dirs']['workflows']
        for p in iter_workflow_files(str(workflows_dir)):
            try:
                content_yaml = load_yaml(str(p))
            except Exception:
                continue
                
            name = content_yaml.get('name')
            if not name:
                name = p.name.replace(".workflow.yaml", "")
                
            name = re.sub(r'[^a-zA-Z0-9_-]', '_', name)
            name = re.sub(r'_+', '_', name)
            tool_name = name.strip('_')
            
            vars_list = content_yaml.get("variables") or content_yaml.get("vars") or content_yaml.get("inputs")
            if isinstance(vars_list, list):
                vars_str = ", ".join(v.get("name", v) if isinstance(v, dict) else str(v) for v in vars_list)
            elif isinstance(vars_list, dict):
                vars_str = ", ".join(vars_list.keys())
            else:
                vars_str = "None"
                
            if not vars_str:
                vars_str = "None"
                
            desc = content_yaml.get("description", "Workflow Tool")
            desc = desc.replace("\n", " ").strip() if desc else "Workflow Tool"
                
            workflows_info.append({
                "name": tool_name,
                "desc": desc[:100],
                "inputs": vars_str
            })
            
        mcp_doc = docs_dir / "mcp_integration.md"
        if not mcp_doc.exists():
            return False
            
        mcp_content = mcp_doc.read_text(encoding='utf-8')
        
        new_section = "<!-- TOOL_REGISTRY_START -->\n"
        new_section += "## Available Tools\n\n"
        
        new_section += "### Workflows\n\n"
        new_section += "| Tool Name | Description | Inputs |\n"
        new_section += "|-----------|-------------|--------|\n"
        for t in sorted(workflows_info, key=lambda x: x["name"]):
            new_section += f"| `{t['name']}` | {t['desc']} | `{t['inputs']}` |\n"
        new_section += "\n"
        
        new_section += "### Prompts\n\n"
        new_section += "| Tool Name | Description | Inputs |\n"
        new_section += "|-----------|-------------|--------|\n"
        for t in sorted(prompts_info, key=lambda x: x["name"]):
            new_section += f"| `{t['name']}` | {t['desc']} | `{t['inputs']}` |\n"
        new_section += "\n"
        
        new_section += "### Skills\n\n"
        new_section += "| Tool Name | Description | Inputs |\n"
        new_section += "|-----------|-------------|--------|\n"
        for t in sorted(skills_info, key=lambda x: x["name"]):
            new_section += f"| `{t['name']}` | {t['desc']} | `{t['inputs']}` |\n"
        new_section += "\n"
        new_section += "<!-- TOOL_REGISTRY_END -->"
        
        if "<!-- TOOL_REGISTRY_START -->" in mcp_content:
            new_mcp_content = re.sub(r'<!-- TOOL_REGISTRY_START -->.*<!-- TOOL_REGISTRY_END -->', new_section, mcp_content, flags=re.DOTALL)
        else:
            new_mcp_content = mcp_content + "\n\n" + new_section
            
        if check_mode:
            if mcp_content != new_mcp_content:
                print(f"❌ Content mismatch: {mcp_doc}")
                return True
            return False
        else:
            mcp_doc.write_text(new_mcp_content, encoding='utf-8')
            print(f"✅ Updated {mcp_doc}")
            return False

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
        docs_dir = self.root / CONFIG['dirs']['docs']
        if not prompts_dir.exists():
            return False

        print(f"🔍 Scanning Prompts in {prompts_dir}...")
        changes_detected = False

        from promptops.skill_export import process_skills
        if not check_mode:
            process_skills(prompts_dir, docs_dir)
        else:
            # We skip running process_skills in check_mode to avoid writing files,
            # or we could make process_skills support check_mode.
            pass

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
            source_path: The filesystem path to the source `.prompt.md` file.
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
        # source: prompts/A/B/foo.prompt.md
        # output: docs/prompts/A/B/foo.md

        rel_to_prompts = source_path.relative_to(self.root / CONFIG['dirs']['prompts'])
        output_path = self.root / CONFIG['dirs']['docs'] / "prompts" / rel_to_prompts.with_suffix(".md")

        output_path.parent.mkdir(parents=True, exist_ok=True)

        # Link to GitHub source for the button
        rel_path_from_root = source_path.relative_to(self.root)
        github_url = f"https://github.com/fderuiter/proompts/blob/main/{rel_path_from_root}"
        
        metadata = data.get('metadata', {})
        autonomy = metadata.get('autonomy')
        maturity = metadata.get('maturity')
        
        tags = []
        badges = []
        if autonomy:
            tags.append(autonomy)
            badges.append(f"![Autonomy: {autonomy}](https://img.shields.io/badge/Autonomy-{autonomy}-blue)")
        if maturity:
            tags.append(maturity)
            badges.append(f"![Maturity: {maturity}](https://img.shields.io/badge/Maturity-{maturity}-green)")
            
        tags_block = ""
        if tags:
            tags_block = "tags:\n" + "\n".join(f"  - {t}" for t in tags)
            
        badge_str = " " + " ".join(badges) if badges else ""

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
{tags_block}
---

# {title}{badge_str}

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
                if not full_prompt_path.exists():
                    # Fallback to skills.md in that directory
                    skills_md = full_prompt_path.parent / "skills.md"
                    if skills_md.exists():
                        rel_skills_md = os.path.relpath(skills_md, output_path.parent)
                        prompts_used.append(f"[{full_prompt_path.stem}]({rel_skills_md})")
                        continue

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
    changes |= gen.build_tool_registry(check_mode=args.check)
    changes |= gen.build_maturity_dashboard(check_mode=args.check)
    
    if args.check:
        if changes:
             print("❌ Documentation is out of date. Run 'tools/tools/scripts/generate_docs.py' to update.")
             sys.exit(1)
        else:
             print("✅ Documentation is up-to-date.")
             sys.exit(0)
    
    print("✨ Documentation generation complete.")

if __name__ == "__main__":
    main()
