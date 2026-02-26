---
title: Real-Time Adjudication Visibility Dashboard
---

# Real-Time Adjudication Visibility Dashboard

Design a dashboard that provides real-time visibility into clinical endpoint adjudication workflows.

[View Source YAML](../../../../../prompts/clinical/adjudication/adjudication_workflow/01_real_time_adjudication_dashboard.prompt.yaml)

```yaml
---
name: Real-Time Adjudication Visibility Dashboard
version: 0.1.0
description: Design a dashboard that provides real-time visibility into clinical endpoint adjudication workflows.
metadata:
  domain: clinical
  complexity: medium
  tags:
  - adjudication
  - real-time
  - visibility
  - dashboard
  requires_context: true
variables: []
model: gpt-4
modelParameters:
  temperature: 0.2
messages:
- role: system
  content: '- Phase III cardiovascular device study with ~950 suspected events across 120 sites.

    - A blinded Clinical Events Committee adjudicates each event.

    - Stakeholders need immediate insight into blocked events and next actions.


    Ask clarifying questions if any requirement is unclear before producing the dashboard description.'
- role: user
  content: "1. Draft a textual workflow diagram from site submission to final CEC decision.\n2. Define the minimal data model\
    \ for a role-based dashboard showing:\n   - event aging in days\n   - disagreement rate\n   - percentage of dossiers missing\
    \ required documents\n   - adjudicator workload\n3. List five automated alerts or reminders that reduce turnaround time.\n\
    4. Recommend two commercial or open-source eAdjudication platforms and justify the choice.\n\nOutput format:\n- **Section\
    \ 1:** Workflow diagram\n- **Section 2:** Dashboard data model (table)\n- **Section 3:** Alert rules (bullets)\n- **Section\
    \ 4:** Platform recommendations (table)"
testData:
- input: ''
  expected: '- **Section 1:** Workflow diagram

    - **Section 2:** Dashboard data model (table)

    - **Section 3:** Alert rules (bullets)

    - **Section 4:** Platform recommendations (table)'
evaluators:
- name: Output includes 'Section 1:'
  string:
    contains: 'Section 1:'

```
