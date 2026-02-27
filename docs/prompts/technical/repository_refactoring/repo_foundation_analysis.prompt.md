---
title: Repository Foundation & Developer Experience Analysis
---

# Repository Foundation & Developer Experience Analysis

Analyze the repository's foundation and developer experience to prepare it for future growth and easy onboarding.

[View Source YAML](https://github.com/fderuiter/proompts/blob/main/prompts/technical/repository_refactoring/repo_foundation_analysis.prompt.yaml)

```yaml
---
name: Repository Foundation & Developer Experience Analysis
version: 0.1.0
description: Analyze the repository's foundation and developer experience to prepare it for future growth and easy onboarding.
metadata:
  domain: technical
  complexity: high
  tags:
  - repository-refactoring
  - repository
  - foundation
  - developer
  - experience
  requires_context: true
variables: []
model: gpt-4
modelParameters:
  temperature: 0.2
messages:
- role: system
  content: You are a Senior Staff Engineer tasked with analyzing a repository's foundation and developer experience.
- role: user
  content: "As a Senior Staff Engineer, your task is to conduct a thorough analysis of the repository's foundation and developer\
    \ experience. Your goal is to produce a detailed and actionable report section for a `REPO_HEALTH_ANALYSIS.md` file.\n\
    \nYour analysis must cover the following areas, with specific, actionable recommendations for each:\n\n1.  **README.md\
    \ Evaluation:**\n    *   Assess its clarity, completeness, and accuracy for a new developer.\n    *   Verify that it includes\
    \ a clear \"getting started\" guide (local setup, running tests, etc.).\n    *   If improvements are needed, provide a\
    \ complete, revised `README.md` content block.\n\n2.  **Essential Meta-Files Audit:**\n    *   Check for the existence\
    \ and quality of `.gitignore`, `LICENSE`, and `CONTRIBUTING.md`.\n    *   For each file, suggest specific improvements\
    \ or provide a complete, robust version if one is missing or inadequate.\n\n3.  **Directory Structure Assessment:**\n\
    \    *   Evaluate the current structure for logical conventions, scalability, and maintainability.\n    *   If improvements\
    \ are needed, propose a clear, refactored directory structure and explain the rationale (e.g., separating `/src`, `/tests`,\
    \ and `/docs`).\n\n**Output Format:**\nYour final output must be a single markdown section with clear, well-defined headings\
    \ for each part of the analysis. For any proposed new file content, present it within a markdown code block."
testData: []
evaluators: []

```
