# Sample-Size & Randomization Strategy

```text
System
You are a senior biostatistician at an international CRO. You follow ICH E9(R1), FDA, EMA and CDISC guidance, and you communicate in concise, submission-ready language.

User
Project context  
• Indication: Moderate–to-severe plaque psoriasis  
• Trial phase: Phase III, multicenter, double-blind, placebo-controlled  
• Arms: Investigational drug 150 mg Q2W vs placebo (1 : 1)  
• Primary endpoint: Proportion of patients achieving PASI-75 at Week 16  
• Assumptions: Response 68% vs 10%; two-sided α = 0.05  
• Drop-out rate: 12 %

Task  
1. Determine the minimum total sample size to attain ≥ 90% power.  
2. Recommend an appropriate stratified block-randomization scheme (block size range, stratification factors, generation method).  
3. Explain any sensitivity or re-estimation options.  
4. Provide the R code (using `pwr` or `power.prop.test` plus `randomizeR`) with inline comments.  

Output format  
• Executive summary (≤ 150 words)  
• Table 1 – sample-size scenarios  
• Table 2 – randomization design parameters  
• Verified R script (markdown fenced block)  

Constraints  
– Reason step-by-step internally; show only final answer.  
– Cite statistical textbooks or guidelines where appropriate.  
```
