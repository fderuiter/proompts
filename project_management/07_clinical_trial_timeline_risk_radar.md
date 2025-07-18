<!-- markdownlint-disable MD029 -->

# Clinical-Trial Timeline & Risk Radar

**"You are a senior Clinical Project Manager at a global CRO.
Goal → Evaluate the current study timeline for schedule or budget threats and draft a ranked risk-mitigation plan.

Context ###
CSV_DATA:
"""
Task,Planned_Start,Planned_End,Actual_Start,Actual_End,Slack_Days
Screening,2025-08-01,2025-10-15,2025-08-03,,
Site_Activation,2025-07-15,2025-09-01,2025-07-20,2025-09-12,-11
...
"""

## Instructions

1. Compare *Planned* versus *Actual* dates; calculate schedule variance in days.
1. Flag any task where variance > 7 days **or** negative Slack.
1. Build a 5-row **Risk Register** with columns: `Risk`, `Probability (High/Med/Low)`, `Impact (High/Med/Low)`, `Mitigation Action`, `Owner`.
1. End with a concise "Top-3 Next Actions" list.

## Output format (Markdown table + bullet list only)

Think step-by-step and reference tasks by name; then output."**
