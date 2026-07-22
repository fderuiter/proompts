#!/usr/bin/env python3
"""
Generate Overviews Script

## What is this?
This script automatically creates ``overview.md`` files for prompt directories if they are missing.

## Why use it?
- **Maintains Consistency:** Ensures all prompt directories have the required documentation file.
- **Reduces Boilerplate:** Saves developers time by generating the standard overview structure.

## How to use it?
```bash
python3 tools/tools/scripts/generate_overviews.py
```
"""

from __future__ import annotations

from pathlib import Path

from promptops.utils import PROMPTS_DIR, WORKFLOWS_DIR, load_yaml, OVERVIEW_NAME, walk_workspace
from promptops.sync import DirectoryReconciler


def get_prompt_metadata(path: Path) -> tuple[str, str]:
    """
    Extract the title and description for a prompt or workflow from a YAML file or, if missing, derive a title from the file name.
    
    Parameters:
        path (Path): Path to the prompt/workflow YAML file.
    
    Returns:
        tuple[str, str]: A two-tuple of `(title, description)`. `title` is taken from the YAML `name` or `title` field when present, otherwise derived from the filename (known suffixes removed, numeric leading index stripped, underscores converted to spaces, and title-cased). `description` is taken from the YAML `description` field or is an empty string. Both values are trimmed of surrounding whitespace.
    """
    data = load_yaml(path)
    title = data.get("name") or data.get("title")
    description = data.get("description", "")

    if title:
        return str(title).strip(), str(description).strip()

    name = path.name
    for ext in (".prompt.md", ".prompt.yml", ".workflow.yaml", ".workflow.yml"):
        if name.lower().endswith(ext):
            name = name[: -len(ext)]
            break
    if name.split("_", 1)[0].isdigit():
        name = name.split("_", 1)[1]

    title = name.replace("_", " ").title()
    return title, str(description).strip()


def generate_overview(directory: Path, content_cache: dict[Path, bool] | None = None) -> str:
    """
    Generate a markdown overview for prompt and workflow files in a directory.
    
    Builds an "Overview" markdown document that lists prompt/workflow files directly under `directory`
    and links to subdirectory overviews for subdirectories that contain prompt/workflow files.
    If neither files nor subdirectories with content are found, returns an empty string.
    
    Parameters:
        directory (Path): Directory to scan for `.prompt.md/.prompt.yml` and `.workflow.yaml/.workflow.yml` files.
        content_cache (dict[Path, bool] | None): Optional cache mapping subdirectory Paths to a boolean indicating
            whether that subdirectory (recursively) contains prompt/workflow files; when provided, it is consulted
            and updated to avoid repeated recursive scans.
    
    Returns:
        str: Generated markdown overview ending with a single newline, or an empty string if there is no content.
    """
    title = directory.name.replace("_", " ").title()
    prompt_files: list[Path] = []
    
    # Use walk_workspace for a shallow scan
    root, dirs, files = next(walk_workspace(directory), (None, [], []))
    if files:
        for f in files:
            if any(f.endswith(ext) for ext in (".prompt.md", ".prompt.yaml", ".prompt.yml", ".workflow.yaml", ".workflow.yml")) or f == "skills.md":
                prompt_files.append(directory / f)

    lines = []
    for file in sorted(prompt_files):
        heading, description = get_prompt_metadata(file)
        if description:
            lines.append(f"- **[{heading}]({file.name})**: {description}")
        else:
            lines.append(f"- [{heading}]({file.name})")

    # Scan for subdirectories that have prompts or overviews
    subdirs = []
    for d in dirs:
        child = directory / d
        # Check if this subdir has prompts recursively or has an overview
        has_sub_prompts = False
        if content_cache is not None and child in content_cache:
            has_sub_prompts = content_cache[child]
        else:
            for sub_root, _, sub_files in walk_workspace(child):
                for f in sub_files:
                    if any(f.endswith(ext) for ext in (".prompt.md", ".prompt.yaml", ".prompt.yml", ".workflow.yaml", ".workflow.yml")) or f == "skills.md":
                        has_sub_prompts = True
                        break
                if has_sub_prompts:
                    break
            if content_cache is not None:
                content_cache[child] = has_sub_prompts

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


def ensure_overview(directory: Path, content_cache: dict[Path, bool] | None = None, reconciler: 'DirectoryReconciler' | None = None) -> bool:
    """
    Ensure an up-to-date overview.md exists for the given directory.
    
    Generates the overview content for `directory` and writes it to OVERVIEW_NAME if the generated content is non-empty and differs from the existing file (if any). When a `reconciler` is provided, writing is delegated to it instead of performing a direct file write.
    
    Parameters:
        content_cache (dict[Path, bool] | None): Optional memoization mapping used to cache whether directories contain prompt/workflow files (recursively).
        reconciler (DirectoryReconciler | None): Optional reconciler to handle writing/updating the overview file; if provided, `reconciler.write_file(path, content)` is called.
    
    Returns:
        bool: `True` if an overview file was created or updated, `False` otherwise.
    """
    path = directory / OVERVIEW_NAME
    content = generate_overview(directory, content_cache)

    if not content:
        return False
    
    if reconciler:
        return reconciler.write_file(path, content)
    
    if path.exists():
        if path.read_text(encoding="utf-8") == content:
            return False
            
    path.write_text(content, encoding="utf-8")
    return True


def main() -> int:
    """
    Generate or update overview.md files for prompt and workflow directories.
    
    Scans the configured PROMPTS_DIR and WORKFLOWS_DIR (including subdirectories) for prompt/workflow definition files and creates or updates overview.md files using a DirectoryReconciler. Prints a line for each directory where an overview was generated.
    
    Returns:
        int: Exit code; currently always `0`.
    """
    changed = False

    # helper to check if directory has content (recursively)
    content_cache: dict[Path, bool] = {}

    def has_content(d: Path) -> bool:
        """Missing docstring."""
        if d in content_cache:
            return content_cache[d]
        for sub_root, _, sub_files in walk_workspace(d):
            for f in sub_files:
                if any(f.endswith(ext) for ext in (".prompt.md", ".prompt.yaml", ".prompt.yml", ".workflow.yaml", ".workflow.yml")) or f == "skills.md":
                    content_cache[d] = True
                    return True
        content_cache[d] = False
        return False

    # Walk through all directories under PROMPTS_DIR and WORKFLOWS_DIR
    for root_dir in [PROMPTS_DIR, WORKFLOWS_DIR]:
        if not root_dir.exists():
            continue
            
        reconciler = DirectoryReconciler(root_dir, manage_pattern=OVERVIEW_NAME)

        # Include the root_dir itself in the list of directories to process
        dirs_to_process = []
        for root, _, _ in walk_workspace(root_dir):
            dirs_to_process.append(Path(root))

        for directory in dirs_to_process:
            if has_content(directory):
                if ensure_overview(directory, content_cache, reconciler):
                    print(f"Generated overview for {directory}")
                    changed = True
                    
        # Reconcile, but do not delete empty directories in the source tree
        deleted = reconciler.reconcile(prune_empty_dirs=False)
        if deleted > 0:
            changed = True
                
    return 0 if changed else 0


if __name__ == "__main__":
    raise SystemExit(main())
