
<!-- markdownlint-disable MD012 -->

# Inventory & Demand-Planning Simulation

Act as a **supply-chain data scientist** specializing in inventory optimization.

Context supplied below:

```csv
SKU, Monthly_Demand_24M, LeadTime_Days, HoldingCost_USD
…
```

**Goal**
Generate a 12-month demand forecast, compute EOQ & safety-stock per SKU (95 % service level), and propose inventory-rebalancing moves.

**Deliverables**
Return a **JSON object** with keys:

* `forecast`              – table of projected demand
* `inventory_plan`        – recommended reorder point, EOQ, safety-stock
* `risks`                 – top 3 forecast or supply risks + mitigation

Use chain-of-thought internally but **do not** expose it; present only the JSON plus a ≤ 120-word note on methodology.
