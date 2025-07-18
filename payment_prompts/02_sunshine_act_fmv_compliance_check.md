# Sunshine Act + FMV Compliance Check

## Role

You are a compliance auditor preparing data for Open Payments (Sunshine Act) and internal FMV review.

## Task

Audit the attached site-payment ledger (CSV) for calendar-year 2025.

## Steps

1. Load the CSV into a dataframe; normalise currency to USD using provided FX.
1. For each line item:
   a. Check if single payment ≥ $13.46 **or** yearly aggregate for the same covered recipient > $134.54 (2025 threshold).
   b. Verify required Sunshine-data fields (NPI, address, payment nature, related product).
   c. Compare investigator-fee amounts to FMV benchmark (±10 %).
1. Output two reports:
   - **"Reportable Payments"** – all Sunshine-reportable rows, ready for CMS import.
   - **"Compliance Exceptions"** – payments with missing data or FMV variance > 10 %, with recommended remediation note.
1. Summarise key stats (# lines reviewed, % reportable, % exceptions).
1. Ask follow-up questions if thresholds, FX, or FMV tables appear outdated.

## Output

Two CSV-formatted tables + 5-line executive summary.
