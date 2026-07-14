---
title: Clinical Prompts Workflow
---

# Clinical Prompts Workflow

A workflow to generate a CRF shell, audit it, and create a CDASH mapping guide.

## Workflow Diagram

```mermaid
graph TD
    classDef stepNode fill:#1a5f7a,stroke:var(--md-default-fg-color,var(--text-color,#0d3a4d)),stroke-width:2px,color:#ffffff;
    classDef inputNode fill:#2c5e43,stroke:var(--md-default-fg-color,var(--text-color,#183b27)),stroke-width:2px,color:#ffffff;
    INPUT_protocol_summary([Input: protocol_summary]):::inputNode
    INPUT_variable_list([Input: variable_list]):::inputNode
    crf_shell[crf_shell<br><i>01_crf_shell_generator.prompt.md</i>]:::stepNode
    INPUT_protocol_summary -. input .-> crf_shell
    crf_shell -->|sequential| quality_audit
    quality_audit[quality_audit<br><i>02_crf_quality_auditor.prompt.md</i>]:::stepNode
    crf_shell -. input .-> quality_audit
    quality_audit -->|sequential| cdash_mapping
    cdash_mapping[cdash_mapping<br><i>03_cdash_mapping_completion_guide.prompt.md</i>]:::stepNode
    INPUT_variable_list -. input .-> cdash_mapping
    linkStyle default stroke:var(--md-default-fg-color,var(--text-color,#767676)),stroke-width:2px;
```


