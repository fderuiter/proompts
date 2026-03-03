import unittest
import sys
from pathlib import Path

# Add the tools/scripts directory to sys.path
sys.path.append(str(Path(__file__).parent))
from migrate_prompts import extract_template_vars

class TestExtractTemplateVars(unittest.TestCase):
    def test_extract_template_vars(self):
        """Test extraction of simple template variables."""
        content = {
            "messages": [
                {"content": "Hello {{name}}, welcome to {{place}}!"},
                {"content": "This is a {{test}} message."},
                {"content": "No variables here."},
                {"role": "user", "content": "Another {{name}} test."}
            ]
        }
        expected = ["name", "place", "test"]
        result = extract_template_vars(content)
        self.assertEqual(result, expected)

    def test_no_messages(self):
        """Test with content lacking 'messages' key."""
        content = {"other_key": "value"}
        expected = []
        result = extract_template_vars(content)
        self.assertEqual(result, expected)

    def test_empty_messages(self):
        """Test with empty 'messages' list."""
        content = {"messages": []}
        expected = []
        result = extract_template_vars(content)
        self.assertEqual(result, expected)

    def test_messages_without_content(self):
        """Test with messages that don't have a 'content' key."""
        content = {
            "messages": [
                {"role": "system"},
                {"role": "user", "text": "Hello {{name}}"} # not 'content' key
            ]
        }
        expected = []
        result = extract_template_vars(content)
        self.assertEqual(result, expected)

    def test_duplicate_variables(self):
        """Test that duplicate variables are deduplicated."""
        content = {
            "messages": [
                {"content": "Hello {{name}}, your name is {{name}}!"}
            ]
        }
        expected = ["name"]
        result = extract_template_vars(content)
        self.assertEqual(result, expected)

    def test_variables_with_spaces_inside(self):
        """Test variables with spaces inside the curly braces."""
        content = {
            "messages": [
                {"content": "Hello {{ name }}, welcome to {{  place  }}!"}
            ]
        }
        expected = ["  place  ", " name "]
        result = extract_template_vars(content)
        self.assertEqual(result, expected)

    def test_incomplete_variables(self):
        """Test that incomplete/malformed variable syntax is ignored."""
        content = {
            "messages": [
                {"content": "Hello {{name}, welcome to {place}}!"},
                {"content": "This is {test}."}
            ]
        }
        expected = []
        result = extract_template_vars(content)
        self.assertEqual(result, expected)

    def test_empty_content(self):
        """Test with empty string as content."""
        content = {
            "messages": [
                {"content": ""}
            ]
        }
        expected = []
        result = extract_template_vars(content)
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
