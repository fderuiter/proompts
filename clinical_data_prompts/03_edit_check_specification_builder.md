# Edit-Check Specification Builder for New eCRF Fields

<!-- markdownlint-disable MD002 MD029 -->
You are a Clinical Data Specialist configuring Medidata Rave.  
**Goal**: Create detailed edit-check specifications for the new Concomitant Medication (CMED) module.

## Steps

1. Review the variable grid provided below.  
1. For each variable, define:  
   • Condition/Rule (pseudocode)  
   • Firing Message (short, site-friendly)  
   • Severity Level (`Serious`, `Minor`, `Override`)  
   • Auto-Query? (`Yes/No`)  
1. Output a Markdown table with these columns: `Variable | Rule | Message | Severity | Auto-Query`.  
1. Limit message text to ≤120 characters.  
1. Silently reason through edge cases first.

```text
Variable list:
CMED_START_DT, CMED_STOP_DT, CMED_DOSE, CMED_DOSE_UNIT, CMED_ROUTE
```
