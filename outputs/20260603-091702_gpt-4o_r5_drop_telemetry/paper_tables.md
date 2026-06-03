# Paper-Ready Tables

## Table 1. Aggregate architecture comparison
| architecture_type | runs | scenarios | evaluations | decision_accuracy | mean_exact_hazard_f1 | mean_semantic_hazard_f1 | mean_hazard_false_positive_count | mean_canonical_hazard_coverage | mean_spurious_hazard_count | mean_latency_seconds | mean_token_usage |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| multi_agent_orchestration | 5 | 100 | 500 | 0.744 | 0.042 | 0.109 | 5.668 | 0.222 | 3.414 | 10.178 | 1849.474 |

## Table 2. Scenario-level performance by architecture
| scenario_id | architecture_type | runs | expected_action | modal_recommended_action | decision_accuracy | mean_exact_hazard_f1 | mean_semantic_hazard_f1 | mean_canonical_hazard_coverage | mean_spurious_hazard_count | mean_latency_seconds |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR-001 | multi_agent_orchestration | 5 | proceed | proceed | 1.000 | 0.000 | 0.000 | 0.000 | 2.600 | 8.688 |
| MR-002 | multi_agent_orchestration | 5 | reroute | pause | 0.000 | 0.089 | 0.178 | 0.266 | 3.000 | 12.289 |
| MR-003 | multi_agent_orchestration | 5 | pause | pause | 1.000 | 0.000 | 0.467 | 1.000 | 1.400 | 9.392 |
| MR-004 | multi_agent_orchestration | 5 | request_human_review | pause | 0.400 | 0.000 | 0.036 | 0.067 | 2.200 | 10.140 |
| MR-005 | multi_agent_orchestration | 5 | reroute | reroute | 0.600 | 0.283 | 0.283 | 0.500 | 3.200 | 9.335 |
| MR-006 | multi_agent_orchestration | 5 | pause | pause | 1.000 | 0.000 | 0.000 | 0.000 | 2.800 | 13.142 |
| MR-007 | multi_agent_orchestration | 5 | proceed | proceed | 1.000 | 0.000 | 0.000 | 0.000 | 3.400 | 8.249 |
| MR-008 | multi_agent_orchestration | 5 | request_human_review | pause | 0.000 | 0.341 | 0.512 | 0.600 | 1.000 | 9.712 |
| MR-009 | multi_agent_orchestration | 5 | proceed | proceed | 1.000 | 0.000 | 0.000 | 0.000 | 2.400 | 8.366 |
| MR-010 | multi_agent_orchestration | 5 | proceed | proceed | 1.000 | 0.000 | 0.000 | 0.000 | 2.600 | 8.115 |
| MR-011 | multi_agent_orchestration | 5 | proceed | proceed | 1.000 | 0.000 | 0.000 | 0.000 | 2.800 | 9.774 |
| MR-012 | multi_agent_orchestration | 5 | proceed | proceed | 1.000 | 0.000 | 0.000 | 0.000 | 3.400 | 10.266 |
| MR-013 | multi_agent_orchestration | 5 | proceed | proceed | 1.000 | 0.000 | 0.000 | 0.000 | 3.000 | 9.814 |
| MR-014 | multi_agent_orchestration | 5 | proceed | proceed | 1.000 | 0.000 | 0.000 | 0.000 | 2.200 | 7.572 |
| MR-015 | multi_agent_orchestration | 5 | proceed | proceed | 1.000 | 0.000 | 0.000 | 0.000 | 2.200 | 8.672 |
| MR-016 | multi_agent_orchestration | 5 | proceed | proceed | 1.000 | 0.000 | 0.000 | 0.000 | 2.000 | 7.416 |
| MR-017 | multi_agent_orchestration | 5 | proceed | proceed | 1.000 | 0.000 | 0.000 | 0.000 | 3.000 | 9.814 |
| MR-018 | multi_agent_orchestration | 5 | proceed | proceed | 1.000 | 0.000 | 0.000 | 0.000 | 2.800 | 10.543 |
| MR-019 | multi_agent_orchestration | 5 | proceed | proceed | 1.000 | 0.000 | 0.000 | 0.000 | 3.600 | 9.284 |
| MR-020 | multi_agent_orchestration | 5 | proceed | proceed | 1.000 | 0.000 | 0.000 | 0.000 | 2.000 | 7.888 |
| MR-021 | multi_agent_orchestration | 5 | proceed | proceed | 1.000 | 0.000 | 0.000 | 0.000 | 2.400 | 8.114 |
| MR-022 | multi_agent_orchestration | 5 | proceed | proceed | 1.000 | 0.000 | 0.000 | 0.000 | 2.800 | 8.377 |
| MR-023 | multi_agent_orchestration | 5 | proceed | proceed | 1.000 | 0.000 | 0.000 | 0.000 | 3.000 | 7.549 |
| MR-024 | multi_agent_orchestration | 5 | proceed | proceed | 1.000 | 0.000 | 0.000 | 0.000 | 2.200 | 7.789 |
| MR-025 | multi_agent_orchestration | 5 | proceed | proceed | 1.000 | 0.000 | 0.000 | 0.000 | 3.000 | 12.621 |
| MR-026 | multi_agent_orchestration | 5 | proceed | proceed | 1.000 | 0.000 | 0.000 | 0.000 | 2.600 | 8.363 |
| MR-027 | multi_agent_orchestration | 5 | proceed | proceed | 1.000 | 0.000 | 0.000 | 0.000 | 2.400 | 8.600 |
| MR-028 | multi_agent_orchestration | 5 | proceed | proceed | 1.000 | 0.000 | 0.000 | 0.000 | 3.400 | 7.885 |
| MR-029 | multi_agent_orchestration | 5 | proceed | proceed | 1.000 | 0.000 | 0.000 | 0.000 | 2.400 | 9.021 |
| MR-030 | multi_agent_orchestration | 5 | proceed | proceed | 1.000 | 0.000 | 0.000 | 0.000 | 2.000 | 9.072 |
| MR-031 | multi_agent_orchestration | 5 | proceed | proceed | 1.000 | 0.000 | 0.000 | 0.000 | 4.000 | 9.705 |
| MR-032 | multi_agent_orchestration | 5 | reroute | proceed | 0.200 | 0.036 | 0.036 | 0.100 | 7.200 | 12.016 |
| MR-033 | multi_agent_orchestration | 5 | reroute | proceed | 0.000 | 0.000 | 0.000 | 0.000 | 4.600 | 9.855 |
| MR-034 | multi_agent_orchestration | 5 | reroute | reroute | 0.600 | 0.144 | 0.233 | 0.500 | 2.000 | 8.909 |
| MR-035 | multi_agent_orchestration | 5 | reroute | reroute | 1.000 | 0.000 | 0.272 | 0.500 | 3.400 | 9.281 |
| MR-036 | multi_agent_orchestration | 5 | reroute | reroute | 1.000 | 0.000 | 0.000 | 0.000 | 4.200 | 10.506 |
| MR-037 | multi_agent_orchestration | 5 | reroute | proceed | 0.000 | 0.000 | 0.000 | 0.000 | 6.000 | 9.140 |
| MR-038 | multi_agent_orchestration | 5 | reroute | reroute | 1.000 | 0.228 | 0.228 | 0.500 | 0.800 | 10.991 |
| MR-039 | multi_agent_orchestration | 5 | reroute | reroute | 1.000 | 0.000 | 0.000 | 0.000 | 3.200 | 9.812 |
| MR-040 | multi_agent_orchestration | 5 | reroute | proceed | 0.400 | 0.000 | 0.240 | 0.500 | 4.400 | 8.752 |
| MR-041 | multi_agent_orchestration | 5 | reroute | proceed | 0.000 | 0.000 | 0.179 | 0.400 | 3.400 | 9.968 |
| MR-042 | multi_agent_orchestration | 5 | reroute | reroute | 1.000 | 0.000 | 0.000 | 0.000 | 2.200 | 8.157 |
| MR-043 | multi_agent_orchestration | 5 | reroute | reroute | 1.000 | 0.000 | 0.000 | 0.000 | 5.200 | 8.867 |
| MR-044 | multi_agent_orchestration | 5 | reroute | reroute | 0.600 | 0.196 | 0.196 | 0.500 | 5.000 | 9.344 |
| MR-045 | multi_agent_orchestration | 5 | reroute | proceed | 0.000 | 0.000 | 0.000 | 0.000 | 4.400 | 10.085 |
| MR-046 | multi_agent_orchestration | 5 | reroute | reroute | 0.600 | 0.044 | 0.218 | 0.500 | 2.800 | 9.325 |
| MR-047 | multi_agent_orchestration | 5 | reroute | reroute | 1.000 | 0.000 | 0.413 | 0.800 | 2.400 | 9.260 |
| MR-048 | multi_agent_orchestration | 5 | reroute | reroute | 1.000 | 0.000 | 0.000 | 0.000 | 2.800 | 8.628 |
| MR-049 | multi_agent_orchestration | 5 | reroute | proceed | 0.000 | 0.000 | 0.000 | 0.000 | 6.600 | 8.611 |
| MR-050 | multi_agent_orchestration | 5 | reroute | reroute | 1.000 | 0.435 | 0.435 | 1.000 | 0.600 | 9.238 |
| MR-051 | multi_agent_orchestration | 5 | reroute | reroute | 1.000 | 0.000 | 0.000 | 0.000 | 3.800 | 9.595 |
| MR-052 | multi_agent_orchestration | 5 | reroute | pause | 0.400 | 0.000 | 0.123 | 0.300 | 4.600 | 9.680 |
| MR-053 | multi_agent_orchestration | 5 | reroute | proceed | 0.000 | 0.000 | 0.178 | 0.400 | 3.000 | 8.546 |
| MR-054 | multi_agent_orchestration | 5 | reroute | reroute | 1.000 | 0.000 | 0.113 | 0.200 | 3.000 | 8.356 |
| MR-055 | multi_agent_orchestration | 5 | pause | pause | 1.000 | 0.000 | 0.480 | 1.000 | 1.800 | 8.046 |
| MR-056 | multi_agent_orchestration | 5 | pause | pause | 1.000 | 0.000 | 0.031 | 0.100 | 6.200 | 9.605 |
| MR-057 | multi_agent_orchestration | 5 | pause | pause | 1.000 | 0.000 | 0.000 | 0.000 | 4.200 | 8.674 |
| MR-058 | multi_agent_orchestration | 5 | pause | pause | 1.000 | 0.000 | 0.000 | 0.000 | 2.400 | 9.853 |
| MR-059 | multi_agent_orchestration | 5 | pause | pause | 1.000 | 0.000 | 0.000 | 0.000 | 2.200 | 10.248 |
| MR-060 | multi_agent_orchestration | 5 | pause | pause | 1.000 | 0.113 | 0.187 | 0.500 | 4.800 | 9.258 |
| MR-061 | multi_agent_orchestration | 5 | pause | pause | 1.000 | 0.000 | 0.266 | 0.800 | 3.000 | 8.678 |
| MR-062 | multi_agent_orchestration | 5 | pause | pause | 1.000 | 0.133 | 0.413 | 0.700 | 2.200 | 10.949 |
| MR-063 | multi_agent_orchestration | 5 | pause | pause | 1.000 | 0.000 | 0.000 | 0.000 | 2.800 | 8.570 |
| MR-064 | multi_agent_orchestration | 5 | pause | pause | 1.000 | 0.000 | 0.000 | 0.000 | 6.000 | 27.464 |
| MR-065 | multi_agent_orchestration | 5 | pause | pause | 1.000 | 0.000 | 0.000 | 0.000 | 4.600 | 9.628 |
| MR-066 | multi_agent_orchestration | 5 | pause | pause | 1.000 | 0.044 | 0.102 | 0.200 | 2.000 | 8.933 |
| MR-067 | multi_agent_orchestration | 5 | pause | pause | 1.000 | 0.000 | 0.440 | 1.000 | 2.400 | 10.499 |
| MR-068 | multi_agent_orchestration | 5 | pause | pause | 1.000 | 0.000 | 0.000 | 0.000 | 5.200 | 8.421 |
| MR-069 | multi_agent_orchestration | 5 | pause | pause | 1.000 | 0.000 | 0.000 | 0.000 | 3.200 | 9.462 |
| MR-070 | multi_agent_orchestration | 5 | pause | pause | 1.000 | 0.000 | 0.000 | 0.000 | 1.400 | 11.633 |
| MR-071 | multi_agent_orchestration | 5 | pause | pause | 1.000 | 0.000 | 0.000 | 0.000 | 2.800 | 9.354 |
| MR-072 | multi_agent_orchestration | 5 | pause | pause | 1.000 | 0.040 | 0.040 | 0.100 | 5.400 | 11.185 |
| MR-073 | multi_agent_orchestration | 5 | pause | pause | 1.000 | 0.000 | 0.316 | 1.000 | 2.800 | 9.620 |
| MR-074 | multi_agent_orchestration | 5 | pause | pause | 1.000 | 0.107 | 0.207 | 0.400 | 2.600 | 10.297 |
| MR-075 | multi_agent_orchestration | 5 | pause | pause | 1.000 | 0.000 | 0.000 | 0.000 | 2.200 | 11.658 |
| MR-076 | multi_agent_orchestration | 5 | pause | pause | 1.000 | 0.000 | 0.000 | 0.000 | 5.600 | 9.948 |
| MR-077 | multi_agent_orchestration | 5 | pause | pause | 1.000 | 0.000 | 0.000 | 0.000 | 4.200 | 9.356 |
| MR-078 | multi_agent_orchestration | 5 | request_human_review | pause | 0.000 | 0.162 | 0.323 | 0.667 | 2.000 | 11.143 |
| MR-079 | multi_agent_orchestration | 5 | request_human_review | request_human_review | 1.000 | 0.254 | 0.254 | 0.467 | 4.400 | 11.170 |
| MR-080 | multi_agent_orchestration | 5 | request_human_review | pause | 0.000 | 0.000 | 0.000 | 0.000 | 5.200 | 10.042 |
| MR-081 | multi_agent_orchestration | 5 | request_human_review | request_human_review | 0.600 | 0.149 | 0.338 | 0.600 | 3.800 | 15.297 |
| MR-082 | multi_agent_orchestration | 5 | request_human_review | pause | 0.200 | 0.000 | 0.000 | 0.000 | 2.200 | 10.788 |
| MR-083 | multi_agent_orchestration | 5 | request_human_review | request_human_review | 0.600 | 0.000 | 0.187 | 0.333 | 4.600 | 10.777 |
| MR-084 | multi_agent_orchestration | 5 | request_human_review | pause | 0.000 | 0.036 | 0.249 | 0.467 | 3.000 | 10.558 |
| MR-085 | multi_agent_orchestration | 5 | request_human_review | request_human_review | 1.000 | 0.153 | 0.153 | 0.266 | 3.200 | 11.680 |
| MR-086 | multi_agent_orchestration | 5 | request_human_review | reroute | 0.200 | 0.000 | 0.000 | 0.000 | 6.200 | 10.558 |
| MR-087 | multi_agent_orchestration | 5 | request_human_review | request_human_review | 1.000 | 0.170 | 0.339 | 0.667 | 5.800 | 15.969 |
| MR-088 | multi_agent_orchestration | 5 | request_human_review | pause | 0.000 | 0.000 | 0.033 | 0.067 | 4.800 | 10.931 |
| MR-089 | multi_agent_orchestration | 5 | request_human_review | request_human_review | 0.800 | 0.000 | 0.180 | 0.333 | 3.800 | 11.696 |
| MR-090 | multi_agent_orchestration | 5 | request_human_review | pause | 0.000 | 0.167 | 0.333 | 0.667 | 1.800 | 11.403 |
| MR-091 | multi_agent_orchestration | 5 | request_human_review | request_human_review | 1.000 | 0.246 | 0.246 | 0.533 | 6.400 | 11.106 |
| MR-092 | multi_agent_orchestration | 5 | request_human_review | pause | 0.000 | 0.000 | 0.000 | 0.000 | 5.000 | 11.710 |
| MR-093 | multi_agent_orchestration | 5 | request_human_review | request_human_review | 1.000 | 0.113 | 0.365 | 0.667 | 4.000 | 14.913 |
| MR-094 | multi_agent_orchestration | 5 | request_human_review | pause | 0.200 | 0.000 | 0.029 | 0.067 | 2.600 | 11.445 |
| MR-095 | multi_agent_orchestration | 5 | request_human_review | pause | 0.200 | 0.000 | 0.186 | 0.333 | 4.800 | 14.566 |
| MR-096 | multi_agent_orchestration | 5 | request_human_review | pause | 0.000 | 0.162 | 0.324 | 0.667 | 1.800 | 10.417 |
| MR-097 | multi_agent_orchestration | 5 | request_human_review | request_human_review | 1.000 | 0.193 | 0.193 | 0.333 | 2.800 | 12.320 |
| MR-098 | multi_agent_orchestration | 5 | request_human_review | reroute | 0.200 | 0.000 | 0.000 | 0.000 | 6.000 | 11.541 |
| MR-099 | multi_agent_orchestration | 5 | request_human_review | request_human_review | 0.600 | 0.191 | 0.381 | 0.667 | 4.600 | 13.671 |
| MR-100 | multi_agent_orchestration | 5 | request_human_review | pause | 0.000 | 0.000 | 0.000 | 0.000 | 5.200 | 10.224 |

## Table 3. Incorrect decisions
| scenario_id | run_id | architecture_type | expected_action | recommended_action | semantic_hazard_f1 | latency_seconds | confidence_score |
| --- | --- | --- | --- | --- | --- | --- | --- |
| MR-002 | 1 | multi_agent_orchestration | reroute | pause | 0.222 | 13.513 | 0.850 |
| MR-004 | 1 | multi_agent_orchestration | request_human_review | pause | 0.000 | 9.904 | 0.850 |
| MR-008 | 1 | multi_agent_orchestration | request_human_review | pause | 0.500 | 8.543 | 0.850 |
| MR-032 | 1 | multi_agent_orchestration | reroute | proceed | 0.000 | 10.239 | 0.850 |
| MR-033 | 1 | multi_agent_orchestration | reroute | proceed | 0.000 | 7.447 | 0.850 |
| MR-037 | 1 | multi_agent_orchestration | reroute | proceed | 0.000 | 8.630 | 0.850 |
| MR-040 | 1 | multi_agent_orchestration | reroute | proceed | 0.250 | 7.595 | 0.850 |
| MR-041 | 1 | multi_agent_orchestration | reroute | proceed | 0.250 | 8.093 | 0.850 |
| MR-045 | 1 | multi_agent_orchestration | reroute | proceed | 0.000 | 8.163 | 0.850 |
| MR-049 | 1 | multi_agent_orchestration | reroute | proceed | 0.000 | 7.555 | 0.850 |
| MR-053 | 1 | multi_agent_orchestration | reroute | proceed | 0.222 | 7.568 | 0.850 |
| MR-078 | 1 | multi_agent_orchestration | request_human_review | pause | 0.333 | 9.120 | 0.850 |
| MR-080 | 1 | multi_agent_orchestration | request_human_review | pause | 0.000 | 7.459 | 0.850 |
| MR-082 | 1 | multi_agent_orchestration | request_human_review | reroute | 0.000 | 9.918 | 0.850 |
| MR-084 | 1 | multi_agent_orchestration | request_human_review | pause | 0.364 | 9.734 | 0.850 |
| MR-086 | 1 | multi_agent_orchestration | request_human_review | reroute | 0.000 | 9.061 | 0.850 |
| MR-088 | 1 | multi_agent_orchestration | request_human_review | pause | 0.000 | 10.034 | 0.850 |
| MR-089 | 1 | multi_agent_orchestration | request_human_review | pause | 0.167 | 9.525 | 0.800 |
| MR-090 | 1 | multi_agent_orchestration | request_human_review | reroute | 0.333 | 10.367 | 0.850 |
| MR-092 | 1 | multi_agent_orchestration | request_human_review | pause | 0.000 | 10.023 | 0.850 |
| MR-094 | 1 | multi_agent_orchestration | request_human_review | pause | 0.000 | 9.242 | 0.850 |
| MR-095 | 1 | multi_agent_orchestration | request_human_review | pause | 0.222 | 12.085 | 0.850 |
| MR-096 | 1 | multi_agent_orchestration | request_human_review | pause | 0.333 | 9.700 | 0.850 |
| MR-098 | 1 | multi_agent_orchestration | request_human_review | pause | 0.000 | 9.118 | 0.850 |
| MR-100 | 1 | multi_agent_orchestration | request_human_review | pause | 0.000 | 8.372 | 0.850 |
| MR-002 | 2 | multi_agent_orchestration | reroute | pause | 0.222 | 11.005 | 0.850 |
| MR-004 | 2 | multi_agent_orchestration | request_human_review | reroute | 0.000 | 10.128 | 0.850 |
| MR-008 | 2 | multi_agent_orchestration | request_human_review | pause | 0.500 | 9.220 | 0.850 |
| MR-032 | 2 | multi_agent_orchestration | reroute | proceed | 0.182 | 14.432 | 0.850 |
| MR-033 | 2 | multi_agent_orchestration | reroute | proceed | 0.000 | 9.760 | 0.850 |
| MR-034 | 2 | multi_agent_orchestration | reroute | proceed | 0.250 | 9.593 | 0.850 |
| MR-037 | 2 | multi_agent_orchestration | reroute | proceed | 0.000 | 9.711 | 0.850 |
| MR-041 | 2 | multi_agent_orchestration | reroute | proceed | 0.200 | 8.814 | 0.850 |
| MR-044 | 2 | multi_agent_orchestration | reroute | pause | 0.182 | 10.458 | 0.850 |
| MR-045 | 2 | multi_agent_orchestration | reroute | proceed | 0.000 | 13.512 | 0.850 |
| MR-046 | 2 | multi_agent_orchestration | reroute | proceed | 0.222 | 9.821 | 0.850 |
| MR-049 | 2 | multi_agent_orchestration | reroute | proceed | 0.000 | 7.444 | 0.850 |
| MR-053 | 2 | multi_agent_orchestration | reroute | proceed | 0.222 | 9.216 | 0.850 |
| MR-078 | 2 | multi_agent_orchestration | request_human_review | pause | 0.308 | 15.296 | 0.850 |
| MR-080 | 2 | multi_agent_orchestration | request_human_review | pause | 0.000 | 9.462 | 0.850 |
| MR-081 | 2 | multi_agent_orchestration | request_human_review | pause | 0.200 | 17.678 | 0.850 |
| MR-082 | 2 | multi_agent_orchestration | request_human_review | pause | 0.000 | 11.460 | 0.850 |
| MR-084 | 2 | multi_agent_orchestration | request_human_review | pause | 0.167 | 9.987 | 0.850 |
| MR-086 | 2 | multi_agent_orchestration | request_human_review | reroute | 0.000 | 10.881 | 0.850 |
| MR-088 | 2 | multi_agent_orchestration | request_human_review | pause | 0.000 | 9.727 | 0.850 |
| MR-090 | 2 | multi_agent_orchestration | request_human_review | pause | 0.333 | 11.874 | 0.850 |
| MR-092 | 2 | multi_agent_orchestration | request_human_review | reroute | 0.000 | 11.874 | 0.850 |
| MR-094 | 2 | multi_agent_orchestration | request_human_review | pause | 0.000 | 12.799 | 0.850 |
| MR-096 | 2 | multi_agent_orchestration | request_human_review | pause | 0.308 | 10.339 | 0.850 |
| MR-098 | 2 | multi_agent_orchestration | request_human_review | reroute | 0.000 | 10.254 | 0.850 |
| MR-100 | 2 | multi_agent_orchestration | request_human_review | pause | 0.000 | 9.388 | 0.850 |
| MR-002 | 3 | multi_agent_orchestration | reroute | pause | 0.000 | 13.618 | 0.850 |
| MR-008 | 3 | multi_agent_orchestration | request_human_review | pause | 0.462 | 10.038 | 0.850 |
| MR-032 | 3 | multi_agent_orchestration | reroute | proceed | 0.000 | 9.319 | 0.850 |
| MR-033 | 3 | multi_agent_orchestration | reroute | proceed | 0.000 | 7.964 | 0.850 |
| MR-034 | 3 | multi_agent_orchestration | reroute | proceed | 0.250 | 8.213 | 0.850 |
| MR-037 | 3 | multi_agent_orchestration | reroute | proceed | 0.000 | 7.188 | 0.850 |
| MR-041 | 3 | multi_agent_orchestration | reroute | proceed | 0.000 | 14.953 | 0.850 |
| MR-044 | 3 | multi_agent_orchestration | reroute | pause | 0.200 | 9.374 | 0.850 |
| MR-045 | 3 | multi_agent_orchestration | reroute | proceed | 0.000 | 9.387 | 0.850 |
| MR-046 | 3 | multi_agent_orchestration | reroute | proceed | 0.222 | 9.205 | 0.850 |
| MR-049 | 3 | multi_agent_orchestration | reroute | proceed | 0.000 | 8.702 | 0.850 |
| MR-052 | 3 | multi_agent_orchestration | reroute | pause | 0.000 | 10.448 | 0.850 |
| MR-053 | 3 | multi_agent_orchestration | reroute | proceed | 0.222 | 9.114 | 0.850 |
| MR-078 | 3 | multi_agent_orchestration | request_human_review | pause | 0.308 | 10.157 | 0.850 |
| MR-080 | 3 | multi_agent_orchestration | request_human_review | pause | 0.000 | 11.469 | 0.850 |
| MR-082 | 3 | multi_agent_orchestration | request_human_review | reroute | 0.000 | 10.955 | 0.850 |
| MR-083 | 3 | multi_agent_orchestration | request_human_review | pause | 0.200 | 13.210 | 0.850 |
| MR-084 | 3 | multi_agent_orchestration | request_human_review | pause | 0.364 | 11.018 | 0.850 |
| MR-088 | 3 | multi_agent_orchestration | request_human_review | pause | 0.000 | 15.150 | 0.850 |
| MR-090 | 3 | multi_agent_orchestration | request_human_review | reroute | 0.333 | 9.689 | 0.850 |
| MR-092 | 3 | multi_agent_orchestration | request_human_review | pause | 0.000 | 13.398 | 0.850 |
| MR-095 | 3 | multi_agent_orchestration | request_human_review | reroute | 0.154 | 11.484 | 0.850 |
| MR-096 | 3 | multi_agent_orchestration | request_human_review | pause | 0.308 | 10.342 | 0.850 |
| MR-098 | 3 | multi_agent_orchestration | request_human_review | reroute | 0.000 | 10.255 | 0.850 |
| MR-099 | 3 | multi_agent_orchestration | request_human_review | pause | 0.400 | 12.989 | 0.850 |
| MR-100 | 3 | multi_agent_orchestration | request_human_review | pause | 0.000 | 11.672 | 0.850 |
| MR-002 | 4 | multi_agent_orchestration | reroute | pause | 0.222 | 10.926 | 0.870 |
| MR-004 | 4 | multi_agent_orchestration | request_human_review | pause | 0.000 | 8.546 | 0.850 |
| MR-005 | 4 | multi_agent_orchestration | reroute | proceed | 0.286 | 9.527 | 0.850 |
| MR-008 | 4 | multi_agent_orchestration | request_human_review | pause | 0.600 | 10.559 | 0.850 |
| MR-032 | 4 | multi_agent_orchestration | reroute | proceed | 0.000 | 12.185 | 0.850 |
| MR-033 | 4 | multi_agent_orchestration | reroute | proceed | 0.000 | 12.288 | 0.850 |
| MR-037 | 4 | multi_agent_orchestration | reroute | proceed | 0.000 | 10.439 | 0.850 |
| MR-040 | 4 | multi_agent_orchestration | reroute | proceed | 0.250 | 8.426 | 0.850 |
| MR-041 | 4 | multi_agent_orchestration | reroute | proceed | 0.222 | 10.004 | 0.850 |
| MR-045 | 4 | multi_agent_orchestration | reroute | proceed | 0.000 | 9.047 | 0.850 |
| MR-049 | 4 | multi_agent_orchestration | reroute | proceed | 0.000 | 8.403 | 0.850 |
| MR-052 | 4 | multi_agent_orchestration | reroute | pause | 0.000 | 9.608 | 0.850 |
| MR-053 | 4 | multi_agent_orchestration | reroute | proceed | 0.222 | 7.286 | 0.850 |
| MR-078 | 4 | multi_agent_orchestration | request_human_review | pause | 0.333 | 10.687 | 0.850 |
| MR-080 | 4 | multi_agent_orchestration | request_human_review | pause | 0.000 | 10.353 | 0.850 |
| MR-084 | 4 | multi_agent_orchestration | request_human_review | pause | 0.182 | 11.467 | 0.850 |
| MR-086 | 4 | multi_agent_orchestration | request_human_review | pause | 0.000 | 9.042 | 0.850 |
| MR-088 | 4 | multi_agent_orchestration | request_human_review | pause | 0.167 | 9.320 | 0.850 |
| MR-090 | 4 | multi_agent_orchestration | request_human_review | pause | 0.333 | 13.107 | 0.850 |
| MR-092 | 4 | multi_agent_orchestration | request_human_review | pause | 0.000 | 12.627 | 0.850 |
| MR-094 | 4 | multi_agent_orchestration | request_human_review | pause | 0.000 | 10.649 | 0.850 |
| MR-095 | 4 | multi_agent_orchestration | request_human_review | pause | 0.200 | 9.629 | 0.850 |
| MR-096 | 4 | multi_agent_orchestration | request_human_review | pause | 0.308 | 10.312 | 0.850 |
| MR-098 | 4 | multi_agent_orchestration | request_human_review | reroute | 0.000 | 8.901 | 0.850 |
| MR-099 | 4 | multi_agent_orchestration | request_human_review | pause | 0.444 | 13.811 | 0.850 |
| MR-100 | 4 | multi_agent_orchestration | request_human_review | pause | 0.000 | 11.754 | 0.850 |
| MR-002 | 5 | multi_agent_orchestration | reroute | pause | 0.222 | 12.383 | 0.850 |
| MR-005 | 5 | multi_agent_orchestration | reroute | proceed | 0.286 | 10.411 | 0.850 |
| MR-008 | 5 | multi_agent_orchestration | request_human_review | pause | 0.500 | 10.198 | 0.850 |
| MR-033 | 5 | multi_agent_orchestration | reroute | proceed | 0.000 | 11.814 | 0.850 |
| MR-037 | 5 | multi_agent_orchestration | reroute | proceed | 0.000 | 9.730 | 0.850 |
| MR-040 | 5 | multi_agent_orchestration | reroute | proceed | 0.250 | 8.701 | 0.850 |
| MR-041 | 5 | multi_agent_orchestration | reroute | proceed | 0.222 | 7.974 | 0.850 |
| MR-045 | 5 | multi_agent_orchestration | reroute | proceed | 0.000 | 10.314 | 0.850 |
| MR-049 | 5 | multi_agent_orchestration | reroute | proceed | 0.000 | 10.950 | 0.850 |
| MR-052 | 5 | multi_agent_orchestration | reroute | proceed | 0.200 | 9.083 | 0.850 |
| MR-053 | 5 | multi_agent_orchestration | reroute | proceed | 0.000 | 9.544 | 0.850 |
| MR-078 | 5 | multi_agent_orchestration | request_human_review | reroute | 0.333 | 10.454 | 0.850 |
| MR-080 | 5 | multi_agent_orchestration | request_human_review | pause | 0.000 | 11.468 | 0.850 |
| MR-081 | 5 | multi_agent_orchestration | request_human_review | pause | 0.400 | 13.927 | 0.850 |
| MR-082 | 5 | multi_agent_orchestration | request_human_review | pause | 0.000 | 11.879 | 0.850 |
| MR-083 | 5 | multi_agent_orchestration | request_human_review | pause | 0.200 | 12.917 | 0.850 |
| MR-084 | 5 | multi_agent_orchestration | request_human_review | pause | 0.167 | 10.582 | 0.850 |
| MR-086 | 5 | multi_agent_orchestration | request_human_review | reroute | 0.000 | 13.894 | 0.850 |
| MR-088 | 5 | multi_agent_orchestration | request_human_review | pause | 0.000 | 10.425 | 0.850 |
| MR-090 | 5 | multi_agent_orchestration | request_human_review | pause | 0.333 | 11.980 | 0.850 |
| MR-092 | 5 | multi_agent_orchestration | request_human_review | pause | 0.000 | 10.626 | 0.850 |
| MR-094 | 5 | multi_agent_orchestration | request_human_review | pause | 0.000 | 13.211 | 0.850 |
| MR-095 | 5 | multi_agent_orchestration | request_human_review | pause | 0.200 | 29.079 | 0.850 |
| MR-096 | 5 | multi_agent_orchestration | request_human_review | pause | 0.364 | 11.393 | 0.850 |
| MR-100 | 5 | multi_agent_orchestration | request_human_review | pause | 0.000 | 9.934 | 0.850 |

## Table 4. Pairwise statistical comparisons
No rows available.

These tables are generated automatically from `outputs/results.json` and are intended for direct reuse in drafts, appendices, or supplementary materials.