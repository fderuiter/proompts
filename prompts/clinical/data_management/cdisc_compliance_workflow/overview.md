# Cdisc Compliance Workflow Overview

## Prompts
- **[Protocol-to-TS Generator](01_protocol_to_ts_generator.prompt.yaml)**: Automates the extraction of trial design parameters from a clinical protocol for the CDISC SDTM Trial Summary (TS) domain.
- **[Raw-to-SDTM Auto-Mapper](02_raw_to_sdtm_auto_mapper.prompt.yaml)**: Intelligently maps raw EDC variables to standard SDTM variables based on fuzzy logic and context.
- **[ADaM Derivation Writer](03_adam_derivation_writer.prompt.yaml)**: Translates SAS/R programming logic into plain-English derivation descriptions for CDISC define.xml documentation.
- **[Controlled Terminology Harmonizer](04_controlled_terminology_harmonizer.prompt.yaml)**: Standardizes a list of values (e.g., Units) to CDISC Controlled Terminology (NCI Preferred Terms).
- **[ADaM ADRS RECIST Derivation Architect](05_adam_adrs_recist_derivation_architect.prompt.yaml)**: Automates the complex derivation of oncology RECIST 1.1 criteria for the ADaM ADRS (Tumor Response) domain based on raw EDC data and SDTM Tu/TR domains.
- **[Pinnacle 21 Conformance Resolution Architect](06_pinnacle21_conformance_resolution_architect.prompt.yaml)**: Automates the resolution of complex Pinnacle 21 (P21) conformance rule rejections by analyzing validation issues against CDISC Implementation Guides and generating precise mitigation or mapping correction strategies.
- **[SDTM Pharmacokinetics Mapping Architect](07_sdtm_pharmacokinetics_mapping_architect.prompt.yaml)**: Automates the complex algorithmic mapping of raw EDC and external vendor pharmacokinetic data into CDISC SDTM PC (Pharmacokinetics Concentrations) and PP (Pharmacokinetics Parameters) domains.
- **[SDTM Protocol Deviation Modeling Architect](12_sdtm_protocol_deviation_modeling_architect.prompt.yaml)**: Automates the complex algorithmic mapping of raw EDC and CTMS protocol deviation data into the CDISC SDTM DV (Protocol Deviations) domain.
- **[SDTM Concomitant Medications Mapping Architect](14_sdtm_concomitant_medications_mapping_architect.prompt.yaml)**: Automates the complex algorithmic mapping of raw EDC Concomitant Medication data and WHODrug coding data into the CDISC SDTM CM (Concomitant Medications) domain.
