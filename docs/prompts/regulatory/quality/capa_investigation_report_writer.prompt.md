---
title: CAPA Investigation Report Writer
---

# CAPA Investigation Report Writer

Draft a formal CAPA investigation report for regulatory review.

[View Source YAML](../../../../prompts/regulatory/quality/capa_investigation_report_writer.prompt.yaml)

```yaml
---
name: CAPA Investigation Report Writer
version: 0.1.0
description: Draft a formal CAPA investigation report for regulatory review.
metadata:
  domain: regulatory
  complexity: high
  tags:
  - quality
  - capa
  - investigation
  - report
  - writer
  requires_context: false
variables:
- name: actions_taken
  description: The actions taken to use for this prompt
  required: true
- name: effectiveness_check
  description: The effectiveness check to use for this prompt
  required: true
- name: incident_summary
  description: A summary of the key information
  required: true
- name: root_cause
  description: The root cause to use for this prompt
  required: true
model: gpt-4o
modelParameters:
  temperature: 0.2
messages:
- role: system
  content: Act as a Technical Regulatory Writer. Your task is to write a formal CAPA Investigation Report based on rough notes
    provided by the user. The report must be objective, concise, and professional, avoiding emotional language or speculation.
    It must be ready for review by auditors or regulators.
- role: user
  content: 'Please write a formal CAPA Investigation Report based on the following rough notes:


    **Incident:** <incident_summary>{{incident_summary}}</incident_summary>

    **Root Cause Found:** <root_cause>{{root_cause}}</root_cause>

    **Actions Taken:** <actions_taken>{{actions_taken}}</actions_taken>

    **Effectiveness Check:** <effectiveness_check>{{effectiveness_check}}</effectiveness_check>


    Please structure this into a final report format with the following headers:

    1. **Background**

    2. **Investigation Methodology**

    3. **Root Cause Conclusion**

    4. **Corrective Action Plan**

    5. **Effectiveness Verification Criteria**'
testData:
- input:
    incident_summary: 'Labeling machine X misprinted batch #123 with the wrong expiration date.'
    root_cause: The operator manually entered the date instead of scanning the work order barcode, leading to a typo.
    actions_taken: Updated the machine software to require barcode scanning; disabled manual entry for critical fields. Retrained
      all operators.
    effectiveness_check: Monitored the next 5 production runs; 100% of labels matched the work order.
  expected: Investigation Methodology
evaluators:
- name: Background
  regex:
    pattern: (?i)Background
- name: Investigation Methodology
  regex:
    pattern: (?i)Investigation Methodology
- name: Root Cause Conclusion
  regex:
    pattern: (?i)Root Cause Conclusion
- name: Corrective Action Plan
  regex:
    pattern: (?i)Corrective Action Plan
- name: Effectiveness Verification Criteria
  regex:
    pattern: (?i)Effectiveness Verification Criteria

```
