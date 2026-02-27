---
title: Clinical Prompts Workflow
---

# Clinical Prompts Workflow

A workflow to generate a CRF shell, audit it, and create a CDASH mapping guide.

## Workflow Diagram

```mermaid
graph TD
    Input_protocol_summary[Input: protocol_summary] --> Steps
    Input_variable_list[Input: variable_list] --> Steps
    crf_shell[Step: crf_shell]
    Input_protocol_summary --> crf_shell
    quality_audit[Step: quality_audit]
    crf_shell --> quality_audit
    cdash_mapping[Step: cdash_mapping]
    Input_variable_list --> cdash_mapping
```

[View Source YAML](https://github.com/fderuiter/proompts/blob/main/workflows/clinical/clinical_prompts.workflow.yaml)
