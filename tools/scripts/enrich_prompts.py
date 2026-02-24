#!/usr/bin/env python3
"""Enrich prompt YAML files with meaningful variable descriptions and metadata.

Strategy:
  1. Variable descriptions: inferred from surrounding message context where
     {{var_name}} appears, or from the variable name and prompt description.
  2. Metadata: domain/complexity/tags/requires_context derived from the file
     path and prompt content heuristics.
"""

from __future__ import annotations

import re
from pathlib import Path
from typing import Any

import yaml


# Configure yaml to use block scalars for multiline strings
def str_presenter(dumper, data):
    if len(data.splitlines()) > 1:  # check for multiline string
        return dumper.represent_scalar('tag:yaml.org,2002:str', data, style='|')
    return dumper.represent_scalar('tag:yaml.org,2002:str', data)

yaml.add_representer(str, str_presenter)

try:
    from utils import ROOT, iter_prompt_files, load_yaml
except ImportError:
    import sys
    sys.path.append(str(Path(__file__).parent))
    from utils import ROOT, iter_prompt_files, load_yaml

PROMPTS_DIR = ROOT / "prompts"

# ────────────────────────────────────────────────────────────────────────────
# 1.  Configuration & Mapping
# ────────────────────────────────────────────────────────────────────────────

CONFIG_PATH = Path(__file__).parent / "enrich_config.yaml"
CONFIG = load_yaml(CONFIG_PATH)

DOMAIN_MAP: dict[str, str] = CONFIG.get("domain_map", {})
TAG_LABELS: dict[str, str] = CONFIG.get("tag_labels", {})


def _path_parts(file_path: Path) -> list[str]:
    """Return path parts relative to prompts dir."""
    try:
        rel = file_path.resolve().relative_to(PROMPTS_DIR.resolve())
    except ValueError:
        return []
    return list(rel.parts[:-1])  # exclude filename


def infer_domain(parts: list[str]) -> str:
    if parts:
        return DOMAIN_MAP.get(parts[0], parts[0])
    return "general"


def infer_tags(parts: list[str], name: str) -> list[str]:
    """Produce a short list of tags from path parts and prompt name."""
    tags: list[str] = []
    for p in parts[1:]:  # skip the domain itself
        label = TAG_LABELS.get(p, p.replace("_", "-"))
        if label not in tags:
            tags.append(label)
    # Split prompt name into individual words for tags
    # Handle CamelCase, hyphens, underscores, and special chars
    cleaned = re.sub(r'[^a-zA-Z0-9\s-]', ' ', name)
    # Split CamelCase
    cleaned = re.sub(r'([a-z])([A-Z])', r'\1 \2', cleaned)
    name_words = cleaned.lower().split()
    stop = {"a", "an", "the", "of", "for", "and", "to", "in", "is", "with",
            "from", "by", "on", "my", "your", "i", "its", "it", "or", "as",
            "be", "at", "im", "that", "this", "are", "eli5", "like", "up",
            "how", "you", "me", "we", "so", "do", "can", "not", "no", "has",
            "should", "would", "based", "s", "ii", "iii", "iv", "v"}
    for w in name_words:
        if len(w) > 2 and w not in stop and w not in tags:
            tags.append(w)
            if len(tags) >= 5:
                break
    return tags[:5]


# ────────────────────────────────────────────────────────────────────────────
# 2.  Complexity heuristic
# ────────────────────────────────────────────────────────────────────────────

def infer_complexity(content: dict) -> str:
    """low / medium / high based on variable count and message length."""
    num_vars = len(content.get("variables", []))
    total_msg_len = sum(len(m.get("content", "")) for m in content.get("messages", []))
    if num_vars >= 4 or total_msg_len > 1500:
        return "high"
    elif num_vars >= 2 or total_msg_len > 600:
        return "medium"
    return "low"


# ────────────────────────────────────────────────────────────────────────────
# 3.  requires_context heuristic
# ────────────────────────────────────────────────────────────────────────────

CONTEXT_KEYWORDS = set(CONFIG.get("context_keywords", []))


def infer_requires_context(content: dict) -> bool:
    """True if prompt likely needs external documents."""
    all_text = " ".join(
        m.get("content", "") for m in content.get("messages", [])
    ).lower()
    var_names = {v.get("name", "") for v in content.get("variables", [])}
    if var_names & CONTEXT_KEYWORDS:
        return True
    hits = sum(1 for kw in CONTEXT_KEYWORDS if kw in all_text)
    return hits >= 2


# ────────────────────────────────────────────────────────────────────────────
# 4.  Variable description inference
# ────────────────────────────────────────────────────────────────────────────

def _extract_surrounding_context(text: str, var_name: str, window: int = 120) -> str:
    """Return snippet of text surrounding {{var_name}}."""
    pattern = r'\{\{' + re.escape(var_name) + r'\}\}'
    m = re.search(pattern, text)
    if not m:
        return ""
    start = max(0, m.start() - window)
    end = min(len(text), m.end() + window)
    return text[start:end]


def _infer_description_from_inline_label(text: str, var_name: str) -> str | None:
    """Try to extract `{{var}} – description` or ``{{var}}`` – description patterns."""
    patterns = [
        # `{{var}}` – description  or  `{{var}}` — description
        r'`?\{\{' + re.escape(var_name) + r'\}\}`?\s*[–—\-]+\s*(.+?)(?:\n|$|;|\.|\\n)',
        # var_name: description (as in inline documentation)
        r'(?:^|\n)\s*[-*]?\s*' + re.escape(var_name) + r'\s*[:=]\s*(.+?)(?:\n|$)',
        # Label: {{var}} (reverse mapping)
        r'(?:^|\n)\s*[-*]?\s*(.+?)\s*[:=]\s*`?\{\{' + re.escape(var_name) + r'\}\}`?',
    ]
    for pat in patterns:
        m = re.search(pat, text, re.IGNORECASE)
        if m:
            desc = m.group(1).strip().rstrip('.')
            # Clean trailing punctuation and excess
            if len(desc) > 5:  # Allow slightly shorter labels like "Context"
                return desc[:150]
    return None


# Common variable name → fallback description mapping
COMMON_VAR_DESCRIPTIONS: dict[str, str] = CONFIG.get("common_var_descriptions", {})


def infer_variable_description(
    var_name: str,
    content: dict,
    prompt_name: str,
    prompt_description: str,
) -> str:
    """Infer a human-readable description for a variable."""
    # 1. Try to extract description from message content (inline labels)
    all_msg_text = "\n".join(m.get("content", "") for m in content.get("messages", []))
    inline = _infer_description_from_inline_label(all_msg_text, var_name)
    if inline:
        return inline

    # 2. Try surrounding context
    ctx = _extract_surrounding_context(all_msg_text, var_name)
    if ctx:
        inline2 = _infer_description_from_inline_label(ctx, var_name)
        if inline2:
            return inline2

    # 3. Check common variable names
    key = var_name.lower().strip()
    if key in COMMON_VAR_DESCRIPTIONS:
        return COMMON_VAR_DESCRIPTIONS[key]

    # 4. Partial match: check if variable name contains a known key
    for known_key, desc in COMMON_VAR_DESCRIPTIONS.items():
        if known_key in key or key in known_key:
            return desc

    # 5. Generate from variable name itself
    readable_name = var_name.replace("_", " ").replace("-", " ").strip()
    return f"The {readable_name} to use for this prompt"


# ────────────────────────────────────────────────────────────────────────────
# 5.  Main enrichment logic
# ────────────────────────────────────────────────────────────────────────────

def enrich_file(file_path: Path, dry_run: bool = False) -> bool:
    """Enrich a single prompt file with descriptions and metadata.
    Returns True if the file was modified.
    """
    content = load_yaml(file_path)
    if not content:
        print(f"  SKIP (empty): {file_path}")
        return False

    modified = False
    parts = _path_parts(file_path)

    # ── A. Fill in variable descriptions ────────────────────────────────
    variables = content.get("variables", [])
    prompt_name = content.get("name", "")
    prompt_desc = content.get("description", "")

    for var in variables:
        if var.get("description") == "TODO" or not var.get("description"):
            new_desc = infer_variable_description(
                var["name"], content, prompt_name, prompt_desc
            )
            var["description"] = new_desc
            modified = True

    # ── B. Add or complete metadata ─────────────────────────────────────
    metadata = content.get("metadata")
    # Handle missing or null metadata block
    if metadata is None:
        metadata = {}
        content["metadata"] = metadata
        modified = True

    # Infer values if missing
    if "domain" not in metadata:
        metadata["domain"] = infer_domain(parts)
        modified = True
    if "complexity" not in metadata:
        metadata["complexity"] = infer_complexity(content)
        modified = True
    if "tags" not in metadata:
        metadata["tags"] = infer_tags(parts, prompt_name)
        modified = True
    if "requires_context" not in metadata:
        metadata["requires_context"] = infer_requires_context(content)
        modified = True

    if not modified:
        print(f"  OK (already enriched): {file_path}")
        return False

    if dry_run:
        print(f"  DRY-RUN would enrich: {file_path}")
        return True

    # ── Write back ──────────────────────────────────────────────────────
    # Reorder keys for readability: name, version, description, metadata,
    # variables, model, modelParameters, messages, testData, evaluators
    ordered: dict[str, Any] = {}
    key_order = [
        "name", "version", "description", "metadata", "variables",
        "model", "modelParameters", "messages", "testData", "evaluators",
        "last_modified",
    ]
    for k in key_order:
        if k in content:
            ordered[k] = content[k]
    # Any remaining keys not in the predefined order
    for k, v in content.items():
        if k not in ordered:
            ordered[k] = v

    yaml_text = yaml.dump(
        ordered,
        default_flow_style=False,
        sort_keys=False,
        allow_unicode=True,
        width=120,
    )
    file_path.write_text("---\n" + yaml_text, encoding="utf-8")
    print(f"  ENRICHED: {file_path}")
    return True


def main() -> int:
    import argparse
    parser = argparse.ArgumentParser(description="Enrich prompt files with descriptions and metadata")
    parser.add_argument("--dry-run", action="store_true",
                        help="Show what would change without writing files")
    parser.add_argument("--file", type=str, default=None,
                        help="Enrich a single file instead of all")
    args = parser.parse_args()

    if args.file:
        p = Path(args.file)
        enrich_file(p, dry_run=args.dry_run)
        return 0

    updated = 0
    total = 0
    for file_path in iter_prompt_files(ROOT):
        total += 1
        if enrich_file(file_path, dry_run=args.dry_run):
            updated += 1

    print(f"\n{'DRY-RUN: ' if args.dry_run else ''}Processed {total} files, "
          f"{updated} enriched.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
