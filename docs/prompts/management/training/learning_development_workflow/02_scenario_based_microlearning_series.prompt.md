---
title: Scenario-Based Microlearning Series
---

# Scenario-Based Microlearning Series

Design short interactive modules that help CRO staff apply GCP principles correctly during site visits.

[View Source YAML](../../../../../prompts/management/training/learning_development_workflow/02_scenario_based_microlearning_series.prompt.yaml)

```yaml
---
name: Scenario-Based Microlearning Series
version: 0.1.0
description: Design short interactive modules that help CRO staff apply GCP principles correctly during site visits.
metadata:
  domain: management
  complexity: medium
  tags:
  - training
  - scenario-based
  - microlearning
  - series
  requires_context: false
variables:
- name: audience_role
  description: primary learner roles (e
  required: true
model: gpt-4o
modelParameters:
  temperature: 0.2
messages:
- role: system
  content: 'Recent audits show increased protocol deviations linked to poor application of GCP guidelines. Scenario-based
    practice improves knowledge transfer.


    1. List three high-risk violation themes to target and explain why.

    2. Outline one complete sample module with scenario synopsis, branching decision points, feedback logic, and regulatory
    citations.

    3. After approval, create briefs for the remaining five modules.

    4. Incorporate adult-learning techniques such as retrieval practice, spaced repetition, and immediate feedback.

    5. Design for mobile-first LMS (SCORM 1.2) and specify metrics like completion and confidence ratings.


    Ask clarifying questions before step two if necessary.'
- role: user
  content: '- `{{audience_role}}` – primary learner roles (e.g., CRAs, Study Coordinators).


    Output format: Markdown sections titled **Violation Themes**, **Sample Module**, **Module Briefs**, and **Metrics**.'
testData: []
evaluators: []

```
