# Paper-Ready Tables

## Table 1. Aggregate architecture comparison
| architecture_type | runs | scenarios | evaluations | decision_accuracy | mean_exact_hazard_f1 | mean_semantic_hazard_f1 | mean_hazard_false_positive_count | mean_canonical_hazard_coverage | mean_spurious_hazard_count | mean_latency_seconds | mean_token_usage |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| multi_agent_orchestration | 5 | 100 | 500 | 0.758 | 0.065 | 0.160 | 4.002 | 0.263 | 2.020 | 8.983 | 1717.004 |

## Table 2. Scenario-level performance by architecture
| scenario_id | architecture_type | runs | expected_action | modal_recommended_action | decision_accuracy | mean_exact_hazard_f1 | mean_semantic_hazard_f1 | mean_canonical_hazard_coverage | mean_spurious_hazard_count | mean_latency_seconds |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR-001 | multi_agent_orchestration | 5 | proceed | proceed | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 7.412 |
| MR-002 | multi_agent_orchestration | 5 | reroute | pause | 0.000 | 0.152 | 0.303 | 0.400 | 2.000 | 9.095 |
| MR-003 | multi_agent_orchestration | 5 | pause | pause | 1.000 | 0.000 | 0.580 | 1.000 | 0.400 | 7.991 |
| MR-004 | multi_agent_orchestration | 5 | request_human_review | request_human_review | 0.600 | 0.000 | 0.154 | 0.266 | 1.800 | 8.797 |
| MR-005 | multi_agent_orchestration | 5 | reroute | reroute | 0.600 | 0.286 | 0.514 | 0.900 | 3.200 | 8.394 |
| MR-006 | multi_agent_orchestration | 5 | pause | pause | 0.800 | 0.000 | 0.000 | 0.000 | 1.800 | 8.022 |
| MR-007 | multi_agent_orchestration | 5 | proceed | proceed | 1.000 | 0.000 | 0.000 | 0.000 | 1.600 | 7.396 |
| MR-008 | multi_agent_orchestration | 5 | request_human_review | proceed | 0.000 | 0.386 | 0.578 | 0.600 | 0.000 | 8.217 |
| MR-009 | multi_agent_orchestration | 5 | proceed | proceed | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 7.408 |
| MR-010 | multi_agent_orchestration | 5 | proceed | proceed | 1.000 | 0.000 | 0.000 | 0.000 | 1.000 | 9.009 |
| MR-011 | multi_agent_orchestration | 5 | proceed | proceed | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 7.932 |
| MR-012 | multi_agent_orchestration | 5 | proceed | proceed | 1.000 | 0.000 | 0.000 | 0.000 | 0.800 | 8.051 |
| MR-013 | multi_agent_orchestration | 5 | proceed | proceed | 1.000 | 0.000 | 0.000 | 0.000 | 0.600 | 8.208 |
| MR-014 | multi_agent_orchestration | 5 | proceed | proceed | 1.000 | 0.000 | 0.000 | 0.000 | 0.200 | 7.625 |
| MR-015 | multi_agent_orchestration | 5 | proceed | proceed | 1.000 | 0.000 | 0.000 | 0.000 | 0.200 | 7.751 |
| MR-016 | multi_agent_orchestration | 5 | proceed | proceed | 1.000 | 0.000 | 0.000 | 0.000 | 0.600 | 9.090 |
| MR-017 | multi_agent_orchestration | 5 | proceed | proceed | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 7.639 |
| MR-018 | multi_agent_orchestration | 5 | proceed | proceed | 1.000 | 0.000 | 0.000 | 0.000 | 1.400 | 8.762 |
| MR-019 | multi_agent_orchestration | 5 | proceed | proceed | 1.000 | 0.000 | 0.000 | 0.000 | 1.000 | 10.137 |
| MR-020 | multi_agent_orchestration | 5 | proceed | proceed | 1.000 | 0.000 | 0.000 | 0.000 | 0.800 | 7.800 |
| MR-021 | multi_agent_orchestration | 5 | proceed | proceed | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 7.635 |
| MR-022 | multi_agent_orchestration | 5 | proceed | proceed | 1.000 | 0.000 | 0.000 | 0.000 | 0.600 | 10.456 |
| MR-023 | multi_agent_orchestration | 5 | proceed | proceed | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 7.138 |
| MR-024 | multi_agent_orchestration | 5 | proceed | proceed | 1.000 | 0.000 | 0.000 | 0.000 | 2.000 | 7.962 |
| MR-025 | multi_agent_orchestration | 5 | proceed | proceed | 1.000 | 0.000 | 0.000 | 0.000 | 0.200 | 8.293 |
| MR-026 | multi_agent_orchestration | 5 | proceed | proceed | 1.000 | 0.000 | 0.000 | 0.000 | 0.200 | 9.047 |
| MR-027 | multi_agent_orchestration | 5 | proceed | proceed | 1.000 | 0.000 | 0.000 | 0.000 | 0.200 | 7.562 |
| MR-028 | multi_agent_orchestration | 5 | proceed | proceed | 1.000 | 0.000 | 0.000 | 0.000 | 0.800 | 9.535 |
| MR-029 | multi_agent_orchestration | 5 | proceed | proceed | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 7.748 |
| MR-030 | multi_agent_orchestration | 5 | proceed | proceed | 1.000 | 0.000 | 0.000 | 0.000 | 1.200 | 8.580 |
| MR-031 | multi_agent_orchestration | 5 | proceed | proceed | 1.000 | 0.000 | 0.000 | 0.000 | 0.400 | 8.019 |
| MR-032 | multi_agent_orchestration | 5 | reroute | proceed | 0.200 | 0.207 | 0.207 | 0.400 | 3.200 | 10.436 |
| MR-033 | multi_agent_orchestration | 5 | reroute | proceed | 0.000 | 0.233 | 0.233 | 0.500 | 3.400 | 8.674 |
| MR-034 | multi_agent_orchestration | 5 | reroute | reroute | 0.600 | 0.279 | 0.279 | 0.500 | 2.000 | 9.268 |
| MR-035 | multi_agent_orchestration | 5 | reroute | reroute | 1.000 | 0.000 | 0.495 | 0.800 | 2.400 | 8.660 |
| MR-036 | multi_agent_orchestration | 5 | reroute | reroute | 1.000 | 0.000 | 0.000 | 0.000 | 2.400 | 8.630 |
| MR-037 | multi_agent_orchestration | 5 | reroute | proceed | 0.000 | 0.000 | 0.000 | 0.000 | 3.600 | 9.033 |
| MR-038 | multi_agent_orchestration | 5 | reroute | reroute | 1.000 | 0.571 | 0.571 | 1.000 | 0.000 | 8.542 |
| MR-039 | multi_agent_orchestration | 5 | reroute | reroute | 1.000 | 0.000 | 0.050 | 0.100 | 3.000 | 9.907 |
| MR-040 | multi_agent_orchestration | 5 | reroute | reroute | 0.800 | 0.000 | 0.257 | 0.500 | 3.800 | 8.598 |
| MR-041 | multi_agent_orchestration | 5 | reroute | proceed | 0.000 | 0.000 | 0.250 | 0.500 | 3.200 | 10.081 |
| MR-042 | multi_agent_orchestration | 5 | reroute | reroute | 1.000 | 0.000 | 0.121 | 0.200 | 1.400 | 8.702 |
| MR-043 | multi_agent_orchestration | 5 | reroute | reroute | 1.000 | 0.000 | 0.000 | 0.000 | 2.600 | 9.643 |
| MR-044 | multi_agent_orchestration | 5 | reroute | reroute | 0.600 | 0.120 | 0.240 | 0.600 | 4.600 | 10.998 |
| MR-045 | multi_agent_orchestration | 5 | reroute | proceed | 0.000 | 0.231 | 0.288 | 0.500 | 1.800 | 8.983 |
| MR-046 | multi_agent_orchestration | 5 | reroute | reroute | 1.000 | 0.000 | 0.305 | 0.500 | 2.600 | 9.683 |
| MR-047 | multi_agent_orchestration | 5 | reroute | reroute | 1.000 | 0.000 | 0.614 | 0.900 | 1.400 | 8.560 |
| MR-048 | multi_agent_orchestration | 5 | reroute | reroute | 1.000 | 0.000 | 0.000 | 0.000 | 2.800 | 9.070 |
| MR-049 | multi_agent_orchestration | 5 | reroute | proceed | 0.000 | 0.000 | 0.000 | 0.000 | 4.800 | 9.369 |
| MR-050 | multi_agent_orchestration | 5 | reroute | reroute | 1.000 | 0.571 | 0.571 | 1.000 | 0.000 | 9.282 |
| MR-051 | multi_agent_orchestration | 5 | reroute | reroute | 1.000 | 0.000 | 0.057 | 0.100 | 2.000 | 9.743 |
| MR-052 | multi_agent_orchestration | 5 | reroute | reroute | 0.600 | 0.000 | 0.252 | 0.500 | 4.000 | 8.428 |
| MR-053 | multi_agent_orchestration | 5 | reroute | proceed | 0.000 | 0.000 | 0.250 | 0.500 | 2.800 | 8.552 |
| MR-054 | multi_agent_orchestration | 5 | reroute | reroute | 1.000 | 0.000 | 0.190 | 0.333 | 1.800 | 8.340 |
| MR-055 | multi_agent_orchestration | 5 | pause | pause | 1.000 | 0.000 | 0.667 | 1.000 | 0.000 | 8.703 |
| MR-056 | multi_agent_orchestration | 5 | pause | pause | 1.000 | 0.000 | 0.000 | 0.000 | 4.600 | 8.788 |
| MR-057 | multi_agent_orchestration | 5 | pause | pause | 1.000 | 0.000 | 0.000 | 0.000 | 4.200 | 8.942 |
| MR-058 | multi_agent_orchestration | 5 | pause | pause | 1.000 | 0.000 | 0.000 | 0.000 | 1.000 | 9.412 |
| MR-059 | multi_agent_orchestration | 5 | pause | pause | 1.000 | 0.000 | 0.000 | 0.000 | 1.400 | 9.121 |
| MR-060 | multi_agent_orchestration | 5 | pause | pause | 1.000 | 0.080 | 0.200 | 0.500 | 3.600 | 10.151 |
| MR-061 | multi_agent_orchestration | 5 | pause | pause | 1.000 | 0.000 | 0.000 | 0.000 | 3.000 | 9.112 |
| MR-062 | multi_agent_orchestration | 5 | pause | pause | 1.000 | 0.133 | 0.507 | 0.700 | 1.200 | 8.702 |
| MR-063 | multi_agent_orchestration | 5 | pause | pause | 1.000 | 0.000 | 0.000 | 0.000 | 1.200 | 8.834 |
| MR-064 | multi_agent_orchestration | 5 | pause | pause | 1.000 | 0.000 | 0.000 | 0.000 | 6.000 | 9.346 |
| MR-065 | multi_agent_orchestration | 5 | pause | pause | 1.000 | 0.000 | 0.000 | 0.000 | 4.000 | 8.436 |
| MR-066 | multi_agent_orchestration | 5 | pause | pause | 1.000 | 0.050 | 0.050 | 0.100 | 1.600 | 9.539 |
| MR-067 | multi_agent_orchestration | 5 | pause | pause | 1.000 | 0.000 | 0.667 | 1.000 | 1.000 | 7.770 |
| MR-068 | multi_agent_orchestration | 5 | pause | pause | 1.000 | 0.000 | 0.170 | 0.400 | 4.800 | 9.232 |
| MR-069 | multi_agent_orchestration | 5 | pause | pause | 1.000 | 0.000 | 0.000 | 0.000 | 2.000 | 7.718 |
| MR-070 | multi_agent_orchestration | 5 | pause | pause | 1.000 | 0.000 | 0.000 | 0.000 | 1.200 | 8.672 |
| MR-071 | multi_agent_orchestration | 5 | pause | pause | 1.000 | 0.000 | 0.000 | 0.000 | 1.600 | 7.832 |
| MR-072 | multi_agent_orchestration | 5 | pause | pause | 1.000 | 0.040 | 0.040 | 0.100 | 4.400 | 8.801 |
| MR-073 | multi_agent_orchestration | 5 | pause | pause | 1.000 | 0.000 | 0.000 | 0.000 | 4.000 | 9.215 |
| MR-074 | multi_agent_orchestration | 5 | pause | pause | 1.000 | 0.174 | 0.290 | 0.500 | 1.200 | 9.126 |
| MR-075 | multi_agent_orchestration | 5 | pause | pause | 1.000 | 0.000 | 0.000 | 0.000 | 1.600 | 10.363 |
| MR-076 | multi_agent_orchestration | 5 | pause | pause | 1.000 | 0.000 | 0.000 | 0.000 | 2.600 | 10.073 |
| MR-077 | multi_agent_orchestration | 5 | pause | pause | 1.000 | 0.000 | 0.000 | 0.000 | 3.000 | 8.468 |
| MR-078 | multi_agent_orchestration | 5 | request_human_review | pause | 0.000 | 0.218 | 0.391 | 0.600 | 0.400 | 8.853 |
| MR-079 | multi_agent_orchestration | 5 | request_human_review | request_human_review | 1.000 | 0.466 | 0.466 | 0.667 | 1.600 | 10.585 |
| MR-080 | multi_agent_orchestration | 5 | request_human_review | pause | 0.000 | 0.000 | 0.000 | 0.000 | 3.800 | 10.766 |
| MR-081 | multi_agent_orchestration | 5 | request_human_review | request_human_review | 0.600 | 0.129 | 0.520 | 0.800 | 1.800 | 9.126 |
| MR-082 | multi_agent_orchestration | 5 | request_human_review | pause | 0.400 | 0.000 | 0.000 | 0.000 | 1.400 | 9.563 |
| MR-083 | multi_agent_orchestration | 5 | request_human_review | pause | 0.200 | 0.000 | 0.209 | 0.333 | 4.400 | 8.493 |
| MR-084 | multi_agent_orchestration | 5 | request_human_review | pause | 0.200 | 0.169 | 0.426 | 0.667 | 1.200 | 9.481 |
| MR-085 | multi_agent_orchestration | 5 | request_human_review | request_human_review | 1.000 | 0.306 | 0.306 | 0.467 | 1.200 | 11.456 |
| MR-086 | multi_agent_orchestration | 5 | request_human_review | reroute | 0.000 | 0.000 | 0.000 | 0.000 | 3.600 | 11.700 |
| MR-087 | multi_agent_orchestration | 5 | request_human_review | request_human_review | 1.000 | 0.228 | 0.455 | 0.667 | 2.800 | 9.115 |
| MR-088 | multi_agent_orchestration | 5 | request_human_review | pause | 0.000 | 0.000 | 0.040 | 0.067 | 3.800 | 9.602 |
| MR-089 | multi_agent_orchestration | 5 | request_human_review | request_human_review | 0.600 | 0.000 | 0.186 | 0.333 | 4.600 | 10.709 |
| MR-090 | multi_agent_orchestration | 5 | request_human_review | pause | 0.000 | 0.210 | 0.419 | 0.667 | 0.400 | 9.405 |
| MR-091 | multi_agent_orchestration | 5 | request_human_review | request_human_review | 1.000 | 0.391 | 0.391 | 0.600 | 2.200 | 9.548 |
| MR-092 | multi_agent_orchestration | 5 | request_human_review | pause | 0.000 | 0.000 | 0.000 | 0.000 | 4.600 | 11.803 |
| MR-093 | multi_agent_orchestration | 5 | request_human_review | request_human_review | 0.800 | 0.089 | 0.536 | 0.800 | 1.600 | 8.364 |
| MR-094 | multi_agent_orchestration | 5 | request_human_review | request_human_review | 0.600 | 0.000 | 0.143 | 0.266 | 2.600 | 9.014 |
| MR-095 | multi_agent_orchestration | 5 | request_human_review | pause | 0.400 | 0.000 | 0.209 | 0.333 | 4.600 | 9.548 |
| MR-096 | multi_agent_orchestration | 5 | request_human_review | pause | 0.000 | 0.182 | 0.364 | 0.667 | 2.200 | 8.944 |
| MR-097 | multi_agent_orchestration | 5 | request_human_review | request_human_review | 1.000 | 0.373 | 0.373 | 0.600 | 1.600 | 9.733 |
| MR-098 | multi_agent_orchestration | 5 | request_human_review | reroute | 0.200 | 0.000 | 0.000 | 0.000 | 3.600 | 11.389 |
| MR-099 | multi_agent_orchestration | 5 | request_human_review | request_human_review | 1.000 | 0.229 | 0.542 | 0.800 | 2.400 | 8.062 |
| MR-100 | multi_agent_orchestration | 5 | request_human_review | pause | 0.000 | 0.000 | 0.036 | 0.067 | 3.800 | 8.802 |

## Table 3. Incorrect decisions
| scenario_id | run_id | architecture_type | expected_action | recommended_action | semantic_hazard_f1 | latency_seconds | confidence_score |
| --- | --- | --- | --- | --- | --- | --- | --- |
| MR-002 | 1 | multi_agent_orchestration | reroute | pause | 0.571 | 8.220 | 0.850 |
| MR-004 | 1 | multi_agent_orchestration | request_human_review | pause | 0.000 | 7.441 | 0.850 |
| MR-008 | 1 | multi_agent_orchestration | request_human_review | pause | 0.545 | 8.864 | 0.780 |
| MR-032 | 1 | multi_agent_orchestration | reroute | proceed | 0.000 | 10.139 | 0.850 |
| MR-033 | 1 | multi_agent_orchestration | reroute | proceed | 0.250 | 8.597 | 0.850 |
| MR-037 | 1 | multi_agent_orchestration | reroute | proceed | 0.000 | 9.523 | 0.880 |
| MR-041 | 1 | multi_agent_orchestration | reroute | proceed | 0.250 | 14.743 | 0.850 |
| MR-044 | 1 | multi_agent_orchestration | reroute | pause | 0.400 | 10.943 | 0.850 |
| MR-045 | 1 | multi_agent_orchestration | reroute | proceed | 0.333 | 10.118 | 0.880 |
| MR-049 | 1 | multi_agent_orchestration | reroute | proceed | 0.000 | 8.704 | 0.850 |
| MR-052 | 1 | multi_agent_orchestration | reroute | proceed | 0.250 | 8.198 | 0.850 |
| MR-053 | 1 | multi_agent_orchestration | reroute | proceed | 0.250 | 9.653 | 0.850 |
| MR-078 | 1 | multi_agent_orchestration | request_human_review | pause | 0.444 | 8.450 | 0.850 |
| MR-080 | 1 | multi_agent_orchestration | request_human_review | pause | 0.000 | 9.418 | 0.850 |
| MR-081 | 1 | multi_agent_orchestration | request_human_review | pause | 0.444 | 9.826 | 0.820 |
| MR-082 | 1 | multi_agent_orchestration | request_human_review | pause | 0.000 | 11.261 | 0.820 |
| MR-084 | 1 | multi_agent_orchestration | request_human_review | pause | 0.400 | 7.893 | 0.850 |
| MR-086 | 1 | multi_agent_orchestration | request_human_review | reroute | 0.000 | 8.749 | 0.850 |
| MR-088 | 1 | multi_agent_orchestration | request_human_review | pause | 0.000 | 9.490 | 0.850 |
| MR-089 | 1 | multi_agent_orchestration | request_human_review | pause | 0.182 | 8.752 | 0.800 |
| MR-090 | 1 | multi_agent_orchestration | request_human_review | pause | 0.444 | 9.497 | 0.850 |
| MR-092 | 1 | multi_agent_orchestration | request_human_review | pause | 0.000 | 9.726 | 0.850 |
| MR-093 | 1 | multi_agent_orchestration | request_human_review | pause | 0.500 | 9.526 | 0.850 |
| MR-094 | 1 | multi_agent_orchestration | request_human_review | reroute | 0.182 | 8.596 | 0.820 |
| MR-096 | 1 | multi_agent_orchestration | request_human_review | pause | 0.364 | 10.494 | 0.850 |
| MR-100 | 1 | multi_agent_orchestration | request_human_review | pause | 0.000 | 7.475 | 0.850 |
| MR-002 | 2 | multi_agent_orchestration | reroute | pause | 0.000 | 10.632 | 0.850 |
| MR-005 | 2 | multi_agent_orchestration | reroute | proceed | 0.286 | 8.678 | 0.850 |
| MR-008 | 2 | multi_agent_orchestration | request_human_review | proceed | 0.600 | 8.387 | 0.780 |
| MR-032 | 2 | multi_agent_orchestration | reroute | proceed | 0.286 | 10.242 | 0.850 |
| MR-033 | 2 | multi_agent_orchestration | reroute | proceed | 0.222 | 7.785 | 0.850 |
| MR-034 | 2 | multi_agent_orchestration | reroute | proceed | 0.286 | 7.912 | 0.850 |
| MR-037 | 2 | multi_agent_orchestration | reroute | proceed | 0.000 | 9.417 | 0.880 |
| MR-040 | 2 | multi_agent_orchestration | reroute | proceed | 0.250 | 8.192 | 0.850 |
| MR-041 | 2 | multi_agent_orchestration | reroute | proceed | 0.250 | 8.696 | 0.850 |
| MR-045 | 2 | multi_agent_orchestration | reroute | proceed | 0.286 | 9.759 | 0.880 |
| MR-049 | 2 | multi_agent_orchestration | reroute | proceed | 0.000 | 8.231 | 0.850 |
| MR-052 | 2 | multi_agent_orchestration | reroute | proceed | 0.286 | 8.297 | 0.850 |
| MR-053 | 2 | multi_agent_orchestration | reroute | proceed | 0.250 | 8.236 | 0.850 |
| MR-078 | 2 | multi_agent_orchestration | request_human_review | reroute | 0.444 | 10.525 | 0.820 |
| MR-080 | 2 | multi_agent_orchestration | request_human_review | pause | 0.000 | 8.293 | 0.850 |
| MR-083 | 2 | multi_agent_orchestration | request_human_review | pause | 0.200 | 7.952 | 0.800 |
| MR-084 | 2 | multi_agent_orchestration | request_human_review | pause | 0.444 | 8.802 | 0.850 |
| MR-086 | 2 | multi_agent_orchestration | request_human_review | pause | 0.000 | 8.902 | 0.850 |
| MR-088 | 2 | multi_agent_orchestration | request_human_review | pause | 0.000 | 8.169 | 0.850 |
| MR-090 | 2 | multi_agent_orchestration | request_human_review | reroute | 0.444 | 9.223 | 0.820 |
| MR-092 | 2 | multi_agent_orchestration | request_human_review | pause | 0.000 | 14.253 | 0.850 |
| MR-095 | 2 | multi_agent_orchestration | request_human_review | pause | 0.200 | 9.286 | 0.880 |
| MR-096 | 2 | multi_agent_orchestration | request_human_review | pause | 0.364 | 8.733 | 0.850 |
| MR-098 | 2 | multi_agent_orchestration | request_human_review | pause | 0.000 | 9.209 | 0.850 |
| MR-100 | 2 | multi_agent_orchestration | request_human_review | pause | 0.000 | 8.800 | 0.850 |
| MR-002 | 3 | multi_agent_orchestration | reroute | pause | 0.000 | 10.238 | 0.850 |
| MR-008 | 3 | multi_agent_orchestration | request_human_review | pause | 0.600 | 8.386 | 0.800 |
| MR-033 | 3 | multi_agent_orchestration | reroute | proceed | 0.222 | 8.355 | 0.850 |
| MR-034 | 3 | multi_agent_orchestration | reroute | proceed | 0.286 | 12.076 | 0.850 |
| MR-037 | 3 | multi_agent_orchestration | reroute | proceed | 0.000 | 8.703 | 0.880 |
| MR-041 | 3 | multi_agent_orchestration | reroute | proceed | 0.250 | 8.603 | 0.850 |
| MR-045 | 3 | multi_agent_orchestration | reroute | proceed | 0.286 | 8.805 | 0.880 |
| MR-049 | 3 | multi_agent_orchestration | reroute | proceed | 0.000 | 11.974 | 0.880 |
| MR-053 | 3 | multi_agent_orchestration | reroute | proceed | 0.250 | 8.568 | 0.850 |
| MR-078 | 3 | multi_agent_orchestration | request_human_review | pause | 0.222 | 9.110 | 0.850 |
| MR-080 | 3 | multi_agent_orchestration | request_human_review | pause | 0.000 | 8.173 | 0.850 |
| MR-081 | 3 | multi_agent_orchestration | request_human_review | pause | 0.444 | 9.269 | 0.850 |
| MR-083 | 3 | multi_agent_orchestration | request_human_review | pause | 0.200 | 8.697 | 0.850 |
| MR-084 | 3 | multi_agent_orchestration | request_human_review | pause | 0.444 | 8.607 | 0.850 |
| MR-086 | 3 | multi_agent_orchestration | request_human_review | reroute | 0.000 | 11.060 | 0.850 |
| MR-088 | 3 | multi_agent_orchestration | request_human_review | pause | 0.000 | 8.666 | 0.850 |
| MR-089 | 3 | multi_agent_orchestration | request_human_review | pause | 0.182 | 8.800 | 0.800 |
| MR-090 | 3 | multi_agent_orchestration | request_human_review | pause | 0.400 | 8.037 | 0.850 |
| MR-092 | 3 | multi_agent_orchestration | request_human_review | pause | 0.000 | 9.621 | 0.850 |
| MR-094 | 3 | multi_agent_orchestration | request_human_review | reroute | 0.182 | 9.208 | 0.850 |
| MR-096 | 3 | multi_agent_orchestration | request_human_review | pause | 0.364 | 7.779 | 0.850 |
| MR-098 | 3 | multi_agent_orchestration | request_human_review | reroute | 0.000 | 10.633 | 0.850 |
| MR-100 | 3 | multi_agent_orchestration | request_human_review | pause | 0.182 | 8.846 | 0.850 |
| MR-002 | 4 | multi_agent_orchestration | reroute | pause | 0.444 | 8.504 | 0.850 |
| MR-006 | 4 | multi_agent_orchestration | pause | proceed | 0.000 | 7.806 | 0.850 |
| MR-008 | 4 | multi_agent_orchestration | request_human_review | proceed | 0.600 | 6.889 | 0.750 |
| MR-032 | 4 | multi_agent_orchestration | reroute | pause | 0.250 | 11.781 | 0.850 |
| MR-033 | 4 | multi_agent_orchestration | reroute | proceed | 0.222 | 10.240 | 0.850 |
| MR-037 | 4 | multi_agent_orchestration | reroute | proceed | 0.000 | 9.122 | 0.880 |
| MR-041 | 4 | multi_agent_orchestration | reroute | proceed | 0.250 | 10.072 | 0.850 |
| MR-045 | 4 | multi_agent_orchestration | reroute | proceed | 0.286 | 7.838 | 0.880 |
| MR-049 | 4 | multi_agent_orchestration | reroute | proceed | 0.000 | 8.822 | 0.850 |
| MR-053 | 4 | multi_agent_orchestration | reroute | proceed | 0.250 | 7.738 | 0.850 |
| MR-078 | 4 | multi_agent_orchestration | request_human_review | pause | 0.444 | 7.577 | 0.850 |
| MR-080 | 4 | multi_agent_orchestration | request_human_review | pause | 0.000 | 18.014 | 0.850 |
| MR-082 | 4 | multi_agent_orchestration | request_human_review | pause | 0.000 | 7.680 | 0.850 |
| MR-083 | 4 | multi_agent_orchestration | request_human_review | pause | 0.222 | 8.713 | 0.850 |
| MR-084 | 4 | multi_agent_orchestration | request_human_review | pause | 0.444 | 9.720 | 0.850 |
| MR-086 | 4 | multi_agent_orchestration | request_human_review | reroute | 0.000 | 19.963 | 0.850 |
| MR-088 | 4 | multi_agent_orchestration | request_human_review | pause | 0.000 | 8.918 | 0.850 |
| MR-090 | 4 | multi_agent_orchestration | request_human_review | pause | 0.364 | 9.620 | 0.850 |
| MR-092 | 4 | multi_agent_orchestration | request_human_review | pause | 0.000 | 11.085 | 0.850 |
| MR-095 | 4 | multi_agent_orchestration | request_human_review | pause | 0.200 | 9.828 | 0.880 |
| MR-096 | 4 | multi_agent_orchestration | request_human_review | pause | 0.364 | 7.476 | 0.850 |
| MR-098 | 4 | multi_agent_orchestration | request_human_review | reroute | 0.000 | 9.422 | 0.850 |
| MR-100 | 4 | multi_agent_orchestration | request_human_review | pause | 0.000 | 8.784 | 0.850 |
| MR-002 | 5 | multi_agent_orchestration | reroute | pause | 0.500 | 7.880 | 0.850 |
| MR-004 | 5 | multi_agent_orchestration | request_human_review | pause | 0.200 | 10.062 | 0.850 |
| MR-005 | 5 | multi_agent_orchestration | reroute | proceed | 0.571 | 8.266 | 0.850 |
| MR-008 | 5 | multi_agent_orchestration | request_human_review | proceed | 0.545 | 8.560 | 0.780 |
| MR-032 | 5 | multi_agent_orchestration | reroute | proceed | 0.250 | 11.065 | 0.850 |
| MR-033 | 5 | multi_agent_orchestration | reroute | proceed | 0.250 | 8.395 | 0.850 |
| MR-037 | 5 | multi_agent_orchestration | reroute | proceed | 0.000 | 8.400 | 0.850 |
| MR-041 | 5 | multi_agent_orchestration | reroute | proceed | 0.250 | 8.292 | 0.850 |
| MR-044 | 5 | multi_agent_orchestration | reroute | pause | 0.400 | 12.188 | 0.850 |
| MR-045 | 5 | multi_agent_orchestration | reroute | proceed | 0.250 | 8.394 | 0.850 |
| MR-049 | 5 | multi_agent_orchestration | reroute | proceed | 0.000 | 9.116 | 0.850 |
| MR-053 | 5 | multi_agent_orchestration | reroute | proceed | 0.250 | 8.565 | 0.850 |
| MR-078 | 5 | multi_agent_orchestration | request_human_review | pause | 0.400 | 8.602 | 0.850 |
| MR-080 | 5 | multi_agent_orchestration | request_human_review | pause | 0.000 | 9.934 | 0.850 |
| MR-082 | 5 | multi_agent_orchestration | request_human_review | pause | 0.000 | 9.527 | 0.820 |
| MR-083 | 5 | multi_agent_orchestration | request_human_review | pause | 0.222 | 9.416 | 0.850 |
| MR-086 | 5 | multi_agent_orchestration | request_human_review | reroute | 0.000 | 9.827 | 0.820 |
| MR-088 | 5 | multi_agent_orchestration | request_human_review | pause | 0.200 | 12.765 | 0.850 |
| MR-090 | 5 | multi_agent_orchestration | request_human_review | pause | 0.444 | 10.648 | 0.850 |
| MR-092 | 5 | multi_agent_orchestration | request_human_review | pause | 0.000 | 14.329 | 0.850 |
| MR-095 | 5 | multi_agent_orchestration | request_human_review | pause | 0.200 | 9.010 | 0.880 |
| MR-096 | 5 | multi_agent_orchestration | request_human_review | pause | 0.364 | 10.240 | 0.850 |
| MR-098 | 5 | multi_agent_orchestration | request_human_review | reroute | 0.000 | 11.937 | 0.850 |
| MR-100 | 5 | multi_agent_orchestration | request_human_review | pause | 0.000 | 10.103 | 0.850 |

## Table 4. Pairwise statistical comparisons
No rows available.

These tables are generated automatically from `outputs/results.json` and are intended for direct reuse in drafts, appendices, or supplementary materials.