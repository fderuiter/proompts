# Stochastic Model Chain Workflow Overview

## Prompts
- **[Stochastic Architect](01_stochastic_architect.prompt.yaml)**: Analyzes a conversation or scenario to map it into a formal Stochastic State Model, defining states, risk scores, and a transition probability matrix.
- **[Stochastic Engineer](02_stochastic_engineer.prompt.yaml)**: Generates a Python Monte Carlo simulation script based on provided state definitions and transition matrix.
- **[Stochastic Strategist](03_stochastic_strategist.prompt.yaml)**: Analyzes the stochastic model and simulation logic to provide strategic advice, identifying "Black Swan" paths and leverage points.
