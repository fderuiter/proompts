---
title: Stochastic Model Chain: Architect -> Engineer -> Strategist
---

# Stochastic Model Chain: Architect -> Engineer -> Strategist

A three-stage workflow to model, simulate, and analyze conversation risks using Game Theory and Monte Carlo simulations.

## Workflow Diagram

```mermaid
graph TD
    classDef stepNode fill:#1a5f7a,stroke:var(--md-default-fg-color,var(--text-color,#0d3a4d)),stroke-width:2px,color:#ffffff;
    classDef inputNode fill:#2c5e43,stroke:var(--md-default-fg-color,var(--text-color,#183b27)),stroke-width:2px,color:#ffffff;
    INPUT_conversation_scenario([Input: conversation_scenario]):::inputNode
    architect_step[architect_step<br><i>01_stochastic_architect.prompt.md</i>]:::stepNode
    INPUT_conversation_scenario -. conversation_scenario .-> architect_step
    architect_step -->|sequential| engineer_step
    engineer_step[engineer_step<br><i>02_stochastic_engineer.prompt.md</i>]:::stepNode
    architect_step -. architect_output .-> engineer_step
    engineer_step -->|sequential| strategist_step
    strategist_step[strategist_step<br><i>03_stochastic_strategist.prompt.md</i>]:::stepNode
    architect_step -. architect_output .-> strategist_step
    engineer_step -. engineer_output .-> strategist_step
    linkStyle default stroke:var(--md-default-fg-color,var(--text-color,#767676)),stroke-width:2px;
```


