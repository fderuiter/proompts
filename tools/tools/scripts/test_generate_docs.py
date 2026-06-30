import unittest
from pathlib import Path
import sys
import os
from unittest.mock import MagicMock

# Mock yaml before importing generate_docs since it might not be installed
sys.modules["yaml"] = MagicMock()

from tools.scripts.generate_docs import FileParser

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
        path = root / "clinical" / "test.prompt.md"
        self.assertEqual(FileParser.derive_category(path, root, {}), "Clinical")

    def test_nested_category_legacy_fallback(self):
        """Test nested folders still fall back to top-level directory category."""
        root = Path("/repo/prompts")
        path = root / "clinical" / "oncology" / "test.prompt.md"
        self.assertEqual(FileParser.derive_category(path, root, {}), "Clinical")

    def test_none_data_uses_legacy_fallback(self):
        """Test None metadata still uses folder-based fallback for compatibility."""
        root = Path("/repo/prompts")
        path = root / "clinical" / "test.prompt.md"
        self.assertEqual(FileParser.derive_category(path, root, None), "Clinical")

    def test_domain_tag_takes_precedence(self):
        """Test namespaced domain tag overrides folder-based category."""
        root = Path("/repo/prompts")
        path = root / "google_jules" / "test.prompt.md"
        data = {"metadata": {"tags": ["domain:technical", "topic:architecture"]}}
        self.assertEqual(FileParser.derive_category(path, root, data), "Technical")

    def test_first_domain_tag_wins(self):
        """Test first matching domain tag is used when multiple are present."""
        root = Path("/repo/prompts")
        path = root / "google_jules" / "test.prompt.md"
        data = {"metadata": {"tags": ["domain:clinical", "domain:technical"]}}
        self.assertEqual(FileParser.derive_category(path, root, data), "Clinical")

    def test_metadata_domain_fallback(self):
        """Test metadata domain is used when namespaced domain tag is absent."""
        root = Path("/repo/prompts")
        path = root / "misc" / "test.prompt.md"
        data = {"metadata": {"domain": "business/strategy", "tags": ["topic:finance"]}}
        self.assertEqual(FileParser.derive_category(path, root, data), "Business")

    def test_metadata_without_domain_uses_legacy_fallback(self):
        """Test metadata without domain information still falls back to directory."""
        root = Path("/repo/prompts")
        path = root / "scientific" / "test.prompt.md"
        data = {"metadata": {"tags": ["topic:biology"]}}
        self.assertEqual(FileParser.derive_category(path, root, data), "Scientific")

    def test_legacy_tags_supported(self):
        """Test top-level legacy tags are still supported for category derivation."""
        root = Path("/repo/prompts")
        path = root / "misc" / "test.prompt.md"
        data = {"tags": ["domain:scientific", "topic:biology"]}
        self.assertEqual(FileParser.derive_category(path, root, data), "Scientific")

    def test_category_with_underscores(self):
        """Test category name with underscores is formatted correctly."""
        root = Path("/repo/prompts")
        path = root / "data_management" / "test.prompt.md"
        self.assertEqual(FileParser.derive_category(path, root, {}), "Data Management")

    def test_not_in_root(self):
        """Test path not relative to root_dir returns Uncategorized."""
        root = Path("/repo/prompts")
        path = Path("/other/path/test.prompt.md")
        self.assertEqual(FileParser.derive_category(path, root), "Uncategorized")

if __name__ == "__main__":
    unittest.main()
