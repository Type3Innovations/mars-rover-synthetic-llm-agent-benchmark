# Scenario-level statistical tests

Repeated runs were aggregated to scenario-level means (100 paired scenario units per model) before paired testing.
Bootstrap confidence intervals resample scenarios, not individual runs.

## gpt-5.5

| Metric | Single mean | Multi mean | Diff (single-multi) | 95% CI (diff) | Cohen's dz | 95% CI (dz) | p-value | Holm-adjusted |
|---|---:|---:|---:|---|---:|---|---|---|
| decision_correct | 0.974 | 0.934 | 0.04 | [-0.004, 0.086] | 0.173 | [-0.019, 0.328] | p = 0.238 | p = 0.238 |
| exact_hazard_f1 | 0.018 | 0.0 | 0.018 | [0.008, 0.03] | 0.329 | [0.232, 0.433] | p < 0.001 | p = 0.001 |
| semantic_hazard_f1 | 0.075 | 0.06 | 0.015 | [0.005, 0.026] | 0.268 | [0.097, 0.425] | p = 0.065 | p = 0.130 |
| latency_seconds | 6.064 | 35.585 | -29.522 | [-30.217, -28.83] | -8.253 | [-9.612, -7.337] | p < 0.001 | p < 0.001 |
| total_tokens | 547.656 | 3160.208 | -2612.552 | [-2657.73, -2567.856] | -11.393 | [-13.13, -10.255] | p < 0.001 | p < 0.001 |
