---
layout: default
title: Stochastic Model Chain: Architect -> Engineer -> Strategist
parent: Workflows
nav_order: 99
---

# Stochastic Model Chain: Architect -> Engineer -> Strategist

A three-stage workflow to model, simulate, and analyze conversation risks using Game Theory and Monte Carlo simulations.

## Workflow Diagram

<div class="mermaid">
graph TD
    Input_conversation_scenario[Input: conversation_scenario] --> Steps
    architect_step[Step: architect_step]
    Input_conversation_scenario --> architect_step
    engineer_step[Step: engineer_step]
    architect_step --> engineer_step
    strategist_step[Step: strategist_step]
    architect_step --> strategist_step
    engineer_step --> strategist_step
</div>

[View Source YAML](../../workflows/stochastic_model_chain.workflow.yaml)
