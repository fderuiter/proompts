# Usage Guide

This guide provides examples of how to use the prompts in this repository.

## Using Prompts with an Agent

Most prompts are designed to be used with an LLM agent. You can load the prompt YAML file, parse it, and feed the `messages` to the LLM API (e.g., OpenAI, Anthropic).

### Python Example

```python
import yaml
import openai

def load_prompt(filepath):
    with open(filepath, 'r') as f:
        return yaml.safe_load(f)

def run_prompt(prompt_data, variables):
    messages = prompt_data['messages']
    # Replace placeholders
    for msg in messages:
        for key, value in variables.items():
            msg['content'] = msg['content'].replace(f"{{{{{key}}}}}", str(value))

    response = openai.chat.completions.create(
        model=prompt_data['model'],
        messages=messages,
        temperature=prompt_data['modelParameters'].get('temperature', 0.7)
    )
    return response.choices[0].message.content

# Example usage
prompt = load_prompt('prompts/technical/software_engineering/tasks/01_code_review.prompt.yaml')
result = run_prompt(prompt, {"code": "def foo(): pass"})
print(result)
```

## Using Prompts Manually

You can also copy the content of the `messages` field and paste it into ChatGPT or Claude. Remember to replace any `{{variable}}` placeholders with your actual data.

## Running Tests

To verify that a prompt behaves as expected, you can run the defined tests using a test runner (not included in this repo yet, but `testData` provides the cases).

Each prompt file may contain `testData` which lists input variables and expected output.

```yaml
testData:
  - input: |
      project_name: MyProject
    expected: |
      Repository Overview
```

## Search Prompts

You can search for prompts using the included script:

```bash
python3 tools/scripts/search_prompts.py "code review"
```

## Validation

Before submitting a new prompt, run the validation suite:

```bash
python3 tools/scripts/test_all.py
```
