---
title: Technical Writer Workflow
---

# Technical Writer Workflow

A workflow for drafting a CSR results and safety section, an Investigator's Brochure summary of changes, and an SAE reporting SOP.

## Workflow Diagram

```mermaid
graph TD
    Input_study_context[Input: study_context] --> Steps
    Input_sponsor_requirements[Input: sponsor_requirements] --> Steps
    csr_section[Step: csr_section]
    ib_summary[Step: ib_summary]
    sae_sop[Step: sae_sop]
    Input_study_context --> sae_sop
    Input_sponsor_requirements --> sae_sop
```

[View Source YAML](../../workflows/technical/technical_writer.workflow.yaml)
