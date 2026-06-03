# Paper-Ready Tables

## Table 1. Aggregate architecture comparison
| architecture_type | runs | scenarios | evaluations | decision_accuracy | mean_exact_hazard_f1 | mean_semantic_hazard_f1 | mean_hazard_false_positive_count | mean_canonical_hazard_coverage | mean_spurious_hazard_count | mean_latency_seconds | mean_token_usage |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| multi_agent_orchestration | 5 | 100 | 500 | 0.934 | 0.000 | 0.060 | 6.084 | 0.127 | 2.506 | 35.585 | 3160.208 |
| single_agent | 5 | 100 | 500 | 0.974 | 0.018 | 0.075 | 3.812 | 0.119 | 1.420 | 6.064 | 547.656 |

## Table 2. Scenario-level performance by architecture
| scenario_id | architecture_type | runs | expected_action | modal_recommended_action | decision_accuracy | mean_exact_hazard_f1 | mean_semantic_hazard_f1 | mean_canonical_hazard_coverage | mean_spurious_hazard_count | mean_latency_seconds |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR-001 | multi_agent_orchestration | 5 | proceed | proceed | 1.000 | 0.000 | 0.000 | 0.000 | 1.600 | 31.633 |
| MR-001 | single_agent | 5 | proceed | proceed | 1.000 | 0.000 | 0.000 | 0.000 | 1.600 | 4.843 |
| MR-002 | multi_agent_orchestration | 5 | reroute | pause | 0.000 | 0.000 | 0.198 | 0.333 | 2.000 | 42.488 |
| MR-002 | single_agent | 5 | reroute | reroute | 1.000 | 0.000 | 0.197 | 0.333 | 1.400 | 7.829 |
| MR-003 | multi_agent_orchestration | 5 | pause | pause | 1.000 | 0.000 | 0.000 | 0.000 | 2.400 | 36.141 |
| MR-003 | single_agent | 5 | pause | pause | 1.000 | 0.000 | 0.000 | 0.000 | 0.800 | 6.329 |
| MR-004 | multi_agent_orchestration | 5 | request_human_review | request_human_review | 1.000 | 0.000 | 0.040 | 0.067 | 2.600 | 41.990 |
| MR-004 | single_agent | 5 | request_human_review | reroute | 0.200 | 0.000 | 0.000 | 0.000 | 1.000 | 6.485 |
| MR-005 | multi_agent_orchestration | 5 | reroute | reroute | 1.000 | 0.000 | 0.050 | 0.100 | 2.800 | 30.887 |
| MR-005 | single_agent | 5 | reroute | reroute | 1.000 | 0.000 | 0.000 | 0.000 | 0.200 | 4.957 |
| MR-006 | multi_agent_orchestration | 5 | pause | pause | 0.600 | 0.000 | 0.369 | 0.800 | 1.800 | 44.041 |
| MR-006 | single_agent | 5 | pause | pause | 1.000 | 0.000 | 0.629 | 1.000 | 1.000 | 9.011 |
| MR-007 | multi_agent_orchestration | 5 | proceed | proceed | 1.000 | 0.000 | 0.000 | 0.000 | 3.200 | 33.263 |
| MR-007 | single_agent | 5 | proceed | proceed | 1.000 | 0.000 | 0.000 | 0.000 | 1.600 | 5.553 |
| MR-008 | multi_agent_orchestration | 5 | request_human_review | reroute | 0.200 | 0.000 | 0.299 | 0.400 | 3.400 | 39.682 |
| MR-008 | single_agent | 5 | request_human_review | request_human_review | 1.000 | 0.173 | 0.345 | 0.400 | 1.600 | 8.059 |
| MR-009 | multi_agent_orchestration | 5 | proceed | proceed | 1.000 | 0.000 | 0.000 | 0.000 | 1.400 | 25.708 |
| MR-009 | single_agent | 5 | proceed | proceed | 1.000 | 0.000 | 0.000 | 0.000 | 1.200 | 4.499 |
| MR-010 | multi_agent_orchestration | 5 | proceed | proceed | 1.000 | 0.000 | 0.000 | 0.000 | 2.000 | 27.438 |
| MR-010 | single_agent | 5 | proceed | proceed | 1.000 | 0.000 | 0.000 | 0.000 | 1.000 | 4.650 |
| MR-011 | multi_agent_orchestration | 5 | proceed | proceed | 1.000 | 0.000 | 0.000 | 0.000 | 1.800 | 29.936 |
| MR-011 | single_agent | 5 | proceed | proceed | 1.000 | 0.000 | 0.000 | 0.000 | 2.000 | 4.242 |
| MR-012 | multi_agent_orchestration | 5 | proceed | proceed | 1.000 | 0.000 | 0.000 | 0.000 | 1.400 | 27.809 |
| MR-012 | single_agent | 5 | proceed | proceed | 1.000 | 0.000 | 0.000 | 0.000 | 0.400 | 4.462 |
| MR-013 | multi_agent_orchestration | 5 | proceed | proceed | 1.000 | 0.000 | 0.080 | 0.200 | 2.000 | 32.584 |
| MR-013 | single_agent | 5 | proceed | proceed | 1.000 | 0.000 | 0.000 | 0.000 | 2.000 | 4.516 |
| MR-014 | multi_agent_orchestration | 5 | proceed | proceed | 1.000 | 0.000 | 0.000 | 0.000 | 2.200 | 37.856 |
| MR-014 | single_agent | 5 | proceed | proceed | 1.000 | 0.000 | 0.000 | 0.000 | 0.800 | 6.690 |
| MR-015 | multi_agent_orchestration | 5 | proceed | proceed | 1.000 | 0.000 | 0.000 | 0.000 | 1.600 | 27.171 |
| MR-015 | single_agent | 5 | proceed | proceed | 1.000 | 0.000 | 0.000 | 0.000 | 1.000 | 4.705 |
| MR-016 | multi_agent_orchestration | 5 | proceed | proceed | 1.000 | 0.000 | 0.000 | 0.000 | 1.800 | 27.720 |
| MR-016 | single_agent | 5 | proceed | proceed | 1.000 | 0.000 | 0.000 | 0.000 | 1.000 | 4.407 |
| MR-017 | multi_agent_orchestration | 5 | proceed | proceed | 1.000 | 0.000 | 0.000 | 0.000 | 2.000 | 28.827 |
| MR-017 | single_agent | 5 | proceed | proceed | 1.000 | 0.000 | 0.000 | 0.000 | 1.800 | 4.468 |
| MR-018 | multi_agent_orchestration | 5 | proceed | proceed | 1.000 | 0.000 | 0.000 | 0.000 | 1.400 | 31.525 |
| MR-018 | single_agent | 5 | proceed | proceed | 1.000 | 0.000 | 0.000 | 0.000 | 1.200 | 5.215 |
| MR-019 | multi_agent_orchestration | 5 | proceed | proceed | 1.000 | 0.000 | 0.000 | 0.000 | 1.800 | 34.525 |
| MR-019 | single_agent | 5 | proceed | proceed | 1.000 | 0.000 | 0.000 | 0.000 | 1.800 | 4.473 |
| MR-020 | multi_agent_orchestration | 5 | proceed | proceed | 1.000 | 0.000 | 0.000 | 0.000 | 2.600 | 32.214 |
| MR-020 | single_agent | 5 | proceed | proceed | 1.000 | 0.000 | 0.000 | 0.000 | 0.800 | 4.396 |
| MR-021 | multi_agent_orchestration | 5 | proceed | proceed | 1.000 | 0.000 | 0.000 | 0.000 | 1.600 | 28.318 |
| MR-021 | single_agent | 5 | proceed | proceed | 1.000 | 0.000 | 0.000 | 0.000 | 1.000 | 5.067 |
| MR-022 | multi_agent_orchestration | 5 | proceed | proceed | 1.000 | 0.000 | 0.000 | 0.000 | 3.000 | 30.177 |
| MR-022 | single_agent | 5 | proceed | proceed | 1.000 | 0.000 | 0.000 | 0.000 | 1.000 | 5.050 |
| MR-023 | multi_agent_orchestration | 5 | proceed | proceed | 1.000 | 0.000 | 0.000 | 0.000 | 1.800 | 32.701 |
| MR-023 | single_agent | 5 | proceed | proceed | 1.000 | 0.000 | 0.000 | 0.000 | 1.200 | 7.389 |
| MR-024 | multi_agent_orchestration | 5 | proceed | proceed | 1.000 | 0.000 | 0.000 | 0.000 | 1.400 | 29.637 |
| MR-024 | single_agent | 5 | proceed | proceed | 1.000 | 0.000 | 0.000 | 0.000 | 0.800 | 4.333 |
| MR-025 | multi_agent_orchestration | 5 | proceed | proceed | 1.000 | 0.000 | 0.000 | 0.000 | 1.400 | 29.829 |
| MR-025 | single_agent | 5 | proceed | proceed | 1.000 | 0.000 | 0.000 | 0.000 | 1.800 | 4.741 |
| MR-026 | multi_agent_orchestration | 5 | proceed | proceed | 1.000 | 0.000 | 0.000 | 0.000 | 2.400 | 33.792 |
| MR-026 | single_agent | 5 | proceed | proceed | 1.000 | 0.000 | 0.000 | 0.000 | 0.800 | 5.135 |
| MR-027 | multi_agent_orchestration | 5 | proceed | proceed | 1.000 | 0.000 | 0.000 | 0.000 | 1.600 | 27.179 |
| MR-027 | single_agent | 5 | proceed | proceed | 1.000 | 0.000 | 0.000 | 0.000 | 1.000 | 5.596 |
| MR-028 | multi_agent_orchestration | 5 | proceed | proceed | 1.000 | 0.000 | 0.000 | 0.000 | 2.600 | 29.182 |
| MR-028 | single_agent | 5 | proceed | proceed | 1.000 | 0.000 | 0.000 | 0.000 | 1.800 | 4.886 |
| MR-029 | multi_agent_orchestration | 5 | proceed | proceed | 1.000 | 0.000 | 0.000 | 0.000 | 1.200 | 26.668 |
| MR-029 | single_agent | 5 | proceed | proceed | 1.000 | 0.000 | 0.000 | 0.000 | 1.600 | 4.843 |
| MR-030 | multi_agent_orchestration | 5 | proceed | proceed | 1.000 | 0.000 | 0.000 | 0.000 | 1.600 | 30.200 |
| MR-030 | single_agent | 5 | proceed | proceed | 1.000 | 0.000 | 0.000 | 0.000 | 1.200 | 4.523 |
| MR-031 | multi_agent_orchestration | 5 | proceed | proceed | 1.000 | 0.000 | 0.167 | 0.400 | 1.000 | 33.425 |
| MR-031 | single_agent | 5 | proceed | proceed | 1.000 | 0.000 | 0.000 | 0.000 | 1.400 | 4.341 |
| MR-032 | multi_agent_orchestration | 5 | reroute | reroute | 1.000 | 0.000 | 0.210 | 0.500 | 4.000 | 37.327 |
| MR-032 | single_agent | 5 | reroute | reroute | 1.000 | 0.000 | 0.295 | 0.500 | 0.800 | 6.227 |
| MR-033 | multi_agent_orchestration | 5 | reroute | proceed | 0.400 | 0.000 | 0.000 | 0.000 | 2.800 | 36.211 |
| MR-033 | single_agent | 5 | reroute | reroute | 1.000 | 0.000 | 0.000 | 0.000 | 1.600 | 5.791 |
| MR-034 | multi_agent_orchestration | 5 | reroute | reroute | 1.000 | 0.000 | 0.178 | 0.400 | 1.600 | 34.226 |
| MR-034 | single_agent | 5 | reroute | reroute | 1.000 | 0.133 | 0.333 | 0.500 | 1.000 | 5.662 |
| MR-035 | multi_agent_orchestration | 5 | reroute | reroute | 1.000 | 0.000 | 0.257 | 0.500 | 2.200 | 34.968 |
| MR-035 | single_agent | 5 | reroute | reroute | 1.000 | 0.000 | 0.337 | 0.500 | 1.600 | 5.638 |
| MR-036 | multi_agent_orchestration | 5 | reroute | reroute | 1.000 | 0.000 | 0.000 | 0.000 | 2.800 | 35.090 |
| MR-036 | single_agent | 5 | reroute | reroute | 1.000 | 0.000 | 0.000 | 0.000 | 2.000 | 5.578 |
| MR-037 | multi_agent_orchestration | 5 | reroute | proceed | 0.400 | 0.000 | 0.000 | 0.000 | 3.200 | 37.813 |
| MR-037 | single_agent | 5 | reroute | reroute | 1.000 | 0.000 | 0.000 | 0.000 | 1.200 | 6.588 |
| MR-038 | multi_agent_orchestration | 5 | reroute | reroute | 1.000 | 0.000 | 0.229 | 0.500 | 1.200 | 35.174 |
| MR-038 | single_agent | 5 | reroute | reroute | 1.000 | 0.000 | 0.305 | 0.500 | 0.800 | 7.267 |
| MR-039 | multi_agent_orchestration | 5 | reroute | reroute | 1.000 | 0.000 | 0.000 | 0.000 | 3.800 | 36.317 |
| MR-039 | single_agent | 5 | reroute | reroute | 1.000 | 0.000 | 0.000 | 0.000 | 1.600 | 5.911 |
| MR-040 | multi_agent_orchestration | 5 | reroute | reroute | 0.800 | 0.000 | 0.183 | 0.400 | 2.800 | 38.042 |
| MR-040 | single_agent | 5 | reroute | reroute | 1.000 | 0.286 | 0.286 | 0.500 | 2.000 | 5.686 |
| MR-041 | multi_agent_orchestration | 5 | reroute | reroute | 1.000 | 0.000 | 0.000 | 0.000 | 2.000 | 37.314 |
| MR-041 | single_agent | 5 | reroute | reroute | 1.000 | 0.000 | 0.000 | 0.000 | 2.000 | 5.672 |
| MR-042 | multi_agent_orchestration | 5 | reroute | reroute | 1.000 | 0.000 | 0.000 | 0.000 | 2.000 | 31.466 |
| MR-042 | single_agent | 5 | reroute | reroute | 1.000 | 0.000 | 0.000 | 0.000 | 0.800 | 5.557 |
| MR-043 | multi_agent_orchestration | 5 | reroute | reroute | 1.000 | 0.000 | 0.000 | 0.000 | 3.200 | 34.754 |
| MR-043 | single_agent | 5 | reroute | reroute | 1.000 | 0.000 | 0.000 | 0.000 | 1.200 | 6.229 |
| MR-044 | multi_agent_orchestration | 5 | reroute | reroute | 1.000 | 0.000 | 0.239 | 0.500 | 2.400 | 37.051 |
| MR-044 | single_agent | 5 | reroute | reroute | 1.000 | 0.000 | 0.286 | 0.500 | 1.200 | 7.065 |
| MR-045 | multi_agent_orchestration | 5 | reroute | reroute | 0.800 | 0.000 | 0.050 | 0.100 | 2.800 | 38.804 |
| MR-045 | single_agent | 5 | reroute | reroute | 1.000 | 0.000 | 0.000 | 0.000 | 1.800 | 5.887 |
| MR-046 | multi_agent_orchestration | 5 | reroute | reroute | 1.000 | 0.000 | 0.222 | 0.500 | 1.600 | 34.503 |
| MR-046 | single_agent | 5 | reroute | reroute | 1.000 | 0.124 | 0.314 | 0.500 | 0.800 | 5.812 |
| MR-047 | multi_agent_orchestration | 5 | reroute | reroute | 1.000 | 0.000 | 0.234 | 0.500 | 2.800 | 35.947 |
| MR-047 | single_agent | 5 | reroute | reroute | 1.000 | 0.000 | 0.346 | 0.500 | 1.200 | 5.244 |
| MR-048 | multi_agent_orchestration | 5 | reroute | reroute | 1.000 | 0.000 | 0.000 | 0.000 | 2.800 | 34.255 |
| MR-048 | single_agent | 5 | reroute | reroute | 1.000 | 0.000 | 0.000 | 0.000 | 1.400 | 4.805 |
| MR-049 | multi_agent_orchestration | 5 | reroute | proceed | 0.000 | 0.000 | 0.000 | 0.000 | 2.800 | 38.024 |
| MR-049 | single_agent | 5 | reroute | reroute | 1.000 | 0.000 | 0.000 | 0.000 | 1.000 | 6.065 |
| MR-050 | multi_agent_orchestration | 5 | reroute | reroute | 1.000 | 0.000 | 0.223 | 0.500 | 1.600 | 34.003 |
| MR-050 | single_agent | 5 | reroute | reroute | 1.000 | 0.000 | 0.295 | 0.500 | 0.600 | 6.151 |
| MR-051 | multi_agent_orchestration | 5 | reroute | reroute | 1.000 | 0.000 | 0.000 | 0.000 | 3.400 | 34.977 |
| MR-051 | single_agent | 5 | reroute | reroute | 1.000 | 0.000 | 0.000 | 0.000 | 1.000 | 6.032 |
| MR-052 | multi_agent_orchestration | 5 | reroute | reroute | 1.000 | 0.000 | 0.200 | 0.400 | 2.200 | 39.061 |
| MR-052 | single_agent | 5 | reroute | reroute | 1.000 | 0.286 | 0.286 | 0.500 | 1.200 | 5.803 |
| MR-053 | multi_agent_orchestration | 5 | reroute | reroute | 0.800 | 0.000 | 0.000 | 0.000 | 2.200 | 38.297 |
| MR-053 | single_agent | 5 | reroute | reroute | 1.000 | 0.000 | 0.000 | 0.000 | 1.600 | 5.871 |
| MR-054 | multi_agent_orchestration | 5 | reroute | reroute | 1.000 | 0.000 | 0.000 | 0.000 | 2.200 | 33.852 |
| MR-054 | single_agent | 5 | reroute | reroute | 1.000 | 0.000 | 0.000 | 0.000 | 1.200 | 4.929 |
| MR-055 | multi_agent_orchestration | 5 | pause | pause | 1.000 | 0.000 | 0.360 | 1.000 | 1.400 | 33.258 |
| MR-055 | single_agent | 5 | pause | pause | 1.000 | 0.000 | 0.600 | 1.000 | 0.400 | 6.393 |
| MR-056 | multi_agent_orchestration | 5 | pause | pause | 1.000 | 0.000 | 0.133 | 0.300 | 2.600 | 35.750 |
| MR-056 | single_agent | 5 | pause | pause | 1.000 | 0.000 | 0.080 | 0.100 | 1.000 | 5.533 |
| MR-057 | multi_agent_orchestration | 5 | pause | pause | 1.000 | 0.000 | 0.000 | 0.000 | 2.600 | 33.299 |
| MR-057 | single_agent | 5 | pause | pause | 1.000 | 0.000 | 0.000 | 0.000 | 2.200 | 5.244 |
| MR-058 | multi_agent_orchestration | 5 | pause | pause | 1.000 | 0.000 | 0.000 | 0.000 | 1.600 | 38.337 |
| MR-058 | single_agent | 5 | pause | pause | 1.000 | 0.000 | 0.000 | 0.000 | 1.200 | 5.085 |
| MR-059 | multi_agent_orchestration | 5 | pause | pause | 1.000 | 0.000 | 0.000 | 0.000 | 3.200 | 33.909 |
| MR-059 | single_agent | 5 | pause | pause | 1.000 | 0.000 | 0.000 | 0.000 | 1.600 | 7.119 |
| MR-060 | multi_agent_orchestration | 5 | pause | pause | 1.000 | 0.000 | 0.044 | 0.100 | 3.400 | 35.431 |
| MR-060 | single_agent | 5 | pause | pause | 1.000 | 0.000 | 0.000 | 0.000 | 3.000 | 5.352 |
| MR-061 | multi_agent_orchestration | 5 | pause | pause | 1.000 | 0.000 | 0.000 | 0.000 | 3.400 | 34.154 |
| MR-061 | single_agent | 5 | pause | pause | 1.000 | 0.000 | 0.000 | 0.000 | 1.800 | 4.571 |
| MR-062 | multi_agent_orchestration | 5 | pause | pause | 1.000 | 0.000 | 0.100 | 0.200 | 1.800 | 34.384 |
| MR-062 | single_agent | 5 | pause | pause | 1.000 | 0.000 | 0.160 | 0.200 | 0.000 | 4.691 |
| MR-063 | multi_agent_orchestration | 5 | pause | pause | 1.000 | 0.000 | 0.000 | 0.000 | 2.000 | 31.889 |
| MR-063 | single_agent | 5 | pause | pause | 1.000 | 0.000 | 0.000 | 0.000 | 0.600 | 6.065 |
| MR-064 | multi_agent_orchestration | 5 | pause | pause | 1.000 | 0.000 | 0.000 | 0.000 | 3.400 | 34.627 |
| MR-064 | single_agent | 5 | pause | pause | 1.000 | 0.000 | 0.000 | 0.000 | 3.000 | 5.392 |
| MR-065 | multi_agent_orchestration | 5 | pause | pause | 1.000 | 0.000 | 0.000 | 0.000 | 3.400 | 32.402 |
| MR-065 | single_agent | 5 | pause | pause | 1.000 | 0.000 | 0.000 | 0.000 | 2.000 | 5.197 |
| MR-066 | multi_agent_orchestration | 5 | pause | pause | 1.000 | 0.000 | 0.000 | 0.000 | 2.000 | 36.789 |
| MR-066 | single_agent | 5 | pause | pause | 1.000 | 0.000 | 0.000 | 0.000 | 1.400 | 4.627 |
| MR-067 | multi_agent_orchestration | 5 | pause | pause | 1.000 | 0.000 | 0.000 | 0.000 | 1.600 | 34.780 |
| MR-067 | single_agent | 5 | pause | pause | 1.000 | 0.000 | 0.160 | 0.400 | 1.800 | 6.758 |
| MR-068 | multi_agent_orchestration | 5 | pause | pause | 1.000 | 0.000 | 0.089 | 0.200 | 2.800 | 36.348 |
| MR-068 | single_agent | 5 | pause | pause | 1.000 | 0.000 | 0.067 | 0.100 | 2.200 | 5.554 |
| MR-069 | multi_agent_orchestration | 5 | pause | pause | 1.000 | 0.000 | 0.000 | 0.000 | 2.800 | 33.985 |
| MR-069 | single_agent | 5 | pause | pause | 1.000 | 0.000 | 0.000 | 0.000 | 1.200 | 7.066 |
| MR-070 | multi_agent_orchestration | 5 | pause | pause | 1.000 | 0.000 | 0.000 | 0.000 | 3.000 | 35.001 |
| MR-070 | single_agent | 5 | pause | pause | 1.000 | 0.000 | 0.000 | 0.000 | 0.800 | 4.834 |
| MR-071 | multi_agent_orchestration | 5 | pause | pause | 1.000 | 0.000 | 0.000 | 0.000 | 2.600 | 35.147 |
| MR-071 | single_agent | 5 | pause | pause | 1.000 | 0.000 | 0.000 | 0.000 | 0.800 | 6.840 |
| MR-072 | multi_agent_orchestration | 5 | pause | pause | 1.000 | 0.000 | 0.000 | 0.000 | 3.200 | 36.697 |
| MR-072 | single_agent | 5 | pause | pause | 1.000 | 0.000 | 0.000 | 0.000 | 3.000 | 5.795 |
| MR-073 | multi_agent_orchestration | 5 | pause | pause | 1.000 | 0.000 | 0.314 | 1.000 | 2.200 | 32.288 |
| MR-073 | single_agent | 5 | pause | pause | 1.000 | 0.000 | 0.300 | 0.600 | 1.400 | 4.846 |
| MR-074 | multi_agent_orchestration | 5 | pause | pause | 1.000 | 0.000 | 0.000 | 0.000 | 1.800 | 36.254 |
| MR-074 | single_agent | 5 | pause | pause | 1.000 | 0.000 | 0.067 | 0.100 | 1.400 | 6.018 |
| MR-075 | multi_agent_orchestration | 5 | pause | pause | 1.000 | 0.000 | 0.000 | 0.000 | 1.800 | 34.239 |
| MR-075 | single_agent | 5 | pause | pause | 1.000 | 0.000 | 0.000 | 0.000 | 1.600 | 5.889 |
| MR-076 | multi_agent_orchestration | 5 | pause | pause | 0.800 | 0.000 | 0.000 | 0.000 | 2.600 | 40.668 |
| MR-076 | single_agent | 5 | pause | pause | 1.000 | 0.000 | 0.000 | 0.000 | 1.800 | 5.784 |
| MR-077 | multi_agent_orchestration | 5 | pause | pause | 1.000 | 0.000 | 0.000 | 0.000 | 3.000 | 32.380 |
| MR-077 | single_agent | 5 | pause | pause | 1.000 | 0.000 | 0.000 | 0.000 | 1.800 | 4.962 |
| MR-078 | multi_agent_orchestration | 5 | request_human_review | request_human_review | 1.000 | 0.000 | 0.165 | 0.333 | 3.000 | 40.812 |
| MR-078 | single_agent | 5 | request_human_review | request_human_review | 0.600 | 0.113 | 0.193 | 0.333 | 2.000 | 8.291 |
| MR-079 | multi_agent_orchestration | 5 | request_human_review | request_human_review | 1.000 | 0.000 | 0.000 | 0.000 | 3.800 | 43.526 |
| MR-079 | single_agent | 5 | request_human_review | request_human_review | 1.000 | 0.000 | 0.000 | 0.000 | 2.200 | 5.651 |
| MR-080 | multi_agent_orchestration | 5 | request_human_review | reroute | 0.200 | 0.000 | 0.000 | 0.000 | 2.800 | 43.857 |
| MR-080 | single_agent | 5 | request_human_review | request_human_review | 1.000 | 0.000 | 0.000 | 0.000 | 2.000 | 7.651 |
| MR-081 | multi_agent_orchestration | 5 | request_human_review | request_human_review | 1.000 | 0.000 | 0.193 | 0.333 | 3.400 | 40.933 |
| MR-081 | single_agent | 5 | request_human_review | request_human_review | 1.000 | 0.000 | 0.250 | 0.333 | 1.400 | 7.431 |
| MR-082 | multi_agent_orchestration | 5 | request_human_review | request_human_review | 1.000 | 0.000 | 0.000 | 0.000 | 1.200 | 40.119 |
| MR-082 | single_agent | 5 | request_human_review | request_human_review | 1.000 | 0.000 | 0.000 | 0.000 | 0.400 | 9.584 |
| MR-083 | multi_agent_orchestration | 5 | request_human_review | request_human_review | 1.000 | 0.000 | 0.000 | 0.000 | 4.200 | 41.321 |
| MR-083 | single_agent | 5 | request_human_review | request_human_review | 1.000 | 0.000 | 0.000 | 0.000 | 2.400 | 5.930 |
| MR-084 | multi_agent_orchestration | 5 | request_human_review | request_human_review | 1.000 | 0.000 | 0.183 | 0.333 | 1.800 | 45.960 |
| MR-084 | single_agent | 5 | request_human_review | request_human_review | 1.000 | 0.124 | 0.204 | 0.333 | 1.400 | 9.649 |
| MR-085 | multi_agent_orchestration | 5 | request_human_review | request_human_review | 1.000 | 0.000 | 0.000 | 0.000 | 3.800 | 39.645 |
| MR-085 | single_agent | 5 | request_human_review | request_human_review | 1.000 | 0.000 | 0.000 | 0.000 | 2.000 | 6.627 |
| MR-086 | multi_agent_orchestration | 5 | request_human_review | request_human_review | 1.000 | 0.000 | 0.000 | 0.000 | 3.000 | 39.964 |
| MR-086 | single_agent | 5 | request_human_review | request_human_review | 0.800 | 0.000 | 0.000 | 0.000 | 1.600 | 8.862 |
| MR-087 | multi_agent_orchestration | 5 | request_human_review | request_human_review | 1.000 | 0.000 | 0.179 | 0.333 | 3.800 | 39.770 |
| MR-087 | single_agent | 5 | request_human_review | request_human_review | 1.000 | 0.192 | 0.249 | 0.333 | 2.200 | 7.028 |
| MR-088 | multi_agent_orchestration | 5 | request_human_review | request_human_review | 1.000 | 0.000 | 0.036 | 0.067 | 2.600 | 38.749 |
| MR-088 | single_agent | 5 | request_human_review | request_human_review | 1.000 | 0.000 | 0.000 | 0.000 | 1.000 | 6.833 |
| MR-089 | multi_agent_orchestration | 5 | request_human_review | request_human_review | 1.000 | 0.000 | 0.000 | 0.000 | 3.400 | 39.257 |
| MR-089 | single_agent | 5 | request_human_review | request_human_review | 1.000 | 0.000 | 0.000 | 0.000 | 0.800 | 8.000 |
| MR-090 | multi_agent_orchestration | 5 | request_human_review | request_human_review | 1.000 | 0.000 | 0.165 | 0.333 | 3.200 | 39.853 |
| MR-090 | single_agent | 5 | request_human_review | request_human_review | 0.600 | 0.070 | 0.183 | 0.333 | 2.400 | 9.059 |
| MR-091 | multi_agent_orchestration | 5 | request_human_review | request_human_review | 1.000 | 0.000 | 0.000 | 0.000 | 4.200 | 37.225 |
| MR-091 | single_agent | 5 | request_human_review | request_human_review | 1.000 | 0.000 | 0.000 | 0.000 | 2.200 | 5.902 |
| MR-092 | multi_agent_orchestration | 5 | request_human_review | request_human_review | 0.800 | 0.000 | 0.000 | 0.000 | 3.600 | 43.223 |
| MR-092 | single_agent | 5 | request_human_review | request_human_review | 0.800 | 0.000 | 0.000 | 0.000 | 2.800 | 8.759 |
| MR-093 | multi_agent_orchestration | 5 | request_human_review | request_human_review | 1.000 | 0.000 | 0.201 | 0.333 | 3.000 | 41.341 |
| MR-093 | single_agent | 5 | request_human_review | request_human_review | 1.000 | 0.050 | 0.250 | 0.333 | 1.600 | 8.186 |
| MR-094 | multi_agent_orchestration | 5 | request_human_review | request_human_review | 1.000 | 0.000 | 0.044 | 0.067 | 1.400 | 37.890 |
| MR-094 | single_agent | 5 | request_human_review | request_human_review | 0.800 | 0.000 | 0.000 | 0.000 | 0.200 | 8.855 |
| MR-095 | multi_agent_orchestration | 5 | request_human_review | request_human_review | 1.000 | 0.000 | 0.000 | 0.000 | 4.600 | 40.042 |
| MR-095 | single_agent | 5 | request_human_review | request_human_review | 1.000 | 0.000 | 0.000 | 0.000 | 2.200 | 6.613 |
| MR-096 | multi_agent_orchestration | 5 | request_human_review | request_human_review | 0.600 | 0.000 | 0.180 | 0.333 | 2.000 | 41.533 |
| MR-096 | single_agent | 5 | request_human_review | request_human_review | 0.800 | 0.120 | 0.200 | 0.333 | 1.600 | 7.659 |
| MR-097 | multi_agent_orchestration | 5 | request_human_review | request_human_review | 1.000 | 0.000 | 0.000 | 0.000 | 4.200 | 40.612 |
| MR-097 | single_agent | 5 | request_human_review | request_human_review | 1.000 | 0.000 | 0.000 | 0.000 | 1.800 | 6.683 |
| MR-098 | multi_agent_orchestration | 5 | request_human_review | request_human_review | 1.000 | 0.000 | 0.000 | 0.000 | 3.200 | 40.771 |
| MR-098 | single_agent | 5 | request_human_review | request_human_review | 0.800 | 0.000 | 0.000 | 0.000 | 1.400 | 8.602 |
| MR-099 | multi_agent_orchestration | 5 | request_human_review | request_human_review | 1.000 | 0.000 | 0.194 | 0.333 | 3.400 | 38.902 |
| MR-099 | single_agent | 5 | request_human_review | request_human_review | 1.000 | 0.150 | 0.257 | 0.333 | 2.000 | 6.632 |
| MR-100 | multi_agent_orchestration | 5 | request_human_review | request_human_review | 1.000 | 0.000 | 0.000 | 0.000 | 3.000 | 39.196 |
| MR-100 | single_agent | 5 | request_human_review | request_human_review | 1.000 | 0.000 | 0.000 | 0.000 | 1.000 | 7.096 |

## Table 3. Incorrect decisions
| scenario_id | run_id | architecture_type | expected_action | recommended_action | semantic_hazard_f1 | latency_seconds | confidence_score |
| --- | --- | --- | --- | --- | --- | --- | --- |
| MR-002 | 1 | multi_agent_orchestration | reroute | request_human_review | 0.200 | 40.554 | 0.890 |
| MR-004 | 1 | single_agent | request_human_review | reroute | 0.000 | 5.216 | 0.860 |
| MR-008 | 1 | multi_agent_orchestration | request_human_review | reroute | 0.286 | 41.678 | 0.740 |
| MR-033 | 1 | multi_agent_orchestration | reroute | proceed | 0.000 | 32.600 | 0.830 |
| MR-037 | 1 | multi_agent_orchestration | reroute | proceed | 0.000 | 37.039 | 0.830 |
| MR-049 | 1 | multi_agent_orchestration | reroute | proceed | 0.000 | 36.568 | 0.830 |
| MR-080 | 1 | multi_agent_orchestration | request_human_review | reroute | 0.000 | 37.894 | 0.840 |
| MR-092 | 1 | single_agent | request_human_review | reroute | 0.000 | 9.114 | 0.780 |
| MR-094 | 1 | single_agent | request_human_review | reroute | 0.000 | 8.351 | 0.860 |
| MR-098 | 1 | single_agent | request_human_review | reroute | 0.000 | 9.406 | 0.860 |
| MR-002 | 2 | multi_agent_orchestration | reroute | pause | 0.167 | 47.475 | 0.900 |
| MR-004 | 2 | single_agent | request_human_review | reroute | 0.000 | 6.955 | 0.840 |
| MR-006 | 2 | multi_agent_orchestration | pause | request_human_review | 0.222 | 44.448 | 0.850 |
| MR-008 | 2 | multi_agent_orchestration | request_human_review | reroute | 0.308 | 38.593 | 0.820 |
| MR-049 | 2 | multi_agent_orchestration | reroute | proceed | 0.000 | 43.886 | 0.820 |
| MR-078 | 2 | single_agent | request_human_review | reroute | 0.200 | 7.063 | 0.840 |
| MR-080 | 2 | multi_agent_orchestration | request_human_review | reroute | 0.000 | 40.379 | 0.840 |
| MR-092 | 2 | multi_agent_orchestration | request_human_review | reroute | 0.000 | 34.616 | 0.820 |
| MR-096 | 2 | single_agent | request_human_review | reroute | 0.200 | 7.326 | 0.840 |
| MR-096 | 2 | multi_agent_orchestration | request_human_review | reroute | 0.182 | 37.788 | 0.840 |
| MR-002 | 3 | multi_agent_orchestration | reroute | pause | 0.222 | 40.029 | 0.900 |
| MR-004 | 3 | single_agent | request_human_review | reroute | 0.000 | 5.265 | 0.860 |
| MR-006 | 3 | multi_agent_orchestration | pause | request_human_review | 0.222 | 40.729 | 0.850 |
| MR-008 | 3 | multi_agent_orchestration | request_human_review | reroute | 0.286 | 34.092 | 0.800 |
| MR-033 | 3 | multi_agent_orchestration | reroute | proceed | 0.000 | 38.408 | 0.840 |
| MR-037 | 3 | multi_agent_orchestration | reroute | proceed | 0.000 | 39.161 | 0.830 |
| MR-040 | 3 | multi_agent_orchestration | reroute | pause | 0.222 | 35.982 | 0.850 |
| MR-049 | 3 | multi_agent_orchestration | reroute | proceed | 0.000 | 33.917 | 0.820 |
| MR-080 | 3 | multi_agent_orchestration | request_human_review | reroute | 0.000 | 44.223 | 0.840 |
| MR-090 | 3 | single_agent | request_human_review | reroute | 0.167 | 7.399 | 0.870 |
| MR-002 | 4 | multi_agent_orchestration | reroute | request_human_review | 0.200 | 46.799 | 0.890 |
| MR-004 | 4 | single_agent | request_human_review | reroute | 0.000 | 6.444 | 0.820 |
| MR-033 | 4 | multi_agent_orchestration | reroute | proceed | 0.000 | 36.449 | 0.830 |
| MR-037 | 4 | multi_agent_orchestration | reroute | proceed | 0.000 | 36.112 | 0.850 |
| MR-049 | 4 | multi_agent_orchestration | reroute | proceed | 0.000 | 35.494 | 0.830 |
| MR-076 | 4 | multi_agent_orchestration | pause | request_human_review | 0.000 | 48.642 | 0.840 |
| MR-080 | 4 | multi_agent_orchestration | request_human_review | reroute | 0.000 | 45.648 | 0.830 |
| MR-096 | 4 | multi_agent_orchestration | request_human_review | reroute | 0.167 | 43.725 | 0.860 |
| MR-002 | 5 | multi_agent_orchestration | reroute | pause | 0.200 | 37.584 | 0.890 |
| MR-008 | 5 | multi_agent_orchestration | request_human_review | reroute | 0.308 | 38.220 | 0.780 |
| MR-045 | 5 | multi_agent_orchestration | reroute | proceed | 0.000 | 41.068 | 0.830 |
| MR-049 | 5 | multi_agent_orchestration | reroute | proceed | 0.000 | 40.253 | 0.820 |
| MR-053 | 5 | multi_agent_orchestration | reroute | proceed | 0.000 | 38.589 | 0.840 |
| MR-078 | 5 | single_agent | request_human_review | reroute | 0.200 | 6.816 | 0.860 |
| MR-086 | 5 | single_agent | request_human_review | reroute | 0.000 | 10.977 | 0.840 |
| MR-090 | 5 | single_agent | request_human_review | reroute | 0.200 | 7.984 | 0.860 |

## Table 4. Pairwise statistical comparisons
| architecture_a | architecture_b | metric | test_name | test_statistic_name | test_statistic_value | architecture_a_mean | architecture_b_mean | difference_b_minus_a | bootstrap_ci_low | bootstrap_ci_high | effect_size_name | effect_size | effect_size_ci_low | effect_size_ci_high | cohens_dz | cohens_dz_ci_low | cohens_dz_ci_high | exact_p_value | holm_adjusted_p_value | sign_test_p_value | favored_architecture |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| multi_agent_orchestration | single_agent | decision_correct | exact McNemar test | discordant_pairs | 44 | 0.934 | 0.974 | 0.040 | 0.014 | 0.066 | rank_biserial_correlation | 0.455 | 0.182 | 0.697 | 0.136 | 0.053 | 0.215 | 0.004 | 0.011 | 0.004 | single_agent |
| multi_agent_orchestration | single_agent | exact_hazard_f1 | exact paired sign test | positive_differences | 38 | 0.000 | 0.018 | 0.018 | 0.013 | 0.024 | rank_biserial_correlation | 1.000 | 1.000 | 1.000 | 0.280 | 0.234 | 0.325 | 0.000 | 0.000 | 0.000 | single_agent |
| multi_agent_orchestration | single_agent | semantic_hazard_f1 | exact paired sign test | positive_differences | 113 | 0.060 | 0.075 | 0.015 | 0.007 | 0.022 | rank_biserial_correlation | 0.725 | 0.603 | 0.841 | 0.173 | 0.084 | 0.267 | 0.000 | 0.000 | 0.000 | single_agent |
| multi_agent_orchestration | single_agent | canonical_hazard_coverage | exact paired sign test | positive_differences | 10 | 0.127 | 0.119 | -0.008 | -0.022 | 0.005 | rank_biserial_correlation | -0.231 | -0.625 | 0.161 | -0.053 | -0.138 | 0.038 | 0.327 | 0.654 | 0.327 | multi_agent_orchestration |
| multi_agent_orchestration | single_agent | plausible_noncanonical_hazard_count | exact paired sign test | positive_differences | 26 | 3.578 | 2.392 | -1.186 | -1.284 | -1.092 | rank_biserial_correlation | -0.867 | -0.914 | -0.817 | -1.073 | -1.178 | -0.978 | 0.000 | 0.000 | 0.000 | single_agent |
| multi_agent_orchestration | single_agent | spurious_hazard_count | exact paired sign test | positive_differences | 31 | 2.506 | 1.420 | -1.086 | -1.180 | -0.994 | rank_biserial_correlation | -0.841 | -0.893 | -0.786 | -1.017 | -1.131 | -0.920 | 0.000 | 0.000 | 0.000 | single_agent |
| multi_agent_orchestration | single_agent | hazard_false_positive_count | exact paired sign test | positive_differences | 2 | 6.084 | 3.812 | -2.272 | -2.368 | -2.178 | rank_biserial_correlation | -0.992 | -1.000 | -0.979 | -2.060 | -2.226 | -1.919 | 0.000 | 0.000 | 0.000 | single_agent |
| multi_agent_orchestration | single_agent | hazard_false_negative_count | exact paired sign test | positive_differences | 16 | 1.668 | 1.680 | 0.012 | -0.008 | 0.034 | rank_biserial_correlation | 0.231 | -0.161 | 0.625 | 0.053 | -0.035 | 0.138 | 0.327 | 0.654 | 0.327 | multi_agent_orchestration |
| multi_agent_orchestration | single_agent | latency_seconds | exact paired sign test | positive_differences | 0 | 35.585 | 6.064 | -29.521 | -29.958 | -29.092 | rank_biserial_correlation | -1.000 | -1.000 | -1.000 | -5.864 | -6.410 | -5.383 | 0.000 | 0.000 | 0.000 | single_agent |
| multi_agent_orchestration | single_agent | token_usage | exact paired sign test | positive_differences | 0 | 3160.208 | 547.656 | -2612.552 | -2634.046 | -2591.528 | rank_biserial_correlation | -1.000 | -1.000 | -1.000 | -10.679 | -11.328 | -10.145 | 0.000 | 0.000 | 0.000 | single_agent |
| multi_agent_orchestration | single_agent | confidence_score | exact paired sign test | positive_differences | 343 | 0.867 | 0.883 | 0.016 | 0.014 | 0.019 | rank_biserial_correlation | 0.556 | 0.476 | 0.632 | 0.569 | 0.476 | 0.673 | 0.000 | 0.000 | 0.000 | single_agent |

These tables are generated automatically from `outputs/results.json` and are intended for direct reuse in drafts, appendices, or supplementary materials.