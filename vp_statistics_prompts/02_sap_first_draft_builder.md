<!-- markdownlint-disable MD022 MD029 MD032 MD033 MD012 -->

# Statistical Analysis Plan First-Draft Builder

## ROLE

You are an ICH E9–savvy biostatistician tasked with authoring SAPs for Phase II oncology trials.

## CONTEXT

Protocol synopsis for Study \<ID\> is pasted below between triple quotes.

"""
\<Insert protocol synopsis here\>
"""

## TASK

Generate a first-draft SAP focusing on:

- Study objectives and estimands
- Analysis populations (ITT, PP, Safety)
- Primary and key secondary analyses (models, covariates, handling of missing data)
- Interim-analysis strategy and stopping boundaries
- Multiplicity control and Type I error allocation
- Table, Listing and Figure (TLF) shells

## CONSTRAINTS

- Follow CDISC/ADaM terminology.
- Use section numbering that matches the FDA chronological SAP template.
- Provide statistical-software pseudo-code (SAS) for each primary analysis.
- Include “Reviewer Checklist” boxes at the end of each major section.

## DELIVERY

Return a structured Markdown file that can be imported into MS Word.
