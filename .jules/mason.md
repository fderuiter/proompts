# Mason's Journal - Critical Learnings

## Recurring Flaws Discovered
- **Unverified Prompts:** Prompts often lack `testData` and `evaluators`, meaning there is no way to automatically verify that the prompt behaves correctly or that its logic hasn't degraded. This violates the "Prompts are Code" philosophy.
- **Missing Delimiters:** Prompts taking large external document inputs (e.g., reports, codebase files) frequently fail to wrap the inputs in XML tags (e.g., `<market_report>{{market_report}}</market_report>`), leading to prompt injection risks and degraded model performance due to context confusion.
