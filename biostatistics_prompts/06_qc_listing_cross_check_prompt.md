<!-- markdownlint-disable MD029 -->
# QC Listing & Cross-check Prompt

*Purpose — automate a Listing plus QC cross-check between independent R and SAS runs.*

```text
**System:**  
Act as Lead Programmer overseeing double-programming.

**User:**  
Goal ▸ Produce Listing 16-3 of concomitant medications (ADCM) for subjects with serious AEs.  
Steps ▸ 1⃣ Use **R** to pull ADCM where USUBJID ∈ ADAE[SAEFL=='Y'] and list USUBJID, CMTRT, CMDECOD, CMSTDTC, CMENDTC.  
    2⃣ Use **SAS** to replicate the same logic independently.  
    3⃣ Perform a record-level compare (key = USUBJID+CMDECOD+CMSTDTC) and report “PASS” or “DIFF” summary.  
Constraints ▸ Return three code blocks in the order: R-extract, SAS-extract, R-compare.  
    If differences exist, print a diff table; else print “QC PASS – R and SAS identical”.  
    No additional commentary.

```

Why it’s a “top” prompt

* ✔ Embeds self-QC inside the prompt, reflecting industry guidance that LLM outputs must be programmatically verifiable.
* ✔ Leverages negative prompting to suppress unwanted chatty text.
* ✔ Transforms the workflow into a double-programming simulator.
