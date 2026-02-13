#!/usr/bin/env python3
"""Update `docs/index.md` and `docs/table-of-contents.md` from prompt metadata."""

from __future__ import annotations

import argparse
from collections import defaultdict
from pathlib import Path

try:
    from utils import PROMPTS_DIR, ROOT, iter_prompt_files, load_yaml
except ImportError:
    import sys
    sys.path.append(str(Path(__file__).parent))
    from utils import PROMPTS_DIR, ROOT, iter_prompt_files, load_yaml

DOCS_DIR = ROOT / "docs"

INDEX_HEADER = """---
layout: home
title: Home
nav_order: 0
---

# Proompts

Welcome to **Proompts**, a curated collection of high-quality prompts and workflows for AI-assisted product development, regulatory compliance, and clinical research.

Whether you are a Product Manager, Clinical Lead, or Software Engineer, this repository provides the building blocks to operationalize LLMs in your daily work.

## Getting Started

1. **Browse Categories**: Explore prompts by domain (e.g., [Clinical](clinical.md), [Software Engineering](software_engineering.md)).
2. **Run Workflows**: Use our [Workflows](workflows.md) to chain multiple prompts together for complex tasks like "Idea to Epic".
3. **Copy & Customize**: All prompts are in YAML format, ready to be used in your own tools or agents.

## Key Concepts

- **Prompts**: Single-task instructions for an LLM (e.g., "Review this code", "Draft a protocol").
- **Workflows**: Sequences of prompts that pass data from one step to the next to achieve a larger goal.
- **Agents**: The AI systems that execute these prompts and workflows.

## Explore by Domain

<div class="grid-container">
  <a href="clinical.html" class="card">
    <h3>🏥 Clinical</h3>
    <p>Protocols, monitoring, safety, and regulatory workflows.</p>
  </a>
  <a href="business.html" class="card">
    <h3>💼 Business</h3>
    <p>Market research, CFO insights, and operational planning.</p>
  </a>
  <a href="technical.html" class="card">
    <h3>💻 Technical</h3>
    <p>Architecture, software engineering, and code reviews.</p>
  </a>
  <a href="workflows.html" class="card">
    <h3>🔄 Workflows</h3>
    <p>End-to-end chains: "Idea to Epic" and "Protocol Design".</p>
  </a>
  <a href="regulatory.html" class="card">
    <h3>⚖️ Regulatory</h3>
    <p>FDA submissions, compliance checks, and gap analysis.</p>
  </a>
  <a href="management.html" class="card">
    <h3>📊 Management</h3>
    <p>Project tracking, leadership, and team effectiveness.</p>
  </a>
  <a href="system_architecture.html" class="card">
    <h3>🏗️ Architecture</h3>
    <p>System internals, simulation engine, and validation pipeline.</p>
  </a>
</div>

<style>
.grid-container {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 20px;
  margin-top: 20px;
}
.card {
  border: 1px solid #30363d; /* Matches dark theme border */
  border-radius: 6px;
  padding: 20px;
  text-decoration: none !important;
  color: inherit;
  transition: transform 0.2s, box-shadow 0.2s;
  background-color: #0d1117; /* Matches dark theme bg */
}
.card:hover {
  transform: translateY(-3px);
  box-shadow: 0 10px 20px rgba(0,0,0,0.4);
  border-color: #58a6ff;
}
.card h3 {
  margin-top: 0;
  color: #58a6ff;
}
</style>

## Search
"""

SEARCH_UI = """
<div class="search-container">
    <input type="text" id="search-input" placeholder="Search prompts..." style="width: 100%; padding: 10px; margin-bottom: 20px;">
    <ul id="results-container"></ul>
</div>

<script src="https://unpkg.com/simple-jekyll-search@latest/dest/simple-jekyll-search.min.js"></script>
<script>
    window.simpleJekyllSearch = new SimpleJekyllSearch({
        searchInput: document.getElementById('search-input'),
        resultsContainer: document.getElementById('results-container'),
        json: '{{ site.baseurl }}/search.json',
        searchResultTemplate: '<li><a href="{{ site.baseurl }}/{url}"><strong>{title}</strong></a><br><span style="font-size:0.8em">{description}</span></li>',
        noResultsText: 'No prompts found',
        limit: 10,
        fuzzy: false
    })
</script>
"""


def read_meta(path: Path) -> tuple[str, str]:
    """Return category and title from a prompt file."""
    try:
        data = load_yaml(path)
        title = str(data.get("name") or data.get("title") or "").strip()
        # Use parent's parent name for category, e.g. "clinical" for "prompts/clinical/adjudication"
        category = path.parent.parent.name
        if category == "prompts": # a prompt in a top-level category dir
            category = path.parent.name

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
    for path in iter_prompt_files(PROMPTS_DIR):
        if not path.is_file():
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

    # Prepend the fixed header content to the generated index
    # We no longer append the full list to index.md, as it uses the grid view.
    index_lines = [INDEX_HEADER, SEARCH_UI]
    toc_lines: list[str] = []

    for category, items in groups.items():
        for path, title in items:
            rel = Path("..") / path.relative_to(ROOT)
            link = f"[{title}]({rel.as_posix()})"
            toc_lines.append(link)

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


def run_update(check: bool = False) -> int:
    index, toc = generate()

    if check:
        if check_files(index, toc):
            return 0
        print("docs index out of date")
        return 1

    write_files(index, toc)
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description="Update documentation index")
    parser.add_argument("--check", action="store_true", help="verify generated files are up to date")
    args = parser.parse_args()
    return run_update(check=args.check)


if __name__ == "__main__":
    raise SystemExit(main())
