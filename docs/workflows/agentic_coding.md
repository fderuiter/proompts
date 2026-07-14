---
title: Agentic Coding: From Idea to Epics
---

# Agentic Coding: From Idea to Epics

A workflow that takes a product concept, generates a product brief, and then creates project epics from that brief.

## Workflow Diagram

```mermaid
graph TD
    INPUT_product_concept([Input: product_concept])
    generate_product_brief[generate_product_brief<br><i>01_product_brief.prompt.md</i>]
    INPUT_product_concept -. vision .-> generate_product_brief
    generate_product_brief -->|sequential| create_project_epics
    create_project_epics[create_project_epics<br><i>02_project_brief_epic.prompt.md</i>]
    generate_product_brief -. project_description .-> create_project_epics
```


