---
title: Project Charter and Scope Definition
---

# Project Charter and Scope Definition

Create a complete project charter summarizing background, objectives, scope, deliverables, and key risks.

[View Source YAML](../../../../../prompts/management/project_management/project_management_workflow/01_project_charter_scope.prompt.yaml)

```yaml
---
name: Project Charter and Scope Definition
version: 0.1.0
description: Create a complete project charter summarizing background, objectives, scope, deliverables, and key risks.
metadata:
  domain: management
  complexity: high
  tags:
  - project-management
  - project
  - charter
  - scope
  - definition
  requires_context: true
variables:
- name: budget
  description: '`{{deadline}}`'
  required: true
- name: business_outcome
  description: The business outcome to use for this prompt
  required: true
- name: deadline
  description: '`{{stakeholders}}`'
  required: true
- name: project_description
  description: '`{{budget}}`'
  required: true
- name: project_name
  description: '`{{project_description}}`'
  required: true
- name: stakeholders
  description: '`{{business_outcome}}`'
  required: true
model: gpt-4o
modelParameters:
  temperature: 0.2
messages:
- role: system
  content: 'You are a senior project-management consultant beginning a new initiative. The user will provide the project name,
    brief description, budget, deadline, stakeholders, and desired business outcome.


    Ensure the charter is concise and ready for executive review.'
- role: user
  content: '1. Draft the charter sections: Background, Objectives, In-Scope, Out-of-Scope, Major Deliverables, Success Criteria/KPIs,
    Assumptions, Constraints, Top Three Risks, Milestone Schedule, High-Level Budget Table, Approval Signatures.

    1. Use H2 section headings and a two-column table for the milestone schedule.

    1. Keep each paragraph under 120 words.

    1. Ask clarifying questions if any details are missing before you begin.


    Inputs:

    - `{{project_name}}`

    - `{{project_description}}`

    - `{{budget}}`

    - `{{deadline}}`

    - `{{stakeholders}}`

    - `{{business_outcome}}`


    Output Format:

    Markdown document with the sections listed above.'
testData:
- vars:
    project_name: Example Project
    project_description: Example description
    budget: 100k USD
    deadline: '2024-12-31'
    stakeholders: CEO, CTO
    business_outcome: Increase efficiency
  expected: 'Markdown document with sections including Background and Objectives.

    '
evaluators:
- name: Contains Background heading
  string:
    contains: Background

```
