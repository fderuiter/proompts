# Prompt Best Practices Guide

This guide outlines best practices for creating high-quality prompts in this repository.

## Prompt File Structure

All prompts must be stored as `.prompt.yaml` or `.prompt.yml` files following this structure:

### Required Fields

1. **`name`** (string) - Short, descriptive title for the prompt
   - Use title case
   - Be specific and clear
   - Example: "Risk Assessment Expert" or "Code Review Assistant"

2. **`description`** (string) - Concise summary of what the prompt does
   - 1-2 sentences maximum
   - Describe the purpose and expected outcome
   - Example: "Provide a comprehensive biocompatibility risk assessment for a specified device."

3. **`model`** (string) - Model identifier to use
   - Examples: `gpt-4o`, `gpt-4o-mini`, `claude-3-5-sonnet-20241022`
   - Choose based on task complexity

4. **`modelParameters`** (object) - Model configuration
   - **`temperature`** (float) - Controls randomness (0.0-2.0)
     - 0.0-0.3: Deterministic, factual tasks
     - 0.4-0.7: Balanced creativity and consistency
     - 0.8-1.0+: Creative, varied outputs

5. **`messages`** (array) - Ordered list of message objects
   - Must have at least 2 messages (typically system + user)
   - Each message has:
     - **`role`** (string): "system", "user", or "assistant"
     - **`content`** (string): The message text
   - Use `{{variable_name}}` for runtime placeholders
   - Use YAML multi-line strings (`|` or `|-`) for readability

6. **`testData`** (array) - Sample inputs with expected outputs
   - **Best Practice**: Include at least 2 test cases per prompt
   - Each test case should have:
     - Input variables matching `{{placeholders}}` in messages
     - `expected` output description or example
   - Use realistic, meaningful examples (not just placeholders)

7. **`evaluators`** (array) - Validation rules for outputs
   - **Best Practice**: Include at least 1 evaluator per prompt
   - Common evaluator types:
     - `string.startsWith`: Check output begins with expected text
     - `string.contains`: Check output includes required content
     - `string.endsWith`: Check output ends with expected text
   - Each evaluator has:
     - **`name`** (string): Description of what it checks
     - **`string`** (object): The validation rule

## Best Practices

### 1. Clear Instructions

- Make system messages precise and actionable
- Specify the expected output format explicitly
- Include constraints or requirements upfront
- Break complex tasks into numbered steps

**Good Example:**
```yaml
messages:
  - role: system
    content: |-
      You are a senior biological safety consultant. Apply ISO 10993 and ISO 14971.
      
      Focus on clear, actionable steps.
  - role: user
    content: |-
      1. Identify potential biological hazards.
      2. Evaluate likelihood and severity of each hazard.
      3. Recommend testing strategies and mitigation controls.
      4. Provide a structured summary table.
```

### 2. Meaningful Variables

- Use descriptive variable names: `{{device_type}}` not `{{input}}`
- Document expected variables in the user message
- Keep variable naming consistent across related prompts

**Good Example:**
```yaml
content: |-
  Inputs:
  - `{{medical_device_type}}` — description of the device
  - `{{intended_use}}` — clinical purpose of the device
```

### 3. Comprehensive Test Data

- Provide realistic examples, not placeholders
- Test edge cases and typical use cases
- Include expected outputs that demonstrate desired format

**Bad Example:**
```yaml
testData:
  - input: "example input"
    expected: "example output"
```

**Good Example:**
```yaml
testData:
  - medical_device_type: "Silicone-coated intravascular catheter for central venous access"
    intended_use: "Long-term medication delivery in oncology patients"
    expected: |-
      | Hazard | Likelihood | Severity | Testing | Mitigation |
      | --- | --- | --- | --- | --- |
      | Cytotoxicity | Medium | High | ISO 10993-5 | Validated biocompatible silicone |
```

### 4. Effective Evaluators

- Use evaluators to verify critical output characteristics
- Check for required structure, not exact text matches
- Combine multiple evaluators for complex outputs

**Good Example:**
```yaml
evaluators:
  - name: Output starts with a markdown table row
    string:
      startsWith: '|'
  - name: Output contains hazard assessment
    string:
      contains: 'Hazard'
  - name: Output includes mitigation strategies
    string:
      contains: 'Mitigation'
```

### 5. Temperature Selection

Choose temperature based on task type:

- **0.0-0.2**: Code generation, data extraction, factual answers
- **0.3-0.5**: Technical documentation, analysis, structured outputs
- **0.6-0.8**: Creative writing, brainstorming, varied responses
- **0.9-1.5**: Poetry, highly creative tasks, maximum variety

## YAML Formatting

### Multi-line Strings

Use appropriate YAML block scalars:

- `|` (literal) - Preserves line breaks and trailing newline
- `|-` (literal, strip) - Preserves line breaks, removes trailing newline
- `>` (folded) - Joins lines, adds single newline at end
- `>-` (folded, strip) - Joins lines, no trailing newline

**Example:**
```yaml
messages:
  - role: system
    content: |-
      You are an expert.
      Line breaks are preserved.
  - role: user
    content: >
      This text will be folded into a single line.
      Good for paragraphs.
```

### Variable Placeholders

Always use double curly braces with no extra formatting:
- ✅ `{{variable_name}}`
- ❌ `{variable_name}`
- ❌ `${{variable_name}}`
- ❌ `` `{{variable_name}}` ``

## Common Pitfalls

### ❌ Empty Test Data
```yaml
testData: []
evaluators: []
```

### ✅ Meaningful Test Data
```yaml
testData:
  - code_snippet: "function add(a, b) { return a + b }"
    expected: "Code review with suggestions for type safety and documentation"
evaluators:
  - name: Review includes improvement suggestions
    string:
      contains: "suggest"
```

### ❌ Vague Instructions
```yaml
content: "Analyze this: {{input}}"
```

### ✅ Specific Instructions
```yaml
content: |-
  Analyze the following code snippet for:
  1. Security vulnerabilities
  2. Performance issues
  3. Code style violations
  
  Code:
  ```
  {{code_snippet}}
  ```
  
  Output format: Markdown with sections for each category.
```

## Validation

Before committing, validate your prompts:

```bash
# Run all validation checks
python3 tools/scripts/test_all.py

# Just validate schema
python3 tools/scripts/validate_prompt_schema.py

# Check YAML syntax
yamllint prompts/**/*.prompt.yaml
```

## Resources

- [Template Prompt](template_prompt.prompt.yaml) - Reference example
- [Workflows Documentation](workflows.md) - Chaining prompts together
- [Repository README](../README.md) - General guidance
