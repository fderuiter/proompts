import unittest
import os
import sys
import yaml
import shutil
from run_workflow import resolve_value, run_workflow

# Mock workflow state
WORKFLOW_STATE = {
    "inputs": {
        "simple": "value",
        "nested": {"key": "nested_value"},
        "list": ["item1", "item2"],
        "list_dicts": [{"name": "obj1", "val": 10}, {"name": "obj2", "val": 20}]
    },
    "steps": {
        "step1": {"output": "step1_output"}
    }
}

class TestWorkflowResolutions(unittest.TestCase):
    def test_basic_substitution(self):
        # Should work with both old and new (if syntax matches)
        # Old syntax: {{inputs.simple}}
        # New syntax: {{inputs.simple}}
        self.assertEqual(resolve_value("{{inputs.simple}}", WORKFLOW_STATE), "value")

    def test_nested_substitution(self):
        # Old syntax: {{inputs.nested.key}}
        # New syntax: {{inputs.nested.key}}
        self.assertEqual(resolve_value("{{inputs.nested.key}}", WORKFLOW_STATE), "nested_value")

    def test_list_index(self):
        # This requires Jinja2. Old implementation doesn't support [0]
        # Expected: item1
        result = resolve_value("{{inputs.list[0]}}", WORKFLOW_STATE)
        self.assertEqual(result, "item1")

    def test_jinja2_filter(self):
        # This requires Jinja2.
        # Expected: VALUE
        result = resolve_value("{{inputs.simple | upper}}", WORKFLOW_STATE)
        self.assertEqual(result, "VALUE")

    def test_step_output(self):
        self.assertEqual(resolve_value("{{steps.step1.output}}", WORKFLOW_STATE), "step1_output")

    def test_list_dict_access(self):
        # Testing specific index access
        self.assertEqual(resolve_value("{{inputs.list_dicts[1].val}}", WORKFLOW_STATE), 20)

if __name__ == "__main__":
    unittest.main()
