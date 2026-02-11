#!/usr/bin/env python3
"""Generate Mermaid.js flowchart diagrams from .workflow.yaml files."""

from __future__ import annotations

import re
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent))
from utils import load_yaml, iter_workflow_files

# Captures {{inputs.var_name}} and {{steps.step_id.output}}
VAR_PATTERN = re.compile(r"\{\{(steps\.|inputs\.)(.*?)\}\}")


def generate_mermaid_for_workflow(workflow_data: dict) -> str:
    """Generate Mermaid.js flowchart TD syntax from a workflow dictionary."""
    lines: list[str] = ["```mermaid", "flowchart TD"]

    # --- Global Inputs subgraph ---
    inputs = workflow_data.get("inputs") or []
    if inputs:
        lines.append("    subgraph Inputs [Global Inputs]")
        for inp in inputs:
            name = inp["name"]
            lines.append(f"        inp_{name}(({name}))")
        lines.append("    end")

    # --- Step nodes ---
    steps = workflow_data.get("steps") or []
    for step in steps:
        step_id = step["step_id"]
        prompt_file = step.get("prompt_file", "Unknown Prompt")
        lines.append(
            f'    {step_id}["{step_id}<br/><small>{prompt_file}</small>"]'
        )

    # --- Edges (data flow) ---
    for step in steps:
        step_id = step["step_id"]
        map_inputs = step.get("map_inputs") or {}
        for input_var, source_string in map_inputs.items():
            for source_type, source_name in VAR_PATTERN.findall(
                str(source_string)
            ):
                clean_source = source_name.replace(".output", "")
                if source_type == "inputs.":
                    lines.append(
                        f"    inp_{clean_source} -->|{input_var}| {step_id}"
                    )
                elif source_type == "steps.":
                    lines.append(
                        f"    {clean_source} -->|{input_var}| {step_id}"
                    )

    lines.append("```")
    return "\n".join(lines)


def main(root: Path | None = None) -> int:
    """Generate a companion .md diagram for every workflow file."""
    print("Generating Workflow Diagrams...")
    count = 0

    for workflow_file in iter_workflow_files(root) if root else iter_workflow_files():
        data = load_yaml(workflow_file)
        if not data:
            continue

        diagram = generate_mermaid_for_workflow(data)

        readme_path = workflow_file.with_suffix(".md")
        content = f"# {data.get('name', 'Workflow')}\n\n"
        content += f"{data.get('description', '')}\n\n"
        content += "## Visual Flow\n\n"
        content += diagram + "\n"

        readme_path.write_text(content, encoding="utf-8")
        print(f"  ✓ {workflow_file.name} → {readme_path.name}")
        count += 1

    print(f"\nGenerated {count} diagram(s).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
