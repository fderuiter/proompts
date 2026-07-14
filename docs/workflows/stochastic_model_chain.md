---
title: Stochastic Model Chain: Architect -> Engineer -> Strategist
---

# Stochastic Model Chain: Architect -> Engineer -> Strategist

A three-stage workflow to model, simulate, and analyze conversation risks using Game Theory and Monte Carlo simulations.

## Workflow Diagram

```mermaid
graph TD
    INPUT_conversation_scenario([Input: conversation_scenario])
    architect_step[architect_step<br><i>01_stochastic_architect.prompt.md</i>]
    INPUT_conversation_scenario -. conversation_scenario .-> architect_step
    architect_step -->|sequential| engineer_step
    engineer_step[engineer_step<br><i>02_stochastic_engineer.prompt.md</i>]
    architect_step -. architect_output .-> engineer_step
    engineer_step -->|sequential| strategist_step
    strategist_step[strategist_step<br><i>03_stochastic_strategist.prompt.md</i>]
    architect_step -. architect_output .-> strategist_step
    engineer_step -. engineer_output .-> strategist_step
```


