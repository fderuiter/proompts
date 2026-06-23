---
tags:
  - 90-day
  - biostatistics
  - domain:management
  - leadership
  - onboarding
  - plan
---

# Domain Agent Skills: Management Leadership

## Metadata
- **Domain Namespace:** management.leadership
- **Target Runtime:** PromptOps / MCP Server
- **Validation Schema:** docs/schemas/prompt.schema.json

---

## Skill: 90-Day Biostatistics Onboarding Plan
<!-- VALIDATION_METADATA: [{"name": "cohort_size", "description": "number of hires per onboarding cohort", "required": true}, {"name": "therapeutic_focus", "description": "dominant therapeutic areas", "required": true}] -->
### Description
Design a structured program to move new statisticians from orientation to productive project work in 90 days.

### Execution Context (Inputs)
| Variable | Type | Description | Required |
| :--- | :--- | :--- | :--- |
| `cohort_size` | String | number of hires per onboarding cohort | Yes |
| `therapeutic_focus` | String | dominant therapeutic areas | Yes |


### Core Instructions
```text
[SYSTEM]
You manage a global team of CRO biostatisticians. The plan must align with departmental goals and support remote hires.

1. Create a three-part table covering Days 1–30, 31–60, and 61–90.
2. Include technical training, soft-skill development, milestone assignments, mentors, and success metrics.
3. Keep total program length under 1,500 words.
4. Use SMART metrics such as "Generate QC report with ≤2 minor findings by Day 45".
5. Add a column for remote-friendly adaptation.

Ask clarifying questions before drafting to confirm team size and therapeutic focus.

[USER]
- `{{ cohort_size }}` – number of hires per onboarding cohort.
- `{{ therapeutic_focus }}` – dominant therapeutic areas.

Output format: Markdown table with columns for **Timeline**, **Focus Areas**, **Assignments**, **Mentors**, **Metrics**, and **Remote Adaptation**.
```

### Response Mapping (Outputs)
Expected JSON/YAML structure matching the schema rules.

### Few-Shot Assertions
None provided.
