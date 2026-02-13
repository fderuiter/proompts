#!/usr/bin/env python3
"""Create ``overview.md`` files for prompt directories if missing."""

from __future__ import annotations

from pathlib import Path
import sys

try:
    from utils import PROMPTS_DIR, load_yaml, OVERVIEW_NAME
except ImportError:
    import sys
    sys.path.append(str(Path(__file__).parent))
    from utils import PROMPTS_DIR, load_yaml, OVERVIEW_NAME


def title_from_prompt(path: Path) -> str:
    """Return prompt title from a YAML file or fallback to filename."""
    data = load_yaml(path)
    title = data.get("name") or data.get("title")
    if title:
        return str(title).strip()

    name = path.name
    for ext in (".prompt.yaml", ".prompt.yml"):
        if name.lower().endswith(ext):
            name = name[: -len(ext)]
            break
    if name.split("_", 1)[0].isdigit():
        name = name.split("_", 1)[1]
    return name.replace("_", " ").title()


def generate_overview(directory: Path) -> str:
    title = directory.name.replace("_", " ").title()
    lines = [f"# {title} Overview", ""]
    prompt_files = []
    for pattern in ("*.prompt.yaml", "*.prompt.yml"):
        prompt_files.extend(directory.glob(pattern))
    
    # Filter out hidden files (e.g. ._ files on Mac)
    prompt_files = [f for f in prompt_files if not f.name.startswith('.')]
    
    lines = []
    for file in sorted(prompt_files):
        heading = title_from_prompt(file)
        lines.append(f"- [{heading}]({file.name})")
    
    # Scan for subdirectories that have prompts or overviews
    subdirs = []
    for child in directory.iterdir():
        if child.is_dir() and not child.name.startswith('.'):
            # Check if this subdir has prompts recursively or has an overview
            has_sub_prompts = False
            for pattern in ("*.prompt.yaml", "*.prompt.yml"):
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
            
    path.write_text(content, encoding="utf-8")
    return True


def main() -> int:
    changed = False
    
    # helper to check if directory has prompts (recursively)
    def has_prompts(d: Path) -> bool:
        for pattern in ("*.prompt.yaml", "*.prompt.yml"):
            if any(d.rglob(pattern)):
                return True
        return False

    # Walk through all directories under PROMPTS_DIR
    for directory in PROMPTS_DIR.rglob("*"):
        if directory.is_dir() and has_prompts(directory):
            if ensure_overview(directory):
                print(f"Generated overview for {directory}")
                changed = True
                
    return 0 if changed else 0


if __name__ == "__main__":
    raise SystemExit(main())
