# Scenario-level statistical tests

Repeated runs were aggregated to scenario-level means (100 paired scenario units per model) before paired testing.
Bootstrap confidence intervals resample scenarios, not individual runs.

## gpt-4o

| Metric | Single mean | Multi mean | Diff (single-multi) | 95% CI (diff) | Cohen's dz | 95% CI (dz) | p-value | Holm-adjusted |
|---|---:|---:|---:|---|---:|---|---|---|
| decision_correct | 0.81 | 0.734 | 0.076 | [0.024, 0.13] | 0.278 | [0.107, 0.432] | p = 0.029 | p = 0.087 |
| exact_hazard_f1 | 0.081 | 0.043 | 0.038 | [0.011, 0.068] | 0.261 | [0.09, 0.413] | p = 0.200 | p = 0.401 |
| semantic_hazard_f1 | 0.131 | 0.106 | 0.025 | [-0.011, 0.062] | 0.136 | [-0.065, 0.314] | p = 0.560 | p = 0.560 |
| latency_seconds | 2.32 | 11.833 | -9.513 | [-9.949, -9.129] | -4.529 | [-6.624, -3.37] | p < 0.001 | p < 0.001 |
| total_tokens | 457.938 | 2273.06 | -1815.122 | [-1842.764, -1787.016] | -12.71 | [-14.35, -11.526] | p < 0.001 | p < 0.001 |
