# Clinical ETL Pipeline Review and Optimisation

You are a performance-tuning specialist for large oncology Phase III trials.

## Context

The following GitHub gist (link) contains a multi-step ETL: `ingest_raw.R`, `transform.sas`, `load_to_db.sql`. Peak run-time is 4 h.

## Tasks

1. Code review – list the top 5 maintainability issues and any CDISC compliance risks.
1. Benchmark plan – propose a reproducible approach (e.g., `bench::mark` in R, `/fullstimer` in SAS) to isolate slow steps, including metrics to capture.
1. Optimisation suggestions – give concrete refactors (vectorisation, hash joins, partitioned loads) and estimate percentage run-time saved.

## Constraints

- Solutions must keep the code portable to on-prem SAS 9.4 and Posit Workbench.
- No proprietary libraries.
- Provide reasoning first, then the recommendations ("Thought process → Solution" pattern).
