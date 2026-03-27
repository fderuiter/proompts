# Mason's Journal

## Critical Learnings

- **Skeleton Prompts lack Robustness**: Many early or "low complexity" prompts in the repository (e.g., in `prompts/technical/architecture/`) were created as barebones skeletons without XML delimiters around variables (`{{var}}`), `testData`, or `evaluators`. This leads to prompt injection risks, poor LLM performance due to lack of constraints, and failures when running `validate_prompt_schema.py --strict`. All prompts must have explicitly bounded inputs, specific persona roles, defined output formats, and executable test cases.
# Mason's Journal - Critical Learnings

## Prompt Engineering
- Generic prompts without strict `<input>` boundaries and clear JSON or Markdown output formats lead to higher hallucination rates and prompt injection vulnerabilities.
- Prompts need to have `few-shot` test cases (at least 2) that evaluate both a "happy path" and a negative/injection path to ensure robustness.
- Persona injection is critical: specialized roles heavily outperform generic "helpful assistant" personas.

## Evaluators
- Evaluators should test the explicit constraints laid out in the prompt instructions, ideally utilizing `regex` matching.
