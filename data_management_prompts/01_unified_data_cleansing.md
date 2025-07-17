# Unified Data Cleansing & Consolidation

You are a senior data engineer.

## Context
- Source-1: 2024-Q4 e-commerce CSV (schema below)
- Source-2: CRM export (JSON)
- Goal: build a single, analysis-ready table by close of business.

## Task
1. Identify schema mismatches, missing values, and outliers.
2. Propose normalization rules (naming, data types, units, time-zones).
3. Generate Python-pandas pseudocode for:
   a. loading both sources,
   b. applying the rules,
   c. returning a consolidated DataFrame.
4. List any assumptions; ask clarifying questions if something is ambiguous.

## Output format
Use fenced Markdown blocks:
```python
# step-by-step pseudocode here
```

Follow with a bullet list of remaining open questions.
