from pathlib import Path

try:
    from utils import PROMPTS_DIR, load_yaml
except ImportError:
    import sys
    sys.path.append(str(Path(__file__).parent))
    from utils import PROMPTS_DIR, load_yaml

import yaml

TODAY = "2025-07-18"
AUTHOR = "fderuiter"

REQUIRED_SECTIONS = [
    "purpose",
    "context",
    "instructions",
    "inputs",
    "output_format",
]
OPTIONAL_SECTIONS = ["additional_notes", "example_usage", "references"]

for d in sorted([p for p in PROMPTS_DIR.iterdir() if p.is_dir() and p.name.startswith("c")]):
    for path in sorted(d.glob("*.prompt.yaml")):
        data = load_yaml(path) or {}
        prompt = data.get("prompt", {})
        changed = False

        for key in REQUIRED_SECTIONS:
            if key not in prompt:
                prompt[key] = ""
                changed = True
        for key in OPTIONAL_SECTIONS:
            prompt.setdefault(key, "")

        if data.get("author") is None:
            data["author"] = AUTHOR
            changed = True
        if data.get("category") != d.name:
            data["category"] = d.name
            changed = True
        if data.get("last_modified") != TODAY:
            data["last_modified"] = TODAY
            changed = True

        data["prompt"] = prompt

        if changed:
            path.write_text(
                yaml.safe_dump(data, sort_keys=False),
                encoding="utf-8",
            )
            print("Standardized", path)

