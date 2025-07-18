<!-- markdownlint-disable MD029 -->
# Dual-Language Figure Prompt

*Purpose — generate a Kaplan-Meier Figure in both R and SAS from ADaM ADTTE, ready for shell insertion.*

```text
**System:**  
You are a bilingual (R & SAS) biostat programmer.  
When asked for “dual”, output two separate code blocks: first R (survfit/ggplot2), then SAS (PROC LIFETEST/SGPLOT).

**User:**  
Create Figure 15-2 “Time-to-Progression” Kaplan-Meier plot.  
Inputs ▸ ADTTE with variables TRT01P, AVALL=:time, CNSR.  
Specifications ▸ • Stratify by TRT01P; risk table required.  
    • Censor marks = vertical ticks.  
    • X-axis: 0-1825 days, major every 180 days.  
    • Y-axis: Survival probability (0-1).  
    • Add HR (95% CI) using Cox model in plot subtitle.  
Output ▸ dual = TRUE.  Return two pristine code blocks, labeled ```R``` and ```SAS``` only.

```

Why it’s a “top” prompt

* ✔ Demonstrates prompt chaining without losing determinism.
* ✔ Mirrors real-world need to keep R & SAS graphics in sync for health-authority review.
* ✔ Matches a successful KM-curve prompt pattern validated in recent studies.
