import unittest
from pathlib import Path
import sys
import os
from unittest.mock import MagicMock, patch

# Add the current directory to sys.path to import generate_docs
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from generate_docs import DocumentationGenerator, CONFIG

class TestRenderWorkflow(unittest.TestCase):
    def setUp(self):
        # Create a dummy DocumentationGenerator instance
        self.root = Path("/tmp/mock_root")
        self.gen = DocumentationGenerator(self.root)

    def test_render_workflow_with_mermaid(self):
        # Mock data with mermaid content
        data = {
            'name': 'Test Workflow',
            'description': 'A test workflow.',
            'steps': [
                {'step_id': 'step1', 'map_inputs': {'input1': 'inputs.foo'}}
            ],
            'inputs': [{'name': 'foo'}]
        }

        source_path = Path("workflows/test.workflow.yaml")

        # We need to mock CONFIG['dirs']['workflow_docs'] used in _render_workflow_page
        # Since CONFIG is a global constant, we might need to patch it or ensure it works.
        # CONFIG uses relative paths, so self.root / CONFIG... works.

        # We don't want to actually write files, so we'll mock path methods
        with patch('pathlib.Path.write_text') as mock_write:
            # Also mock relative_to/relpath calls if needed, but Path operations should be fine
            # except for actual IO.

            # The method uses os.path.relpath which might fail if paths don't exist?
            # os.path.relpath calculates relative path string, doesn't check existence.

            output_path, changed = self.gen._render_workflow_page(source_path, data, check_mode=False)

            # Verify write_text was called with expected content
            args, _ = mock_write.call_args
            content = args[0]

            self.assertIn("# Test Workflow", content)
            self.assertIn("## Workflow Diagram", content)
            self.assertIn("```mermaid", content)
            self.assertIn("graph TD", content)
            self.assertIn("Input_foo", content)

    def test_render_workflow_without_mermaid(self):
        # Mock data without steps/inputs -> no mermaid
        data = {
            'name': 'Simple Workflow',
            'description': 'No diagram needed.'
        }

        source_path = Path("workflows/simple.workflow.yaml")

        with patch('pathlib.Path.write_text') as mock_write:
            output_path, changed = self.gen._render_workflow_page(source_path, data, check_mode=False)

            args, _ = mock_write.call_args
            content = args[0]

            self.assertIn("# Simple Workflow", content)
            self.assertNotIn("## Workflow Diagram", content)
            self.assertNotIn("```mermaid", content)

if __name__ == "__main__":
    unittest.main()
