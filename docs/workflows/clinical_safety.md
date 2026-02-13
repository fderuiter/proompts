---
layout: default
title: Clinical Safety Workflow
parent: Workflows
nav_order: 99
---

# Clinical Safety Workflow

A workflow for creating a clinical safety synopsis, an adverse event narrative, and trending safety signals.

## Workflow Diagram

<div class="mermaid">
graph TD
    Input_surveillance_data[Input: surveillance_data] --> Steps
    Input_adverse_event_data[Input: adverse_event_data] --> Steps
    Input_post_market_data[Input: post_market_data] --> Steps
    safety_synopsis[Step: safety_synopsis]
    Input_surveillance_data --> safety_synopsis
    adverse_event_narrative[Step: adverse_event_narrative]
    Input_adverse_event_data --> adverse_event_narrative
    safety_signal_trending[Step: safety_signal_trending]
    Input_post_market_data --> safety_signal_trending
</div>

[View Source YAML](../../workflows/clinical_safety.workflow.yaml)
