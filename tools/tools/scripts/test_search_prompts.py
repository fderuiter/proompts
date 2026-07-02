import unittest
import io
from unittest.mock import patch
from pathlib import Path
from promptops.utils import ROOT

from promptops.cli import search_prompts_func as search

def create_valid_mock_prompt(name, description):
    return {
        'name': name,
        'description': description,
        'version': '0.1.0',
        'metadata': {'domain': 'test', 'complexity': 'low', 'tags': [], 'requires_context': False},
        'variables': [],
        'model': 'test-model',
        'modelParameters': {'temperature': 0.7},
        'messages': [{'role': 'user', 'content': 'test content'}, {'role': 'system', 'content': 'system'}],
        'testData': ['test'],
        'evaluators': [{'python': 'test'}]
    }

class TestSearchPrompts(unittest.TestCase):

    @patch('promptops.cli.load_yaml')
    @patch('promptops.cli.iter_prompt_files')
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_search_match_name(self, mock_stdout, mock_iter, mock_load):
        mock_iter.return_value = [ROOT / 'prompts/test/fake1.yaml']
        mock_load.return_value = create_valid_mock_prompt('Test Prompt', 'A prompt for testing')
        search('test')
        output = mock_stdout.getvalue()
        self.assertIn("Match: Test Prompt", output)

    @patch('promptops.cli.load_yaml')
    @patch('promptops.cli.iter_prompt_files')
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_search_match_description(self, mock_stdout, mock_iter, mock_load):
        mock_iter.return_value = [ROOT / 'prompts/test/fake1.yaml']
        mock_load.return_value = create_valid_mock_prompt('Other Prompt', 'A prompt for testing')
        search('test')
        output = mock_stdout.getvalue()
        self.assertIn("Match: Other Prompt", output)

    @patch('promptops.cli.load_yaml')
    @patch('promptops.cli.iter_prompt_files')
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_search_no_match(self, mock_stdout, mock_iter, mock_load):
        mock_iter.return_value = [ROOT / 'prompts/test/fake1.yaml']
        mock_load.return_value = create_valid_mock_prompt('Other Prompt', 'A prompt for testing')
        search('xyz123')
        output = mock_stdout.getvalue()
        self.assertIn("No prompts found matching 'xyz123'", output)

    @patch('promptops.cli.load_yaml')
    @patch('promptops.cli.iter_prompt_files')
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_search_verbose(self, mock_stdout, mock_iter, mock_load):
        mock_iter.return_value = [ROOT / 'prompts/test/fake1.yaml']
        mock_load.return_value = create_valid_mock_prompt('Test Prompt', 'A prompt for testing')
        search('test', verbose=True)
        output = mock_stdout.getvalue()
        self.assertIn("Match: Test Prompt", output)
        self.assertIn("Description: A prompt for testing", output)

    @patch('promptops.cli.load_yaml')
    @patch('promptops.cli.iter_prompt_files')
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_search_multiple_matches(self, mock_stdout, mock_iter, mock_load):
        mock_iter.return_value = [
            ROOT / 'prompts/test/fake1.yaml',
            ROOT / 'prompts/test/fake2.yaml',
            ROOT / 'prompts/test/fake3.yaml'
        ]

        def load_yaml_side_effect(path):
            if path == ROOT / 'prompts/test/fake1.yaml':
                return create_valid_mock_prompt('Test Prompt 1', 'desc 1')
            elif path == ROOT / 'prompts/test/fake2.yaml':
                return create_valid_mock_prompt('Other', 'desc 2')
            elif path == ROOT / 'prompts/test/fake3.yaml':
                return create_valid_mock_prompt('Prompt 3', 'test desc 3')
            return {}

        mock_load.side_effect = load_yaml_side_effect
        search('test')
        output = mock_stdout.getvalue()
        self.assertIn("Match: Test Prompt 1", output)
        self.assertIn("Match: Prompt 3", output)
        self.assertNotIn("Match: Other", output)

if __name__ == '__main__':
    unittest.main()
