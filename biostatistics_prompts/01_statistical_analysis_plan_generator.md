<!-- markdownlint-disable MD029 -->
# Statistical Analysis-Plan (SAP) Generator

**Prompt**
*You are an experienced biostatistics consultant for Phase III clinical trials.*

**Context (fill-in):** The trial compares **$intervention$** vs **$control$** in **$population$** with a primary endpoint of **$endpoint$** measured at **$time-point$**. Randomisation is stratified by **$factors$**.

**Task:** Draft a complete SAP that my study team can review.

**Please include—in Markdown with H2 headings—the following sections:**

1. Study objectives & hypotheses (null/alternative)
1. Sample-size justification (show formula, inputs, and power curve image link placeholder)
1. Primary, secondary, and safety endpoints with exact statistical tests chosen and assumptions checked
1. Missing-data handling plan (imputation strategy + sensitivity analyses)
1. Interim-analysis rules and alpha-spending function (use O’Brien-Fleming unless rationale differs)
1. Shell tables/figures template (structured as Simple JSON so we can auto-format later)
1. Reproducibility checklist (software, version control, random-seed policy)

**Output constraints:**
• Keep total length ≤ 1 500 words.
• Begin each subsection with a 1-sentence plain-English summary for clinicians.
• After the plan, list any assumptions that need sponsor confirmation.
**Think step-by-step** and show your reasoning internally before presenting the final SAP.
