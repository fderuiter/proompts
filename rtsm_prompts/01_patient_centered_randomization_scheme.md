# Design a Patient-Centered Randomization Scheme

You are an RTSM architect with 10 years' experience in global phase 3 studies.

## Context

• Trial phase: 3  
• Sites: 42  
• Arms: active 1 : placebo 1  
• Stratification factors: region (3 levels), prior therapy (yes/no)  
• Blinding: double-dummy  
• Desired balance: 1:1 per stratum  
• Regulatory regions: FDA, EMA, PMDA

## Task

1. Propose the optimal randomization method (e.g., permuted blocks, dynamic / minimization).
1. Justify block sizes or algorithm parameters to minimize predictability yet keep logistical simplicity.
1. Draft a concise Randomization Specification (≤ 600 words) ready for RTSM vendor build, covering:
   • Algorithm description and parameters  
   • Seed management and audit-trail requirements  
   • Dummy-code structure and masking plan  
   • Simulation results showing expected imbalance < 2 patients per arm within each stratum at N = 600.

## Output

- Start with a 4-bullet executive summary.  
- Follow with the specification in a markdown table (sections as rows, < 80 chars per cell).  
- Omit internal reasoning; present only the final deliverable.
