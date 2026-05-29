import unittest
from unittest.mock import patch, MagicMock
from pathlib import Path
import sys

# Add the current directory to sys.path to import generate_overviews
sys.path.append(str(Path(__file__).parent))
from generate_overviews import get_prompt_metadata

class TestGetPromptMetadata(unittest.TestCase):
    @patch("generate_overviews.load_yaml")
    def test_metadata_from_yaml_name(self, mock_load_yaml):
        """Test metadata extraction when 'name' is present in YAML."""
        mock_load_yaml.return_value = {"name": "Test Name", "description": "A test description."}
        path = Path("path/to/test.prompt.yaml")
        self.assertEqual(get_prompt_metadata(path), ("Test Name", "A test description."))

    @patch("generate_overviews.load_yaml")
    def test_metadata_from_yaml_title(self, mock_load_yaml):
        """Test metadata extraction when 'title' is present but 'name' is missing."""
        mock_load_yaml.return_value = {"title": "Test Title", "description": "Another description."}
        path = Path("path/to/test.prompt.yaml")
        self.assertEqual(get_prompt_metadata(path), ("Test Title", "Another description."))

    @patch("generate_overviews.load_yaml")
    def test_title_priority(self, mock_load_yaml):
        """Test that 'name' takes precedence over 'title'."""
        mock_load_yaml.return_value = {"name": "Priority Name", "title": "Secondary Title", "description": "Desc"}
        path = Path("path/to/test.prompt.yaml")
        self.assertEqual(get_prompt_metadata(path), ("Priority Name", "Desc"))

    @patch("generate_overviews.load_yaml")
    def test_fallback_filename_basic(self, mock_load_yaml):
        """Test fallback to filename when YAML has no name/title."""
        mock_load_yaml.return_value = {}
        path = Path("path/to/my_prompt.prompt.yaml")
        self.assertEqual(get_prompt_metadata(path), ("My Prompt", ""))

    @patch("generate_overviews.load_yaml")
    def test_fallback_filename_numbered(self, mock_load_yaml):
        """Test fallback to filename with numbered prefix."""
        mock_load_yaml.return_value = {}
        path = Path("path/to/01_numbered_prompt.prompt.yaml")
        self.assertEqual(get_prompt_metadata(path), ("Numbered Prompt", ""))

    @patch("generate_overviews.load_yaml")
    def test_fallback_filename_yml(self, mock_load_yaml):
        """Test fallback to filename with .yml extension."""
        mock_load_yaml.return_value = {}
        path = Path("path/to/another_prompt.prompt.yml")
        self.assertEqual(get_prompt_metadata(path), ("Another Prompt", ""))

    @patch("generate_overviews.load_yaml")
    def test_fallback_formatting(self, mock_load_yaml):
        """Test fallback formatting with underscores and capitalization."""
        mock_load_yaml.return_value = {}
        path = Path("path/to/complex_file_name_example.prompt.yaml")
        self.assertEqual(get_prompt_metadata(path), ("Complex File Name Example", ""))

    @patch("generate_overviews.load_yaml")
    def test_metadata_from_workflow(self, mock_load_yaml):
        """Test metadata extraction from .workflow.yaml file."""
        mock_load_yaml.return_value = {"name": "My Workflow", "description": "Workflow desc"}
        path = Path("path/to/my_workflow.workflow.yaml")
        self.assertEqual(get_prompt_metadata(path), ("My Workflow", "Workflow desc"))

    @patch("generate_overviews.load_yaml")
    def test_fallback_workflow_filename(self, mock_load_yaml):
        """Test fallback to filename for .workflow.yaml files."""
        mock_load_yaml.return_value = {}
        path = Path("path/to/complex_workflow.workflow.yaml")
        self.assertEqual(get_prompt_metadata(path), ("Complex Workflow", ""))

if __name__ == "__main__":
    unittest.main()
