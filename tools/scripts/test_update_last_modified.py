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


    @patch("update_last_modified.datetime")
    def test_update_file_no_change(self, mock_datetime):
        """Test update_file returns False when the last_modified timestamp is already up-to-date."""
        from datetime import datetime, timezone

        # Setup a fixed time
        fixed_time = datetime(2023, 10, 27, 12, 0, 0, tzinfo=timezone.utc)
        mock_datetime.now.return_value = fixed_time

        fixed_iso = "2023-10-27T12:00:00Z"

        initial_content = f"name: test\nlast_modified: {fixed_iso}\ndescription: test"

        with tempfile.NamedTemporaryFile(mode='w+', delete=False) as tmp:
            tmp.write(initial_content)
            tmp_path = Path(tmp.name)

        try:
            result = update_file(tmp_path)
            self.assertFalse(result)

            # File should not be modified
            content = tmp_path.read_text()
            self.assertEqual(content, initial_content)
        finally:
            tmp_path.unlink()


    @patch("update_last_modified.sys.argv", ["update_last_modified.py"])
    def test_main_no_files(self):
        """Test main() returns 0 when no files are provided."""
        from update_last_modified import main
        self.assertEqual(main(), 0)

    @patch("update_last_modified.sys.argv", ["update_last_modified.py", "mock_file.yaml"])
    @patch("update_last_modified.update_file", return_value=True)
    @patch("update_last_modified.Path.is_file", return_value=True)
    def test_main_with_files_updated(self, mock_is_file, mock_update_file):
        """Test main() returns 1 when valid files are updated."""
        from update_last_modified import main
        with patch("sys.stdout", new_callable=io.StringIO) as mock_stdout:
            self.assertEqual(main(), 1)
            self.assertIn("Updated last_modified in mock_file.yaml", mock_stdout.getvalue())

    @patch("update_last_modified.sys.argv", ["update_last_modified.py", "mock_file.yaml"])
    @patch("update_last_modified.update_file", return_value=False)
    @patch("update_last_modified.Path.is_file", return_value=True)
    def test_main_with_files_not_updated(self, mock_is_file, mock_update_file):
        """Test main() returns 0 when valid files are not updated (already up-to-date)."""
        from update_last_modified import main
        with patch("sys.stdout", new_callable=io.StringIO) as mock_stdout:
            self.assertEqual(main(), 0)
            self.assertEqual(mock_stdout.getvalue(), "")

    @patch("update_last_modified.sys.argv", ["update_last_modified.py", "--check", "mock_file.yaml"])
    @patch("update_last_modified.update_file", return_value=True)
    @patch("update_last_modified.Path.is_file", return_value=True)
    def test_main_check_mode(self, mock_is_file, mock_update_file):
        """Test main() properly handles the --check flag."""
        from update_last_modified import main
        with patch("sys.stdout", new_callable=io.StringIO) as mock_stdout:
            self.assertEqual(main(), 1)
            mock_update_file.assert_called_once_with(Path("mock_file.yaml"), check=True)
            self.assertIn("Updated last_modified in mock_file.yaml", mock_stdout.getvalue())

    @patch("update_last_modified.sys.argv", ["update_last_modified.py", "mock_file.txt"])
    @patch("update_last_modified.update_file")
    @patch("update_last_modified.Path.is_file", return_value=True)
    def test_main_ignores_non_yaml_files(self, mock_is_file, mock_update_file):
        """Test main() ignores files that do not end in .yaml or .yml."""
        from update_last_modified import main
        self.assertEqual(main(), 0)
        mock_update_file.assert_not_called()


if __name__ == "__main__":
    unittest.main()
