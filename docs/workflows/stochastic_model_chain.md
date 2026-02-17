---
layout: default
title: Stochastic Model Chain: Architect -&gt; Engineer -&gt; Strategist
parent: Workflows
nav_order: 99
---

# Stochastic Model Chain: Architect -&gt; Engineer -&gt; Strategist

A three-stage workflow to model, simulate, and analyze conversation risks using Game Theory and Monte Carlo simulations.

## Workflow Diagram\n\n<div class="mermaid">\ngraph TD
    Input_conversation_scenario[Input: conversation_scenario] --> Steps
    architect_step[Step: architect_step]
    Input_conversation_scenario --> architect_step
    engineer_step[Step: engineer_step]
    architect_step --> engineer_step
    strategist_step[Step: strategist_step]
    architect_step --> strategist_step
    engineer_step --> strategist_step\n</div>\n
[View Source YAML](../../workflows/technical/stochastic_model_chain.workflow.yaml)
