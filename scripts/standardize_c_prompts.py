import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
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

for d in sorted([p for p in ROOT.iterdir() if p.is_dir() and p.name.startswith("c")]):
    for path in sorted(d.glob("*.json")):
        data = json.loads(path.read_text(encoding="utf-8"))
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
            path.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")
            print("Standardized", path)

