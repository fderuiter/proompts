# Mason's Journal

## Critical Learnings

- **Skeleton Prompts lack Robustness**: Many early or "low complexity" prompts in the repository (e.g., in `prompts/technical/architecture/`) were created as barebones skeletons without XML delimiters around variables (`{{var}}`), `testData`, or `evaluators`. This leads to prompt injection risks, poor LLM performance due to lack of constraints, and failures when running `validate_prompt_schema.py --strict`. All prompts must have explicitly bounded inputs, specific persona roles, defined output formats, and executable test cases.
