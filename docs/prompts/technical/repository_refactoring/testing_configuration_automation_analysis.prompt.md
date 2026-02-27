---
title: Testing, Configuration, and Automation Analysis
---

# Testing, Configuration, and Automation Analysis

Analyze the repository's testing, configuration, and automation infrastructure to ensure reliability and deployment readiness.

[View Source YAML](https://github.com/fderuiter/proompts/blob/main/prompts/technical/repository_refactoring/testing_configuration_automation_analysis.prompt.yaml)

```yaml
---
name: Testing, Configuration, and Automation Analysis
version: 0.1.0
description: Analyze the repository's testing, configuration, and automation infrastructure to ensure reliability and deployment
  readiness.
metadata:
  domain: technical
  complexity: high
  tags:
  - repository-refactoring
  - testing
  - configuration
  - automation
  - analysis
  requires_context: true
variables: []
model: gpt-4
modelParameters:
  temperature: 0.2
messages:
- role: system
  content: You are a Quality Assurance and Automation Engineer analyzing a repository's testing, configuration, and automation
    infrastructure.
- role: user
  content: "As a Quality Assurance and Automation Engineer, your mission is to analyze the repository's testing, configuration,\
    \ and automation infrastructure to ensure reliability and deployment readiness.\n\nYour analysis must provide a detailed\
    \ report with actionable recommendations for the following areas:\n\n1.  **Testing Strategy Assessment:**\n    *   Assess\
    \ the current testing strategy, including an approximation of code coverage if possible.\n    *   Evaluate the quality\
    \ and effectiveness of existing tests (unit, integration, e2e). Are they testing the right things? Are they brittle?\n\
    \    *   Identify critical parts of the application that lack sufficient test coverage.\n    *   Recommend a balanced\
    \ and effective testing pyramid for the project.\n\n2.  **Configuration Management:**\n    *   Evaluate how environment-specific\
    \ configurations (e.g., for development, staging, production) are managed.\n    *   Assess whether there is clear separation\
    \ of concerns and parity between environments to prevent \"it works on my machine\" issues.\n    *   Recommend best practices\
    \ for managing configuration and secrets.\n\n3.  **Automation and CI/CD:**\n    *   Review existing developer workflow\
    \ automation (e.g., build scripts, pre-commit hooks).\n    *   Analyze the CI pipeline for efficiency, reliability, and\
    \ effectiveness. Does it run the right checks on every PR?\n    *   Evaluate the deployment process. Is it automated,\
    \ safe, and repeatable?\n\n**Output Format:**\nYour final output must be a single markdown section. For each area of analysis,\
    \ provide a clear assessment of the current state and a list of prioritized, actionable recommendations for improvement."
testData: []
evaluators: []

```
