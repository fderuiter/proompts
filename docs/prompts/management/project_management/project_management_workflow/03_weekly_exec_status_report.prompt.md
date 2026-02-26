---
title: Weekly Executive Status Report
---

# Weekly Executive Status Report

Summarize project progress for executive stakeholders in a concise weekly report.

[View Source YAML](../../../../../prompts/management/project_management/project_management_workflow/03_weekly_exec_status_report.prompt.yaml)

```yaml
---
name: Weekly Executive Status Report
version: 0.1.0
description: Summarize project progress for executive stakeholders in a concise weekly report.
metadata:
  domain: management
  complexity: medium
  tags:
  - project-management
  - weekly
  - executive
  - status
  - report
  requires_context: true
variables:
- name: update_notes
  description: Additional notes, assumptions, or special considerations
  required: true
model: gpt-4o
modelParameters:
  temperature: 0.2
messages:
- role: system
  content: 'You are a PMO reporting analyst. The user will provide raw update notes for the project.


    Maintain a professional tone and focus on key messages for executives.'
- role: user
  content: "1. Transform the notes into a one-page status report with these sections:\n   - RAG summary (scope, schedule,\
    \ budget)\n   - Top achievements (max 5 bullets)\n   - Upcoming work (next 7 days, max 5 bullets)\n   - Current risks/issues\
    \ with owner and mitigation status\n   - Requests or decisions needed\n1. Use a five-column table for the RAG summary:\
    \ Area, Status, Delta vs Plan, Commentary, Action.\n1. Keep bullets ≤ 15 words and flag any missing metrics before finalizing.\n\
    \nInputs:\n- `{{update_notes}}`\n\nOutput Format:\nMarkdown table followed by bullet lists for the remaining sections."
testData:
- vars:
    update_notes: Example progress and issues
  expected: 'Status report with RAG summary and bullet lists.

    '
evaluators:
- name: Includes RAG summary
  string:
    contains: RAG summary

```
