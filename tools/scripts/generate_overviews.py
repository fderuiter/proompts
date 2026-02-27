#!/usr/bin/env python3
"""Create ``overview.md`` files for prompt directories if missing."""

from __future__ import annotations

import sys
from pathlib import Path

# Add the parent directory of 'tools' to sys.path so we can import 'tools.scripts.utils'
# Assuming this script is in tools/scripts/
try:
    from utils import PROMPTS_DIR, WORKFLOWS_DIR, load_yaml
except ImportError:
    sys.path.append(str(Path(__file__).parent))
    from utils import PROMPTS_DIR, WORKFLOWS_DIR, load_yaml

OVERVIEW_NAME = "overview.md"


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
    # Remove leading numbers if present (e.g., 01_foo -> foo)
    parts = name.split("_", 1)
    if parts[0].isdigit() and len(parts) > 1:
        name = parts[1]

    title = name.replace("_", " ").title()
    return title, str(description).strip()


def generate_overview_content(directory: Path) -> str:
    """Generate the markdown content for an overview file."""

    # 1. Collect Prompts/Workflows in this directory
    prompt_files = []
    for pattern in ("*.prompt.yaml", "*.prompt.yml", "*.workflow.yaml", "*.workflow.yml"):
        prompt_files.extend(directory.glob(pattern))
    
    # Filter out hidden files
    prompt_files = [f for f in prompt_files if not f.name.startswith('.')]
    prompt_files.sort(key=lambda f: f.name)

    # 2. Collect Subdirectories that are relevant
    # A relevant subdirectory is one that contains prompt/workflow files (recursively)
    subdirs = []
    for child in directory.iterdir():
        if child.is_dir() and not child.name.startswith('.'):
            # Check if this subdir has any relevant content deep down
            has_content_recursive = False
            for pattern in ("*.prompt.yaml", "*.prompt.yml", "*.workflow.yaml", "*.workflow.yml"):
                if any(child.rglob(pattern)):
                    has_content_recursive = True
                    break
            
            if has_content_recursive:
                # Use the subdirectory name as title
                title_sd = child.name.replace("_", " ").title()
                subdirs.append((title_sd, child.name))

    subdirs.sort(key=lambda x: x[0])

    # If no content at all, return empty
    if not prompt_files and not subdirs:
        return ""

    # Build the Markdown
    title = directory.name.replace("_", " ").title()
    lines = [f"# {title} Overview", ""]

    # Add Categories (Subdirectories) section if any
    if subdirs:
        lines.append("## Categories")
        for title_sd, dirname in subdirs:
            lines.append(f"- [**{title_sd}**]({dirname}/overview.md)")
        lines.append("")

    # Add Prompts/Workflows section if any files exist
    if prompt_files:
        has_workflows = any(f.name.endswith(('workflow.yaml', 'workflow.yml')) for f in prompt_files)
        has_prompts = any(f.name.endswith(('prompt.yaml', 'prompt.yml')) for f in prompt_files)

        if has_workflows and has_prompts:
            lines.append("## Prompts & Workflows")
        elif has_workflows:
            lines.append("## Workflows")
        else:
            lines.append("## Prompts")

        for file in prompt_files:
            heading, description = get_prompt_metadata(file)
            if description:
                lines.append(f"- **[{heading}]({file.name})**: {description}")
            else:
                lines.append(f"- [{heading}]({file.name})")
        lines.append("")

    return "\n".join(lines).rstrip() + "\n"


def ensure_overview(directory: Path) -> bool:
    """Create or update overview.md if content differs."""
    path = directory / OVERVIEW_NAME
    content = generate_overview_content(directory)
    
    if not content:
        # If no content is generated, but file exists, delete it
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

    # Process PROMPTS_DIR and WORKFLOWS_DIR
    roots = [d for d in [PROMPTS_DIR, WORKFLOWS_DIR] if d.exists()]

    for root_dir in roots:
        # Walk strictly top-down so we can handle parents?
        # Actually, we want to generate for every directory that has content.
        # os.walk or rglob('*') gives us all dirs.
        # We need to sort them so output is deterministic, though execution order doesn't matter much for individual files.
        all_dirs = sorted([p for p in root_dir.rglob("*") if p.is_dir()])
        # Also include the root_dir itself if it has files (usually not prompts directly in root, but possible)
        all_dirs.insert(0, root_dir)

        for directory in all_dirs:
            # Skip hidden directories
            if directory.name.startswith('.'):
                continue

            # Check if directory should have an overview
            # It should if it has prompt files OR subdirectories with prompt files
            # generate_overview_content handles this check internally and returns "" if empty.
            if ensure_overview(directory):
                print(f"Generated/Updated overview for {directory}")
                changed = True
                
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
