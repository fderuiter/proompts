# Future-Proof Data-Architecture Blueprint

Assume the role of an enterprise data-architect advisor.

## Scenario

- Current stack: on-prem SQL Server + nightly ETL to S3.
- Forecast: 10× data growth over 18 months; need low-latency ML-serving.
- Budget: $250 k capex + $6 k/mo opex.

## Deliverables

1. Compare at least 3 target architectures (lakehouse on Databricks, Snowflake with Iceberg tables, open-source Delta + DuckDB, etc.).
1. For each, break down: storage layer, compute engine, governance tooling, estimated 3-year TCO.
1. Recommend the best fit and justify with a decision matrix (criteria: scalability, cost, team skill alignment, vendor lock-in).
1. List the first five migration milestones and rough duration.
1. End with "Any questions?" if uncertainties remain.

## Output format

Decision matrix in Markdown, followed by a Gantt-style milestone table.
