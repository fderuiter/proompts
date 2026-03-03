---
name: Prompt submission
about: Submit a new prompt or workflow to the repository
title: '[Prompt] '
labels: 'enhancement, prompt'
assignees: ''
---

**Prompt Description**
A clear and concise description of what the prompt does, its persona, and its intended use case.

**Category/Domain**
Where does this prompt belong? (e.g., `business/`, `clinical/`, `technical/`, `speculative/`, `google_jules/`)

**Variables Used**
List any `{{variables}}` used in the prompt and their purpose.

**Expected Output / Test Data**
Provide an example of what the model should output when given this prompt and specific test data.

**Checklist:**
- [ ] I have read the [CONTRIBUTING.md](../CONTRIBUTING.md) guide.
- [ ] My prompt follows the schema defined in `docs/template_prompt.prompt.yaml`.
- [ ] I have included realistic `testData` with at least 1-2 examples.
- [ ] I have included `evaluators` to validate output quality.
- [ ] The prompt temperature is appropriately tuned for its persona (Strict = 0.1, Creative = 0.7+).

**Additional context**
Add any other context, related issues, or specific model recommendations (e.g., gpt-4o, gemini-3-pro) here.
