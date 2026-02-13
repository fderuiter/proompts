---
layout: default
title: BioSkills Workflow
parent: Workflows
nav_order: 99
---

# BioSkills Workflow

A workflow for coaching, feedback, and assessment of bioskills.

## Workflow Diagram\n\n<div class="mermaid">\ngraph TD
    Input_procedure_name[Input: procedure_name] --> Steps
    Input_procedure_notes[Input: procedure_notes] --> Steps
    coaching[Step: coaching]
    Input_procedure_name --> coaching
    feedback[Step: feedback]
    Input_procedure_notes --> feedback
    assessment[Step: assessment]
    Input_procedure_name --> assessment\n</div>\n
[View Source YAML](../../workflows/scientific/bioskills.workflow.yaml)
