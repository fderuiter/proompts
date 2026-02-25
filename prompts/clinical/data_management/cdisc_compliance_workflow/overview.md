# Cdisc Compliance Workflow Overview

## Prompts
- **[Protocol-to-TS Generator](01_protocol_to_ts_generator.prompt.yaml)**: Automates the extraction of trial design parameters from a clinical protocol for the CDISC SDTM Trial Summary (TS) domain.
- **[Raw-to-SDTM Auto-Mapper](02_raw_to_sdtm_auto_mapper.prompt.yaml)**: Intelligently maps raw EDC variables to standard SDTM variables based on fuzzy logic and context.
- **[ADaM Derivation Writer](03_adam_derivation_writer.prompt.yaml)**: Translates SAS/R programming logic into plain-English derivation descriptions for CDISC define.xml documentation.
- **[Controlled Terminology Harmonizer](04_controlled_terminology_harmonizer.prompt.yaml)**: Standardizes a list of values (e.g., Units) to CDISC Controlled Terminology (NCI Preferred Terms).
