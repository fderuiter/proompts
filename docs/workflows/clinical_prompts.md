---
layout: default
title: Clinical Prompts Workflow
parent: Workflows
nav_order: 99
---

# Clinical Prompts Workflow

A workflow to generate a CRF shell, audit it, and create a CDASH mapping guide.

## Workflow Diagram\n\n<div class="mermaid">\ngraph TD
    Input_protocol_summary[Input: protocol_summary] --> Steps
    Input_variable_list[Input: variable_list] --> Steps
    crf_shell[Step: crf_shell]
    Input_protocol_summary --> crf_shell
    quality_audit[Step: quality_audit]
    crf_shell --> quality_audit
    cdash_mapping[Step: cdash_mapping]
    Input_variable_list --> cdash_mapping\n</div>\n
[View Source YAML](../../workflows/clinical/clinical_prompts.workflow.yaml)
