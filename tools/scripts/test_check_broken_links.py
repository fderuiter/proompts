import unittest
from pathlib import Path
from unittest.mock import patch, MagicMock

import sys
sys.path.append(str(Path(__file__).parent))
from check_broken_links import check_link

class TestCheckBrokenLinks(unittest.TestCase):
    def test_ignore_external_links(self):
        source_file = Path("dummy.md")
        cache = {}

        self.assertEqual(check_link(source_file, "http://example.com", cache), (True, ""))
        self.assertEqual(check_link(source_file, "https://example.com", cache), (True, ""))
        self.assertEqual(check_link(source_file, "mailto:test@example.com", cache), (True, ""))

    def test_pure_anchor_link(self):
        source_file = Path("dummy.md")
        cache = {}

        # Test valid anchor
        cache[str(source_file)] = {"section-1"}
        with patch.object(Path, 'exists', return_value=True):
            self.assertEqual(check_link(source_file, "#section-1", cache), (True, ""))

        # Test missing anchor
        with patch.object(Path, 'exists', return_value=True):
            self.assertEqual(check_link(source_file, "#missing", cache), (False, "Anchor #missing not found in dummy.md"))

    def test_file_not_found(self):
        source_file = Path("docs/dummy.md")
        cache = {}

        with patch.object(Path, 'exists', return_value=False):
            self.assertEqual(check_link(source_file, "missing.md", cache), (False, "File not found: missing.md"))

    def test_directory_link(self):
        source_file = Path("docs/dummy.md")
        cache = {}

        with patch.object(Path, 'exists', return_value=True):
            with patch.object(Path, 'is_dir', return_value=True):
                self.assertEqual(check_link(source_file, "../docs", cache), (True, ""))

    def test_file_with_valid_anchor(self):
        source_file = Path("docs/dummy.md")
        cache = {}

        with patch.object(Path, 'exists', return_value=True):
            with patch.object(Path, 'is_dir', return_value=False):
                # We need to patch get_anchors_in_file since check_link calls it when cache miss
                with patch('check_broken_links.get_anchors_in_file', return_value={"target-section"}):
                    self.assertEqual(check_link(source_file, "other.md#target-section", cache), (True, ""))

    def test_file_with_invalid_anchor(self):
        source_file = Path("docs/dummy.md")
        cache = {}

        with patch.object(Path, 'exists', return_value=True):
            with patch.object(Path, 'is_dir', return_value=False):
                with patch('check_broken_links.get_anchors_in_file', return_value={"target-section"}):
                    # For absolute path simulation or relative path, just the file name differs
                    self.assertEqual(check_link(source_file, "other.md#missing-section", cache),
                                     (False, "Anchor #missing-section not found in other.md"))

    def test_absolute_path_link(self):
        # Setup ROOT_DIR mock and path resolution
        source_file = Path("docs/dummy.md")
        cache = {}

        with patch.object(Path, 'exists', return_value=True):
            with patch.object(Path, 'is_dir', return_value=False):
                self.assertEqual(check_link(source_file, "/README.md", cache), (True, ""))

if __name__ == '__main__':
    unittest.main()
