import unittest
from unittest.mock import patch, MagicMock
from pathlib import Path
import sys

# Add the current directory to sys.path to import generate_overviews
sys.path.append(str(Path(__file__).parent))
from generate_overviews import title_from_prompt

class TestTitleFromPrompt(unittest.TestCase):
    @patch("generate_overviews.load_yaml")
    def test_title_from_yaml_name(self, mock_load_yaml):
        """Test title extraction when 'name' is present in YAML."""
        mock_load_yaml.return_value = {"name": "Test Name", "description": "desc"}
        path = Path("path/to/test.prompt.yaml")
        self.assertEqual(title_from_prompt(path), "Test Name")

    @patch("generate_overviews.load_yaml")
    def test_title_from_yaml_title(self, mock_load_yaml):
        """Test title extraction when 'title' is present but 'name' is missing."""
        mock_load_yaml.return_value = {"title": "Test Title", "description": "desc"}
        path = Path("path/to/test.prompt.yaml")
        self.assertEqual(title_from_prompt(path), "Test Title")

    @patch("generate_overviews.load_yaml")
    def test_title_priority(self, mock_load_yaml):
        """Test that 'name' takes precedence over 'title'."""
        mock_load_yaml.return_value = {"name": "Priority Name", "title": "Secondary Title"}
        path = Path("path/to/test.prompt.yaml")
        self.assertEqual(title_from_prompt(path), "Priority Name")

    @patch("generate_overviews.load_yaml")
    def test_fallback_filename_basic(self, mock_load_yaml):
        """Test fallback to filename when YAML has no name/title."""
        mock_load_yaml.return_value = {}
        path = Path("path/to/my_prompt.prompt.yaml")
        self.assertEqual(title_from_prompt(path), "My Prompt")

    @patch("generate_overviews.load_yaml")
    def test_fallback_filename_numbered(self, mock_load_yaml):
        """Test fallback to filename with numbered prefix."""
        mock_load_yaml.return_value = {}
        path = Path("path/to/01_numbered_prompt.prompt.yaml")
        self.assertEqual(title_from_prompt(path), "Numbered Prompt")

    @patch("generate_overviews.load_yaml")
    def test_fallback_filename_yml(self, mock_load_yaml):
        """Test fallback to filename with .yml extension."""
        mock_load_yaml.return_value = {}
        path = Path("path/to/another_prompt.prompt.yml")
        self.assertEqual(title_from_prompt(path), "Another Prompt")

    @patch("generate_overviews.load_yaml")
    def test_fallback_formatting(self, mock_load_yaml):
        """Test fallback formatting with underscores and capitalization."""
        mock_load_yaml.return_value = {}
        path = Path("path/to/complex_file_name_example.prompt.yaml")
        self.assertEqual(title_from_prompt(path), "Complex File Name Example")

    @patch("generate_overviews.load_yaml")
    def test_title_from_workflow(self, mock_load_yaml):
        """Test title extraction from .workflow.yaml file."""
        mock_load_yaml.return_value = {"name": "My Workflow"}
        path = Path("path/to/my_workflow.workflow.yaml")
        self.assertEqual(title_from_prompt(path), "My Workflow")

    @patch("generate_overviews.load_yaml")
    def test_fallback_workflow_filename(self, mock_load_yaml):
        """Test fallback to filename for .workflow.yaml files."""
        mock_load_yaml.return_value = {}
        path = Path("path/to/complex_workflow.workflow.yaml")
        self.assertEqual(title_from_prompt(path), "Complex Workflow")

if __name__ == "__main__":
    unittest.main()
