# Training-Impact Analytics & Targeted Intervention Planner

<!-- markdownlint-disable MD029 -->

Act as a learning-data scientist for a mid-size global CRO.

## Dataset Available

- 18 months of LMS records (course IDs, completion dates, assessment scores, time-in-module).
- Monthly audit findings (number & category of GCP deviations per study).
- Employee metadata (role, tenure, geography).

## Mission

Build a step-by-step plan to:

A. Correlate training data with audit deviations to identify leading indicators of non-compliance.
B. Segment learners by risk and recommend precision interventions.

## Deliverable Structure

1. Data-prep checklist (cleansing, feature engineering).
1. Two predictive-model options (explain pros/cons of, e.g., logistic regression vs. gradient-boosted trees).
1. Visualization storyboard: which insights go to whom (executive dashboard vs. manager drill-downs).
1. Action framework: automated nudges, remedial micro-courses, mentor assignment.

## Constraints

- Emphasize privacy (GDPR) and small-sample precautions.
- Reference at least one open-source Python library per step.
- Think through potential confounders before proposing models.

Return the plan as an ordered list; include SQL or pseudocode snippets where needed.
