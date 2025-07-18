# Analyze Adjudication KPIs & Recommend Fixes

System
You are a Clinical Data-Science Analyst specializing in adjudication performance metrics.

User
Context:

• Attached is a CSV export (“adjudication_log.csv”) covering every event in our ongoing oncology trial.
• Leadership wants a data-driven plan to shave 20 % off median cycle time.

Task:

1. Load the CSV and calculate:
   • Median and 90th-percentile cycle time (event-trigger → final decision)
   • Reviewer disagreement rate
   • Top three root causes of delays (missing docs, late site replies, tie-break meetings, etc., inferred from status fields)

1. Create simple bar charts (one per metric) and save them as PNGs.
1. Recommend at least five concrete process changes (technology, staffing, training) that would yield the target 20 % reduction, citing any trends you observe.

- **Metrics Summary Table**
- Embedded charts (or provide download links)
- Bullet-list Recommendations, each tied to a metric.

If the data columns are ambiguous, ask for a data dictionary before analysis.
