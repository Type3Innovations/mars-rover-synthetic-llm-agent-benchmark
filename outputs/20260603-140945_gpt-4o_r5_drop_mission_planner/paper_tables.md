# Paper-Ready Tables

## Table 1. Aggregate architecture comparison
| architecture_type | runs | scenarios | evaluations | decision_accuracy | mean_exact_hazard_f1 | mean_semantic_hazard_f1 | mean_hazard_false_positive_count | mean_canonical_hazard_coverage | mean_spurious_hazard_count | mean_latency_seconds | mean_token_usage |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| multi_agent_orchestration | 5 | 100 | 500 | 0.684 | 0.042 | 0.099 | 4.988 | 0.185 | 3.004 | 9.452 | 1827.730 |

## Table 2. Scenario-level performance by architecture
| scenario_id | architecture_type | runs | expected_action | modal_recommended_action | decision_accuracy | mean_exact_hazard_f1 | mean_semantic_hazard_f1 | mean_canonical_hazard_coverage | mean_spurious_hazard_count | mean_latency_seconds |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR-001 | multi_agent_orchestration | 5 | proceed | proceed | 1.000 | 0.000 | 0.000 | 0.000 | 2.600 | 8.044 |
| MR-002 | multi_agent_orchestration | 5 | reroute | pause | 0.000 | 0.000 | 0.000 | 0.000 | 3.000 | 11.807 |
| MR-003 | multi_agent_orchestration | 5 | pause | pause | 1.000 | 0.000 | 0.480 | 1.000 | 2.000 | 9.288 |
| MR-004 | multi_agent_orchestration | 5 | request_human_review | pause | 0.000 | 0.000 | 0.000 | 0.000 | 1.600 | 10.313 |
| MR-005 | multi_agent_orchestration | 5 | reroute | reroute | 1.000 | 0.302 | 0.302 | 0.500 | 2.800 | 9.183 |
| MR-006 | multi_agent_orchestration | 5 | pause | pause | 1.000 | 0.000 | 0.057 | 0.100 | 2.600 | 11.264 |
| MR-007 | multi_agent_orchestration | 5 | proceed | proceed | 1.000 | 0.000 | 0.000 | 0.000 | 3.600 | 8.443 |
| MR-008 | multi_agent_orchestration | 5 | request_human_review | pause | 0.000 | 0.320 | 0.385 | 0.480 | 1.600 | 8.835 |
| MR-009 | multi_agent_orchestration | 5 | proceed | proceed | 1.000 | 0.000 | 0.000 | 0.000 | 2.000 | 8.567 |
| MR-010 | multi_agent_orchestration | 5 | proceed | proceed | 1.000 | 0.000 | 0.000 | 0.000 | 2.800 | 8.962 |
| MR-011 | multi_agent_orchestration | 5 | proceed | proceed | 1.000 | 0.000 | 0.000 | 0.000 | 2.800 | 7.073 |
| MR-012 | multi_agent_orchestration | 5 | proceed | proceed | 1.000 | 0.000 | 0.000 | 0.000 | 3.400 | 8.115 |
| MR-013 | multi_agent_orchestration | 5 | proceed | proceed | 1.000 | 0.000 | 0.000 | 0.000 | 3.000 | 9.221 |
| MR-014 | multi_agent_orchestration | 5 | proceed | proceed | 1.000 | 0.000 | 0.000 | 0.000 | 2.200 | 7.268 |
| MR-015 | multi_agent_orchestration | 5 | proceed | proceed | 1.000 | 0.000 | 0.000 | 0.000 | 2.400 | 7.823 |
| MR-016 | multi_agent_orchestration | 5 | proceed | proceed | 1.000 | 0.000 | 0.000 | 0.000 | 1.800 | 10.126 |
| MR-017 | multi_agent_orchestration | 5 | proceed | proceed | 1.000 | 0.000 | 0.000 | 0.000 | 2.600 | 7.836 |
| MR-018 | multi_agent_orchestration | 5 | proceed | proceed | 1.000 | 0.000 | 0.000 | 0.000 | 2.600 | 7.636 |
| MR-019 | multi_agent_orchestration | 5 | proceed | proceed | 1.000 | 0.000 | 0.000 | 0.000 | 2.200 | 8.808 |
| MR-020 | multi_agent_orchestration | 5 | proceed | proceed | 1.000 | 0.000 | 0.000 | 0.000 | 1.800 | 8.339 |
| MR-021 | multi_agent_orchestration | 5 | proceed | proceed | 1.000 | 0.000 | 0.000 | 0.000 | 3.000 | 9.250 |
| MR-022 | multi_agent_orchestration | 5 | proceed | proceed | 1.000 | 0.000 | 0.000 | 0.000 | 3.000 | 9.581 |
| MR-023 | multi_agent_orchestration | 5 | proceed | proceed | 1.000 | 0.000 | 0.000 | 0.000 | 2.800 | 9.234 |
| MR-024 | multi_agent_orchestration | 5 | proceed | proceed | 1.000 | 0.000 | 0.000 | 0.000 | 3.000 | 8.644 |
| MR-025 | multi_agent_orchestration | 5 | proceed | proceed | 1.000 | 0.000 | 0.000 | 0.000 | 3.000 | 8.859 |
| MR-026 | multi_agent_orchestration | 5 | proceed | proceed | 1.000 | 0.000 | 0.000 | 0.000 | 2.200 | 7.876 |
| MR-027 | multi_agent_orchestration | 5 | proceed | proceed | 1.000 | 0.000 | 0.000 | 0.000 | 2.000 | 8.455 |
| MR-028 | multi_agent_orchestration | 5 | proceed | proceed | 1.000 | 0.000 | 0.000 | 0.000 | 2.000 | 8.731 |
| MR-029 | multi_agent_orchestration | 5 | proceed | proceed | 1.000 | 0.000 | 0.000 | 0.000 | 2.800 | 7.331 |
| MR-030 | multi_agent_orchestration | 5 | proceed | proceed | 1.000 | 0.000 | 0.000 | 0.000 | 2.200 | 8.830 |
| MR-031 | multi_agent_orchestration | 5 | proceed | proceed | 1.000 | 0.000 | 0.000 | 0.000 | 3.000 | 7.427 |
| MR-032 | multi_agent_orchestration | 5 | reroute | proceed | 0.200 | 0.150 | 0.150 | 0.300 | 4.400 | 8.842 |
| MR-033 | multi_agent_orchestration | 5 | reroute | proceed | 0.000 | 0.000 | 0.000 | 0.000 | 3.000 | 8.636 |
| MR-034 | multi_agent_orchestration | 5 | reroute | reroute | 0.600 | 0.286 | 0.286 | 0.500 | 1.200 | 9.414 |
| MR-035 | multi_agent_orchestration | 5 | reroute | reroute | 1.000 | 0.000 | 0.355 | 0.600 | 2.400 | 10.329 |
| MR-036 | multi_agent_orchestration | 5 | reroute | reroute | 1.000 | 0.000 | 0.040 | 0.067 | 3.400 | 9.788 |
| MR-037 | multi_agent_orchestration | 5 | reroute | proceed | 0.000 | 0.000 | 0.000 | 0.000 | 4.200 | 10.158 |
| MR-038 | multi_agent_orchestration | 5 | reroute | reroute | 1.000 | 0.329 | 0.329 | 0.600 | 0.600 | 9.901 |
| MR-039 | multi_agent_orchestration | 5 | reroute | reroute | 1.000 | 0.000 | 0.000 | 0.000 | 4.000 | 9.269 |
| MR-040 | multi_agent_orchestration | 5 | reroute | proceed | 0.000 | 0.000 | 0.229 | 0.400 | 3.200 | 10.034 |
| MR-041 | multi_agent_orchestration | 5 | reroute | proceed | 0.000 | 0.000 | 0.050 | 0.100 | 3.400 | 8.402 |
| MR-042 | multi_agent_orchestration | 5 | reroute | reroute | 1.000 | 0.000 | 0.000 | 0.000 | 2.600 | 8.408 |
| MR-043 | multi_agent_orchestration | 5 | reroute | reroute | 1.000 | 0.000 | 0.000 | 0.000 | 4.400 | 10.462 |
| MR-044 | multi_agent_orchestration | 5 | reroute | reroute | 0.600 | 0.133 | 0.133 | 0.300 | 4.400 | 13.064 |
| MR-045 | multi_agent_orchestration | 5 | reroute | proceed | 0.200 | 0.000 | 0.000 | 0.000 | 2.800 | 9.323 |
| MR-046 | multi_agent_orchestration | 5 | reroute | reroute | 1.000 | 0.057 | 0.264 | 0.500 | 1.800 | 8.848 |
| MR-047 | multi_agent_orchestration | 5 | reroute | reroute | 1.000 | 0.000 | 0.290 | 0.500 | 2.000 | 8.625 |
| MR-048 | multi_agent_orchestration | 5 | reroute | reroute | 1.000 | 0.000 | 0.000 | 0.000 | 2.600 | 7.827 |
| MR-049 | multi_agent_orchestration | 5 | reroute | proceed | 0.000 | 0.000 | 0.000 | 0.000 | 4.600 | 9.488 |
| MR-050 | multi_agent_orchestration | 5 | reroute | reroute | 1.000 | 0.414 | 0.414 | 0.800 | 1.000 | 9.836 |
| MR-051 | multi_agent_orchestration | 5 | reroute | reroute | 0.800 | 0.000 | 0.000 | 0.000 | 3.400 | 10.575 |
| MR-052 | multi_agent_orchestration | 5 | reroute | proceed | 0.400 | 0.000 | 0.164 | 0.300 | 3.400 | 9.412 |
| MR-053 | multi_agent_orchestration | 5 | reroute | proceed | 0.000 | 0.000 | 0.100 | 0.200 | 3.000 | 9.630 |
| MR-054 | multi_agent_orchestration | 5 | reroute | reroute | 1.000 | 0.000 | 0.113 | 0.200 | 2.600 | 8.044 |
| MR-055 | multi_agent_orchestration | 5 | pause | pause | 1.000 | 0.000 | 0.500 | 1.000 | 2.000 | 7.000 |
| MR-056 | multi_agent_orchestration | 5 | pause | pause | 1.000 | 0.000 | 0.000 | 0.000 | 3.200 | 8.295 |
| MR-057 | multi_agent_orchestration | 5 | pause | pause | 1.000 | 0.000 | 0.000 | 0.000 | 3.000 | 7.222 |
| MR-058 | multi_agent_orchestration | 5 | pause | pause | 1.000 | 0.000 | 0.000 | 0.000 | 2.600 | 8.496 |
| MR-059 | multi_agent_orchestration | 5 | pause | pause | 1.000 | 0.000 | 0.000 | 0.000 | 2.800 | 11.361 |
| MR-060 | multi_agent_orchestration | 5 | pause | pause | 1.000 | 0.000 | 0.000 | 0.000 | 4.000 | 8.703 |
| MR-061 | multi_agent_orchestration | 5 | pause | pause | 1.000 | 0.000 | 0.400 | 1.000 | 2.000 | 7.296 |
| MR-062 | multi_agent_orchestration | 5 | pause | pause | 1.000 | 0.000 | 0.333 | 0.500 | 1.200 | 9.519 |
| MR-063 | multi_agent_orchestration | 5 | pause | pause | 1.000 | 0.000 | 0.000 | 0.000 | 3.000 | 7.638 |
| MR-064 | multi_agent_orchestration | 5 | pause | pause | 1.000 | 0.000 | 0.000 | 0.000 | 4.000 | 8.891 |
| MR-065 | multi_agent_orchestration | 5 | pause | pause | 1.000 | 0.000 | 0.000 | 0.000 | 3.200 | 8.055 |
| MR-066 | multi_agent_orchestration | 5 | pause | pause | 1.000 | 0.114 | 0.114 | 0.200 | 2.000 | 9.287 |
| MR-067 | multi_agent_orchestration | 5 | pause | pause | 1.000 | 0.000 | 0.460 | 1.000 | 2.000 | 11.823 |
| MR-068 | multi_agent_orchestration | 5 | pause | pause | 1.000 | 0.000 | 0.000 | 0.000 | 3.400 | 8.028 |
| MR-069 | multi_agent_orchestration | 5 | pause | pause | 1.000 | 0.000 | 0.000 | 0.000 | 3.000 | 7.815 |
| MR-070 | multi_agent_orchestration | 5 | pause | pause | 1.000 | 0.000 | 0.000 | 0.000 | 1.600 | 9.307 |
| MR-071 | multi_agent_orchestration | 5 | pause | pause | 1.000 | 0.000 | 0.000 | 0.000 | 3.000 | 7.362 |
| MR-072 | multi_agent_orchestration | 5 | pause | pause | 1.000 | 0.000 | 0.000 | 0.000 | 3.600 | 9.965 |
| MR-073 | multi_agent_orchestration | 5 | pause | pause | 1.000 | 0.000 | 0.387 | 1.000 | 2.000 | 8.962 |
| MR-074 | multi_agent_orchestration | 5 | pause | pause | 1.000 | 0.000 | 0.200 | 0.400 | 3.000 | 9.582 |
| MR-075 | multi_agent_orchestration | 5 | pause | pause | 1.000 | 0.000 | 0.000 | 0.000 | 2.400 | 9.659 |
| MR-076 | multi_agent_orchestration | 5 | pause | pause | 1.000 | 0.000 | 0.000 | 0.000 | 1.800 | 8.543 |
| MR-077 | multi_agent_orchestration | 5 | pause | pause | 1.000 | 0.000 | 0.000 | 0.000 | 3.000 | 7.380 |
| MR-078 | multi_agent_orchestration | 5 | request_human_review | pause | 0.000 | 0.182 | 0.364 | 0.667 | 1.800 | 9.400 |
| MR-079 | multi_agent_orchestration | 5 | request_human_review | request_human_review | 0.600 | 0.400 | 0.400 | 0.667 | 4.000 | 11.721 |
| MR-080 | multi_agent_orchestration | 5 | request_human_review | pause | 0.000 | 0.000 | 0.000 | 0.000 | 5.200 | 9.599 |
| MR-081 | multi_agent_orchestration | 5 | request_human_review | pause | 0.200 | 0.110 | 0.219 | 0.400 | 4.400 | 15.473 |
| MR-082 | multi_agent_orchestration | 5 | request_human_review | pause | 0.000 | 0.000 | 0.000 | 0.000 | 1.800 | 11.525 |
| MR-083 | multi_agent_orchestration | 5 | request_human_review | pause | 0.000 | 0.000 | 0.044 | 0.067 | 5.800 | 9.555 |
| MR-084 | multi_agent_orchestration | 5 | request_human_review | pause | 0.000 | 0.179 | 0.252 | 0.467 | 1.200 | 8.281 |
| MR-085 | multi_agent_orchestration | 5 | request_human_review | pause | 0.400 | 0.116 | 0.116 | 0.200 | 3.200 | 11.510 |
| MR-086 | multi_agent_orchestration | 5 | request_human_review | reroute | 0.000 | 0.000 | 0.000 | 0.000 | 6.000 | 8.979 |
| MR-087 | multi_agent_orchestration | 5 | request_human_review | pause | 0.200 | 0.109 | 0.187 | 0.333 | 5.800 | 14.663 |
| MR-088 | multi_agent_orchestration | 5 | request_human_review | pause | 0.000 | 0.000 | 0.040 | 0.067 | 4.800 | 10.110 |
| MR-089 | multi_agent_orchestration | 5 | request_human_review | pause | 0.400 | 0.000 | 0.031 | 0.067 | 4.800 | 10.808 |
| MR-090 | multi_agent_orchestration | 5 | request_human_review | pause | 0.000 | 0.179 | 0.358 | 0.667 | 1.800 | 9.552 |
| MR-091 | multi_agent_orchestration | 5 | request_human_review | pause | 0.400 | 0.258 | 0.258 | 0.467 | 4.600 | 12.384 |
| MR-092 | multi_agent_orchestration | 5 | request_human_review | pause | 0.000 | 0.000 | 0.000 | 0.000 | 5.200 | 9.741 |
| MR-093 | multi_agent_orchestration | 5 | request_human_review | pause | 0.400 | 0.040 | 0.213 | 0.400 | 4.600 | 13.902 |
| MR-094 | multi_agent_orchestration | 5 | request_human_review | pause | 0.000 | 0.000 | 0.073 | 0.133 | 2.200 | 10.248 |
| MR-095 | multi_agent_orchestration | 5 | request_human_review | request_human_review | 0.600 | 0.000 | 0.040 | 0.067 | 5.600 | 10.412 |
| MR-096 | multi_agent_orchestration | 5 | request_human_review | pause | 0.000 | 0.143 | 0.318 | 0.600 | 2.000 | 8.986 |
| MR-097 | multi_agent_orchestration | 5 | request_human_review | pause | 0.200 | 0.233 | 0.233 | 0.400 | 3.200 | 11.573 |
| MR-098 | multi_agent_orchestration | 5 | request_human_review | reroute | 0.000 | 0.000 | 0.000 | 0.000 | 5.000 | 12.015 |
| MR-099 | multi_agent_orchestration | 5 | request_human_review | pause | 0.200 | 0.178 | 0.214 | 0.333 | 4.400 | 14.432 |
| MR-100 | multi_agent_orchestration | 5 | request_human_review | pause | 0.000 | 0.000 | 0.000 | 0.000 | 4.400 | 10.693 |

## Table 3. Incorrect decisions
| scenario_id | run_id | architecture_type | expected_action | recommended_action | semantic_hazard_f1 | latency_seconds | confidence_score |
| --- | --- | --- | --- | --- | --- | --- | --- |
| MR-002 | 1 | multi_agent_orchestration | reroute | pause | 0.000 | 13.725 | 0.850 |
| MR-004 | 1 | multi_agent_orchestration | request_human_review | pause | 0.000 | 11.520 | 0.850 |
| MR-008 | 1 | multi_agent_orchestration | request_human_review | pause | 0.545 | 8.272 | 0.820 |
| MR-033 | 1 | multi_agent_orchestration | reroute | proceed | 0.000 | 9.000 | 0.850 |
| MR-037 | 1 | multi_agent_orchestration | reroute | proceed | 0.000 | 9.317 | 0.850 |
| MR-040 | 1 | multi_agent_orchestration | reroute | proceed | 0.286 | 9.113 | 0.850 |
| MR-041 | 1 | multi_agent_orchestration | reroute | proceed | 0.000 | 8.805 | 0.850 |
| MR-045 | 1 | multi_agent_orchestration | reroute | proceed | 0.000 | 8.389 | 0.850 |
| MR-049 | 1 | multi_agent_orchestration | reroute | proceed | 0.000 | 7.891 | 0.850 |
| MR-052 | 1 | multi_agent_orchestration | reroute | proceed | 0.286 | 8.998 | 0.850 |
| MR-053 | 1 | multi_agent_orchestration | reroute | proceed | 0.250 | 9.654 | 0.850 |
| MR-078 | 1 | multi_agent_orchestration | request_human_review | reroute | 0.364 | 9.829 | 0.850 |
| MR-080 | 1 | multi_agent_orchestration | request_human_review | pause | 0.000 | 9.978 | 0.850 |
| MR-081 | 1 | multi_agent_orchestration | request_human_review | pause | 0.200 | 14.678 | 0.850 |
| MR-082 | 1 | multi_agent_orchestration | request_human_review | pause | 0.000 | 10.484 | 0.850 |
| MR-083 | 1 | multi_agent_orchestration | request_human_review | pause | 0.000 | 9.785 | 0.850 |
| MR-084 | 1 | multi_agent_orchestration | request_human_review | pause | 0.167 | 9.965 | 0.850 |
| MR-085 | 1 | multi_agent_orchestration | request_human_review | pause | 0.200 | 9.015 | 0.850 |
| MR-086 | 1 | multi_agent_orchestration | request_human_review | reroute | 0.000 | 8.947 | 0.850 |
| MR-088 | 1 | multi_agent_orchestration | request_human_review | pause | 0.000 | 9.203 | 0.850 |
| MR-089 | 1 | multi_agent_orchestration | request_human_review | pause | 0.154 | 10.463 | 0.850 |
| MR-090 | 1 | multi_agent_orchestration | request_human_review | pause | 0.364 | 10.542 | 0.850 |
| MR-092 | 1 | multi_agent_orchestration | request_human_review | pause | 0.000 | 8.802 | 0.850 |
| MR-094 | 1 | multi_agent_orchestration | request_human_review | pause | 0.182 | 11.317 | 0.850 |
| MR-095 | 1 | multi_agent_orchestration | request_human_review | pause | 0.000 | 12.740 | 0.880 |
| MR-096 | 1 | multi_agent_orchestration | request_human_review | pause | 0.364 | 8.780 | 0.850 |
| MR-097 | 1 | multi_agent_orchestration | request_human_review | pause | 0.200 | 13.343 | 0.850 |
| MR-098 | 1 | multi_agent_orchestration | request_human_review | reroute | 0.000 | 13.254 | 0.850 |
| MR-099 | 1 | multi_agent_orchestration | request_human_review | pause | 0.222 | 13.585 | 0.850 |
| MR-100 | 1 | multi_agent_orchestration | request_human_review | pause | 0.000 | 11.924 | 0.850 |
| MR-002 | 2 | multi_agent_orchestration | reroute | pause | 0.000 | 10.029 | 0.850 |
| MR-004 | 2 | multi_agent_orchestration | request_human_review | pause | 0.000 | 9.225 | 0.850 |
| MR-008 | 2 | multi_agent_orchestration | request_human_review | pause | 0.429 | 10.632 | 0.820 |
| MR-032 | 2 | multi_agent_orchestration | reroute | proceed | 0.250 | 9.968 | 0.850 |
| MR-033 | 2 | multi_agent_orchestration | reroute | proceed | 0.000 | 10.042 | 0.850 |
| MR-034 | 2 | multi_agent_orchestration | reroute | proceed | 0.286 | 9.210 | 0.850 |
| MR-037 | 2 | multi_agent_orchestration | reroute | proceed | 0.000 | 12.454 | 0.880 |
| MR-040 | 2 | multi_agent_orchestration | reroute | proceed | 0.286 | 12.128 | 0.850 |
| MR-041 | 2 | multi_agent_orchestration | reroute | proceed | 0.000 | 7.860 | 0.850 |
| MR-045 | 2 | multi_agent_orchestration | reroute | proceed | 0.000 | 9.568 | 0.850 |
| MR-049 | 2 | multi_agent_orchestration | reroute | proceed | 0.000 | 9.572 | 0.850 |
| MR-053 | 2 | multi_agent_orchestration | reroute | proceed | 0.000 | 7.989 | 0.850 |
| MR-078 | 2 | multi_agent_orchestration | request_human_review | pause | 0.364 | 7.263 | 0.850 |
| MR-079 | 2 | multi_agent_orchestration | request_human_review | pause | 0.400 | 12.800 | 0.850 |
| MR-080 | 2 | multi_agent_orchestration | request_human_review | pause | 0.000 | 10.443 | 0.850 |
| MR-081 | 2 | multi_agent_orchestration | request_human_review | pause | 0.333 | 16.502 | 0.850 |
| MR-082 | 2 | multi_agent_orchestration | request_human_review | pause | 0.000 | 18.788 | 0.850 |
| MR-083 | 2 | multi_agent_orchestration | request_human_review | pause | 0.000 | 9.359 | 0.850 |
| MR-084 | 2 | multi_agent_orchestration | request_human_review | pause | 0.182 | 8.396 | 0.850 |
| MR-086 | 2 | multi_agent_orchestration | request_human_review | reroute | 0.000 | 10.674 | 0.850 |
| MR-087 | 2 | multi_agent_orchestration | request_human_review | pause | 0.182 | 13.721 | 0.850 |
| MR-088 | 2 | multi_agent_orchestration | request_human_review | pause | 0.200 | 9.626 | 0.850 |
| MR-089 | 2 | multi_agent_orchestration | request_human_review | pause | 0.000 | 12.082 | 0.800 |
| MR-090 | 2 | multi_agent_orchestration | request_human_review | pause | 0.333 | 8.505 | 0.850 |
| MR-092 | 2 | multi_agent_orchestration | request_human_review | pause | 0.000 | 10.052 | 0.850 |
| MR-093 | 2 | multi_agent_orchestration | request_human_review | pause | 0.000 | 13.882 | 0.850 |
| MR-094 | 2 | multi_agent_orchestration | request_human_review | pause | 0.182 | 9.556 | 0.850 |
| MR-096 | 2 | multi_agent_orchestration | request_human_review | pause | 0.364 | 8.704 | 0.850 |
| MR-097 | 2 | multi_agent_orchestration | request_human_review | pause | 0.200 | 10.588 | 0.850 |
| MR-098 | 2 | multi_agent_orchestration | request_human_review | pause | 0.000 | 9.993 | 0.850 |
| MR-099 | 2 | multi_agent_orchestration | request_human_review | pause | 0.222 | 18.028 | 0.850 |
| MR-100 | 2 | multi_agent_orchestration | request_human_review | pause | 0.000 | 9.520 | 0.850 |
| MR-002 | 3 | multi_agent_orchestration | reroute | pause | 0.000 | 9.943 | 0.850 |
| MR-004 | 3 | multi_agent_orchestration | request_human_review | proceed | 0.000 | 8.602 | 0.850 |
| MR-008 | 3 | multi_agent_orchestration | request_human_review | pause | 0.308 | 9.718 | 0.850 |
| MR-032 | 3 | multi_agent_orchestration | reroute | proceed | 0.000 | 8.910 | 0.850 |
| MR-033 | 3 | multi_agent_orchestration | reroute | proceed | 0.000 | 8.278 | 0.850 |
| MR-037 | 3 | multi_agent_orchestration | reroute | proceed | 0.000 | 10.599 | 0.850 |
| MR-040 | 3 | multi_agent_orchestration | reroute | proceed | 0.286 | 10.443 | 0.850 |
| MR-041 | 3 | multi_agent_orchestration | reroute | proceed | 0.000 | 8.844 | 0.850 |
| MR-044 | 3 | multi_agent_orchestration | reroute | proceed | 0.000 | 8.709 | 0.850 |
| MR-049 | 3 | multi_agent_orchestration | reroute | proceed | 0.000 | 8.708 | 0.850 |
| MR-052 | 3 | multi_agent_orchestration | reroute | pause | 0.000 | 8.985 | 0.850 |
| MR-053 | 3 | multi_agent_orchestration | reroute | proceed | 0.000 | 9.126 | 0.850 |
| MR-078 | 3 | multi_agent_orchestration | request_human_review | pause | 0.364 | 9.818 | 0.850 |
| MR-079 | 3 | multi_agent_orchestration | request_human_review | pause | 0.400 | 12.600 | 0.850 |
| MR-080 | 3 | multi_agent_orchestration | request_human_review | pause | 0.000 | 10.755 | 0.850 |
| MR-082 | 3 | multi_agent_orchestration | request_human_review | pause | 0.000 | 9.175 | 0.850 |
| MR-083 | 3 | multi_agent_orchestration | request_human_review | pause | 0.000 | 12.299 | 0.850 |
| MR-084 | 3 | multi_agent_orchestration | request_human_review | pause | 0.182 | 7.376 | 0.850 |
| MR-085 | 3 | multi_agent_orchestration | request_human_review | pause | 0.000 | 9.630 | 0.850 |
| MR-086 | 3 | multi_agent_orchestration | request_human_review | pause | 0.000 | 9.105 | 0.850 |
| MR-087 | 3 | multi_agent_orchestration | request_human_review | pause | 0.167 | 15.203 | 0.850 |
| MR-088 | 3 | multi_agent_orchestration | request_human_review | pause | 0.000 | 10.802 | 0.850 |
| MR-090 | 3 | multi_agent_orchestration | request_human_review | pause | 0.364 | 10.118 | 0.850 |
| MR-091 | 3 | multi_agent_orchestration | request_human_review | pause | 0.364 | 11.811 | 0.850 |
| MR-092 | 3 | multi_agent_orchestration | request_human_review | pause | 0.000 | 11.346 | 0.850 |
| MR-093 | 3 | multi_agent_orchestration | request_human_review | pause | 0.333 | 14.439 | 0.850 |
| MR-094 | 3 | multi_agent_orchestration | request_human_review | pause | 0.000 | 9.041 | 0.850 |
| MR-095 | 3 | multi_agent_orchestration | request_human_review | pause | 0.200 | 9.769 | 0.880 |
| MR-096 | 3 | multi_agent_orchestration | request_human_review | reroute | 0.167 | 11.292 | 0.850 |
| MR-097 | 3 | multi_agent_orchestration | request_human_review | pause | 0.200 | 14.532 | 0.850 |
| MR-098 | 3 | multi_agent_orchestration | request_human_review | reroute | 0.000 | 10.767 | 0.850 |
| MR-099 | 3 | multi_agent_orchestration | request_human_review | pause | 0.222 | 14.026 | 0.850 |
| MR-100 | 3 | multi_agent_orchestration | request_human_review | pause | 0.000 | 12.490 | 0.850 |
| MR-002 | 4 | multi_agent_orchestration | reroute | pause | 0.000 | 14.067 | 0.850 |
| MR-004 | 4 | multi_agent_orchestration | request_human_review | reroute | 0.000 | 9.753 | 0.850 |
| MR-008 | 4 | multi_agent_orchestration | request_human_review | pause | 0.333 | 8.372 | 0.850 |
| MR-032 | 4 | multi_agent_orchestration | reroute | pause | 0.250 | 9.132 | 0.850 |
| MR-033 | 4 | multi_agent_orchestration | reroute | proceed | 0.000 | 7.970 | 0.850 |
| MR-034 | 4 | multi_agent_orchestration | reroute | proceed | 0.286 | 11.838 | 0.850 |
| MR-037 | 4 | multi_agent_orchestration | reroute | proceed | 0.000 | 9.587 | 0.880 |
| MR-040 | 4 | multi_agent_orchestration | reroute | proceed | 0.286 | 8.967 | 0.850 |
| MR-041 | 4 | multi_agent_orchestration | reroute | proceed | 0.250 | 9.731 | 0.850 |
| MR-045 | 4 | multi_agent_orchestration | reroute | proceed | 0.000 | 8.692 | 0.850 |
| MR-049 | 4 | multi_agent_orchestration | reroute | proceed | 0.000 | 12.804 | 0.850 |
| MR-051 | 4 | multi_agent_orchestration | reroute | proceed | 0.000 | 8.397 | 0.850 |
| MR-053 | 4 | multi_agent_orchestration | reroute | proceed | 0.000 | 9.498 | 0.850 |
| MR-078 | 4 | multi_agent_orchestration | request_human_review | pause | 0.364 | 10.041 | 0.850 |
| MR-080 | 4 | multi_agent_orchestration | request_human_review | pause | 0.000 | 9.078 | 0.850 |
| MR-081 | 4 | multi_agent_orchestration | request_human_review | pause | 0.200 | 14.373 | 0.850 |
| MR-082 | 4 | multi_agent_orchestration | request_human_review | pause | 0.000 | 11.365 | 0.850 |
| MR-083 | 4 | multi_agent_orchestration | request_human_review | pause | 0.000 | 8.178 | 0.850 |
| MR-084 | 4 | multi_agent_orchestration | request_human_review | pause | 0.364 | 6.954 | 0.850 |
| MR-085 | 4 | multi_agent_orchestration | request_human_review | pause | 0.182 | 13.125 | 0.850 |
| MR-086 | 4 | multi_agent_orchestration | request_human_review | reroute | 0.000 | 8.183 | 0.850 |
| MR-087 | 4 | multi_agent_orchestration | request_human_review | pause | 0.222 | 12.813 | 0.850 |
| MR-088 | 4 | multi_agent_orchestration | request_human_review | pause | 0.000 | 8.737 | 0.850 |
| MR-090 | 4 | multi_agent_orchestration | request_human_review | pause | 0.364 | 9.462 | 0.850 |
| MR-091 | 4 | multi_agent_orchestration | request_human_review | pause | 0.364 | 16.552 | 0.850 |
| MR-092 | 4 | multi_agent_orchestration | request_human_review | pause | 0.000 | 9.489 | 0.850 |
| MR-093 | 4 | multi_agent_orchestration | request_human_review | pause | 0.333 | 13.139 | 0.850 |
| MR-094 | 4 | multi_agent_orchestration | request_human_review | pause | 0.000 | 9.843 | 0.850 |
| MR-096 | 4 | multi_agent_orchestration | request_human_review | pause | 0.333 | 8.346 | 0.850 |
| MR-097 | 4 | multi_agent_orchestration | request_human_review | pause | 0.200 | 10.191 | 0.850 |
| MR-098 | 4 | multi_agent_orchestration | request_human_review | pause | 0.000 | 14.535 | 0.850 |
| MR-100 | 4 | multi_agent_orchestration | request_human_review | reroute | 0.000 | 9.053 | 0.850 |
| MR-002 | 5 | multi_agent_orchestration | reroute | pause | 0.000 | 11.269 | 0.850 |
| MR-004 | 5 | multi_agent_orchestration | request_human_review | pause | 0.000 | 12.467 | 0.850 |
| MR-008 | 5 | multi_agent_orchestration | request_human_review | pause | 0.308 | 7.181 | 0.850 |
| MR-032 | 5 | multi_agent_orchestration | reroute | proceed | 0.250 | 6.758 | 0.850 |
| MR-033 | 5 | multi_agent_orchestration | reroute | proceed | 0.000 | 7.890 | 0.850 |
| MR-037 | 5 | multi_agent_orchestration | reroute | proceed | 0.000 | 8.835 | 0.850 |
| MR-040 | 5 | multi_agent_orchestration | reroute | proceed | 0.000 | 9.520 | 0.850 |
| MR-041 | 5 | multi_agent_orchestration | reroute | proceed | 0.000 | 6.771 | 0.850 |
| MR-044 | 5 | multi_agent_orchestration | reroute | pause | 0.222 | 9.727 | 0.850 |
| MR-045 | 5 | multi_agent_orchestration | reroute | proceed | 0.000 | 8.190 | 0.850 |
| MR-049 | 5 | multi_agent_orchestration | reroute | proceed | 0.000 | 8.467 | 0.850 |
| MR-052 | 5 | multi_agent_orchestration | reroute | proceed | 0.286 | 9.493 | 0.850 |
| MR-053 | 5 | multi_agent_orchestration | reroute | proceed | 0.250 | 11.882 | 0.850 |
| MR-078 | 5 | multi_agent_orchestration | request_human_review | pause | 0.364 | 10.047 | 0.850 |
| MR-080 | 5 | multi_agent_orchestration | request_human_review | pause | 0.000 | 7.739 | 0.850 |
| MR-081 | 5 | multi_agent_orchestration | request_human_review | pause | 0.000 | 14.480 | 0.850 |
| MR-082 | 5 | multi_agent_orchestration | request_human_review | pause | 0.000 | 7.812 | 0.850 |
| MR-083 | 5 | multi_agent_orchestration | request_human_review | reroute | 0.222 | 8.153 | 0.850 |
| MR-084 | 5 | multi_agent_orchestration | request_human_review | pause | 0.364 | 8.715 | 0.850 |
| MR-086 | 5 | multi_agent_orchestration | request_human_review | pause | 0.000 | 7.984 | 0.850 |
| MR-087 | 5 | multi_agent_orchestration | request_human_review | pause | 0.182 | 13.319 | 0.850 |
| MR-088 | 5 | multi_agent_orchestration | request_human_review | pause | 0.000 | 12.184 | 0.850 |
| MR-089 | 5 | multi_agent_orchestration | request_human_review | pause | 0.000 | 11.775 | 0.800 |
| MR-090 | 5 | multi_agent_orchestration | request_human_review | pause | 0.364 | 9.131 | 0.850 |
| MR-091 | 5 | multi_agent_orchestration | request_human_review | pause | 0.200 | 9.190 | 0.850 |
| MR-092 | 5 | multi_agent_orchestration | request_human_review | pause | 0.000 | 9.014 | 0.850 |
| MR-094 | 5 | multi_agent_orchestration | request_human_review | pause | 0.000 | 11.481 | 0.850 |
| MR-096 | 5 | multi_agent_orchestration | request_human_review | pause | 0.364 | 7.809 | 0.850 |
| MR-098 | 5 | multi_agent_orchestration | request_human_review | reroute | 0.000 | 11.524 | 0.850 |
| MR-099 | 5 | multi_agent_orchestration | request_human_review | pause | 0.222 | 13.356 | 0.850 |
| MR-100 | 5 | multi_agent_orchestration | request_human_review | pause | 0.000 | 10.479 | 0.850 |

## Table 4. Pairwise statistical comparisons
No rows available.

These tables are generated automatically from `outputs/results.json` and are intended for direct reuse in drafts, appendices, or supplementary materials.