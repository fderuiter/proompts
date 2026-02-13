# Study Director Workflow

A workflow for drafting a GLP-compliant study protocol, auditing raw data, and generating an executive summary.

## Visual Flow

```mermaid
flowchart TD
    subgraph Inputs [Global Inputs]
        inp_protocol_basics((protocol_basics))
        inp_data_csv((data_csv))
        inp_report_sections((report_sections))
    end
    draft_protocol["draft_protocol<br/><small>prompts/management/study_director/01_draft_glp_compliant_study_protocol.prompt.yaml</small>"]
    audit_data["audit_data<br/><small>prompts/management/study_director/02_audit_raw_data_capa_summary.prompt.yaml</small>"]
    executive_summary["executive_summary<br/><small>prompts/management/study_director/03_executive_summary_final_report.prompt.yaml</small>"]
    inp_protocol_basics -->|protocol_basics| draft_protocol
    inp_data_csv -->|data_csv| audit_data
    inp_report_sections -->|report_sections| executive_summary
```
