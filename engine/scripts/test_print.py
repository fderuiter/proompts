from fix_markdown_issues import fix_codeblock_spacing

lines6 = [
    "Before code",
    "```markdown",
    "```python",
    "print('hello')",
    "```",
    "```",
    "After code"
]
import pprint
pprint.pprint(fix_codeblock_spacing(lines6))
