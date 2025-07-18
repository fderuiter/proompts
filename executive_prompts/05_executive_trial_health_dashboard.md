# Executive Trial-Health Dashboard

Act as a clinical-operations performance analyst.

## Task

• Build a weekly executive dashboard summarizing the health of all active studies (Phases I-III).

## Data input (CSV attached)

• Columns: Study_ID, Phase, Region, Planned_Last-Patient-In, Actual_Enrollment, SAEs, Monitoring_Findings, Budget_$$, etc.

## Instructions

- Calculate KPI deltas: enrollment variance (%), budget variance (%), data-query aging (days).
- Flag any metric that exceeds preset red-line thresholds:
   • Enrollment > +10 % late
   • Budget > +7 % overrun
   • Open data queries > 30 days
- For each red flag, suggest one root-cause hypothesis and one actionable mitigation step.
- Output two sections:
   A. "Snapshot Table" in Markdown using the following columns:

   | Study | Phase | KPI in red | Root-cause hypothesis | Mitigation | Owner |
   | ----- | ----- | ---------- | --------------------- | ---------- | ----- |

   B. A concise "Exec-Summary" paragraph (≤ 150 words).
- Do **not** rewrite or reorder input data; only add analyses and summary.
