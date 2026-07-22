import os
import sys
import pytest
from unittest.mock import patch, MagicMock, mock_open

DOCS_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'docs'))

def get_python_blocks():
    blocks = []
    # According to the context, we should focus on usage guides.
    # We will scan top-level .md files in docs/ that have python blocks.
    for filename in os.listdir(DOCS_DIR):
        if not filename.endswith('.md'):
            continue
        filepath = os.path.join(DOCS_DIR, filename)
        with open(filepath, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        
        in_block = False
        block_lines = []
        start_line = 0
        for i, line in enumerate(lines):
            # match ```python or ```python with modifiers
            if line.strip().startswith('```python'):
                in_block = True
                block_lines = []
                start_line = i
            elif in_block and line.strip().startswith('```'):
                in_block = False
                code = "".join(block_lines)
                blocks.append({
                    'filepath': filepath,
                    'code': code,
                    'start_line': start_line,
                    'id': f"{filename}:{start_line+1}"
                })
            elif in_block:
                block_lines.append(line)
    return blocks

PYTHON_BLOCKS = get_python_blocks()

@pytest.fixture(autouse=True)
def mock_external_apis():
    # Mock OpenAI
    mock_openai = MagicMock()
    # For USAGE.md
    mock_openai.chat.completions.create.return_value.choices[0].message.content = "mocked response"
    
    # For gpt_5_2_prompting_guide.md
    mock_response = MagicMock()
    mock_msg = MagicMock()
    mock_msg.model_dump.return_value = {"content": "mocked"}
    mock_response.output = [mock_msg]
    mock_openai.OpenAI.return_value.responses.create.return_value = mock_response
    
    mock_compacted = MagicMock()
    mock_compacted.model_dump.return_value = {"compacted": "yes"}
    mock_openai.OpenAI.return_value.responses.compact.return_value = mock_compacted
    
    sys.modules['openai'] = mock_openai
    
    # Mock Anthropic
    mock_anthropic = MagicMock()
    mock_msg_response = MagicMock()
    mock_msg_response.content = "mocked claude content"
    mock_anthropic.Anthropic.return_value.messages.create.return_value = mock_msg_response
    sys.modules['anthropic'] = mock_anthropic

    # Provide a generic dummy client for partial snippets
    dummy_client = MagicMock()
    dummy_client.messages.create.return_value = mock_msg_response
    
    yield dummy_client

@pytest.fixture(autouse=True)
def mock_filesystem():
    dummy_yaml = """
model: gpt-4
modelParameters:
  temperature: 0.7
messages:
  - role: user
    content: "Review this code: {{code}}"
"""
    with patch('builtins.open', mock_open(read_data=dummy_yaml)) as m_open:
        yield m_open

@pytest.mark.parametrize("block", PYTHON_BLOCKS, ids=[b['id'] for b in PYTHON_BLOCKS])
def test_documentation_code_block(block, mock_external_apis):
    filepath = block['filepath']
    code = block['code']
    start_line = block['start_line']
    
    # Prepend newlines to align line numbers for tracebacks
    aligned_code = ("\n" * (start_line + 1)) + code
    
    # Compile the code block
    compiled_code = compile(aligned_code, filepath, "exec")
    
    # Create isolated namespace
    namespace = {
        "__name__": "__main__",
        "__file__": filepath,
        "client": mock_external_apis # Inject a dummy client for partial snippets
    }
    
    # Execute the code block
    exec(compiled_code, namespace)
