import unittest
import json
import sys
import os
from unittest.mock import patch, mock_open, MagicMock
from pathlib import Path

# Add the current directory to sys.path to import generate_search_index
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from generate_search_index import generate_index

class TestGenerateSearchIndex(unittest.TestCase):
    @patch('generate_search_index.ROOT', new_callable=lambda: Path('/fake/root'))
    @patch('generate_search_index.iter_prompt_files')
    @patch('generate_search_index.load_yaml')
    @patch('builtins.open', new_callable=mock_open)
    @patch('generate_search_index.print')
    def test_generate_index_success(self, mock_print, mock_file, mock_load_yaml, mock_iter, mock_root):
        mock_iter.return_value = [
            Path('/fake/root/prompts/test1.prompt.yaml'),
            Path('/fake/root/prompts/test2.prompt.yaml')
        ]

        mock_load_yaml.side_effect = [
            {"name": "Test 1", "description": "Desc 1", "tags": ["tag1", "tag2"]},
            {"description": "Desc 2"} # Missing name and tags to test fallbacks
        ]

        generate_index("custom_search.json")

        # Verify iter_prompt_files called with ROOT
        mock_iter.assert_called_once_with(mock_root)

        # Verify file opened correctly
        mock_file.assert_called_once_with(mock_root / "custom_search.json", 'w', encoding='utf-8')

        # Get what was written
        written_content = "".join(call.args[0] for call in mock_file().write.call_args_list)
        data = json.loads(written_content)

        self.assertEqual(len(data), 2)

        self.assertEqual(data[0]["title"], "Test 1")
        self.assertEqual(data[0]["description"], "Desc 1")
        self.assertEqual(data[0]["tags"], "tag1, tag2")
        self.assertEqual(data[0]["url"], "prompts/test1.prompt.yaml")

        self.assertEqual(data[1]["title"], "prompts/test2.prompt.yaml")
        self.assertEqual(data[1]["description"], "Desc 2")
        self.assertEqual(data[1]["tags"], "")
        self.assertEqual(data[1]["url"], "prompts/test2.prompt.yaml")

        mock_print.assert_called_once()

    @patch('generate_search_index.ROOT', new_callable=lambda: Path('/fake/root'))
    @patch('generate_search_index.iter_prompt_files')
    @patch('generate_search_index.load_yaml')
    @patch('builtins.open', new_callable=mock_open)
    @patch('generate_search_index.print')
    def test_generate_index_value_error(self, mock_print, mock_file, mock_load_yaml, mock_iter, mock_root):
        # File not relative to ROOT
        mock_iter.return_value = [
            Path('/other/path/test.prompt.yaml')
        ]
        mock_load_yaml.return_value = {}

        generate_index()

        written_content = "".join(call.args[0] for call in mock_file().write.call_args_list)
        data = json.loads(written_content)

        # The ValueError should be caught and item skipped
        self.assertEqual(len(data), 0)
        mock_print.assert_called_once()

    @patch('generate_search_index.ROOT', new_callable=lambda: Path('/fake/root'))
    @patch('generate_search_index.iter_prompt_files')
    @patch('generate_search_index.load_yaml')
    @patch('builtins.open', new_callable=mock_open)
    @patch('generate_search_index.print')
    def test_generate_index_default_output(self, mock_print, mock_file, mock_load_yaml, mock_iter, mock_root):
        mock_iter.return_value = [
            Path('/fake/root/prompts/test.prompt.yaml')
        ]
        mock_load_yaml.return_value = {"name": "Test"}

        generate_index() # No args, should use default "search.json"

        mock_file.assert_called_once_with(mock_root / "search.json", 'w', encoding='utf-8')

if __name__ == '__main__':
    unittest.main()
