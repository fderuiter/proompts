import unittest
import sys
from pathlib import Path
from io import StringIO
from pydantic import ValidationError

# Add the current directory to sys.path to import validate_prompt_schema
sys.path.append(str(Path(__file__).parent))

from validate_prompt_schema import (
    PromptSchema, Message, ModelParameters,
    ComplexityLevel, InputVariable, PromptMetadata,
)

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

    # ------------------------------------------------------------------
    # Original tests
    # ------------------------------------------------------------------

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

    # ------------------------------------------------------------------
    # New: version field
    # ------------------------------------------------------------------

    def test_version_defaults(self):
        """Test that version defaults to '0.1.0' when missing."""
        prompt = PromptSchema(**self.valid_data)
        self.assertEqual(prompt.version, "0.1.0")

    def test_version_explicit(self):
        """Test that an explicit version is preserved."""
        data = {**self.valid_data, "version": "2.0.0"}
        prompt = PromptSchema(**data)
        self.assertEqual(prompt.version, "2.0.0")

    # ------------------------------------------------------------------
    # New: metadata field
    # ------------------------------------------------------------------

    def test_metadata_defaults_to_none(self):
        """Test that metadata defaults to None when missing."""
        prompt = PromptSchema(**self.valid_data)
        self.assertIsNone(prompt.metadata)

    def test_metadata_valid(self):
        """Test a fully-populated metadata block."""
        data = {
            **self.valid_data,
            "metadata": {
                "domain": "clinical",
                "complexity": "high",
                "tags": ["oncology", "protocol"],
                "requires_context": True,
            }
        }
        prompt = PromptSchema(**data)
        self.assertEqual(prompt.metadata.domain, "clinical")
        self.assertEqual(prompt.metadata.complexity, ComplexityLevel.HIGH)
        self.assertEqual(prompt.metadata.tags, ["oncology", "protocol"])
        self.assertTrue(prompt.metadata.requires_context)

    def test_metadata_invalid_complexity(self):
        """Test that an invalid complexity value raises ValidationError."""
        data = {
            **self.valid_data,
            "metadata": {
                "domain": "general",
                "complexity": "extreme",  # invalid
            }
        }
        with self.assertRaises(ValidationError):
            PromptSchema(**data)

    # ------------------------------------------------------------------
    # New: variables field & cross-validation
    # ------------------------------------------------------------------

    def test_variables_defaults_to_empty(self):
        """Test that variables defaults to empty list when missing."""
        prompt = PromptSchema(**self.valid_data)
        self.assertEqual(prompt.variables, [])

    def test_variables_valid(self):
        """Test prompt with correctly defined and used variables."""
        data = {
            **self.valid_data,
            "messages": [
                {"role": "system", "content": "Use {{style}}."},
                {"role": "user", "content": "Summarize: {{input}}"},
            ],
            "variables": [
                {"name": "input", "description": "Text to summarize", "required": True},
                {"name": "style", "description": "Tone of response", "required": False, "default": "formal"},
            ]
        }
        prompt = PromptSchema(**data)
        self.assertEqual(len(prompt.variables), 2)
        self.assertEqual(prompt.variables[1].default, "formal")

    def test_variables_undefined_raises_error(self):
        """Test that using {{var}} without defining it in variables raises error."""
        data = {
            **self.valid_data,
            "messages": [
                {"role": "system", "content": "You are helpful."},
                {"role": "user", "content": "Summarize: {{topic}}"},
            ],
            # no variables defined
        }
        with self.assertRaises(ValidationError) as cm:
            PromptSchema(**data)
        self.assertIn("topic", str(cm.exception))

    def test_variables_unused_prints_warning(self):
        """Test that defining a variable not used in messages prints a warning."""
        data = {
            **self.valid_data,
            "messages": [
                {"role": "system", "content": "You are helpful."},
                {"role": "user", "content": "Hello!"},
            ],
            "variables": [
                {"name": "unused_var", "description": "Not used anywhere"},
            ]
        }
        import io, contextlib
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            prompt = PromptSchema(**data)
        self.assertIn("unused_var", buf.getvalue())

    def test_input_variable_defaults(self):
        """Test InputVariable default values."""
        var = InputVariable(name="x", description="test")
        self.assertTrue(var.required)
        self.assertIsNone(var.default)


class TestComplexityLevel(unittest.TestCase):
    def test_valid_values(self):
        for val in ("low", "medium", "high"):
            self.assertEqual(ComplexityLevel(val).value, val)

    def test_invalid_value(self):
        with self.assertRaises(ValueError):
            ComplexityLevel("extreme")


if __name__ == "__main__":
    unittest.main()
