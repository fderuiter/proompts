import os
from pathlib import Path
from dataclasses import dataclass
from typing import List, Dict, Optional, Any
from promptops.utils import load_yaml, derive_category, iter_prompt_files, iter_workflow_files, derive_title
import re

@dataclass(frozen=True)
class DocItem:
    title: str
    path: Path
    category: str
    item_type: str
    description: str = ""
    graph_mermaid: Optional[str] = None



from promptops.skill_export import process_skills, detect_skill

def generate_docs(prompts_dir: str, output_dir: str, repo_url: str, branch: str = "main", check: bool = False) -> bool:
    prompts_dir = os.environ.get('PROMPTOPS_REGISTRY', prompts_dir)
    prompts_path = Path(prompts_dir)
    docs_path = Path(output_dir)
    sync_ok = True
    
    if not prompts_path.exists():
        print(f"Directory {prompts_dir} does not exist.")
        return False

    items = []
    
    if not check:
        docs_path.mkdir(parents=True, exist_ok=True)
        out_prompts_dir = docs_path / "prompts"
        out_prompts_dir.mkdir(parents=True, exist_ok=True)
        out_workflows_dir = docs_path / "workflows"
        out_workflows_dir.mkdir(parents=True, exist_ok=True)
        
        process_skills(prompts_path, docs_path)
    else:
        out_prompts_dir = docs_path / "prompts"
        out_workflows_dir = docs_path / "workflows"
    
    for path in iter_prompt_files(str(prompts_path)):
        try:
            raw_content = path.read_text(encoding='utf-8')
        except Exception as e:
            raw_content = f"# Error reading source file: {e}"
        
        data = load_yaml(str(path))
        if data is None:
            continue
            
        if data.get('metadata', {}).get('status') == 'draft':
            continue
            
        if check and detect_skill(raw_content, data):
            continue

        title = derive_title(path, data)
        desc = data.get('description', 'No description provided.')
        
        rel_to_prompts = path.relative_to(prompts_path)
        output_file = out_prompts_dir / rel_to_prompts.with_suffix(".md")
        
        if not check:
            output_file.parent.mkdir(parents=True, exist_ok=True)
        
        if repo_url:
            github_url = f"{repo_url}/blob/{branch}/{path.relative_to(prompts_path.parent)}"
            link_md = f"[View Source YAML]({github_url})"
        else:
            link_md = ""
            
        content = f"---\ntitle: {title}\n---\n\n# {title}\n\n{desc}\n\n{link_md}\n\n```yaml\n{raw_content}\n```\n"
        
        if check:
            if not output_file.exists():
                print(f"Drift detected: Missing file {output_file}")
                sync_ok = False
            elif output_file.read_text(encoding='utf-8') != content:
                print(f"Drift detected: Content mismatch in {output_file}")
                sync_ok = False
        else:
            output_file.write_text(content, encoding='utf-8')
        
        items.append(DocItem(
            title=title,
            path=output_file,
            category=derive_category(path, prompts_path, data),
            item_type='prompt'
        ))
        
    workflows_path = prompts_path.parent / "workflows"
    if workflows_path.exists():
        for path in iter_workflow_files(str(workflows_path)):
            data = load_yaml(str(path))
            if data is None:
                continue
                
            if data.get('metadata', {}).get('status') == 'draft':
                continue
                
            title = derive_title(path, data)
            desc = data.get('description', 'No description provided.')
            
            try:
                from promptops.validation import WorkflowSchema
                from promptops.visualization import MermaidGrapher
                wf = WorkflowSchema(**data)
                mermaid = MermaidGrapher.generate(wf)
            except Exception as e:
                print(f"Error parsing {path} for mermaid generation: {e}")
                mermaid = ""

            
            filename = path.stem.replace('.workflow', '') + ".md"
            output_file = out_workflows_dir / filename
            
            if not check:
                output_file.parent.mkdir(parents=True, exist_ok=True)
            
            if repo_url:
                github_url = f"{repo_url}/blob/{branch}/{path.relative_to(workflows_path.parent)}"
                link_md = f"[View Source YAML]({github_url})"
            else:
                link_md = ""
                
            mermaid_block = f"## Workflow Diagram\n\n```mermaid\n{mermaid}\n```\n" if mermaid else ""
            
            content = f"---\ntitle: {title}\n---\n\n# {title}\n\n{desc}\n\n{mermaid_block}\n{link_md}\n"
            
            if check:
                if not output_file.exists():
                    print(f"Drift detected: Missing workflow file {output_file}")
                    sync_ok = False
                elif output_file.read_text(encoding='utf-8') != content:
                    print(f"Drift detected: Content mismatch in workflow {output_file}")
                    sync_ok = False
            else:
                output_file.write_text(content, encoding='utf-8')
            
            category = derive_category(path, workflows_path, data)
                
            items.append(DocItem(
                title=title,
                path=output_file,
                category=category,
                item_type='workflow'
            ))
        
    registry: Dict[str, Dict[str, List[DocItem]]] = {}
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
                rel_path = os.path.relpath(p.path, docs_path)
                md.append(f"- [{p.title}]({rel_path})")
                
        if types['workflow']:
            if category != "Workflows":
                md.append("\n## Workflows")
            for w in sorted(types['workflow'], key=lambda x: x.title.lower()):
                rel_path = os.path.relpath(w.path, docs_path)
                md.append(f"- [{w.title}]({rel_path})")
                
        content = "\n".join(md)
        if check:
            if not out_path.exists():
                print(f"Drift detected: Missing category file {out_path}")
                sync_ok = False
            elif out_path.read_text(encoding='utf-8') != content:
                print(f"Drift detected: Content mismatch in category {out_path}")
                sync_ok = False
        else:
            out_path.write_text(content, encoding='utf-8')
        
    # Generate index.md
    index_path = docs_path / "index.md"
    index_md = [
        "---",
        "title: Knowledge Base Home",
        "---",
        "",
        "# Proompts Knowledge Base",
        "",
        "Welcome to the Proompts documentation. Select a category below:",
        ""
    ]
    
    for category in sorted(registry.keys()):
        if not any(registry[category].values()):
            continue
        filename = category.lower().replace(" ", "_") + ".md"
        index_md.append(f"- [{category}]({filename})")
        
    content = "\n".join(index_md)
    if check:
        if not index_path.exists():
            print(f"Drift detected: Missing index file {index_path}")
            sync_ok = False
        elif index_path.read_text(encoding='utf-8') != content:
            print(f"Drift detected: Content mismatch in index {index_path}")
            sync_ok = False
        if sync_ok:
            print("Documentation is up to date.")
        else:
            print("Documentation drift detected.")
    else:
        index_path.write_text(content, encoding='utf-8')
        print(f"Generated index.md at {index_path}")
        print(f"Documentation generated at {output_dir}")
        
    return sync_ok

