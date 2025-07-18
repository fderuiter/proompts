# Forecast Site-Level Drug Supply & Resupply Strategy

You are a senior clinical supply planner specializing in RTSM forecasting algorithms.

## Context

• Trial: 18-month, adaptive dose-escalation  
• Sites: 28 across US/EU/APAC  
• Average enrollment rate: 10 patients/site/month (Poisson λ = 10)  
• Packaging: 2-visit kits (28-day supply)  
• Lead times: 8 weeks (manufacture) + 2 weeks (shipping)  
• Depot capacities: 3 (USA, Germany, Singapore)  
• Shelf-life: 24 months, temperature-controlled (2-8 °C)  
• Supply strategy preference: trigger-based resupply

## Task

1. Calculate initial shipment quantities per site to keep ≥ 95 % service level for first 6 weeks.
1. Design an RTSM resupply algorithm (n-threshold/percentage or predictive) that balances stock-out risk ≤ 1 % vs. waste ≤ 10 %.
1. Present a timeline identifying manufacturing start, depot release, and first three automatic resupply points.
1. Provide a one-paragraph rationale that a study manager can paste into the Supply Plan appendix.

## Output

- A markdown table with rows = sites, columns = initial kits, reorder threshold, expected monthly consumption, safety stock.  
- A Gantt-style text timeline (ASCII).  
- Conclude with the rationale paragraph.  
- Do NOT reveal chain-of-thought.
