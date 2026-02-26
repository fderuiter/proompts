---
title: Documentation and Repository Structure Implementation
---

# Documentation and Repository Structure Implementation

Implement foundational improvements for the repository's structure and documentation.

[View Source YAML](../../../../prompts/technical/repository_refactoring/documentation_structure_implementation.prompt.yaml)

```yaml
---
name: Documentation and Repository Structure Implementation
version: 0.1.0
description: Implement foundational improvements for the repository's structure and documentation.
metadata:
  domain: technical
  complexity: high
  tags:
  - repository-refactoring
  - documentation
  - repository
  - structure
  - implementation
  requires_context: true
variables: []
model: gpt-4
modelParameters:
  temperature: 0.2
messages:
- role: system
  content: You are a Senior Developer implementing foundational improvements for a repository's structure and documentation.
- role: user
  content: "As a Senior Developer, your task is to implement foundational improvements to this repository's structure and\
    \ documentation, based on a prior analysis. You must provide the complete, final content for each new or updated file.\n\
    \nYour implementation must include the following actions:\n\n1.  **Revamp README.md:**\n    *   Create a comprehensive\
    \ guide that includes:\n        *   A clear project purpose statement.\n        *   Step-by-step installation and setup\
    \ instructions.\n        *   Usage examples for the project's key features.\n        *   Clear contribution guidelines,\
    \ linking to `CONTRIBUTING.md`.\n\n2.  **Reorganize Directory Structure:**\n    *   Reorganize the project files into\
    \ a logical, conventional, and scalable directory structure.\n    *   Use standard conventions where applicable (e.g.,\
    \ `/src` for source code, `/tests` for tests, `/docs` for documentation, `/scripts` for utility scripts).\n    *   Provide\
    \ a list of `mv` commands that represent the file movements.\n\n3.  **Create/Improve Meta-Files:**\n    *   **`.gitignore`**:\
    \ Create a robust `.gitignore` file appropriate for the project's language and ecosystem.\n    *   **`CONTRIBUTING.md`**:\
    \ Create a `CONTRIBUTING.md` that outlines the process for contributing, including how to run tests, coding standards,\
    \ and the pull request process.\n    *   **`LICENSE`**: Add an appropriate open-source license file (e.g., MIT, Apache\
    \ 2.0).\n\n**Output Format:**\nFor each file you create or modify, provide the complete file content within a separate,\
    \ clearly labeled markdown code block. For the directory reorganization, provide the list of `mv` commands."
testData: []
evaluators: []

```
