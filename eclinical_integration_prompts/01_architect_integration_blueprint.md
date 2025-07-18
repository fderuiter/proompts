# Architect the Integration Blueprint

**Role:** You are a Senior Clinical Data Architect experienced in eSource and real-world-data workflows.

**Context:** We are running a multicentre Phase III trial that must move structured patient data from site EHRs into our EDC and CTMS with minimal duplicate entry. We will use **HL7 FHIR R4 APIs** at the site side and must land data in **CDISC SDTM v1.8** domains. Our tech stack already supports RESTful APIs and message queues.

**Task:**

1. Draw a high-level system architecture diagram (textual is fine) showing data flow between EHR → integration layer → EDC → CTMS, including key security checkpoints.
1. List the FHIR resources to invoke and which SDTM tables each maps to.
1. Recommend middleware patterns (e.g., publish-subscribe, ETL, event streaming) and why each fits.
1. Identify risks (site heterogeneity, terminology mismatches, 21 CFR Part 11 validation) and propose mitigations.

**Output format:**

```
## Architecture Overview
(ASCII diagram)

## Resource-to-SDTM Mapping
|FHIR Resource|SDTM Domain|Notes|
...

## Middleware Recommendation
- Pattern
- Justification
...

## Risk & Mitigation Table
```

**If any assumption is unclear, ask follow-up questions before answering.**

*Why it helps:* It leverages proven standards (FHIR ↔ CDISC mappings) and forces the model to surface both design and risk controls.
