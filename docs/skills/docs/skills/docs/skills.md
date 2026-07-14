---
tags:
  - domain:general
  - skill
  - summarization
  - text-processing
---

# Domain Agent Skills: Docs

## Metadata
- **Domain Namespace:** docs
- **Target Runtime:** PromptOps / MCP Server
- **Validation Schema:** docs/schemas/prompt.schema.json

---

## Skill: Text Summarizer
<!-- VALIDATION_METADATA: {"variables": [{"name": "input", "description": "The text to summarize.", "required": true}], "metadata": {"domain": "general", "complexity": "low", "tags": ["summarization", "text-processing", "skill"], "requires_context": false}} -->
### Description
Summarizes input text concisely

### Execution Context (Inputs)
| Variable | Type | Description | Required |
| :--- | :--- | :--- | :--- |
| `input` | String | The text to summarize. | Yes |


### Core Instructions
```text
[SYSTEM]
You are a text summarizer. Your only job is to summarize text given to you.

[USER]
Summarize the given text, beginning with "Summary -":
<input>
{{ input }}
</input>
```

### Response Mapping (Outputs)
Expected JSON/YAML structure matching the schema rules.

### Few-Shot Assertions
Input Context: "The quick brown fox jumped over the lazy dog.
The dog was too tired to react.
"
Asserted Output: "Summary - A fox jumped over a lazy, unresponsive dog."
