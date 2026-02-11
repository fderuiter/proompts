import unittest
import sys
import os
from unittest.mock import patch, MagicMock

# Add the directory containing run_workflow.py to the system path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from run_workflow import resolve_value

class TestResolveValue(unittest.TestCase):

    def test_simple_substitution(self):
        """Test simple variable substitution."""
        state = {"var": "value"}
        result = resolve_value("{{ var }}", state)
        self.assertEqual(result, "value")

    def test_nested_access(self):
        """Test accessing nested dictionary values."""
        state = {"steps": {"step1": {"output": "result"}}}
        result = resolve_value("{{ steps.step1.output }}", state)
        self.assertEqual(result, "result")

    def test_python_expression(self):
        """Test evaluation of Python expressions."""
        state = {}
        result = resolve_value("{{ 1 + 1 }}", state)
        self.assertEqual(result, 2)

    def test_string_without_template(self):
        """Test string with no template markers returned as is."""
        state = {}
        result = resolve_value("just a string", state)
        self.assertEqual(result, "just a string")

    def test_non_string_input(self):
        """Test non-string input is returned as is."""
        state = {}
        result = resolve_value(123, state)
        self.assertEqual(result, 123)
        result = resolve_value({"key": "value"}, state)
        self.assertEqual(result, {"key": "value"})

    def test_invalid_template(self):
        """Test invalid template returns original string (and logs warning)."""
        state = {}
        # Invalid syntax in jinja2
        result = resolve_value("{{ 1 + }}", state)
        self.assertEqual(result, "{{ 1 + }}")

    def test_type_preservation(self):
        """Test that native types are preserved."""
        state = {"val": 42}
        result = resolve_value("{{ val }}", state)
        self.assertIsInstance(result, int)
        self.assertEqual(result, 42)

        state = {"val": [1, 2, 3]}
        result = resolve_value("{{ val }}", state)
        self.assertIsInstance(result, list)
        self.assertEqual(result, [1, 2, 3])

    def test_partial_string_substitution(self):
        """Test substitution within a larger string."""
        state = {"name": "World"}
        result = resolve_value("Hello, {{ name }}!", state)
        self.assertEqual(result, "Hello, World!")

if __name__ == "__main__":
    unittest.main()
