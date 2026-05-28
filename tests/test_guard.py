import unittest
import json
from unittest.mock import patch, MagicMock

import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))

from proompts_guard import guard, ProomptsValidationError

class TestProomptsGuard(unittest.TestCase):
    @patch("proompts_guard.middleware.load_yaml")
    @patch("proompts_guard.middleware.Path.exists")
    def test_valid_json_output(self, mock_exists, mock_load_yaml):
        mock_exists.return_value = True
        mock_load_yaml.return_value = {
            "name": "Test",
            "description": "Test",
            "model": "gpt-4",
            "modelParameters": {"temperature": 0.0},
            "messages": [{"role": "system", "content": "hello"}, {"role": "user", "content": "world"}],
            "testData": [],
            "evaluators": [],
            "output_schema": {
                "type": "object",
                "properties": {
                    "summary": {"type": "string"},
                    "score": {"type": "integer"}
                },
                "required": ["summary"]
            }
        }
        
        @guard(prompt_id="test_prompt")
        def mock_llm_call():
            return '{"summary": "A good summary", "score": 10}'
            
        result = mock_llm_call()
        self.assertEqual(result, '{"summary": "A good summary", "score": 10}')
        
    @patch("proompts_guard.middleware.load_yaml")
    @patch("proompts_guard.middleware.Path.exists")
    def test_missing_field(self, mock_exists, mock_load_yaml):
        mock_exists.return_value = True
        mock_load_yaml.return_value = {
            "name": "Test",
            "description": "Test",
            "model": "gpt-4",
            "modelParameters": {"temperature": 0.0},
            "messages": [{"role": "system", "content": "hello"}, {"role": "user", "content": "world"}],
            "testData": [],
            "evaluators": [],
            "output_schema": {
                "type": "object",
                "properties": {
                    "summary": {"type": "string"}
                },
                "required": ["summary"]
            }
        }
        
        @guard(prompt_id="test_prompt", mode="fail_fast")
        def mock_llm_call():
            return '{"not_summary": "A good summary"}'
            
        with self.assertRaises(ProomptsValidationError) as ctx:
            mock_llm_call()
        self.assertEqual(str(ctx.exception), "missing required field: 'summary'")

    @patch("proompts_guard.middleware.load_yaml")
    @patch("proompts_guard.middleware.Path.exists")
    def test_evaluator_failure(self, mock_exists, mock_load_yaml):
        mock_exists.return_value = True
        mock_load_yaml.return_value = {
            "name": "Test",
            "description": "Test",
            "model": "gpt-4",
            "modelParameters": {"temperature": 0.0},
            "messages": [{"role": "system", "content": "hello"}, {"role": "user", "content": "world"}],
            "testData": [],
            "evaluators": [
                {"name": "must contain hello", "python": "return 'hello' in output"}
            ]
        }
        
        @guard(prompt_id="test_prompt")
        def mock_llm_call():
            return 'world'
            
        with self.assertRaises(ProomptsValidationError) as ctx:
            mock_llm_call()
        self.assertIn("must contain hello", str(ctx.exception))

if __name__ == "__main__":
    unittest.main()
