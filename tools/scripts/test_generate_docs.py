import unittest
from pathlib import Path
import sys
import os
from unittest.mock import MagicMock

# Mock yaml before importing generate_docs since it might not be installed
sys.modules["yaml"] = MagicMock()

# Add the current directory to sys.path to import generate_docs
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from generate_docs import FileParser

class TestDeriveCategory(unittest.TestCase):
    def test_root_file(self):
        """Test file in the root directory returns Uncategorized."""
        root = Path("/repo/prompts")
        path = root / "README.md"
        self.assertEqual(FileParser.derive_category(path, root), "Uncategorized")

    def test_root_directory_itself(self):
        """Test the root directory itself returns Uncategorized."""
        root = Path("/repo/prompts")
        self.assertEqual(FileParser.derive_category(root, root), "Uncategorized")

    def test_simple_category(self):
        """Test file in a simple category folder."""
        root = Path("/repo/prompts")
        path = root / "clinical" / "test.prompt.yaml"
        self.assertEqual(FileParser.derive_category(path, root), "Clinical")

    def test_nested_category(self):
        """Test file in a nested category folder still returns the top-level category."""
        root = Path("/repo/prompts")
        path = root / "clinical" / "oncology" / "test.prompt.yaml"
        self.assertEqual(FileParser.derive_category(path, root), "Clinical")

    def test_technical_architecture(self):
        """Test special mapping for technical/architecture."""
        root = Path("/repo/prompts")
        path = root / "technical" / "architecture" / "test.prompt.yaml"
        self.assertEqual(FileParser.derive_category(path, root), "Architecture")

    def test_technical_software_engineering(self):
        """Test special mapping for technical/software_engineering."""
        root = Path("/repo/prompts")
        path = root / "technical" / "software_engineering" / "test.prompt.yaml"
        self.assertEqual(FileParser.derive_category(path, root), "Software Engineering")

    def test_technical_other(self):
        """Test technical folder with no special subfolder mapping returns Technical."""
        root = Path("/repo/prompts")
        path = root / "technical" / "security" / "test.prompt.yaml"
        self.assertEqual(FileParser.derive_category(path, root), "Technical")

    def test_category_with_underscores(self):
        """Test category name with underscores is formatted correctly."""
        root = Path("/repo/prompts")
        path = root / "data_management" / "test.prompt.yaml"
        self.assertEqual(FileParser.derive_category(path, root), "Data Management")

    def test_not_in_root(self):
        """Test path not relative to root_dir returns Uncategorized."""
        root = Path("/repo/prompts")
        path = Path("/other/path/test.prompt.yaml")
        self.assertEqual(FileParser.derive_category(path, root), "Uncategorized")

if __name__ == "__main__":
    unittest.main()
