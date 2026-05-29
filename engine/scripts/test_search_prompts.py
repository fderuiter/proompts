import unittest
from unittest.mock import patch, MagicMock
from pathlib import Path
import io
import sys

# Mock yaml before importing utils and search_prompts
sys.modules['yaml'] = MagicMock()

# Add the current directory to sys.path to import search_prompts
sys.path.append(str(Path(__file__).parent))
from search_prompts import search

# We need to provide paths that are relative to the actual ROOT
# used in search_prompts. ROOT is usually /app if we are in this container
from utils import ROOT

class TestSearchPrompts(unittest.TestCase):
    @patch('search_prompts.load_yaml')
    @patch('search_prompts.iter_prompt_files')
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_search_match_name(self, mock_stdout, mock_iter, mock_load):
        mock_iter.return_value = [ROOT / 'prompts/test/fake1.yaml']
        mock_load.return_value = {
            'name': 'Test Prompt',
            'description': 'A prompt for testing'
        }

        search('test')

        output = mock_stdout.getvalue()
        self.assertIn("Match: Test Prompt", output)
        self.assertNotIn("Description:", output)
        self.assertNotIn("No prompts found", output)

    @patch('search_prompts.load_yaml')
    @patch('search_prompts.iter_prompt_files')
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_search_match_description(self, mock_stdout, mock_iter, mock_load):
        mock_iter.return_value = [ROOT / 'prompts/test/fake1.yaml']
        mock_load.return_value = {
            'name': 'Other Prompt',
            'description': 'A prompt for testing'
        }

        search('test')

        output = mock_stdout.getvalue()
        self.assertIn("Match: Other Prompt", output)
        self.assertNotIn("Description:", output)
        self.assertNotIn("No prompts found", output)

    @patch('search_prompts.load_yaml')
    @patch('search_prompts.iter_prompt_files')
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_search_no_match(self, mock_stdout, mock_iter, mock_load):
        mock_iter.return_value = [ROOT / 'prompts/test/fake1.yaml']
        mock_load.return_value = {
            'name': 'Other Prompt',
            'description': 'A prompt for something else'
        }

        search('test')

        output = mock_stdout.getvalue()
        self.assertNotIn("Match:", output)
        self.assertIn("No prompts found matching 'test'.", output)

    @patch('search_prompts.load_yaml')
    @patch('search_prompts.iter_prompt_files')
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_search_verbose(self, mock_stdout, mock_iter, mock_load):
        mock_iter.return_value = [ROOT / 'prompts/test/fake1.yaml']
        mock_load.return_value = {
            'name': 'Test Prompt',
            'description': 'A prompt for testing'
        }

        search('test', verbose=True)

        output = mock_stdout.getvalue()
        self.assertIn("Match: Test Prompt", output)
        self.assertIn("Description: A prompt for testing", output)

    @patch('search_prompts.load_yaml')
    @patch('search_prompts.iter_prompt_files')
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_search_multiple_matches(self, mock_stdout, mock_iter, mock_load):
        mock_iter.return_value = [
            ROOT / 'prompts/test/fake1.yaml',
            ROOT / 'prompts/test/fake2.yaml',
            ROOT / 'prompts/test/fake3.yaml'
        ]

        # We match on fake1 and fake3
        def load_yaml_side_effect(path):
            if path == ROOT / 'prompts/test/fake1.yaml':
                return {'name': 'Test Prompt 1', 'description': 'desc 1'}
            elif path == ROOT / 'prompts/test/fake2.yaml':
                return {'name': 'Other', 'description': 'desc 2'}
            elif path == ROOT / 'prompts/test/fake3.yaml':
                return {'name': 'Prompt 3', 'description': 'test desc 3'}
            return {}

        mock_load.side_effect = load_yaml_side_effect

        search('test')

        output = mock_stdout.getvalue()
        self.assertIn("Match: Test Prompt 1", output)
        self.assertNotIn("Match: Other", output)
        self.assertIn("Match: Prompt 3", output)
        self.assertNotIn("Description:", output)
        self.assertNotIn("No prompts found", output)

if __name__ == "__main__":
    unittest.main()
