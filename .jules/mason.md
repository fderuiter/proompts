# Mason's Journal 🧱

## Critical Learnings

### Schema Limitations
- **Global Evaluators:** The current schema applies `evaluators` globally to all `testData` cases. This prevents negative assertions (e.g., "Ensure no vulnerability is found") from being used alongside positive assertions (e.g., "Ensure vulnerability IS found") in the same prompt file. *Workaround:* Use `expected` field in `testData` for specific assertions and keep `evaluators` for structural checks that apply to all outputs.
