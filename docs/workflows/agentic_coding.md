---
title: Agentic Coding: From Idea to Epics
---

# Agentic Coding: From Idea to Epics

A workflow that takes a product concept, generates a product brief, and then creates project epics from that brief.

## Workflow Diagram

```mermaid
graph TD
    classDef stepNode fill:#1a5f7a,stroke:var(--md-default-fg-color,var(--text-color,#0d3a4d)),stroke-width:2px,color:#ffffff;
    classDef inputNode fill:#2c5e43,stroke:var(--md-default-fg-color,var(--text-color,#183b27)),stroke-width:2px,color:#ffffff;
    INPUT_product_concept([Input: product_concept]):::inputNode
    generate_product_brief[generate_product_brief<br><i>01_product_brief.prompt.md</i>]:::stepNode
    INPUT_product_concept -. vision .-> generate_product_brief
    generate_product_brief -->|sequential| create_project_epics
    create_project_epics[create_project_epics<br><i>02_project_brief_epic.prompt.md</i>]:::stepNode
    generate_product_brief -. project_description .-> create_project_epics
    linkStyle default stroke:var(--md-default-fg-color,var(--text-color,#767676)),stroke-width:2px;
```


