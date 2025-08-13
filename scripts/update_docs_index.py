#!/usr/bin/env python3
"""Update `docs/index.md` and `docs/table-of-contents.md` from prompt metadata."""

from __future__ import annotations

import argparse
import json
import sys
from collections import defaultdict
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
DOCS_DIR = ROOT / "docs"
EXCLUDE = {"docs", "scripts", ".github"}
PROMPT_EXTENSIONS = (".prompt.yaml", ".prompt.yml", ".json")


def read_meta(path: Path) -> tuple[str, str]:
    """Return category and title from a prompt file."""
    try:
        text = path.read_text(encoding="utf-8")
        lower = path.name.lower()
        if lower.endswith(".json"):
            data = json.loads(text)
            title = str(data.get("title") or data.get("name") or "").strip()
        else:
            data = yaml.safe_load(text) or {}
            title = str(data.get("name") or data.get("title") or "").strip()
        category = str(data.get("category") or path.parent.name)
    except Exception:
        category = path.parent.name
        title = ""

    if not title:
        name = path.stem
        if "_" in name and name.split("_", 1)[0].isdigit():
            name = name.split("_", 1)[1]
        name = name.replace("_", " ").replace("-", " ")
        title = " ".join(word.capitalize() for word in name.split())

    return category, title


def collect_prompts() -> dict[str, list[tuple[Path, str]]]:
    """Group prompt file paths by category."""
    groups: dict[str, list[tuple[Path, str]]] = defaultdict(list)
    for ext in PROMPT_EXTENSIONS:
        for path in ROOT.rglob(f"*{ext}"):
            if not path.is_file():
                continue
            if any(part in EXCLUDE for part in path.parts):
                continue
            category, title = read_meta(path)
            groups[category].append((path, title))
    # sort files within each category
    for cat in groups:
        groups[cat].sort(key=lambda t: t[0])
    return dict(sorted(groups.items()))


def nice_title(name: str) -> str:
    name = name.replace("_", " ").replace("-", " ")
    return " ".join(word.capitalize() for word in name.split())


def generate() -> tuple[str, str]:
    """Generate index.md and table-of-contents.md content."""
    groups = collect_prompts()
    index_lines = ["# Table of Contents", ""]
    toc_lines: list[str] = []

    for category, items in groups.items():
        index_lines.append(f"## {nice_title(category)}")
        index_lines.append("")
        for path, title in items:
            rel = Path("..") / path.relative_to(ROOT)
            link = f"[{title}]({rel.as_posix()})"
            index_lines.append(f"- {link}")
            toc_lines.append(link)
        index_lines.append("")

    index_content = "\n".join(index_lines).rstrip() + "\n"
    toc_content = "\n".join(toc_lines).rstrip() + "\n"
    return index_content, toc_content


def write_files(index: str, toc: str) -> None:
    (DOCS_DIR / "index.md").write_text(index, encoding="utf-8")
    (DOCS_DIR / "table-of-contents.md").write_text(toc, encoding="utf-8")


def check_files(index: str, toc: str) -> bool:
    index_path = DOCS_DIR / "index.md"
    toc_path = DOCS_DIR / "table-of-contents.md"
    existing_index = index_path.read_text(encoding="utf-8") if index_path.exists() else ""
    existing_toc = toc_path.read_text(encoding="utf-8") if toc_path.exists() else ""
    return existing_index == index and existing_toc == toc


def main() -> int:
    parser = argparse.ArgumentParser(description="Update documentation index")
    parser.add_argument("--check", action="store_true", help="verify generated files are up to date")
    args = parser.parse_args()

    index, toc = generate()

    if args.check:
        if check_files(index, toc):
            return 0
        print("docs index out of date", file=sys.stderr)
        return 1

    write_files(index, toc)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
