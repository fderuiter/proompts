# Stochastic Model Chain: Architect -> Engineer -> Strategist

A three-stage workflow to model, simulate, and analyze conversation risks using Game Theory and Monte Carlo simulations.

## Visual Flow

```mermaid
flowchart TD
    subgraph Inputs [Global Inputs]
        inp_conversation_scenario((conversation_scenario))
    end
    architect_step["architect_step<br/><small>prompts/technical/data_science/stochastic_architect.prompt.yaml</small>"]
    engineer_step["engineer_step<br/><small>prompts/technical/data_science/stochastic_engineer.prompt.yaml</small>"]
    strategist_step["strategist_step<br/><small>prompts/technical/data_science/stochastic_strategist.prompt.yaml</small>"]
    inp_conversation_scenario -->|conversation_scenario| architect_step
    architect_step -->|architect_output| engineer_step
    architect_step -->|architect_output| strategist_step
    engineer_step -->|engineer_output| strategist_step
```
