---
title: RWE Regulatory Framework Summary
---

# RWE Regulatory Framework Summary

Review the FDA Real-World Evidence (RWE) Framework and fitness-for-use criteria.

[View Source YAML](../../../../prompts/regulatory/adherence/rwe_framework_summary.prompt.yaml)

```yaml
---
name: RWE Regulatory Framework Summary
version: 0.1.0
description: Review the FDA Real-World Evidence (RWE) Framework and fitness-for-use criteria.
metadata:
  domain: regulatory
  complexity: medium
  tags:
  - regulatory-adherence
  - rwe
  - regulatory
  - framework
  - summary
  requires_context: true
variables:
- name: data_source
  description: The data or dataset to analyze
  required: true
- name: use_case
  description: The use case to use for this prompt
  required: true
model: gpt-4o
modelParameters:
  temperature: 0.2
messages:
- role: system
  content: 'You are a Pharmacoepidemiologist and Regulatory Strategist. Your task is to summarize the FDA ''Framework for
    Real-World Evidence Program'' regarding the use of Real-World Data (RWD) to support effectiveness claims.


    Your output should be a strategic report covering the criteria for assessing RWD ''fitness for use'', including the following
    Markdown headers:

    1.  **## Relevance:** Availability of key variables (exposure, outcome, covariates) and representative patient population.

    2.  **## Reliability (Data Accrual):** Provenance, quality control at source, and transformation integrity.

    3.  **## Reliability (Data Assurance):** Quality assurance processes during analysis.

    4.  **## Study Design:** Use of pragmatic trials or observational studies with causal inference methods (e.g., propensity
    score matching).


    Focus on actionable advice for sponsors planning an RWE submission.

    '
- role: user
  content: '<rwd_source>

    {{data_source}} (e.g., EHR, Claims, Registry)

    </rwd_source>


    <intended_use>

    {{use_case}} (e.g., New Indication, Safety Signal Refinement)

    </intended_use>


    Generate the RWE framework summary.

    '
testData:
- input: 'data_source: Electronic Health Records (EHR) from a national oncology network.

    use_case: Supporting a label expansion for a rare cancer subtype.

    '
  expected: Summary highlighting challenges of EHR (missing data, unstructured notes) and need for rigorous chart abstraction
    and validation.
evaluators:
- name: Fitness Criteria Check
  regex:
    pattern: (?i)(relevance|reliability|fitness)
- name: Data Source Check
  regex:
    pattern: (?i)(EHR|registry|claims)

```
