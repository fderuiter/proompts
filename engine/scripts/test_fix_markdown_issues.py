import unittest
import sys
from pathlib import Path

# Add the script directory to sys.path
sys.path.append(str(Path(__file__).parent))

from fix_markdown_issues import fix_trailing_spaces, fix_codeblock_spacing, fix_header_style

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

    def test_fix_header_style(self):
        lines = [
            "#Header 1",
            "##Header 2",
            "### Header 3",
            "####",
            "Not a header",
            " # Not header because of leading space",
            "#123",
            "##123"
        ]
        expected = [
            "# Header 1",
            "## Header 2",
            "### Header 3",
            "####",
            "Not a header",
            " # Not header because of leading space",
            "# 123",
            "## 123"
        ]
        self.assertEqual(fix_header_style(lines), expected)

    def test_fix_codeblock_spacing(self):
        # 1. No surrounding blank lines
        lines1 = [
            "Before code",
            "```python",
            "print('hello')",
            "```",
            "After code"
        ]
        expected1 = [
            "Before code",
            "",
            "```python",
            "print('hello')",
            "```",
            "",
            "After code"
        ]
        self.assertEqual(fix_codeblock_spacing(lines1), expected1)

        # 2. Existing surrounding blank lines
        lines2 = [
            "Before code",
            "",
            "```python",
            "print('hello')",
            "```",
            "",
            "After code"
        ]
        self.assertEqual(fix_codeblock_spacing(lines2), lines2)

        # 3. Codeblock at the beginning
        lines3 = [
            "```python",
            "print('hello')",
            "```",
            "After code"
        ]
        expected3 = [
            "```python",
            "print('hello')",
            "```",
            "",
            "After code"
        ]
        self.assertEqual(fix_codeblock_spacing(lines3), expected3)

        # 4. Codeblock at the end
        lines4 = [
            "Before code",
            "```python",
            "print('hello')",
            "```"
        ]
        expected4 = [
            "Before code",
            "",
            "```python",
            "print('hello')",
            "```"
        ]
        self.assertEqual(fix_codeblock_spacing(lines4), expected4)

        # 5. Adjacent codeblocks
        lines5 = [
            "Before code",
            "```python",
            "print('1')",
            "```",
            "```python",
            "print('2')",
            "```",
            "After code"
        ]
        expected5 = [
            "Before code",
            "",
            "```python",
            "print('1')",
            "```",
            "",
            "```python",
            "print('2')",
            "```",
            "",
            "After code"
        ]
        self.assertEqual(fix_codeblock_spacing(lines5), expected5)

        # 6. Nested codeblocks (using different ticks)
        lines6 = [
            "Before code",
            "````markdown",
            "```python",
            "print('hello')",
            "```",
            "````",
            "After code"
        ]
        expected6 = [
            "Before code",
            "",
            "````markdown",
            "```python",
            "print('hello')",
            "```",
            "````",
            "",
            "After code"
        ]
        self.assertEqual(fix_codeblock_spacing(lines6), expected6)

if __name__ == "__main__":
    unittest.main()
