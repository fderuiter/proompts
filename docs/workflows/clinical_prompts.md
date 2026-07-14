---
title: Clinical Prompts Workflow
---

# Clinical Prompts Workflow

A workflow to generate a CRF shell, audit it, and create a CDASH mapping guide.

## Workflow Diagram

```mermaid
graph TD
    INPUT_protocol_summary([Input: protocol_summary])
    INPUT_variable_list([Input: variable_list])
    crf_shell[crf_shell<br><i>01_crf_shell_generator.prompt.md</i>]
    INPUT_protocol_summary -. input .-> crf_shell
    crf_shell -->|sequential| quality_audit
    quality_audit[quality_audit<br><i>02_crf_quality_auditor.prompt.md</i>]
    crf_shell -. input .-> quality_audit
    quality_audit -->|sequential| cdash_mapping
    cdash_mapping[cdash_mapping<br><i>03_cdash_mapping_completion_guide.prompt.md</i>]
    INPUT_variable_list -. input .-> cdash_mapping
```


