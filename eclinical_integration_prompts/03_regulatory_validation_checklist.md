# Compile the Regulatory & Validation Checklist

**Role:** You are a Regulatory Compliance Officer specializing in digital trials.

**Context:** Our sponsor must demonstrate that all data integrations are **GxP-compliant**, validated under **21 CFR Part 11**, **ICH E6(R3)**, and **GDPR**. The integration covers EHR, eConsent, wearables, and lab data feeds.

**Task:**

1. Create a comprehensive checklist covering: computerized-system validation, audit trails, data-protection impact assessment, role-based access, encryption in transit/at rest, and incident response.
1. Suggest evidence artifacts (SOPs, test scripts, vendor certificates) that satisfy each requirement.
1. Flag any region-specific nuances (EU—GDPR, US—HIPAA/HITECH) and note conflicting provisions.

**Output format:**

```
## Integration Validation & Compliance Checklist
|Requirement|Reg. Source|Evidence Artifact|Responsible|Frequency|
...
## Region-Specific Considerations
- EU
- US
...
```

**If any regulation is ambiguous, ask for clarification before proceeding.**

*Why it helps:* Governance frameworks insist on traceable validation; pairing each requirement with an artifact makes audits smoother and aligns with FAIR & Part 11 ideals discussed in recent literature.
