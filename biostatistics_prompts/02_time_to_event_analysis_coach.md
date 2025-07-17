<!-- markdownlint-disable MD029 -->
# Time-to-Event (Survival) Analysis Coach

**Prompt**
*Act as a senior biostatistician mentoring a junior analyst.*

**Dataset snapshot:** 5 000 oncology patients with variables - `t_event`, `event_flag`, `treatment`, `age`, `sex`, `stage`.

**Goal:** Evaluate treatment effect on progression-free survival.

**Instructions:**

1. Explain (for a learner) why a Cox proportional-hazards model is appropriate.
1. Produce tidy R code (commented) to:
   * load data, check proportional-hazards via Schoenfeld residuals, and plot log-minus-log curves;
   * fit the base model `Surv(t_event, event_flag) ~ treatment + age + sex + stage`;
   * output hazard ratios with 95 % CIs in a nicely formatted `gt` table.
1. If PH assumption fails, suggest two alternative modelling strategies with pros/cons.

**Output format:**
• Section A: “Conceptual Walk-through” (Bullets)
• Section B: “R Code” (fenced ```r)
• Section C: “Interpretation & Next Steps” (≤ 250 words)

**Chain-of-thought:** provide rationale before each major chunk of code (commented with `# WHY:`).
