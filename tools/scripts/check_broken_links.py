#!/usr/bin/env python3
"""
🔗 Broken Link Checker
Scans Markdown files for broken internal links and missing anchors.
"""

import re
import sys
import urllib.parse
from pathlib import Path
from typing import List, Tuple, Set

# Configuration
DOCS_DIR = Path("docs")
PROMPTS_DIR = Path("prompts")
ROOT_DIR = Path.cwd()

# Regex to find links: [text](url)
# This is a simple regex and might miss some edge cases, but covers standard markdown links
LINK_PATTERN = re.compile(r'\[([^\]]+)\]\(([^)]+)\)')

def get_all_markdown_files() -> List[Path]:
    """Return a list of all markdown files to scan."""
    files = []
    if DOCS_DIR.exists():
        files.extend([p for p in DOCS_DIR.rglob("*.md") if not p.name.startswith("._")])
    if PROMPTS_DIR.exists():
        files.extend([p for p in PROMPTS_DIR.rglob("*.md") if not p.name.startswith("._")])
    # Also check root files like README.md, CONTRIBUTING.md
    files.extend([p for p in ROOT_DIR.glob("*.md") if not p.name.startswith("._")])
    return files

def get_anchors_in_file(path: Path) -> Set[str]:
    """Extracts all anchors (headers and id attributes) from a file."""
    anchors = set()
    try:
        content = path.read_text(encoding='utf-8')
    except Exception as e:
        print(f"⚠️ Warning: Could not read {path}: {e}")
        return anchors

    # GitHub-style header anchors:
    # # Header Name -> #header-name
    # This is an approximation. GitHub's algorithm is complex (handling special chars, etc.)
    # We will use a simplified version: lowercase, replace spaces with dashes, remove non-alphanumeric
    for line in content.splitlines():
        if line.strip().startswith('#'):
            # Remove leading #'s and whitespace
            header = line.lstrip('#').strip()
            # Generate ID
            anchor = header.lower().replace(' ', '-')
            anchor = re.sub(r'[^\w\-]', '', anchor)
            anchors.add(anchor)
    
    # HTML anchors: <a name="foo"> or <div id="foo">
    # Matches id="foo" or name="foo"
    for match in re.findall(r'(?:id|name)=["\']([^"\']+)["\']', content):
        anchors.add(match)
        
    return anchors

def check_link(source_file: Path, link: str, target_anchors_cache: dict) -> Tuple[bool, str]:
    """
    Validates a single link.
    Returns (is_valid, error_message).
    """
    # Ignore external links
    if link.startswith(('http://', 'https://', 'mailto:', '#')):
        # We ignore pure anchor links (#section) for now to keep it simple, 
        # or we could resolve them against source_file.
        # Let's check pure anchors too.
        if link.startswith('#'):
            target_file = source_file
            anchor = link[1:]
        else:
            return True, ""
    else:
        # Parse URL (handle query params, though rare in file links)
        parsed = urllib.parse.urlparse(link)
        path_part = parsed.path
        anchor = parsed.fragment
        
        # Absolute path relative to repo root (starts with /)
        if path_part.startswith('/'):
            target_file = ROOT_DIR / path_part.lstrip('/')
        else:
            # Relative path
            target_file = (source_file.parent / path_part).resolve()

    # Check if file exists
    if not target_file.exists():
        # Handle "virtual" paths for MkDocs build structure (where prompts/workflows are copied to docs/)
        # Locally, these are in ROOT_DIR/prompts and ROOT_DIR/workflows
        try:
            if target_file.is_relative_to(ROOT_DIR / "docs" / "prompts"):
                rel = target_file.relative_to(ROOT_DIR / "docs" / "prompts")
                alt_target = ROOT_DIR / "prompts" / rel
                if alt_target.exists():
                    target_file = alt_target # Update target_file for anchor check
                else:
                    return False, f"File not found: {link} (checked {alt_target})"
            elif target_file.is_relative_to(ROOT_DIR / "docs" / "workflows_src"):
                rel = target_file.relative_to(ROOT_DIR / "docs" / "workflows_src")
                alt_target = ROOT_DIR / "workflows" / rel
                if alt_target.exists():
                    target_file = alt_target # Update target_file for anchor check
                else:
                     return False, f"File not found: {link} (checked {alt_target})"
            else:
                return False, f"File not found: {link}"
        except ValueError:
            return False, f"File not found: {link}"

    # If it's a directory, it's valid for file browsing
    if target_file.is_dir():
         return True, ""

    # Check anchor if present
    if anchor:
        if str(target_file) not in target_anchors_cache:
            target_anchors_cache[str(target_file)] = get_anchors_in_file(target_file)
        
        known_anchors = target_anchors_cache[str(target_file)]
        if anchor not in known_anchors:
            # Fallback: maybe the manual anchor definition was different?
            # It's hard to be perfect here. We'll report it as a warning or error.
            # For strictness, let's report error.
            return False, f"Anchor #{anchor} not found in {target_file.name}"

    return True, ""

def main():
    print("🔗 Checking for broken links...")
    markdown_files = get_all_markdown_files()
    broken_links_count = 0
    target_anchors_cache = {}

    for file_path in markdown_files:
        try:
            content = file_path.read_text(encoding='utf-8')
        except Exception as e:
            print(f"❌ Error reading {file_path}: {e}")
            continue

        for match in LINK_PATTERN.finditer(content):
            text = match.group(1)
            link = match.group(2)
            
            is_valid, error = check_link(file_path, link, target_anchors_cache)
            if not is_valid:
                print(f"❌ {file_path}:\n   [{text}]({link}) -> {error}")
                broken_links_count += 1

    if broken_links_count > 0:
        print(f"\nFound {broken_links_count} broken links.")
        sys.exit(1)
    else:
        print("\n✅ All internal links verified.")
        sys.exit(0)

if __name__ == "__main__":
    main()
