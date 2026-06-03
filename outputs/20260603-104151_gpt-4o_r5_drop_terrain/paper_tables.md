# Paper-Ready Tables

## Table 1. Aggregate architecture comparison
| architecture_type | runs | scenarios | evaluations | decision_accuracy | mean_exact_hazard_f1 | mean_semantic_hazard_f1 | mean_hazard_false_positive_count | mean_canonical_hazard_coverage | mean_spurious_hazard_count | mean_latency_seconds | mean_token_usage |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| multi_agent_orchestration | 5 | 100 | 500 | 0.666 | 0.007 | 0.070 | 4.264 | 0.119 | 2.798 | 10.776 | 1862.980 |

## Table 2. Scenario-level performance by architecture
| scenario_id | architecture_type | runs | expected_action | modal_recommended_action | decision_accuracy | mean_exact_hazard_f1 | mean_semantic_hazard_f1 | mean_canonical_hazard_coverage | mean_spurious_hazard_count | mean_latency_seconds |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR-001 | multi_agent_orchestration | 5 | proceed | proceed | 1.000 | 0.000 | 0.000 | 0.000 | 2.400 | 7.372 |
| MR-002 | multi_agent_orchestration | 5 | reroute | pause | 0.000 | 0.000 | 0.000 | 0.000 | 3.000 | 13.921 |
| MR-003 | multi_agent_orchestration | 5 | pause | pause | 1.000 | 0.000 | 0.480 | 1.000 | 1.200 | 11.212 |
| MR-004 | multi_agent_orchestration | 5 | request_human_review | proceed | 0.000 | 0.000 | 0.197 | 0.266 | 2.600 | 11.067 |
| MR-005 | multi_agent_orchestration | 5 | reroute | proceed | 0.000 | 0.387 | 0.387 | 0.500 | 1.200 | 9.549 |
| MR-006 | multi_agent_orchestration | 5 | pause | pause | 1.000 | 0.000 | 0.000 | 0.000 | 1.800 | 10.835 |
| MR-007 | multi_agent_orchestration | 5 | proceed | proceed | 1.000 | 0.000 | 0.000 | 0.000 | 2.200 | 10.005 |
| MR-008 | multi_agent_orchestration | 5 | request_human_review | pause | 0.000 | 0.000 | 0.178 | 0.160 | 1.200 | 10.025 |
| MR-009 | multi_agent_orchestration | 5 | proceed | proceed | 1.000 | 0.000 | 0.000 | 0.000 | 1.800 | 9.310 |
| MR-010 | multi_agent_orchestration | 5 | proceed | proceed | 1.000 | 0.000 | 0.000 | 0.000 | 2.000 | 11.709 |
| MR-011 | multi_agent_orchestration | 5 | proceed | proceed | 1.000 | 0.000 | 0.000 | 0.000 | 2.600 | 9.527 |
| MR-012 | multi_agent_orchestration | 5 | proceed | proceed | 1.000 | 0.000 | 0.000 | 0.000 | 2.000 | 8.853 |
| MR-013 | multi_agent_orchestration | 5 | proceed | proceed | 1.000 | 0.000 | 0.000 | 0.000 | 3.000 | 9.470 |
| MR-014 | multi_agent_orchestration | 5 | proceed | proceed | 1.000 | 0.000 | 0.000 | 0.000 | 2.400 | 9.543 |
| MR-015 | multi_agent_orchestration | 5 | proceed | proceed | 1.000 | 0.000 | 0.000 | 0.000 | 2.400 | 8.215 |
| MR-016 | multi_agent_orchestration | 5 | proceed | proceed | 1.000 | 0.000 | 0.000 | 0.000 | 1.800 | 9.986 |
| MR-017 | multi_agent_orchestration | 5 | proceed | proceed | 1.000 | 0.000 | 0.000 | 0.000 | 2.800 | 8.461 |
| MR-018 | multi_agent_orchestration | 5 | proceed | proceed | 1.000 | 0.000 | 0.000 | 0.000 | 2.600 | 8.450 |
| MR-019 | multi_agent_orchestration | 5 | proceed | proceed | 1.000 | 0.000 | 0.000 | 0.000 | 3.400 | 9.791 |
| MR-020 | multi_agent_orchestration | 5 | proceed | proceed | 1.000 | 0.000 | 0.000 | 0.000 | 2.000 | 8.611 |
| MR-021 | multi_agent_orchestration | 5 | proceed | proceed | 1.000 | 0.000 | 0.000 | 0.000 | 2.200 | 11.404 |
| MR-022 | multi_agent_orchestration | 5 | proceed | proceed | 1.000 | 0.000 | 0.000 | 0.000 | 2.600 | 10.523 |
| MR-023 | multi_agent_orchestration | 5 | proceed | proceed | 1.000 | 0.000 | 0.000 | 0.000 | 2.800 | 8.809 |
| MR-024 | multi_agent_orchestration | 5 | proceed | proceed | 1.000 | 0.000 | 0.000 | 0.000 | 1.800 | 8.514 |
| MR-025 | multi_agent_orchestration | 5 | proceed | proceed | 1.000 | 0.000 | 0.000 | 0.000 | 3.200 | 9.186 |
| MR-026 | multi_agent_orchestration | 5 | proceed | proceed | 1.000 | 0.000 | 0.000 | 0.000 | 2.600 | 8.643 |
| MR-027 | multi_agent_orchestration | 5 | proceed | proceed | 1.000 | 0.000 | 0.000 | 0.000 | 2.000 | 9.866 |
| MR-028 | multi_agent_orchestration | 5 | proceed | proceed | 1.000 | 0.000 | 0.000 | 0.000 | 2.400 | 8.773 |
| MR-029 | multi_agent_orchestration | 5 | proceed | proceed | 1.000 | 0.000 | 0.000 | 0.000 | 2.600 | 9.643 |
| MR-030 | multi_agent_orchestration | 5 | proceed | proceed | 1.000 | 0.000 | 0.000 | 0.000 | 2.200 | 8.283 |
| MR-031 | multi_agent_orchestration | 5 | proceed | proceed | 1.000 | 0.000 | 0.000 | 0.000 | 3.600 | 9.710 |
| MR-032 | multi_agent_orchestration | 5 | reroute | proceed | 0.200 | 0.000 | 0.000 | 0.000 | 5.800 | 11.843 |
| MR-033 | multi_agent_orchestration | 5 | reroute | proceed | 0.000 | 0.000 | 0.000 | 0.000 | 5.000 | 10.697 |
| MR-034 | multi_agent_orchestration | 5 | reroute | proceed | 0.200 | 0.000 | 0.000 | 0.000 | 1.400 | 9.450 |
| MR-035 | multi_agent_orchestration | 5 | reroute | reroute | 1.000 | 0.000 | 0.350 | 0.500 | 1.800 | 10.401 |
| MR-036 | multi_agent_orchestration | 5 | reroute | proceed | 0.200 | 0.000 | 0.000 | 0.000 | 3.000 | 13.346 |
| MR-037 | multi_agent_orchestration | 5 | reroute | proceed | 0.000 | 0.000 | 0.000 | 0.000 | 5.000 | 11.318 |
| MR-038 | multi_agent_orchestration | 5 | reroute | reroute | 0.600 | 0.000 | 0.000 | 0.000 | 0.800 | 11.046 |
| MR-039 | multi_agent_orchestration | 5 | reroute | reroute | 1.000 | 0.000 | 0.000 | 0.000 | 3.200 | 9.988 |
| MR-040 | multi_agent_orchestration | 5 | reroute | proceed | 0.000 | 0.000 | 0.000 | 0.000 | 3.400 | 13.319 |
| MR-041 | multi_agent_orchestration | 5 | reroute | proceed | 0.000 | 0.000 | 0.000 | 0.000 | 4.000 | 8.987 |
| MR-042 | multi_agent_orchestration | 5 | reroute | reroute | 1.000 | 0.000 | 0.000 | 0.000 | 2.000 | 9.971 |
| MR-043 | multi_agent_orchestration | 5 | reroute | reroute | 1.000 | 0.000 | 0.000 | 0.000 | 2.800 | 10.854 |
| MR-044 | multi_agent_orchestration | 5 | reroute | reroute | 0.600 | 0.000 | 0.000 | 0.000 | 4.400 | 10.418 |
| MR-045 | multi_agent_orchestration | 5 | reroute | proceed | 0.000 | 0.000 | 0.000 | 0.000 | 4.400 | 12.138 |
| MR-046 | multi_agent_orchestration | 5 | reroute | reroute | 0.800 | 0.000 | 0.000 | 0.000 | 1.000 | 10.340 |
| MR-047 | multi_agent_orchestration | 5 | reroute | reroute | 1.000 | 0.000 | 0.400 | 0.500 | 1.000 | 9.518 |
| MR-048 | multi_agent_orchestration | 5 | reroute | reroute | 0.600 | 0.000 | 0.000 | 0.000 | 3.200 | 11.968 |
| MR-049 | multi_agent_orchestration | 5 | reroute | proceed | 0.000 | 0.000 | 0.000 | 0.000 | 5.200 | 10.073 |
| MR-050 | multi_agent_orchestration | 5 | reroute | reroute | 0.600 | 0.000 | 0.000 | 0.000 | 1.000 | 11.769 |
| MR-051 | multi_agent_orchestration | 5 | reroute | reroute | 1.000 | 0.000 | 0.000 | 0.000 | 2.800 | 10.840 |
| MR-052 | multi_agent_orchestration | 5 | reroute | reroute | 1.000 | 0.000 | 0.000 | 0.000 | 4.400 | 10.475 |
| MR-053 | multi_agent_orchestration | 5 | reroute | proceed | 0.000 | 0.000 | 0.000 | 0.000 | 3.600 | 10.429 |
| MR-054 | multi_agent_orchestration | 5 | reroute | proceed | 0.400 | 0.000 | 0.000 | 0.000 | 1.800 | 9.153 |
| MR-055 | multi_agent_orchestration | 5 | pause | pause | 1.000 | 0.000 | 0.500 | 1.000 | 1.200 | 10.079 |
| MR-056 | multi_agent_orchestration | 5 | pause | pause | 1.000 | 0.000 | 0.000 | 0.000 | 5.200 | 13.423 |
| MR-057 | multi_agent_orchestration | 5 | pause | pause | 1.000 | 0.000 | 0.000 | 0.000 | 4.400 | 10.315 |
| MR-058 | multi_agent_orchestration | 5 | pause | pause | 1.000 | 0.000 | 0.000 | 0.000 | 2.400 | 11.662 |
| MR-059 | multi_agent_orchestration | 5 | pause | pause | 1.000 | 0.000 | 0.000 | 0.000 | 2.000 | 12.186 |
| MR-060 | multi_agent_orchestration | 5 | pause | pause | 1.000 | 0.129 | 0.129 | 0.300 | 4.600 | 9.093 |
| MR-061 | multi_agent_orchestration | 5 | pause | pause | 1.000 | 0.000 | 0.324 | 1.000 | 3.200 | 10.515 |
| MR-062 | multi_agent_orchestration | 5 | pause | pause | 1.000 | 0.133 | 0.400 | 0.600 | 1.800 | 12.210 |
| MR-063 | multi_agent_orchestration | 5 | pause | pause | 1.000 | 0.000 | 0.000 | 0.000 | 3.000 | 9.942 |
| MR-064 | multi_agent_orchestration | 5 | pause | pause | 1.000 | 0.000 | 0.000 | 0.000 | 6.000 | 12.620 |
| MR-065 | multi_agent_orchestration | 5 | pause | pause | 1.000 | 0.000 | 0.000 | 0.000 | 4.000 | 9.917 |
| MR-066 | multi_agent_orchestration | 5 | pause | pause | 1.000 | 0.000 | 0.000 | 0.000 | 2.000 | 11.916 |
| MR-067 | multi_agent_orchestration | 5 | pause | pause | 1.000 | 0.000 | 0.480 | 1.000 | 2.000 | 10.605 |
| MR-068 | multi_agent_orchestration | 5 | pause | pause | 1.000 | 0.000 | 0.124 | 0.300 | 3.800 | 9.699 |
| MR-069 | multi_agent_orchestration | 5 | pause | pause | 1.000 | 0.000 | 0.000 | 0.000 | 3.800 | 9.042 |
| MR-070 | multi_agent_orchestration | 5 | pause | pause | 1.000 | 0.000 | 0.000 | 0.000 | 1.800 | 10.889 |
| MR-071 | multi_agent_orchestration | 5 | pause | pause | 1.000 | 0.000 | 0.000 | 0.000 | 2.800 | 9.886 |
| MR-072 | multi_agent_orchestration | 5 | pause | pause | 1.000 | 0.000 | 0.000 | 0.000 | 6.000 | 10.058 |
| MR-073 | multi_agent_orchestration | 5 | pause | pause | 1.000 | 0.000 | 0.298 | 1.000 | 3.000 | 11.579 |
| MR-074 | multi_agent_orchestration | 5 | pause | pause | 1.000 | 0.050 | 0.144 | 0.300 | 2.600 | 13.327 |
| MR-075 | multi_agent_orchestration | 5 | pause | pause | 1.000 | 0.000 | 0.000 | 0.000 | 2.800 | 12.138 |
| MR-076 | multi_agent_orchestration | 5 | pause | pause | 1.000 | 0.000 | 0.000 | 0.000 | 3.800 | 8.351 |
| MR-077 | multi_agent_orchestration | 5 | pause | pause | 1.000 | 0.000 | 0.000 | 0.000 | 3.800 | 9.461 |
| MR-078 | multi_agent_orchestration | 5 | request_human_review | pause | 0.000 | 0.000 | 0.244 | 0.333 | 1.800 | 10.508 |
| MR-079 | multi_agent_orchestration | 5 | request_human_review | pause | 0.000 | 0.000 | 0.000 | 0.000 | 4.200 | 11.431 |
| MR-080 | multi_agent_orchestration | 5 | request_human_review | pause | 0.000 | 0.000 | 0.000 | 0.000 | 2.200 | 13.315 |
| MR-081 | multi_agent_orchestration | 5 | request_human_review | pause | 0.200 | 0.000 | 0.257 | 0.333 | 2.800 | 15.503 |
| MR-082 | multi_agent_orchestration | 5 | request_human_review | pause | 0.200 | 0.000 | 0.000 | 0.000 | 1.800 | 10.009 |
| MR-083 | multi_agent_orchestration | 5 | request_human_review | pause | 0.200 | 0.000 | 0.279 | 0.333 | 1.000 | 15.521 |
| MR-084 | multi_agent_orchestration | 5 | request_human_review | pause | 0.000 | 0.000 | 0.244 | 0.333 | 1.200 | 9.991 |
| MR-085 | multi_agent_orchestration | 5 | request_human_review | request_human_review | 0.800 | 0.000 | 0.000 | 0.000 | 3.000 | 19.703 |
| MR-086 | multi_agent_orchestration | 5 | request_human_review | pause | 0.000 | 0.000 | 0.000 | 0.000 | 3.200 | 10.162 |
| MR-087 | multi_agent_orchestration | 5 | request_human_review | request_human_review | 0.800 | 0.000 | 0.160 | 0.266 | 5.800 | 13.693 |
| MR-088 | multi_agent_orchestration | 5 | request_human_review | pause | 0.000 | 0.000 | 0.000 | 0.000 | 2.200 | 10.034 |
| MR-089 | multi_agent_orchestration | 5 | request_human_review | request_human_review | 1.000 | 0.000 | 0.250 | 0.333 | 2.000 | 10.970 |
| MR-090 | multi_agent_orchestration | 5 | request_human_review | pause | 0.000 | 0.000 | 0.250 | 0.333 | 2.000 | 12.094 |
| MR-091 | multi_agent_orchestration | 5 | request_human_review | pause | 0.400 | 0.000 | 0.000 | 0.000 | 4.400 | 11.902 |
| MR-092 | multi_agent_orchestration | 5 | request_human_review | pause | 0.000 | 0.000 | 0.000 | 0.000 | 2.400 | 12.518 |
| MR-093 | multi_agent_orchestration | 5 | request_human_review | request_human_review | 0.600 | 0.000 | 0.157 | 0.200 | 3.600 | 15.918 |
| MR-094 | multi_agent_orchestration | 5 | request_human_review | pause | 0.200 | 0.000 | 0.000 | 0.000 | 1.200 | 10.597 |
| MR-095 | multi_agent_orchestration | 5 | request_human_review | pause | 0.000 | 0.000 | 0.272 | 0.333 | 1.400 | 11.144 |
| MR-096 | multi_agent_orchestration | 5 | request_human_review | pause | 0.000 | 0.000 | 0.222 | 0.333 | 2.000 | 10.437 |
| MR-097 | multi_agent_orchestration | 5 | request_human_review | request_human_review | 1.000 | 0.000 | 0.000 | 0.000 | 3.000 | 12.034 |
| MR-098 | multi_agent_orchestration | 5 | request_human_review | pause | 0.000 | 0.000 | 0.000 | 0.000 | 3.400 | 10.268 |
| MR-099 | multi_agent_orchestration | 5 | request_human_review | pause | 0.000 | 0.000 | 0.264 | 0.333 | 3.600 | 13.146 |
| MR-100 | multi_agent_orchestration | 5 | request_human_review | pause | 0.000 | 0.000 | 0.000 | 0.000 | 2.200 | 10.174 |

## Table 3. Incorrect decisions
| scenario_id | run_id | architecture_type | expected_action | recommended_action | semantic_hazard_f1 | latency_seconds | confidence_score |
| --- | --- | --- | --- | --- | --- | --- | --- |
| MR-002 | 1 | multi_agent_orchestration | reroute | pause | 0.000 | 11.664 | 0.850 |
| MR-004 | 1 | multi_agent_orchestration | request_human_review | proceed | 0.286 | 10.474 | 0.850 |
| MR-005 | 1 | multi_agent_orchestration | reroute | proceed | 0.333 | 8.801 | 0.850 |
| MR-008 | 1 | multi_agent_orchestration | request_human_review | proceed | 0.222 | 11.777 | 0.850 |
| MR-032 | 1 | multi_agent_orchestration | reroute | proceed | 0.000 | 8.798 | 0.850 |
| MR-033 | 1 | multi_agent_orchestration | reroute | proceed | 0.000 | 9.216 | 0.850 |
| MR-036 | 1 | multi_agent_orchestration | reroute | proceed | 0.000 | 9.322 | 0.850 |
| MR-037 | 1 | multi_agent_orchestration | reroute | proceed | 0.000 | 11.036 | 0.850 |
| MR-040 | 1 | multi_agent_orchestration | reroute | proceed | 0.000 | 8.195 | 0.850 |
| MR-041 | 1 | multi_agent_orchestration | reroute | proceed | 0.000 | 7.376 | 0.850 |
| MR-045 | 1 | multi_agent_orchestration | reroute | proceed | 0.000 | 13.242 | 0.850 |
| MR-048 | 1 | multi_agent_orchestration | reroute | proceed | 0.000 | 20.385 | 0.850 |
| MR-049 | 1 | multi_agent_orchestration | reroute | proceed | 0.000 | 9.013 | 0.850 |
| MR-053 | 1 | multi_agent_orchestration | reroute | proceed | 0.000 | 8.770 | 0.850 |
| MR-054 | 1 | multi_agent_orchestration | reroute | proceed | 0.000 | 8.390 | 0.850 |
| MR-078 | 1 | multi_agent_orchestration | request_human_review | pause | 0.250 | 10.134 | 0.850 |
| MR-079 | 1 | multi_agent_orchestration | request_human_review | pause | 0.000 | 12.184 | 0.850 |
| MR-080 | 1 | multi_agent_orchestration | request_human_review | pause | 0.000 | 8.704 | 0.850 |
| MR-081 | 1 | multi_agent_orchestration | request_human_review | pause | 0.250 | 14.375 | 0.850 |
| MR-082 | 1 | multi_agent_orchestration | request_human_review | pause | 0.000 | 9.084 | 0.850 |
| MR-083 | 1 | multi_agent_orchestration | request_human_review | pause | 0.250 | 11.458 | 0.850 |
| MR-084 | 1 | multi_agent_orchestration | request_human_review | pause | 0.222 | 9.164 | 0.850 |
| MR-086 | 1 | multi_agent_orchestration | request_human_review | pause | 0.000 | 9.695 | 0.850 |
| MR-088 | 1 | multi_agent_orchestration | request_human_review | pause | 0.000 | 8.521 | 0.850 |
| MR-090 | 1 | multi_agent_orchestration | request_human_review | pause | 0.250 | 11.266 | 0.850 |
| MR-091 | 1 | multi_agent_orchestration | request_human_review | pause | 0.000 | 9.937 | 0.850 |
| MR-092 | 1 | multi_agent_orchestration | request_human_review | pause | 0.000 | 9.112 | 0.850 |
| MR-094 | 1 | multi_agent_orchestration | request_human_review | pause | 0.000 | 11.047 | 0.850 |
| MR-095 | 1 | multi_agent_orchestration | request_human_review | pause | 0.250 | 13.423 | 0.880 |
| MR-096 | 1 | multi_agent_orchestration | request_human_review | pause | 0.222 | 9.422 | 0.850 |
| MR-098 | 1 | multi_agent_orchestration | request_human_review | reroute | 0.000 | 8.397 | 0.850 |
| MR-099 | 1 | multi_agent_orchestration | request_human_review | pause | 0.286 | 13.519 | 0.850 |
| MR-100 | 1 | multi_agent_orchestration | request_human_review | pause | 0.000 | 10.587 | 0.820 |
| MR-002 | 2 | multi_agent_orchestration | reroute | pause | 0.000 | 15.538 | 0.850 |
| MR-004 | 2 | multi_agent_orchestration | request_human_review | reroute | 0.200 | 11.776 | 0.850 |
| MR-005 | 2 | multi_agent_orchestration | reroute | proceed | 0.400 | 7.783 | 0.850 |
| MR-008 | 2 | multi_agent_orchestration | request_human_review | pause | 0.222 | 10.218 | 0.850 |
| MR-033 | 2 | multi_agent_orchestration | reroute | proceed | 0.000 | 12.702 | 0.850 |
| MR-034 | 2 | multi_agent_orchestration | reroute | proceed | 0.000 | 9.316 | 0.850 |
| MR-036 | 2 | multi_agent_orchestration | reroute | pause | 0.000 | 10.547 | 0.850 |
| MR-037 | 2 | multi_agent_orchestration | reroute | proceed | 0.000 | 11.275 | 0.850 |
| MR-040 | 2 | multi_agent_orchestration | reroute | pause | 0.000 | 19.096 | 0.850 |
| MR-041 | 2 | multi_agent_orchestration | reroute | proceed | 0.000 | 9.625 | 0.850 |
| MR-045 | 2 | multi_agent_orchestration | reroute | proceed | 0.000 | 17.920 | 0.850 |
| MR-049 | 2 | multi_agent_orchestration | reroute | proceed | 0.000 | 9.319 | 0.850 |
| MR-050 | 2 | multi_agent_orchestration | reroute | proceed | 0.000 | 10.855 | 0.850 |
| MR-053 | 2 | multi_agent_orchestration | reroute | proceed | 0.000 | 11.367 | 0.850 |
| MR-078 | 2 | multi_agent_orchestration | request_human_review | pause | 0.250 | 9.889 | 0.850 |
| MR-079 | 2 | multi_agent_orchestration | request_human_review | pause | 0.000 | 11.986 | 0.850 |
| MR-080 | 2 | multi_agent_orchestration | request_human_review | pause | 0.000 | 11.357 | 0.850 |
| MR-081 | 2 | multi_agent_orchestration | request_human_review | pause | 0.250 | 17.943 | 0.850 |
| MR-084 | 2 | multi_agent_orchestration | request_human_review | pause | 0.250 | 12.464 | 0.850 |
| MR-085 | 2 | multi_agent_orchestration | request_human_review | pause | 0.000 | 20.481 | 0.850 |
| MR-086 | 2 | multi_agent_orchestration | request_human_review | pause | 0.000 | 10.856 | 0.850 |
| MR-088 | 2 | multi_agent_orchestration | request_human_review | pause | 0.000 | 11.004 | 0.850 |
| MR-090 | 2 | multi_agent_orchestration | request_human_review | pause | 0.250 | 10.960 | 0.850 |
| MR-092 | 2 | multi_agent_orchestration | request_human_review | pause | 0.000 | 17.507 | 0.850 |
| MR-094 | 2 | multi_agent_orchestration | request_human_review | pause | 0.000 | 10.749 | 0.850 |
| MR-095 | 2 | multi_agent_orchestration | request_human_review | pause | 0.250 | 12.848 | 0.850 |
| MR-096 | 2 | multi_agent_orchestration | request_human_review | pause | 0.222 | 9.793 | 0.850 |
| MR-098 | 2 | multi_agent_orchestration | request_human_review | reroute | 0.000 | 10.402 | 0.850 |
| MR-099 | 2 | multi_agent_orchestration | request_human_review | pause | 0.250 | 12.083 | 0.850 |
| MR-100 | 2 | multi_agent_orchestration | request_human_review | pause | 0.000 | 10.340 | 0.850 |
| MR-002 | 3 | multi_agent_orchestration | reroute | pause | 0.000 | 13.373 | 0.850 |
| MR-004 | 3 | multi_agent_orchestration | request_human_review | proceed | 0.000 | 11.570 | 0.850 |
| MR-005 | 3 | multi_agent_orchestration | reroute | proceed | 0.400 | 9.697 | 0.850 |
| MR-008 | 3 | multi_agent_orchestration | request_human_review | pause | 0.000 | 9.627 | 0.850 |
| MR-032 | 3 | multi_agent_orchestration | reroute | proceed | 0.000 | 18.234 | 0.850 |
| MR-033 | 3 | multi_agent_orchestration | reroute | proceed | 0.000 | 12.745 | 0.850 |
| MR-034 | 3 | multi_agent_orchestration | reroute | proceed | 0.000 | 10.645 | 0.850 |
| MR-036 | 3 | multi_agent_orchestration | reroute | proceed | 0.000 | 12.528 | 0.850 |
| MR-037 | 3 | multi_agent_orchestration | reroute | proceed | 0.000 | 10.853 | 0.850 |
| MR-040 | 3 | multi_agent_orchestration | reroute | proceed | 0.000 | 11.060 | 0.850 |
| MR-041 | 3 | multi_agent_orchestration | reroute | proceed | 0.000 | 10.141 | 0.850 |
| MR-044 | 3 | multi_agent_orchestration | reroute | proceed | 0.000 | 9.897 | 0.850 |
| MR-045 | 3 | multi_agent_orchestration | reroute | proceed | 0.000 | 9.615 | 0.850 |
| MR-049 | 3 | multi_agent_orchestration | reroute | proceed | 0.000 | 8.395 | 0.850 |
| MR-053 | 3 | multi_agent_orchestration | reroute | proceed | 0.000 | 11.260 | 0.850 |
| MR-054 | 3 | multi_agent_orchestration | reroute | proceed | 0.000 | 7.360 | 0.850 |
| MR-078 | 3 | multi_agent_orchestration | request_human_review | reroute | 0.250 | 11.347 | 0.850 |
| MR-079 | 3 | multi_agent_orchestration | request_human_review | pause | 0.000 | 11.364 | 0.850 |
| MR-080 | 3 | multi_agent_orchestration | request_human_review | proceed | 0.000 | 13.071 | 0.850 |
| MR-081 | 3 | multi_agent_orchestration | request_human_review | pause | 0.250 | 16.623 | 0.850 |
| MR-082 | 3 | multi_agent_orchestration | request_human_review | pause | 0.000 | 10.854 | 0.850 |
| MR-083 | 3 | multi_agent_orchestration | request_human_review | pause | 0.286 | 25.955 | 0.850 |
| MR-084 | 3 | multi_agent_orchestration | request_human_review | pause | 0.250 | 9.073 | 0.850 |
| MR-086 | 3 | multi_agent_orchestration | request_human_review | pause | 0.000 | 9.875 | 0.850 |
| MR-087 | 3 | multi_agent_orchestration | request_human_review | pause | 0.000 | 12.652 | 0.850 |
| MR-088 | 3 | multi_agent_orchestration | request_human_review | pause | 0.000 | 9.799 | 0.850 |
| MR-090 | 3 | multi_agent_orchestration | request_human_review | pause | 0.250 | 16.078 | 0.850 |
| MR-092 | 3 | multi_agent_orchestration | request_human_review | pause | 0.000 | 11.398 | 0.850 |
| MR-093 | 3 | multi_agent_orchestration | request_human_review | pause | 0.250 | 14.487 | 0.850 |
| MR-094 | 3 | multi_agent_orchestration | request_human_review | pause | 0.000 | 10.783 | 0.850 |
| MR-095 | 3 | multi_agent_orchestration | request_human_review | pause | 0.286 | 7.752 | 0.850 |
| MR-096 | 3 | multi_agent_orchestration | request_human_review | pause | 0.222 | 12.204 | 0.850 |
| MR-098 | 3 | multi_agent_orchestration | request_human_review | pause | 0.000 | 9.829 | 0.850 |
| MR-099 | 3 | multi_agent_orchestration | request_human_review | pause | 0.250 | 12.081 | 0.850 |
| MR-100 | 3 | multi_agent_orchestration | request_human_review | pause | 0.000 | 9.011 | 0.820 |
| MR-002 | 4 | multi_agent_orchestration | reroute | pause | 0.000 | 15.159 | 0.850 |
| MR-004 | 4 | multi_agent_orchestration | request_human_review | proceed | 0.250 | 12.192 | 0.850 |
| MR-005 | 4 | multi_agent_orchestration | reroute | proceed | 0.400 | 10.625 | 0.850 |
| MR-008 | 4 | multi_agent_orchestration | request_human_review | pause | 0.222 | 9.214 | 0.850 |
| MR-032 | 4 | multi_agent_orchestration | reroute | proceed | 0.000 | 10.182 | 0.850 |
| MR-033 | 4 | multi_agent_orchestration | reroute | proceed | 0.000 | 9.785 | 0.850 |
| MR-034 | 4 | multi_agent_orchestration | reroute | proceed | 0.000 | 10.124 | 0.850 |
| MR-037 | 4 | multi_agent_orchestration | reroute | proceed | 0.000 | 11.956 | 0.880 |
| MR-038 | 4 | multi_agent_orchestration | reroute | proceed | 0.000 | 10.444 | 0.850 |
| MR-040 | 4 | multi_agent_orchestration | reroute | proceed | 0.000 | 13.913 | 0.850 |
| MR-041 | 4 | multi_agent_orchestration | reroute | proceed | 0.000 | 8.169 | 0.850 |
| MR-044 | 4 | multi_agent_orchestration | reroute | proceed | 0.000 | 11.567 | 0.850 |
| MR-045 | 4 | multi_agent_orchestration | reroute | proceed | 0.000 | 9.524 | 0.850 |
| MR-046 | 4 | multi_agent_orchestration | reroute | proceed | 0.000 | 11.065 | 0.850 |
| MR-049 | 4 | multi_agent_orchestration | reroute | proceed | 0.000 | 11.676 | 0.850 |
| MR-053 | 4 | multi_agent_orchestration | reroute | proceed | 0.000 | 9.995 | 0.850 |
| MR-054 | 4 | multi_agent_orchestration | reroute | proceed | 0.000 | 9.419 | 0.850 |
| MR-078 | 4 | multi_agent_orchestration | request_human_review | pause | 0.222 | 10.408 | 0.850 |
| MR-079 | 4 | multi_agent_orchestration | request_human_review | pause | 0.000 | 10.193 | 0.850 |
| MR-080 | 4 | multi_agent_orchestration | request_human_review | pause | 0.000 | 19.501 | 0.850 |
| MR-081 | 4 | multi_agent_orchestration | request_human_review | pause | 0.286 | 15.564 | 0.850 |
| MR-082 | 4 | multi_agent_orchestration | request_human_review | pause | 0.000 | 11.166 | 0.850 |
| MR-083 | 4 | multi_agent_orchestration | request_human_review | pause | 0.286 | 20.071 | 0.850 |
| MR-084 | 4 | multi_agent_orchestration | request_human_review | pause | 0.250 | 11.398 | 0.850 |
| MR-086 | 4 | multi_agent_orchestration | request_human_review | reroute | 0.000 | 10.336 | 0.850 |
| MR-088 | 4 | multi_agent_orchestration | request_human_review | proceed | 0.000 | 10.479 | 0.820 |
| MR-090 | 4 | multi_agent_orchestration | request_human_review | pause | 0.250 | 11.159 | 0.850 |
| MR-091 | 4 | multi_agent_orchestration | request_human_review | pause | 0.000 | 12.909 | 0.850 |
| MR-092 | 4 | multi_agent_orchestration | request_human_review | pause | 0.000 | 11.266 | 0.850 |
| MR-093 | 4 | multi_agent_orchestration | request_human_review | pause | 0.250 | 15.419 | 0.850 |
| MR-094 | 4 | multi_agent_orchestration | request_human_review | pause | 0.000 | 10.702 | 0.850 |
| MR-095 | 4 | multi_agent_orchestration | request_human_review | pause | 0.286 | 10.327 | 0.850 |
| MR-096 | 4 | multi_agent_orchestration | request_human_review | pause | 0.222 | 11.140 | 0.850 |
| MR-098 | 4 | multi_agent_orchestration | request_human_review | pause | 0.000 | 10.933 | 0.850 |
| MR-099 | 4 | multi_agent_orchestration | request_human_review | pause | 0.286 | 14.964 | 0.850 |
| MR-100 | 4 | multi_agent_orchestration | request_human_review | pause | 0.000 | 9.128 | 0.850 |
| MR-002 | 5 | multi_agent_orchestration | reroute | pause | 0.000 | 13.871 | 0.850 |
| MR-004 | 5 | multi_agent_orchestration | request_human_review | proceed | 0.250 | 9.323 | 0.850 |
| MR-005 | 5 | multi_agent_orchestration | reroute | proceed | 0.400 | 10.837 | 0.880 |
| MR-008 | 5 | multi_agent_orchestration | request_human_review | pause | 0.222 | 9.288 | 0.850 |
| MR-032 | 5 | multi_agent_orchestration | reroute | pause | 0.000 | 11.878 | 0.850 |
| MR-033 | 5 | multi_agent_orchestration | reroute | proceed | 0.000 | 9.035 | 0.850 |
| MR-034 | 5 | multi_agent_orchestration | reroute | proceed | 0.000 | 8.657 | 0.850 |
| MR-036 | 5 | multi_agent_orchestration | reroute | proceed | 0.000 | 9.719 | 0.850 |
| MR-037 | 5 | multi_agent_orchestration | reroute | proceed | 0.000 | 11.469 | 0.850 |
| MR-038 | 5 | multi_agent_orchestration | reroute | proceed | 0.000 | 11.876 | 0.850 |
| MR-040 | 5 | multi_agent_orchestration | reroute | proceed | 0.000 | 14.329 | 0.820 |
| MR-041 | 5 | multi_agent_orchestration | reroute | proceed | 0.000 | 9.625 | 0.850 |
| MR-045 | 5 | multi_agent_orchestration | reroute | proceed | 0.000 | 10.389 | 0.880 |
| MR-048 | 5 | multi_agent_orchestration | reroute | proceed | 0.000 | 13.120 | 0.850 |
| MR-049 | 5 | multi_agent_orchestration | reroute | proceed | 0.000 | 11.961 | 0.850 |
| MR-050 | 5 | multi_agent_orchestration | reroute | proceed | 0.000 | 13.410 | 0.850 |
| MR-053 | 5 | multi_agent_orchestration | reroute | proceed | 0.000 | 10.755 | 0.850 |
| MR-078 | 5 | multi_agent_orchestration | request_human_review | pause | 0.250 | 10.764 | 0.850 |
| MR-079 | 5 | multi_agent_orchestration | request_human_review | pause | 0.000 | 11.426 | 0.850 |
| MR-080 | 5 | multi_agent_orchestration | request_human_review | proceed | 0.000 | 13.942 | 0.850 |
| MR-082 | 5 | multi_agent_orchestration | request_human_review | pause | 0.000 | 10.457 | 0.850 |
| MR-083 | 5 | multi_agent_orchestration | request_human_review | pause | 0.286 | 10.566 | 0.850 |
| MR-084 | 5 | multi_agent_orchestration | request_human_review | pause | 0.250 | 7.855 | 0.850 |
| MR-086 | 5 | multi_agent_orchestration | request_human_review | pause | 0.000 | 10.047 | 0.850 |
| MR-088 | 5 | multi_agent_orchestration | request_human_review | pause | 0.000 | 10.367 | 0.850 |
| MR-090 | 5 | multi_agent_orchestration | request_human_review | pause | 0.250 | 11.006 | 0.850 |
| MR-091 | 5 | multi_agent_orchestration | request_human_review | pause | 0.000 | 15.670 | 0.850 |
| MR-092 | 5 | multi_agent_orchestration | request_human_review | proceed | 0.000 | 13.308 | 0.850 |
| MR-095 | 5 | multi_agent_orchestration | request_human_review | pause | 0.286 | 11.369 | 0.850 |
| MR-096 | 5 | multi_agent_orchestration | request_human_review | pause | 0.222 | 9.625 | 0.850 |
| MR-098 | 5 | multi_agent_orchestration | request_human_review | pause | 0.000 | 11.778 | 0.850 |
| MR-099 | 5 | multi_agent_orchestration | request_human_review | pause | 0.250 | 13.083 | 0.850 |
| MR-100 | 5 | multi_agent_orchestration | request_human_review | pause | 0.000 | 11.804 | 0.850 |

## Table 4. Pairwise statistical comparisons
No rows available.

These tables are generated automatically from `outputs/results.json` and are intended for direct reuse in drafts, appendices, or supplementary materials.