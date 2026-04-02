# Paw Overview

> [!NOTE]
> The **Principal Architect Workflow (PAW)** is a state-machine workflow for disciplined software engineering tasks, enforcing Design, Refactor, Implementation, and QA phases.

## 🗺️ Workflow Architecture

```mermaid
graph TD
    %% Define Nodes
    Start([TODO.md & Codebase]) --> Phase1

    subgraph "Phase 1: Tactical Recon"
        Phase1(paw_01_tactical_recon)
    end

    Phase1 -->|Tactical Brief| Phase2

    subgraph "Phase 2: Architectural Blueprint"
        Phase2(paw_02_architectural_blueprint)
    end

    Phase2 -->|Design Spec| Phase3

    subgraph "Phase 3: Precision Strike"
        Phase3(paw_03_precision_strike)
    end

    Phase3 -->|Implementation Code| Phase4

    subgraph "Phase 4: QA Verification"
        Phase4(paw_04_qa_verification)
    end

    Phase4 --> Finish([Updated TODO.md & Clean Code])

    %% Styling
    classDef default fill:#f9f9f9,stroke:#333,stroke-width:1px;
    classDef phase fill:#e1f5fe,stroke:#01579b,stroke-width:2px;
    class Phase1,Phase2,Phase3,Phase4 phase;
```

## Prompts

- **[PAW Phase 1 - Tactical Recon](paw_01_tactical_recon.prompt.yaml)**: Phase 1 of the Principal Architect Workflow (PAW). Analyzes TODO.md and file structure to generate a Tactical Brief.
- **[PAW Phase 2 - Architectural Blueprint](paw_02_architectural_blueprint.prompt.yaml)**: Phase 2 of the Principal Architect Workflow (PAW). Designs the solution based on the Tactical Brief.
- **[PAW Phase 3 - Precision Strike](paw_03_precision_strike.prompt.yaml)**: Phase 3 of the Principal Architect Workflow (PAW). Implements the design spec with surgical accuracy.
- **[PAW Phase 4 - Quality Assurance & Log](paw_04_qa_verification.prompt.yaml)**: Phase 4 of the Principal Architect Workflow (PAW). Verifies the implementation and updates the TODO log.
