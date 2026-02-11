
import unittest
import sys
from pathlib import Path

# Add the script directory to sys.path
sys.path.append(str(Path(__file__).parent))

from fix_markdown_issues import fix_trailing_spaces

class TestFixMarkdownIssues(unittest.TestCase):
    def test_fix_trailing_spaces(self):
        lines = [
            "No trailing",
            "Trailing space ",
            "Multiple spaces   ",
            "Tabs\t",
            "Mixed \t  ",
            "   Leading spaces",
            "",
            "   "
        ]
        expected = [
            "No trailing",
            "Trailing space",
            "Multiple spaces",
            "Tabs",
            "Mixed",
            "   Leading spaces",
            "",
            ""
        ]
        self.assertEqual(fix_trailing_spaces(lines), expected)

if __name__ == "__main__":
    unittest.main()
