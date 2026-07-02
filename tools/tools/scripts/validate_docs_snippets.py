#!/usr/bin/env python3
"""
Lightweight Script Validator
Extracts Python and YAML code blocks from documentation and validates them.
"""

import sys
import copy
import io
import argparse
from pathlib import Path
from contextlib import redirect_stdout
from unittest.mock import MagicMock, mock_open, patch

try:
    import yaml
    from pydantic import ValidationError
except ImportError:
    print("Required dependencies not found. Make sure to run inside the uv virtualenv.")
    sys.exit(1)

def is_block_bad(content_lines, block_start_line):
    """
    Looks backward from the code block to determine if it is marked as a 'Bad Example'
    or has a negative emoji. Returns True if marked bad.
    """
    context = ""
    for j in range(block_start_line - 2, -1, -1):
        line = content_lines[j].strip()
        if line.startswith('```'):
            break
        if line != '':
            context = line + '\n' + context
            if j > 0 and content_lines[j-1].strip() == '':
                break
    
    if 'Bad Example' in context or '❌' in context:
        return True
    return False

def validate_python(code):
    """Executes Python code in isolation to check for syntax/runtime errors."""
    
    # Mock typical external modules that might not be available
    sys.modules['openai'] = MagicMock()
    
    # Mock file contents for load_prompt calls
    mocked_file_content = """
name: test
description: test
model: gpt-4
modelParameters:
  temperature: 0.2
messages:
  - role: system
    content: test
  - role: user
    content: "test: {{code}}"
testData: []
evaluators: []
"""
    f = io.StringIO()
    try:
        with redirect_stdout(f), patch('builtins.open', mock_open(read_data=mocked_file_content)):
            local_vars = {}
            exec(code, local_vars)
        return True, ""
    except Exception as e:
        return False, str(e)

def validate_yaml(code):
    """Parses YAML and partially validates against Pydantic models."""
    from promptops.validation import PromptSchema, WorkflowSchema
    
    try:
        data = yaml.safe_load(code)
    except Exception as e:
        return False, f"YAML parsing error: {e}"
        
    if not isinstance(data, dict):
        return True, ""
        
    # Heuristic: check if this fragment contains workflow specific keys
    is_workflow = any(k in data for k in ['steps', 'step_id', 'map_inputs', 'inputs'])
    
    if is_workflow:
        base = {
            "name": "test_workflow",
            "steps": [{"step_id": "test", "prompt_file": "test", "map_inputs": {}}]
        }
        test_data = copy.deepcopy(base)
        test_data.update(data)
        try:
            WorkflowSchema(**test_data)
            return True, ""
        except ValidationError as e:
            return False, f"Workflow schema validation error:\n{e}"
    else:
        base = {
            "name": "test_prompt",
            "description": "test",
            "model": "gpt-4",
            "modelParameters": {"temperature": 0.5},
            "messages": [
                {"role": "system", "content": "test"},
                {"role": "user", "content": "test"}
            ],
            "testData": [{"inputs": {"test": "test"}, "expected": "test"}],
            "evaluators": []
        }
        test_data = copy.deepcopy(base)
        test_data.update(data)
        try:
            PromptSchema(**test_data)
            return True, ""
        except ValidationError as e:
            return False, f"Prompt schema validation error:\n{e}"

def validate_file(filepath: Path):
    errors = []
    
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            lines = f.readlines()
    except Exception as e:
        return [(0, f"Could not read file: {e}")]
        
    in_block = False
    lang = None
    block_start_line = 0
    code_lines = []
    
    for i, line in enumerate(lines):
        stripped = line.strip()
        if stripped.startswith('```') and not in_block:
            in_block = True
            lang = stripped[3:].strip()
            block_start_line = i + 1
            code_lines = []
        elif stripped == '```' and in_block:
            in_block = False
            code = "".join(code_lines)
            
            # We only validate python and yaml/yml
            if lang in ('python', 'yaml', 'yml'):
                if not is_block_bad(lines, block_start_line):
                    if lang == 'python':
                        is_valid, err_msg = validate_python(code)
                    else:
                        is_valid, err_msg = validate_yaml(code)
                        
                    if not is_valid:
                        errors.append((block_start_line, err_msg))
        elif in_block:
            code_lines.append(line)
            
    return errors

def main():
    parser = argparse.ArgumentParser(description="Validate documentation snippets.")
    parser.add_argument('files', nargs='+', type=Path, help="Markdown files to validate")
    args = parser.parse_args()
    
    total_errors = 0
    total_files = 0
    
    for filepath in args.files:
        if not filepath.exists():
            print(f"⚠️ Warning: File not found: {filepath}")
            continue
            
        total_files += 1
        errors = validate_file(filepath)
        if errors:
            print(f"❌ Validation failed in {filepath}:")
            for line_no, err_msg in errors:
                print(f"  Line {line_no}:\n    {err_msg.replace(chr(10), chr(10)+'    ')}\n")
                total_errors += 1
                
    if total_errors > 0:
        print(f"\nFound {total_errors} documentation snippet error(s).")
        sys.exit(1)
    elif total_files > 0:
        print("\n✅ All documentation snippets verified.")
        sys.exit(0)
    else:
        print("No files to validate.")
        sys.exit(0)

if __name__ == "__main__":
    main()
