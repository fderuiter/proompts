---
title: Study Director Workflow
---

# Study Director Workflow

A workflow for drafting a GLP-compliant study protocol, auditing raw data, and generating an executive summary.

## Workflow Diagram

```mermaid
graph TD
    INPUT_protocol_basics([Input: protocol_basics])
    INPUT_data_csv([Input: data_csv])
    INPUT_report_sections([Input: report_sections])
    draft_protocol[draft_protocol<br><i>01_draft_glp_compliant_study_protocol.prompt.md</i>]
    INPUT_protocol_basics -. protocol_basics .-> draft_protocol
    draft_protocol -->|sequential| audit_data
    audit_data[audit_data<br><i>02_audit_raw_data_capa_summary.prompt.md</i>]
    INPUT_data_csv -. data_csv .-> audit_data
    audit_data -->|sequential| executive_summary
    executive_summary[executive_summary<br><i>03_executive_summary_final_report.prompt.md</i>]
    INPUT_report_sections -. report_sections .-> executive_summary
```


