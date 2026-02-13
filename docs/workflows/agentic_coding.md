---
layout: default
title: Agentic Coding: From Idea to Epics
parent: Workflows
nav_order: 99
---

# Agentic Coding: From Idea to Epics

A workflow that takes a product concept, generates a product brief, and then creates project epics from that brief.

## Workflow Diagram\n\n<div class="mermaid">\ngraph TD
    Input_product_concept[Input: product_concept] --> Steps
    generate_product_brief[Step: generate_product_brief]
    Input_product_concept --> generate_product_brief
    create_project_epics[Step: create_project_epics]
    generate_product_brief --> create_project_epics\n</div>\n
[View Source YAML](../../workflows/technical/agentic_coding.workflow.yaml)
