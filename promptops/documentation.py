import os
from pathlib import Path
from dataclasses import dataclass
from typing import List, Dict, Optional, Any
from promptops.utils import load_yaml, derive_prompt_category, iter_prompt_files, iter_workflow_files
import re

@dataclass(frozen=True)
class DocItem:
    title: str
    path: Path
    category: str
    item_type: str
    description: str = ""
    graph_mermaid: Optional[str] = None

class FileParser:
    RE_NUMERIC_PREFIX = re.compile(r'^\d+_')
    @staticmethod
    def derive_title(path: Path, data: Dict[str, Any]) -> str:
        if name := data.get('name') or data.get('title'):
            return str(name).strip()
        stem = path.stem.replace('.workflow', '')
        clean_name = FileParser.RE_NUMERIC_PREFIX.sub('', stem)
        return clean_name.replace('_', ' ').title()

class WorkflowGrapher:
    RE_STEPS = re.compile(r'steps\.(\w+)\.output')
    RE_INPUTS = re.compile(r'inputs\.(\w+)')
    
    @staticmethod
    def generate(data: Dict[str, Any]) -> str:
        if 'steps' not in data and 'inputs' not in data:
            return ""
        graph = ["graph TD"]
        for inp in data.get('inputs', []):
            name = inp.get('name', 'Unknown')
            graph.append(f"    Input_{name}[Input: {name}] --> Steps")
        for step in data.get('steps', []):
            step_id = step.get('step_id', 'unknown')
            graph.append(f"    {step_id}[Step: {step_id}]")
            
            prompt_file = step.get('prompt_file')
            if prompt_file:
                prompt_node = prompt_file.replace('/', '_').replace('.', '_')
                graph.append(f"    Prompt_{prompt_node}[[{prompt_file}]] -.-> {step_id}")
                
            inputs_map = step.get('map_inputs', {})
            for val in inputs_map.values():
                if isinstance(val, str):
                    for match in WorkflowGrapher.RE_STEPS.findall(val):
                        graph.append(f"    {match} --> {step_id}")
                    for match in WorkflowGrapher.RE_INPUTS.findall(val):
                        graph.append(f"    Input_{match} --> {step_id}")
        return "\n".join(graph) if len(graph) > 1 else ""

def generate_docs(prompts_dir: str, output_dir: str, repo_url: str, branch: str = "main"):
    prompts_dir = os.environ.get('PROMPTOPS_REGISTRY', prompts_dir)
    prompts_path = Path(prompts_dir)
    docs_path = Path(output_dir)
    
    if not prompts_path.exists():
        print(f"Directory {prompts_dir} does not exist.")
        return

    items = []
    
    docs_path.mkdir(parents=True, exist_ok=True)
    out_prompts_dir = docs_path / "prompts"
    out_prompts_dir.mkdir(parents=True, exist_ok=True)
    out_workflows_dir = docs_path / "workflows"
    out_workflows_dir.mkdir(parents=True, exist_ok=True)
    
    for path in iter_prompt_files(str(prompts_path)):
        data = load_yaml(str(path))
        title = FileParser.derive_title(path, data)
        desc = data.get('description', 'No description provided.')
        
        rel_to_prompts = path.relative_to(prompts_path)
        output_file = out_prompts_dir / rel_to_prompts.with_suffix(".md")
        output_file.parent.mkdir(parents=True, exist_ok=True)
        
        if repo_url:
            github_url = f"{repo_url}/blob/{branch}/{path.relative_to(prompts_path.parent)}"
            link_md = f"[View Source YAML]({github_url})"
        else:
            link_md = ""
            
        try:
            raw_content = path.read_text(encoding='utf-8')
        except Exception as e:
            raw_content = f"# Error reading source file: {e}"
            
        content = f"---\ntitle: {title}\n---\n\n# {title}\n\n{desc}\n\n{link_md}\n\n```yaml\n{raw_content}\n```\n"
        output_file.write_text(content, encoding='utf-8')
        
        items.append(DocItem(
            title=title,
            path=output_file,
            category=derive_prompt_category(path, prompts_path, data),
            item_type='prompt'
        ))
        
    workflows_path = prompts_path.parent / "workflows"
    if workflows_path.exists():
        for path in iter_workflow_files(str(workflows_path)):
            data = load_yaml(str(path))
            title = FileParser.derive_title(path, data)
            desc = data.get('description', 'No description provided.')
            mermaid = WorkflowGrapher.generate(data)
            
            filename = path.stem.replace('.workflow', '') + ".md"
            output_file = out_workflows_dir / filename
            output_file.parent.mkdir(parents=True, exist_ok=True)
            
            if repo_url:
                github_url = f"{repo_url}/blob/{branch}/{path.relative_to(workflows_path.parent)}"
                link_md = f"[View Source YAML]({github_url})"
            else:
                link_md = ""
                
            mermaid_block = f"## Workflow Diagram\n\n```mermaid\n{mermaid}\n```\n" if mermaid else ""
            
            content = f"---\ntitle: {title}\n---\n\n# {title}\n\n{desc}\n\n{mermaid_block}\n{link_md}\n"
            output_file.write_text(content, encoding='utf-8')
            
            try:
                rel = path.relative_to(workflows_path)
                category = rel.parts[0].replace('_', ' ').title() if len(rel.parts) > 1 else "Uncategorized"
            except:
                category = "Uncategorized"
                
            items.append(DocItem(
                title=title,
                path=output_file,
                category=category,
                item_type='workflow'
            ))
        
    registry = {}
    for item in items:
        if item.category not in registry:
            registry[item.category] = {'prompt': [], 'workflow': []}
        registry[item.category][item.item_type].append(item)
        if item.item_type == 'workflow':
            if "Workflows" not in registry:
                registry["Workflows"] = {'prompt': [], 'workflow': []}
            registry["Workflows"]['workflow'].append(item)
        
    for category, types in registry.items():
        if not any(types.values()):
            continue
            
        filename = category.lower().replace(" ", "_") + ".md"
        out_path = docs_path / filename
        
        md = [f"---\ntitle: {category}\n---\n\n# {category}\n"]
        
        if types['prompt'] and category != "Workflows":
            md.append("## Prompts")
            for p in sorted(types['prompt'], key=lambda x: x.title.lower()):
                rel = os.path.relpath(p.path, docs_path)
                md.append(f"- [{p.title}]({rel})")
                
        if types['workflow']:
            if category != "Workflows":
                md.append("\n## Workflows")
            for w in sorted(types['workflow'], key=lambda x: x.title.lower()):
                rel = os.path.relpath(w.path, docs_path)
                md.append(f"- [{w.title}]({rel})")
                
        out_path.write_text("\n".join(md), encoding='utf-8')
        
    print(f"Documentation generated at {output_dir}")
