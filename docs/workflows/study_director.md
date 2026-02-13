---
layout: default
title: Study Director Workflow
parent: Workflows
nav_order: 99
---

# Study Director Workflow

A workflow for drafting a GLP-compliant study protocol, auditing raw data, and generating an executive summary.

## Workflow Diagram\n\n<div class="mermaid">\ngraph TD
    Input_protocol_basics[Input: protocol_basics] --> Steps
    Input_data_csv[Input: data_csv] --> Steps
    Input_report_sections[Input: report_sections] --> Steps
    draft_protocol[Step: draft_protocol]
    Input_protocol_basics --> draft_protocol
    audit_data[Step: audit_data]
    Input_data_csv --> audit_data
    executive_summary[Step: executive_summary]
    Input_report_sections --> executive_summary\n</div>\n
[View Source YAML](../../workflows/management/study_director.workflow.yaml)
