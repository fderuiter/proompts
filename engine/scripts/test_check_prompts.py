import unittest
import tempfile
import sys
import io
from unittest.mock import patch, MagicMock
from pathlib import Path

# Remove the global yaml mock

# Add the current directory to sys.path to import check_prompts and utils
sys.path.append(str(Path(__file__).parent))

from check_prompts import (
    check_overview,
    check_directory_contents,
    check_prompt_file,
    main,
    NAMING_RULES
)
from utils import OVERVIEW_NAME

class TestCheckPrompts(unittest.TestCase):

    def test_check_overview_exists(self):
        """Test check_overview when OVERVIEW_NAME exists."""
        with tempfile.TemporaryDirectory() as temp_dir:
            dir_path = Path(temp_dir)
            # Create OVERVIEW_NAME file
            (dir_path / OVERVIEW_NAME).touch()

            result = check_overview(dir_path)
            self.assertTrue(result)

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_check_overview_missing(self, mock_stdout):
        """Test check_overview when OVERVIEW_NAME is missing."""
        with tempfile.TemporaryDirectory() as temp_dir:
            dir_path = Path(temp_dir)
            # Do not create OVERVIEW_NAME file

            result = check_overview(dir_path)
            self.assertFalse(result)
            self.assertIn(f"Missing {OVERVIEW_NAME} in {dir_path}", mock_stdout.getvalue())

    def test_check_directory_contents_valid(self):
        """Test check_directory_contents with valid files."""
        with tempfile.TemporaryDirectory() as temp_dir:
            dir_path = Path(temp_dir)

            # Create valid files
            (dir_path / "test.prompt.yaml").touch()
            (dir_path / "test2.prompt.yml").touch()
            (dir_path / OVERVIEW_NAME).touch()
            (dir_path / "readme.md").touch()
            (dir_path / "README.MD").touch()

            # Create a hidden file which should be ignored
            (dir_path / ".hidden").touch()

            # Create a directory which should be ignored
            (dir_path / "subdir").mkdir()

            result = check_directory_contents(dir_path)
            self.assertTrue(result)

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_check_directory_contents_invalid(self, mock_stdout):
        """Test check_directory_contents with invalid files."""
        with tempfile.TemporaryDirectory() as temp_dir:
            dir_path = Path(temp_dir)

            # Create an invalid file
            invalid_file = dir_path / "invalid.txt"
            invalid_file.touch()

            result = check_directory_contents(dir_path)
            self.assertFalse(result)
            self.assertIn(f"{invalid_file} is not a recognised prompt or workflow file", mock_stdout.getvalue())

    @patch('check_prompts.load_yaml')
    def test_check_prompt_file_valid(self, mock_load_yaml):
        """Test check_prompt_file with a valid file."""
        mock_load_yaml.return_value = {"name": "test"}

        with tempfile.TemporaryDirectory() as temp_dir:
            dir_path = Path(temp_dir)
            file_path = dir_path / "test.prompt.yaml"
            file_path.touch()

            result = check_prompt_file(file_path)
            self.assertTrue(result)
            mock_load_yaml.assert_called_once_with(file_path)

    @patch("sys.stdout", new_callable=io.StringIO)
    @patch('check_prompts.load_yaml')
    def test_check_prompt_file_invalid_yaml(self, mock_load_yaml, mock_stdout):
        """Test check_prompt_file with invalid YAML content."""
        mock_load_yaml.return_value = {}  # load_yaml returns empty dict on failure

        with tempfile.TemporaryDirectory() as temp_dir:
            dir_path = Path(temp_dir)
            file_path = dir_path / "test.prompt.yaml"
            file_path.touch()

            result = check_prompt_file(file_path)
            self.assertFalse(result)
            self.assertIn(f"Failed to parse {file_path}", mock_stdout.getvalue())

    @patch('check_prompts.load_yaml')
    def test_check_prompt_file_meta_valid_name(self, mock_load_yaml):
        """Test check_prompt_file in meta directory with correct name."""
        mock_load_yaml.return_value = {"name": "test"}

        with tempfile.TemporaryDirectory() as temp_dir:
            base_dir = Path(temp_dir)
            meta_dir = base_dir / "meta"
            meta_dir.mkdir()

            file_path = meta_dir / "L01_test.prompt.yaml"
            file_path.touch()

            result = check_prompt_file(file_path)
            self.assertTrue(result)

    @patch("sys.stdout", new_callable=io.StringIO)
    @patch('check_prompts.load_yaml')
    def test_check_prompt_file_meta_invalid_name(self, mock_load_yaml, mock_stdout):
        """Test check_prompt_file in meta directory with incorrect name."""
        mock_load_yaml.return_value = {"name": "test"}

        with tempfile.TemporaryDirectory() as temp_dir:
            base_dir = Path(temp_dir)
            meta_dir = base_dir / "meta"
            meta_dir.mkdir()

            file_path = meta_dir / "invalid.prompt.yaml"
            file_path.touch()

            result = check_prompt_file(file_path)
            self.assertFalse(result)
            self.assertIn(f"{file_path} does not match required pattern for meta", mock_stdout.getvalue())

    @patch('check_prompts.check_directory_contents')
    @patch('check_prompts.check_overview')
    @patch('check_prompts.check_prompt_file')
    @patch('check_prompts.iter_workflow_files')
    @patch('check_prompts.iter_prompt_files')
    @patch('check_prompts.WORKFLOWS_DIR', new_callable=lambda: Path('/fake/workflows'))
    @patch('check_prompts.PROMPTS_DIR', new_callable=lambda: Path('/fake/prompts'))
    def test_main_success(self, mock_prompts_dir, mock_workflows_dir, mock_iter_prompts, mock_iter_workflows, mock_check_prompt, mock_check_overview, mock_check_dir):
        """Test main when all checks pass."""
        # Set up mock iter_prompt_files to yield a couple of files
        prompt1 = mock_prompts_dir / "dir1" / "test1.prompt.yaml"
        prompt2 = mock_prompts_dir / "dir2" / "test2.prompt.yaml"
        mock_iter_prompts.return_value = [prompt1, prompt2]

        workflow1 = mock_workflows_dir / "flow1" / "test1.workflow.yaml"
        mock_iter_workflows.return_value = [workflow1]

        # Make all checks pass
        mock_check_prompt.return_value = True
        mock_check_overview.return_value = True
        mock_check_dir.return_value = True

        result = main()

        self.assertEqual(result, 0)
        # 2 prompts + 1 workflow = 3
        self.assertEqual(mock_check_prompt.call_count, 3)
        # Should check dir1, dir2 and flow1
        self.assertEqual(mock_check_overview.call_count, 3)
        self.assertEqual(mock_check_dir.call_count, 3)

    @patch('check_prompts.check_directory_contents')
    @patch('check_prompts.check_overview')
    @patch('check_prompts.check_prompt_file')
    @patch('check_prompts.iter_prompt_files')
    @patch('check_prompts.PROMPTS_DIR', new_callable=lambda: Path('/fake/prompts'))
    def test_main_prompt_file_fails(self, mock_prompts_dir, mock_iter, mock_check_prompt, mock_check_overview, mock_check_dir):
        """Test main when check_prompt_file fails."""
        prompt1 = mock_prompts_dir / "dir1" / "test1.prompt.yaml"
        mock_iter.return_value = [prompt1]

        mock_check_prompt.return_value = False
        mock_check_overview.return_value = True
        mock_check_dir.return_value = True

        result = main()

        self.assertEqual(result, 1)

    @patch('check_prompts.check_directory_contents')
    @patch('check_prompts.check_overview')
    @patch('check_prompts.check_prompt_file')
    @patch('check_prompts.iter_prompt_files')
    @patch('check_prompts.PROMPTS_DIR', new_callable=lambda: Path('/fake/prompts'))
    def test_main_overview_fails(self, mock_prompts_dir, mock_iter, mock_check_prompt, mock_check_overview, mock_check_dir):
        """Test main when check_overview fails."""
        prompt1 = mock_prompts_dir / "dir1" / "test1.prompt.yaml"
        mock_iter.return_value = [prompt1]

        mock_check_prompt.return_value = True
        mock_check_overview.return_value = False
        mock_check_dir.return_value = True

        result = main()

        self.assertEqual(result, 1)

    @patch('check_prompts.check_directory_contents')
    @patch('check_prompts.check_overview')
    @patch('check_prompts.check_prompt_file')
    @patch('check_prompts.iter_prompt_files')
    @patch('check_prompts.PROMPTS_DIR', new_callable=lambda: Path('/fake/prompts'))
    def test_main_directory_contents_fails(self, mock_prompts_dir, mock_iter, mock_check_prompt, mock_check_overview, mock_check_dir):
        """Test main when check_directory_contents fails."""
        prompt1 = mock_prompts_dir / "dir1" / "test1.prompt.yaml"
        mock_iter.return_value = [prompt1]

        mock_check_prompt.return_value = True
        mock_check_overview.return_value = True
        mock_check_dir.return_value = False

        result = main()

        self.assertEqual(result, 1)

if __name__ == "__main__":
    unittest.main()
