import unittest
from pathlib import Path
import sys
import os
from unittest.mock import MagicMock, patch

# Mock yaml before importing generate_docs since it might not be installed
sys.modules["yaml"] = MagicMock()

from promptops.utils import derive_category
from tools.scripts.generate_docs import DocumentationGenerator

class TestSyncMarkdownAssets(unittest.TestCase):
    @patch("tools.scripts.generate_docs.CONFIG", {'dirs': {'workflows': 'workflows', 'workflow_docs': 'docs/workflows', 'prompts': 'prompts', 'docs': 'docs'}})
    @patch("promptops.utils.iter_markdown_files")
    def test_sync_markdown_assets(self, mock_iter):
        """Test that markdown files are synced from workflows/ to docs/workflows/ and links are rewritten."""
        import tempfile
        import shutil

        with tempfile.TemporaryDirectory() as tmpdir:
            root = Path(tmpdir)
            wf_dir = root / "workflows"
            docs_dir = root / "docs" / "workflows"
            wf_dir.mkdir(parents=True)
            
            # Setup a fake markdown file
            md_file = wf_dir / "overview.md"
            md_content = "Link to [Workflow](test.workflow.yaml) and [Schema](../docs/schema.md)"
            md_file.write_text(md_content)

            # Setup the iter mock
            mock_iter.return_value = [md_file]

            gen = DocumentationGenerator(root)
            changes = gen.sync_markdown_assets()

            self.assertTrue(changes)
            self.assertTrue((docs_dir / "overview.md").exists())
            
            # Verify links are rewritten correctly
            synced_content = (docs_dir / "overview.md").read_text()
            self.assertIn("[Workflow](test.md)", synced_content)
            self.assertIn("[Schema](../schema.md)", synced_content)

            # Re-running shouldn't cause changes
            changes_again = gen.sync_markdown_assets()
            self.assertFalse(changes_again)

class TestDeriveCategory(unittest.TestCase):
    def test_root_file(self):
        """Test file in the root directory returns Uncategorized."""
        root = Path("/repo/prompts")
        path = root / "README.md"
        self.assertEqual(derive_category(path, root), "Uncategorized")

    def test_root_directory_itself(self):
        """Test the root directory itself returns Uncategorized."""
        root = Path("/repo/prompts")
        self.assertEqual(derive_category(root, root), "Uncategorized")

    def test_simple_category(self):
        """Test file in a simple category folder."""
        root = Path("/repo/prompts")
        path = root / "clinical" / "test.prompt.md"
        self.assertEqual(derive_category(path, root, {}), "Clinical")

    def test_nested_category_legacy_fallback(self):
        """Test nested folders still fall back to top-level directory category."""
        root = Path("/repo/prompts")
        path = root / "clinical" / "oncology" / "test.prompt.md"
        self.assertEqual(derive_category(path, root, {}), "Clinical")

    def test_none_data_uses_legacy_fallback(self):
        """Test None metadata still uses folder-based fallback for compatibility."""
        root = Path("/repo/prompts")
        path = root / "clinical" / "test.prompt.md"
        self.assertEqual(derive_category(path, root, None), "Clinical")

    def test_domain_tag_takes_precedence(self):
        """Test namespaced domain tag overrides folder-based category."""
        root = Path("/repo/prompts")
        path = root / "google_jules" / "test.prompt.md"
        data = {"metadata": {"tags": ["domain:technical", "topic:architecture"]}}
        self.assertEqual(derive_category(path, root, data), "Technical")

    def test_first_domain_tag_wins(self):
        """Test first matching domain tag is used when multiple are present."""
        root = Path("/repo/prompts")
        path = root / "google_jules" / "test.prompt.md"
        data = {"metadata": {"tags": ["domain:clinical", "domain:technical"]}}
        self.assertEqual(derive_category(path, root, data), "Clinical")

    def test_metadata_domain_fallback(self):
        """Test metadata domain is used when namespaced domain tag is absent."""
        root = Path("/repo/prompts")
        path = root / "misc" / "test.prompt.md"
        data = {"metadata": {"domain": "business/strategy", "tags": ["topic:finance"]}}
        self.assertEqual(derive_category(path, root, data), "Business")

    def test_metadata_without_domain_uses_legacy_fallback(self):
        """Test metadata without domain information still falls back to directory."""
        root = Path("/repo/prompts")
        path = root / "scientific" / "test.prompt.md"
        data = {"metadata": {"tags": ["topic:biology"]}}
        self.assertEqual(derive_category(path, root, data), "Scientific")

    def test_legacy_tags_supported(self):
        """Test top-level legacy tags are still supported for category derivation."""
        root = Path("/repo/prompts")
        path = root / "misc" / "test.prompt.md"
        data = {"tags": ["domain:scientific", "topic:biology"]}
        self.assertEqual(derive_category(path, root, data), "Scientific")

    def test_category_with_underscores(self):
        """Test category name with underscores is formatted correctly."""
        root = Path("/repo/prompts")
        path = root / "data_management" / "test.prompt.md"
        self.assertEqual(derive_category(path, root, {}), "Data Management")

    def test_not_in_root(self):
        """Test path not relative to root_dir returns Uncategorized."""
        root = Path("/repo/prompts")
        path = Path("/other/path/test.prompt.md")
        self.assertEqual(derive_category(path, root), "Uncategorized")

if __name__ == "__main__":
    unittest.main()
