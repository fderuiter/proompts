import unittest
import sys
import os
from pathlib import Path

# Add the tools/scripts directory to sys.path to import generate_regulatory_prompts
sys.path.append(str(Path(__file__).parent))

from generate_regulatory_prompts import to_snake_case

class TestGenerateRegulatoryPrompts(unittest.TestCase):
    def test_to_snake_case(self):
        # Normal text
        self.assertEqual(to_snake_case("This is a test"), "this_is_a_test")

        # Slashes and parenthesis
        self.assertEqual(to_snake_case("A/B (test)"), "a_b_test")

        # Uppercase
        self.assertEqual(to_snake_case("UPPERCASE"), "uppercase")

        # Special characters
        self.assertEqual(to_snake_case("test@#$name"), "test_name")

        # Multiple spaces/chars resulting in consecutive underscores
        self.assertEqual(to_snake_case("multiple   underscores"), "multiple_underscores")
        self.assertEqual(to_snake_case("a_b__c___d"), "a_b_c_d")

        # Trailing/leading spaces/chars
        self.assertEqual(to_snake_case(" test "), "test")
        self.assertEqual(to_snake_case("__test__"), "test")

        # Empty string
        self.assertEqual(to_snake_case(""), "")

        # Mixed cases
        self.assertEqual(to_snake_case("510(k) Substantial Equivalence"), "510_k_substantial_equivalence")
        self.assertEqual(to_snake_case("QMS (ISO 13485) Audit"), "qms_iso_13485_audit")

if __name__ == '__main__':
    unittest.main()
