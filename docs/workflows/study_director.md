---
title: Study Director Workflow
---

# Study Director Workflow

A workflow for drafting a GLP-compliant study protocol, auditing raw data, and generating an executive summary.

## Workflow Diagram

```mermaid
graph TD
    classDef stepNode fill:#1a5f7a,stroke:var(--md-default-fg-color,var(--text-color,#0d3a4d)),stroke-width:2px,color:#ffffff;
    classDef inputNode fill:#2c5e43,stroke:var(--md-default-fg-color,var(--text-color,#183b27)),stroke-width:2px,color:#ffffff;
    INPUT_protocol_basics([Input: protocol_basics]):::inputNode
    INPUT_data_csv([Input: data_csv]):::inputNode
    INPUT_report_sections([Input: report_sections]):::inputNode
    draft_protocol[draft_protocol<br><i>01_draft_glp_compliant_study_protocol.prompt.md</i>]:::stepNode
    INPUT_protocol_basics -. protocol_basics .-> draft_protocol
    draft_protocol -->|sequential| audit_data
    audit_data[audit_data<br><i>02_audit_raw_data_capa_summary.prompt.md</i>]:::stepNode
    INPUT_data_csv -. data_csv .-> audit_data
    audit_data -->|sequential| executive_summary
    executive_summary[executive_summary<br><i>03_executive_summary_final_report.prompt.md</i>]:::stepNode
    INPUT_report_sections -. report_sections .-> executive_summary
    linkStyle default stroke:var(--md-default-fg-color,var(--text-color,#767676)),stroke-width:2px;
```


