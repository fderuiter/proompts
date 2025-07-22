#!/usr/bin/env python3
"""Update docs index and table of contents for prompt files."""

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOCS_DIR = ROOT / "docs"
EXCLUDE_DIRS = {"docs", "scripts", ".github"}


def title_from_json(path: Path) -> str:
    """Return the prompt title from a JSON file."""
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
        title = data.get("title")
        if title:
            return str(title).strip()
    except Exception:
        pass
    name = path.stem
    if "_" in name and name.split("_", 1)[0].isdigit():
        name = name.split("_", 1)[1]
    name = name.replace("_", " ").replace("-", " ")
    return " ".join(word.capitalize() for word in name.split())


def category_title(directory: Path) -> str:
    """Generate a category title from the directory name."""
    name = directory.name.replace("_", " ").replace("-", " ")
    return " ".join(word.capitalize() for word in name.split())


def prompt_files(directory: Path):
    """Yield all JSON prompt files within directory."""
    for path in sorted(directory.glob("*.json")):
        if path.is_file():
            yield path


def generate():
    index_lines = ["# Table of Contents", ""]
    toc_lines = []

    for cat_dir in sorted([d for d in ROOT.iterdir() if d.is_dir() and d.name not in EXCLUDE_DIRS]):
        files = list(prompt_files(cat_dir))
        if not files:
            continue
        title = category_title(cat_dir)
        index_lines.append(f"## {title}")
        index_lines.append("")
        for file in files:
            heading = title_from_json(file)
            rel = Path("..") / file.relative_to(ROOT)
            link = f"[{heading}]({rel.as_posix()})"
            index_lines.append(f"- {link}")
            toc_lines.append(link)
        index_lines.append("")

    index_content = "\n".join(index_lines).rstrip() + "\n"
    toc_content = "\n".join(toc_lines).rstrip() + "\n"
    return index_content, toc_content


def write_files(index_content: str, toc_content: str):
    (DOCS_DIR / "index.md").write_text(index_content, encoding="utf-8")
    (DOCS_DIR / "table-of-contents.md").write_text(toc_content, encoding="utf-8")


def check_files(index_content: str, toc_content: str) -> bool:
    index_path = DOCS_DIR / "index.md"
    toc_path = DOCS_DIR / "table-of-contents.md"
    existing_index = index_path.read_text(encoding="utf-8") if index_path.exists() else ""
    existing_toc = toc_path.read_text(encoding="utf-8") if toc_path.exists() else ""
    return existing_index == index_content and existing_toc == toc_content


def main() -> int:
    parser = argparse.ArgumentParser(description="Update documentation index")
    parser.add_argument("--check", action="store_true", help="verify generated files are up to date")
    args = parser.parse_args()

    index_content, toc_content = generate()

    if args.check:
        if check_files(index_content, toc_content):
            return 0
        print("docs index out of date", file=sys.stderr)
        return 1

    write_files(index_content, toc_content)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
