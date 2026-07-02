# Defining Skills

This guide explains how to define new skill-based tools and configure their input parameters so they can be recognized by the MCP server and correctly exposed to the AI.

## 1. Syntax and Manifest Placement

Skills are defined within markdown manifest files (e.g., `skills.md`) located in the `prompts` directory.

### Skill Header
A skill is identified by a specific markdown header format. The system registers a new skill whenever it encounters a heading that begins with:

```markdown
## Skill: <Skill Name>
```

### Embedding Metadata
To define input parameters for your skill, embed an HTML comment containing JSON metadata anywhere within the body of the skill block. 

The required syntax for this comment is exactly:
```html
<!-- VALIDATION_METADATA: [...] -->
```

This JSON array configures the tool schema that the AI will use to pass inputs.

## 2. Supported JSON Fields

The JSON block embedded in the `VALIDATION_METADATA` comment represents an array of objects. Each object maps to an `InputVariable` definition. The following fields are supported:

- **`name` (String, Mandatory):** The identifier for the parameter. If this field is missing or falsy, the parameter is entirely ignored and skipped during tool registration. **This is the *only* mandatory requirement for functionality.**
- **`description` (String, Optional):** Instructions guiding the AI on how to provide this value. If omitted, the system falls back to `"The {name} input."`.
- **`required` (Boolean, Optional):** Indicates whether the AI must provide a value for this parameter. If omitted, it defaults to `true`.
- **`default` (Any, Optional):** A fallback value that will be used if the AI omits the parameter.
- **`type` (String, Optional):** The data type of the input (e.g., `"string"`, `"number"`, `"boolean"`). *Note: The MCP server currently hardcodes `"type": "string"` for all tool schemas it exposes to the LLM. Setting this field won't change the schema exposed to the LLM, though it is supported by the internal model.*

## 3. Fallback Behavior

When the system parses a skill block, metadata extraction silently handles errors:

- **Missing Block:** If no `<!-- VALIDATION_METADATA: ... -->` comment exists within the skill body, the system defaults to an empty variable list (`[]`).
- **Malformed JSON:** If the comment exists but contains invalid JSON (e.g., missing quotes, trailing commas), the decoding step fails silently. The system falls back to an empty variable list (`[]`).

**Consequence:** In both fallback scenarios, the skill is still registered as an MCP tool for the AI, but its input schema will be completely empty (meaning it accepts no parameters). If you notice your skill is visible but won't accept inputs, ensure the metadata comment is present and contains valid JSON.

## 4. Multi-parameter Example

Below is an illustrative example of a multi-parameter skill as it should appear in a manifest file:

```markdown
## Skill: SearchDatabase

### Description
This skill searches the local database.

<!-- VALIDATION_METADATA: [
  {
    "name": "search_query",
    "description": "The text to search for.",
    "required": true
  },
  {
    "name": "limit",
    "description": "Max results to return.",
    "required": false,
    "default": 10
  }
] -->

### Core Instructions
```text
[system]
Search for {{ search_query }} with limit {{ limit }}.
```
```
