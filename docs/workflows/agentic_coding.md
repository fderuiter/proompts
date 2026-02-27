---
title: Agentic Coding: From Idea to Epics
---

# Agentic Coding: From Idea to Epics

A workflow that takes a product concept, generates a product brief, and then creates project epics from that brief.

## Workflow Diagram

```mermaid
graph TD
    Input_product_concept[Input: product_concept] --> Steps
    generate_product_brief[Step: generate_product_brief]
    Input_product_concept --> generate_product_brief
    create_project_epics[Step: create_project_epics]
    generate_product_brief --> create_project_epics
```

[View Source YAML](https://github.com/fderuiter/proompts/blob/main/workflows/technical/agentic_coding.workflow.yaml)
