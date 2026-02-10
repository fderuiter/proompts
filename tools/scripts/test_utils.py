import unittest
from unittest.mock import patch
from pathlib import Path
import io
import sys

# Add the current directory to sys.path to import utils
sys.path.append(str(Path(__file__).parent))
from utils import load_yaml

class TestUtils(unittest.TestCase):
    @patch("utils.Path.read_text")
    def test_load_yaml_success(self, mock_read_text):
        """Test load_yaml with valid YAML content."""
        mock_read_text.return_value = "name: test\nvalue: 123"
        result = load_yaml(Path("test.yaml"))
        self.assertEqual(result, {"name": "test", "value": 123})

    @patch("utils.Path.read_text")
    @patch("sys.stdout", new_callable=io.StringIO)
    def test_load_yaml_file_not_found(self, mock_stdout, mock_read_text):
        """Test load_yaml with a non-existent file."""
        mock_read_text.side_effect = FileNotFoundError("File not found")
        result = load_yaml(Path("missing.yaml"))
        self.assertEqual(result, {})
        self.assertIn("Error reading missing.yaml", mock_stdout.getvalue())

    @patch("utils.Path.read_text")
    @patch("sys.stdout", new_callable=io.StringIO)
    def test_load_yaml_invalid_yaml(self, mock_stdout, mock_read_text):
        """Test load_yaml with invalid YAML syntax."""
        mock_read_text.return_value = "name: [invalid"
        result = load_yaml(Path("invalid.yaml"))
        self.assertEqual(result, {})
        self.assertIn("Error reading invalid.yaml", mock_stdout.getvalue())

if __name__ == "__main__":
    unittest.main()
