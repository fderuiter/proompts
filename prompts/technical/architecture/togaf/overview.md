# TOGAF Architecture Development Method (ADM)

This directory contains a comprehensive suite of prompts designed to guide Enterprise Architects through the TOGAF Architecture Development Method (ADM). The ADM is the core engine of The Open Group Architecture Framework (TOGAF), used globally to align IT strategy with business goals.

The ADM is not a linear list; it is a continuous cycle where phases interact to transform an organization.

## Summary of the Flow

| Stage | Phases | Primary Action |
| --- | --- | --- |
| **Commit** | Preliminary, A | Define the *Scope* and *Vision*. |
| **Design** | B, C, D | Define the *Business*, *Data/App*, and *Tech* layers. |
| **Plan** | E, F | Define the *Roadmap* and *Migration Plan*. |
| **Govern** | G, H | Oversee the *Build* and manage *Change*. |

## Prompts

### I. The Strategic Foundation
*   `01_preliminary_phase.prompt.yaml`: **The Setup**. Determining *how* you will do architecture before you actually do it. Customizing the framework, defining the Architecture Capability and Principles.
*   `02_phase_a_vision.prompt.yaml`: **Architecture Vision**. The "Sales Pitch" and scope definition. creating a high-level vision to secure buy-in.

### II. The Core Architecture Domains
*   `03_phase_b_business.prompt.yaml`: **Business Architecture**. Defining the business strategy, governance, and processes. "Business drives technology".
*   `04_phase_c_information_systems.prompt.yaml`: **Information Systems Architectures**. Covering Data and Application Architectures to support the business.
*   `05_phase_d_technology.prompt.yaml`: **Technology Architecture**. Mapping software components to physical infrastructure, hardware, and networks.

### III. Transition Planning
*   `06_phase_e_opportunities.prompt.yaml`: **Opportunities & Solutions**. Weighing options (Make vs. Buy), creating the initial roadmap.
*   `07_phase_f_migration.prompt.yaml`: **Migration Planning**. Detailed project planning, prioritization, and coordination with the PMO.

### IV. Governance & Maintenance
*   `08_phase_g_governance.prompt.yaml`: **Implementation Governance**. Architectural oversight during the build to ensure conformance.
*   `09_phase_h_change_management.prompt.yaml`: **Architecture Change Management**. Managing the lifecycle after deployment and handling change requests.

### The Centerpiece
*   `10_requirements_management.prompt.yaml`: **Requirements Management**. A continuous process at the center of the ADM cycle ensuring architecture adapts to changing business requirements.
