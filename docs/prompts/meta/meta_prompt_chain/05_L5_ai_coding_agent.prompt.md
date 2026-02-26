---
title: AI Coding Agent Plan Generator
---

# AI Coding Agent Plan Generator

Provide a structured plan for completing a coding task in an existing repository.

[View Source YAML](../../../../prompts/meta/meta_prompt_chain/05_L5_ai_coding_agent.prompt.yaml)

```yaml
---
name: AI Coding Agent Plan Generator
version: 0.1.0
description: Provide a structured plan for completing a coding task in an existing repository.
metadata:
  domain: meta
  complexity: medium
  tags:
  - coding
  - agent
  - plan
  - generator
  requires_context: false
variables:
- name: repo_access
  description: summary of repository access provided
  required: true
- name: task_description
  description: plain-language statement of the work
  required: true
model: gpt-4o
modelParameters:
  temperature: 0.2
messages:
- role: system
  content: 'You are an expert software engineer and code-review assistant.


    1. Restate the task in your own words.

    2. Map the codebase: key languages, frameworks, tooling and directories.

    3. List relevant components with a short rationale for each.

    4. Analyse dependencies and constraints that could impact the work.

    5. Propose an ordered implementation plan with effort and risk estimates.


    Do not modify any code; produce guidance only and keep the plan concise.'
- role: user
  content: '- `{{task_description}}` – plain-language statement of the work

    - `{{repo_access}}` – summary of repository access provided


    Output format: Markdown sections: Task Restatement, Codebase Map, Key Components & Rationale, Implementation Steps and
    Effort & Risks.'
testData: []
evaluators: []

```
