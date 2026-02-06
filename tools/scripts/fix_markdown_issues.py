#!/usr/bin/env python3
"""Automatically fix common Markdown issues listed in todo_fix.md."""

from __future__ import annotations

from pathlib import Path
import re

TODO_FILE = "todo_fix.md"

# Regex patterns for list items and headers
ORDERED_RE = re.compile(r"^(\s*)(\d+)\.\s+")
UNORDERED_RE = re.compile(r"^(\s*)([-*+])\s+")
HEADER_RE = re.compile(r"^(#+)([^#\s])")


def load_paths(todo_path: Path):
    paths = []
    with todo_path.open() as f:
        for line in f:
            line = line.strip()
            if line.startswith("- ./") and line.endswith(".md"):
                paths.append(line[3:])
    return paths


def fix_trailing_spaces(lines):
    return [re.sub(r"\s+$", "", l) for l in lines]


def fix_front_matter(lines):
    """Move any headings mistakenly placed inside front matter."""
    if not lines:
        return lines
    try:
        start = lines.index("---")
        end = lines.index("---", start + 1)
    except ValueError:
        return lines
    fm = lines[start:end + 1]
    body = lines[end + 1:]
    headers = [l for l in fm if l.lstrip().startswith("#")]
    fm = [l for l in fm if not l.lstrip().startswith("#")]
    if headers:
        # ensure blank line after front matter
        if fm and fm[-1].strip() != "":
            fm.append("")
        lines = lines[:start] + fm + headers + body
    return lines


def fix_header_style(lines):
    return [HEADER_RE.sub(r"\1 \2", l) for l in lines]


def fix_header_spacing(lines):
    out = []
    i = 0
    while i < len(lines):
        line = lines[i]
        if line.lstrip().startswith("#"):
            if out and out[-1].strip() != "":
                out.append("")
            out.append(line)
            if i + 1 < len(lines) and lines[i + 1].strip() != "":
                out.append("")
            i += 1
        else:
            out.append(line)
            i += 1
    return out


def fix_first_header(lines):
    """Ensure the first header after front matter is level 1."""
    idx = 0
    if lines and lines[0].strip() == "---":
        idx = 1
        while idx < len(lines) and lines[idx].strip() != "---":
            idx += 1
        if idx < len(lines):
            idx += 1
    for j in range(idx, len(lines)):
        if lines[j].lstrip().startswith("#"):
            lines[j] = re.sub(r"^#+", "#", lines[j])
            break
    return lines


def fix_ordered_lists(lines):
    out = []
    i = 0
    while i < len(lines):
        m = ORDERED_RE.match(lines[i])
        if m:
            indent = m.group(1)
            count = 1
            while i < len(lines) and ORDERED_RE.match(lines[i]):
                content = ORDERED_RE.sub("", lines[i]).strip()
                out.append(f"{indent}{count}. {content}")
                i += 1
                count += 1
            continue
        out.append(lines[i])
        i += 1
    return out


def fix_blank_lines_around_lists(lines):
    out = []
    i = 0
    while i < len(lines):
        if ORDERED_RE.match(lines[i]) or UNORDERED_RE.match(lines[i]):
            if out and out[-1].strip() != "":
                out.append("")
            while i < len(lines) and (ORDERED_RE.match(lines[i]) or UNORDERED_RE.match(lines[i])):
                out.append(lines[i])
                i += 1
            if i < len(lines) and lines[i].strip() != "":
                out.append("")
        else:
            out.append(lines[i])
            i += 1
    return out


def fix_multiple_blank_lines(lines):
    out = []
    blank = False
    for l in lines:
        if l.strip() == "":
            if not blank:
                out.append("")
                blank = True
        else:
            out.append(l)
            blank = False
    return out


def escape_bare_pipes(lines):
    out = []
    for l in lines:
        if "|" in l and not l.strip().startswith("|") and not l.strip().startswith("```"):
            l = l.replace("|", "\\|")
        out.append(l)
    return out


def fix_codeblock_spacing(lines):
    out = []
    i = 0
    in_code = False
    while i < len(lines):
        line = lines[i]
        if line.strip().startswith("```"):
            if not in_code and out and out[-1].strip() != "":
                out.append("")
            out.append(line)
            in_code = not in_code
            if in_code and i + 1 < len(lines) and lines[i + 1].strip() != "":
                out.append("")
            elif not in_code and i + 1 < len(lines) and lines[i + 1].strip() != "":
                out.append("")
            i += 1
            continue
        out.append(line)
        i += 1
    return out


def process_file(path: Path):
    text = path.read_text().splitlines()
    original = list(text)
    text = fix_trailing_spaces(text)
    text = fix_front_matter(text)
    text = fix_header_style(text)
    text = fix_first_header(text)
    text = fix_header_spacing(text)
    text = fix_ordered_lists(text)
    text = fix_blank_lines_around_lists(text)
    text = fix_codeblock_spacing(text)
    text = escape_bare_pipes(text)
    text = fix_multiple_blank_lines(text)
    if text != original:
        path.write_text("\n".join(text) + "\n")
        return True
    return False


def main():
    todo_path = Path(TODO_FILE)
    if not todo_path.exists():
        print(f"{TODO_FILE} not found")
        return
    paths = load_paths(todo_path)
    changed = False
    for rel in paths:
        p = Path(rel)
        if p.exists():
            if process_file(p):
                print(f"Fixed {rel}")
                changed = True
    if not changed:
        print("No changes made.")


if __name__ == "__main__":
    main()
