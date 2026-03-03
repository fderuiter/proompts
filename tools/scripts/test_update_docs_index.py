import unittest
from pathlib import Path
import sys
from unittest.mock import MagicMock

# Mock out yaml before importing update_docs_index
sys.modules['yaml'] = MagicMock()

sys.path.append(str(Path(__file__).parent))
from update_docs_index import nice_title

class TestUpdateDocsIndex(unittest.TestCase):
    def test_nice_title_basic(self):
        self.assertEqual(nice_title("hello world"), "Hello World")
        self.assertEqual(nice_title("HELLO WORLD"), "Hello World")

    def test_nice_title_underscores(self):
        self.assertEqual(nice_title("hello_world"), "Hello World")
        self.assertEqual(nice_title("hello_world_test"), "Hello World Test")

    def test_nice_title_hyphens(self):
        self.assertEqual(nice_title("hello-world"), "Hello World")
        self.assertEqual(nice_title("hello-world-test"), "Hello World Test")

    def test_nice_title_mixed(self):
        self.assertEqual(nice_title("hello_world-test"), "Hello World Test")

    def test_nice_title_already_capitalized(self):
        self.assertEqual(nice_title("Hello World"), "Hello World")

    def test_nice_title_empty(self):
        self.assertEqual(nice_title(""), "")

    def test_nice_title_multiple_spaces(self):
        self.assertEqual(nice_title("hello   world"), "Hello World")
        self.assertEqual(nice_title("hello___world"), "Hello World")
        self.assertEqual(nice_title("hello---world"), "Hello World")

    def test_nice_title_trailing_leading_spaces(self):
        self.assertEqual(nice_title("  hello world  "), "Hello World")
        self.assertEqual(nice_title("_hello_world_"), "Hello World")
        self.assertEqual(nice_title("-hello-world-"), "Hello World")

if __name__ == '__main__':
    unittest.main()
