import unittest
import sys
from pathlib import Path
from pydantic import ValidationError

# Add the current directory to sys.path to import validate_prompt_schema
sys.path.append(str(Path(__file__).parent))

from validate_prompt_schema import PromptSchema, Message, ModelParameters

class TestPromptSchema(unittest.TestCase):
    def setUp(self):
        self.valid_data = {
            "name": "Test Prompt",
            "description": "A test prompt description",
            "model": "gpt-4",
            "modelParameters": {"temperature": 0.7},
            "messages": [
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": "Hello!"}
            ],
            "testData": [{"input": "Hello", "expected": "Hi"}],
            "evaluators": [{"type": "contains", "value": "Hi"}]
        }

    def test_valid_schema(self):
        """Test that a valid schema passes validation."""
        prompt = PromptSchema(**self.valid_data)
        self.assertEqual(prompt.name, "Test Prompt")
        self.assertEqual(len(prompt.messages), 2)
        self.assertEqual(prompt.modelParameters.temperature, 0.7)

    def test_missing_required_fields(self):
        """Test that missing required fields raises ValidationError."""
        required_fields = ["name", "description", "model", "modelParameters", "messages", "testData", "evaluators"]
        for field in required_fields:
            data = self.valid_data.copy()
            del data[field]
            with self.subTest(field=field):
                with self.assertRaises(ValidationError):
                    PromptSchema(**data)

    def test_messages_length_validation(self):
        """Test that messages list must have at least 2 items."""
        # Test with 0 messages
        data = self.valid_data.copy()
        data["messages"] = []
        with self.assertRaises(ValidationError) as cm:
            PromptSchema(**data)
        self.assertIn("messages list must have at least 2 items", str(cm.exception))

        # Test with 1 message
        data["messages"] = [{"role": "user", "content": "Hello"}]
        with self.assertRaises(ValidationError) as cm:
            PromptSchema(**data)
        self.assertIn("messages list must have at least 2 items", str(cm.exception))

        # Test with 2 messages (valid) - already covered in test_valid_schema
        # Test with 3 messages (valid)
        data = self.valid_data.copy()
        data["messages"] = [
            {"role": "system", "content": "You are helpful"},
            {"role": "user", "content": "Hello"},
            {"role": "assistant", "content": "Hi there"}
        ]
        prompt = PromptSchema(**data)
        self.assertEqual(len(prompt.messages), 3)

    def test_nested_model_validation(self):
        """Test validation of nested models (ModelParameters, Message)."""
        # Invalid temperature type
        data = self.valid_data.copy()
        data["modelParameters"] = {"temperature": "hot"}
        with self.assertRaises(ValidationError):
            PromptSchema(**data)

        # Invalid message content (missing content)
        data = self.valid_data.copy()
        data["messages"] = [
            {"role": "system", "content": "sys"},
            {"role": "user", "content": None}  # missing content/invalid type
        ]
        with self.assertRaises(ValidationError):
            PromptSchema(**data)

    def test_invalid_types(self):
        """Test that invalid field types raise ValidationError."""
        data = self.valid_data.copy()
        data["messages"] = "not a list"
        with self.assertRaises(ValidationError):
            PromptSchema(**data)

if __name__ == "__main__":
    unittest.main()
