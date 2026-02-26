---
title: Dependencies & Security Posture Analysis
---

# Dependencies & Security Posture Analysis

Perform a thorough audit of the repository's dependencies and overall security posture to identify and mitigate risks.

[View Source YAML](../../../../prompts/technical/repository_refactoring/dependencies_security_analysis.prompt.yaml)

```yaml
---
name: Dependencies & Security Posture Analysis
version: 0.1.0
description: Perform a thorough audit of the repository's dependencies and overall security posture to identify and mitigate
  risks.
metadata:
  domain: technical
  complexity: high
  tags:
  - repository-refactoring
  - dependencies
  - security
  - posture
  - analysis
  requires_context: true
variables: []
model: gpt-4
modelParameters:
  temperature: 0.2
messages:
- role: system
  content: You are a Security and DevOps specialist performing a thorough audit of a repository's dependencies and overall
    security posture.
- role: user
  content: "As a Security and DevOps specialist, you must perform a thorough audit of the repository's dependencies and overall\
    \ security posture to identify and mitigate risks.\n\nYour audit must cover the following areas, providing a prioritized\
    \ list of vulnerabilities and actionable recommendations:\n\n1.  **Dependency Audit:**\n    *   Use a dependency scanning\
    \ tool to identify all third-party dependencies with known vulnerabilities (CVEs).\n    *   For each vulnerable dependency,\
    \ specify the package, the vulnerability, and the recommended version to patch to.\n    *   Identify any deprecated or\
    \ unmaintained packages and suggest modern, secure alternatives.\n\n2.  **Secrets Scanning:**\n    *   Scan the entire\
    \ codebase for hardcoded secrets, API keys, or other credentials.\n    *   For each finding, specify the file and line\
    \ number, and provide a clear recommendation for externalizing it (e.g., using environment variables, a secrets management\
    \ tool).\n\n3.  **Static Application Security Testing (SAST):**\n    *   Scan the codebase for common security flaws such\
    \ as SQL injection, Cross-Site Scripting (XSS), and insecure direct object references.\n    *   For each potential flaw,\
    \ provide the file and code snippet, and explain the potential impact and how to remediate it.\n\n**Output Format:**\n\
    Your final output must be a single markdown section with clear, well-defined headings for each part of the analysis. Findings\
    \ should be presented in a table format where applicable (e.g., for dependencies), ordered by severity (Critical, High,\
    \ Medium, Low).\n\nExample Structure:\n```markdown\n### Dependency Audit\n| Package | Vulnerability | Severity | Recommendation\
    \ |\n|---|---|---|---|\n| ... | ... | ... | ... |\n\n### Secrets Scanning\n*   **File:** `src/config.js:12`, **Secret:**\
    \ Hardcoded API Key, **Recommendation:** Move to environment variable `API_KEY`.\n```"
testData: []
evaluators: []

```
