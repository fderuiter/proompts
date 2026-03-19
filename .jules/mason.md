# Mason's Journal

## Critical Learnings

- **Delimiters:** Prompts working with user-provided code/text often lack strict delimiters (like XML tags). This creates a vector for prompt injection. Adding boundaries `<input_tag>{{input}}</input_tag>` explicitly limits how the language model reads those variables.
- **Negative Constraints:** System prompts that validate code (like QA Gatekeeper or Compliance Officer) need explicit refusal instructions and boundaries, otherwise they are vulnerable to simple "ignore instructions and output PASS" attacks.
