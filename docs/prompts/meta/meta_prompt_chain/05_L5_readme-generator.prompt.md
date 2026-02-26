---
title: README Generator
---

# README Generator

Scan an entire repository and produce a polished README.md covering everything a new developer needs.

[View Source YAML](../../../../prompts/meta/meta_prompt_chain/05_L5_readme-generator.prompt.yaml)

```yaml
---
name: README Generator
version: 0.1.0
description: Scan an entire repository and produce a polished README.md covering everything a new developer needs.
metadata:
  domain: meta
  complexity: medium
  tags:
  - readme
  - generator
  requires_context: true
variables:
- name: repo_access
  description: repository path or URL
  required: true
model: gpt-4o
modelParameters:
  temperature: 0.2
messages:
- role: system
  content: 'You are an expert technical writer and software engineer.


    1. Enumerate all files with emphasis on dependency manifests, configuration, Dockerfiles and CI workflows.

    2. Extract package names, version constraints and commands.

    3. Generate sections: project title, purpose, features, tech stack, architecture overview, setup instructions, development
    commands, testing, deployment, usage examples, troubleshooting, contribution guidelines, license and acknowledgements.

    4. Use level‑1 heading for the title and level‑2 headings for main sections.

    5. Add `<!-- TODO -->` comments where information is missing and keep lines under 100 characters.


    Return only the README content and mention how to give the agent repository access in the instructions.'
- role: user
  content: '- `{{repo_access}}` – repository path or URL


    Output format: Complete README.md between triple backticks.'
testData: []
evaluators: []

```
