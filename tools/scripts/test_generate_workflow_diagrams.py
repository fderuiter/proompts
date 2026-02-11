"""Tests for generate_workflow_diagrams.py."""

from __future__ import annotations

import sys
import tempfile
import unittest
from pathlib import Path

sys.path.append(str(Path(__file__).parent))
from generate_workflow_diagrams import generate_mermaid_for_workflow, main


class TestGenerateMermaid(unittest.TestCase):
    """Unit tests for the Mermaid generation function."""

    def test_inputs_only(self):
        """Steps that only reference global inputs."""
        data = {
            "inputs": [
                {"name": "revenue"},
                {"name": "costs"},
            ],
            "steps": [
                {
                    "step_id": "forecast",
                    "prompt_file": "p/forecast.prompt.yaml",
                    "map_inputs": {
                        "revenue": "{{inputs.revenue}}",
                        "costs": "{{inputs.costs}}",
                    },
                }
            ],
        }
        result = generate_mermaid_for_workflow(data)
        self.assertIn("inp_revenue((revenue))", result)
        self.assertIn("inp_costs((costs))", result)
        self.assertIn("inp_revenue -->|revenue| forecast", result)
        self.assertIn("inp_costs -->|costs| forecast", result)

    def test_inter_step_dependency(self):
        """Steps that reference outputs of previous steps."""
        data = {
            "inputs": [{"name": "idea"}],
            "steps": [
                {
                    "step_id": "step_a",
                    "prompt_file": "a.prompt.yaml",
                    "map_inputs": {"idea": "{{inputs.idea}}"},
                },
                {
                    "step_id": "step_b",
                    "prompt_file": "b.prompt.yaml",
                    "map_inputs": {
                        "prev_output": "{{steps.step_a.output}}"
                    },
                },
            ],
        }
        result = generate_mermaid_for_workflow(data)
        self.assertIn("step_a -->|prev_output| step_b", result)

    def test_no_inputs(self):
        """Workflow with no global inputs section."""
        data = {
            "steps": [
                {
                    "step_id": "only_step",
                    "prompt_file": "x.prompt.yaml",
                }
            ]
        }
        result = generate_mermaid_for_workflow(data)
        self.assertNotIn("subgraph", result)
        self.assertIn("only_step", result)

    def test_no_map_inputs(self):
        """Step without map_inputs should still produce a node."""
        data = {
            "inputs": [{"name": "x"}],
            "steps": [
                {
                    "step_id": "lonely",
                    "prompt_file": "lone.prompt.yaml",
                }
            ],
        }
        result = generate_mermaid_for_workflow(data)
        self.assertIn("lonely", result)
        # No edges expected
        self.assertNotIn("-->", result)

    def test_mermaid_block_fences(self):
        """Output is wrapped in mermaid code fences."""
        data = {"steps": [{"step_id": "s", "prompt_file": "p.yaml"}]}
        result = generate_mermaid_for_workflow(data)
        self.assertTrue(result.startswith("```mermaid"))
        self.assertTrue(result.endswith("```"))


class TestMainIntegration(unittest.TestCase):
    """Integration test for the main() entry point."""

    def test_generates_md_files(self):
        """main() should create .md files next to .workflow.yaml files."""
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            wf = root / "demo.workflow.yaml"
            wf.write_text(
                'name: Demo\n'
                'description: A demo workflow.\n'
                'inputs:\n'
                '  - name: x\n'
                'steps:\n'
                '  - step_id: s1\n'
                '    prompt_file: p.yaml\n'
                '    map_inputs:\n'
                '      x: "{{inputs.x}}"\n',
                encoding="utf-8",
            )

            main(root=root)

            md = root / "demo.workflow.md"
            self.assertTrue(md.exists(), f"{md} was not created")
            content = md.read_text(encoding="utf-8")
            self.assertIn("# Demo", content)
            self.assertIn("```mermaid", content)
            self.assertIn("inp_x -->|x| s1", content)


if __name__ == "__main__":
    unittest.main()
