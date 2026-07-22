"""Module docstring."""
import json
from pathlib import Path
from promptops.validation import PromptSchema

def init_project():
    """Missing docstring."""
    print("Initializing PromptOps in the current repository...")
    
    # Create schema
    schema_dir = Path("schemas")
    schema_dir.mkdir(exist_ok=True)
    schema_path = schema_dir / "prompt.schema.json"
    schema_path.write_text(json.dumps(PromptSchema.model_json_schema(), indent=2), encoding='utf-8')
    print(f"Created schema at {schema_path}")
    
    # Create github action
    action_dir = Path(".github/workflows")
    action_dir.mkdir(parents=True, exist_ok=True)
    action_path = action_dir / "validate-prompts.yml"
    
    action_content = """name: Validate Prompts
on:
  pull_request:
    paths:
      - 'prompts/**'
      - '.github/workflows/validate-prompts.yml'

jobs:
  validate:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.10'
      - name: Install PromptOps
        run: pip install promptops
      - name: Validate Prompts
        run: promptops validate --dir prompts --strict
"""
    action_path.write_text(action_content, encoding='utf-8')
    print(f"Created GitHub Action at {action_path}")
    
    # Create test template
    tests_dir = Path("tests")
    tests_dir.mkdir(exist_ok=True)
    test_path = tests_dir / "simulate_prompts.py"
    
    test_content = """import os
from promptops.simulation import simulate_prompt

def test_simulation():
    # Example test
    # simulate_prompt("prompts/my_prompt.yaml", "tests/mock_data.json")
    pass
"""
    test_path.write_text(test_content, encoding='utf-8')
    print(f"Created simulation test template at {test_path}")
    
    print("Initialization complete!")
