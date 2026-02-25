#!/usr/bin/env python3
"""Create ``overview.md`` files for prompt directories if missing."""

from __future__ import annotations

from pathlib import Path
import sys

try:
    from utils import PROMPTS_DIR, WORKFLOWS_DIR, load_yaml, OVERVIEW_NAME
except ImportError:
    import sys
    sys.path.append(str(Path(__file__).parent))
    from utils import PROMPTS_DIR, WORKFLOWS_DIR, load_yaml, OVERVIEW_NAME


def get_prompt_metadata(path: Path) -> tuple[str, str]:
    """Return prompt title and description from a YAML file or fallback to filename."""
    data = load_yaml(path)
    title = data.get("name") or data.get("title")
    description = data.get("description", "")

    if title:
        return str(title).strip(), str(description).strip()

    name = path.name
    for ext in (".prompt.yaml", ".prompt.yml", ".workflow.yaml", ".workflow.yml"):
        if name.lower().endswith(ext):
            name = name[: -len(ext)]
            break
    if name.split("_", 1)[0].isdigit():
        name = name.split("_", 1)[1]

    title = name.replace("_", " ").title()
    return title, str(description).strip()


def generate_overview(directory: Path) -> str:
    title = directory.name.replace("_", " ").title()
    prompt_files = []
    for pattern in ("*.prompt.yaml", "*.prompt.yml", "*.workflow.yaml", "*.workflow.yml"):
        prompt_files.extend(directory.glob(pattern))
    
    # Filter out hidden files (e.g. ._ files on Mac)
    prompt_files = [f for f in prompt_files if not f.name.startswith('.')]
    
    lines = []
    for file in sorted(prompt_files):
        heading, description = get_prompt_metadata(file)
        if description:
            lines.append(f"- **[{heading}]({file.name})**: {description}")
        else:
            lines.append(f"- [{heading}]({file.name})")
    
    # Scan for subdirectories that have prompts or overviews
    subdirs = []
    for child in directory.iterdir():
        if child.is_dir() and not child.name.startswith('.'):
            # Check if this subdir has prompts recursively or has an overview
            has_sub_prompts = False
            for pattern in ("*.prompt.yaml", "*.prompt.yml", "*.workflow.yaml", "*.workflow.yml"):
                if any(child.rglob(pattern)):
                    has_sub_prompts = True
                    break
            
            if has_sub_prompts:
                # Use the subdirectory name as title, or try to read its overview title?
                # For simplicity, just use name.
                title_sd = child.name.replace("_", " ").title()
                subdirs.append(f"- [{title_sd}/]({child.name}/overview.md)")

    if not lines and not subdirs:
        return ""
    
    sections = [f"# {title} Overview", ""]
    if subdirs:
        sections.append("## Categories")
        sections.extend(sorted(subdirs))
        sections.append("")
        
    if lines:
        has_workflows = any(f.name.endswith('workflow.yaml') or f.name.endswith('workflow.yml') for f in prompt_files)
        has_prompts = any(f.name.endswith('prompt.yaml') or f.name.endswith('prompt.yml') for f in prompt_files)

        if has_workflows and has_prompts:
             sections.append("## Prompts & Workflows")
        elif has_workflows:
             sections.append("## Workflows")
        else:
             sections.append("## Prompts")
        sections.extend(lines)
        
    return "\n".join(sections).rstrip() + "\n"


def ensure_overview(directory: Path) -> bool:
    path = directory / OVERVIEW_NAME
    content = generate_overview(directory)
    
    if not content:
        if path.exists():
            path.unlink()
            return True
        return False
    
    if path.exists():
        if path.read_text(encoding="utf-8") == content:
            return False
            
    path.write_text(content, encoding="utf-8")
    return True


def main() -> int:
    changed = False
    
    # helper to check if directory has content (recursively)
    def has_content(d: Path) -> bool:
        for pattern in ("*.prompt.yaml", "*.prompt.yml", "*.workflow.yaml", "*.workflow.yml"):
            if any(d.rglob(pattern)):
                return True
        return False

    # Walk through all directories under PROMPTS_DIR and WORKFLOWS_DIR
    for root_dir in [PROMPTS_DIR, WORKFLOWS_DIR]:
        if not root_dir.exists():
            continue
        for directory in root_dir.rglob("*"):
            if directory.is_dir() and has_content(directory):
                if ensure_overview(directory):
                    print(f"Generated overview for {directory}")
                    changed = True
                
    return 0 if changed else 0


if __name__ == "__main__":
    raise SystemExit(main())
