import unittest
import sys
from pathlib import Path

# Add the current directory to sys.path to import enrich_prompts
sys.path.append(str(Path(__file__).parent))
from enrich_prompts import infer_complexity

class TestEnrichPrompts(unittest.TestCase):
    def test_infer_complexity_empty(self):
        """Test with an empty dictionary."""
        self.assertEqual(infer_complexity({}), "low")

    def test_infer_complexity_low(self):
        """Test cases that should result in low complexity."""
        # 0 vars, 0 length
        self.assertEqual(infer_complexity({"variables": [], "messages": []}), "low")
        # 1 var, 0 length
        self.assertEqual(infer_complexity({"variables": [{"name": "var1"}], "messages": []}), "low")
        # 0 vars, 600 length
        self.assertEqual(infer_complexity({"variables": [], "messages": [{"content": "a" * 600}]}), "low")
        # 1 var, 600 length
        self.assertEqual(infer_complexity({"variables": [{"name": "var1"}], "messages": [{"content": "a" * 600}]}), "low")

    def test_infer_complexity_medium(self):
        """Test cases that should result in medium complexity."""
        # 2 vars, 0 length
        self.assertEqual(infer_complexity({"variables": [{"name": "var1"}, {"name": "var2"}], "messages": []}), "medium")
        # 3 vars, 0 length
        self.assertEqual(infer_complexity({"variables": [{"name": "v1"}, {"name": "v2"}, {"name": "v3"}], "messages": []}), "medium")
        # 0 vars, 601 length
        self.assertEqual(infer_complexity({"variables": [], "messages": [{"content": "a" * 601}]}), "medium")
        # 0 vars, 1500 length
        self.assertEqual(infer_complexity({"variables": [], "messages": [{"content": "a" * 1500}]}), "medium")
        # 3 vars, 1500 length
        self.assertEqual(infer_complexity({"variables": [{"name": "v1"}, {"name": "v2"}, {"name": "v3"}], "messages": [{"content": "a" * 1500}]}), "medium")
        # 2 vars, 601 length
        self.assertEqual(infer_complexity({"variables": [{"name": "var1"}, {"name": "var2"}], "messages": [{"content": "a" * 601}]}), "medium")

    def test_infer_complexity_high(self):
        """Test cases that should result in high complexity."""
        # 4 vars, 0 length
        self.assertEqual(infer_complexity({"variables": [{"name": "v1"}, {"name": "v2"}, {"name": "v3"}, {"name": "v4"}], "messages": []}), "high")
        # 5 vars, 0 length
        self.assertEqual(infer_complexity({"variables": [{"name": "v1"}, {"name": "v2"}, {"name": "v3"}, {"name": "v4"}, {"name": "v5"}], "messages": []}), "high")
        # 0 vars, 1501 length
        self.assertEqual(infer_complexity({"variables": [], "messages": [{"content": "a" * 1501}]}), "high")
        # 4 vars, 1501 length
        self.assertEqual(infer_complexity({"variables": [{"name": "v1"}, {"name": "v2"}, {"name": "v3"}, {"name": "v4"}], "messages": [{"content": "a" * 1501}]}), "high")

if __name__ == "__main__":
    unittest.main()
