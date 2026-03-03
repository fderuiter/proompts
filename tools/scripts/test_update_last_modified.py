import unittest
from unittest.mock import patch
from pathlib import Path
import io
import sys
import tempfile

# Add the current directory to sys.path to import update_file
sys.path.append(str(Path(__file__).parent))

# Mock yaml before importing anything that might use it
sys.modules['yaml'] = unittest.mock.MagicMock()
from update_last_modified import update_file

class TestUpdateLastModified(unittest.TestCase):
    @patch("pathlib.Path.read_text")
    @patch("sys.stdout", new_callable=io.StringIO)
    def test_update_file_read_error(self, mock_stdout, mock_read_text):
        """Test update_file returns False and logs an error when reading fails."""
        mock_read_text.side_effect = Exception("Mocked read error")
        test_path = Path("some_file.yaml")
        result = update_file(test_path)
        self.assertFalse(result)
        self.assertIn(f"Error reading {test_path}: Mocked read error", mock_stdout.getvalue())

    def test_update_file_updates_existing(self):
        """Test update_file correctly updates an existing last_modified field."""
        with tempfile.NamedTemporaryFile(mode='w+', delete=False) as tmp:
            tmp.write("name: test\nlast_modified: 2023-01-01T00:00:00Z\nother: field")
            tmp_path = Path(tmp.name)

        try:
            result = update_file(tmp_path)
            self.assertTrue(result)

            content = tmp_path.read_text()
            self.assertIn("last_modified:", content)
            self.assertNotIn("2023-01-01T00:00:00Z", content)
            self.assertIn("name: test", content)
            self.assertIn("other: field", content)
        finally:
            tmp_path.unlink()

    def test_update_file_adds_after_name(self):
        """Test update_file adds last_modified field immediately after name:."""
        with tempfile.NamedTemporaryFile(mode='w+', delete=False) as tmp:
            tmp.write("name: test-prompt\ndescription: test")
            tmp_path = Path(tmp.name)

        try:
            result = update_file(tmp_path)
            self.assertTrue(result)

            content = tmp_path.read_text()
            lines = content.splitlines()
            self.assertEqual(lines[0], "name: test-prompt")
            self.assertTrue(lines[1].startswith("last_modified:"))
            self.assertEqual(lines[2], "description: test")
        finally:
            tmp_path.unlink()

    def test_update_file_adds_at_top(self):
        """Test update_file adds last_modified field at top if name: is missing."""
        # Scenario 1: No name, no markers
        with tempfile.NamedTemporaryFile(mode='w+', delete=False) as tmp:
            tmp.write("description: test")
            tmp_path = Path(tmp.name)
        try:
            result = update_file(tmp_path)
            self.assertTrue(result)
            content = tmp_path.read_text()
            self.assertTrue(content.startswith("last_modified:"))
        finally:
            tmp_path.unlink()

        # Scenario 2: With --- marker
        with tempfile.NamedTemporaryFile(mode='w+', delete=False) as tmp:
            tmp.write("---\ndescription: test")
            tmp_path = Path(tmp.name)
        try:
            result = update_file(tmp_path)
            self.assertTrue(result)
            content = tmp_path.read_text()
            lines = content.splitlines()
            self.assertEqual(lines[0], "---")
            self.assertTrue(lines[1].startswith("last_modified:"))
        finally:
            tmp_path.unlink()

    def test_update_file_check_mode(self):
        """Test check mode does not write changes but identifies them."""
        initial_content = "name: test\ndescription: test"
        with tempfile.NamedTemporaryFile(mode='w+', delete=False) as tmp:
            tmp.write(initial_content)
            tmp_path = Path(tmp.name)
        try:
            result = update_file(tmp_path, check=True)
            self.assertTrue(result)
            content = tmp_path.read_text()
            self.assertEqual(content, initial_content)
        finally:
            tmp_path.unlink()

if __name__ == "__main__":
    unittest.main()
