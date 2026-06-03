# Paper-Ready Tables

## Table 1. Aggregate architecture comparison
| architecture_type | runs | scenarios | evaluations | decision_accuracy | mean_exact_hazard_f1 | mean_semantic_hazard_f1 | mean_hazard_false_positive_count | mean_canonical_hazard_coverage | mean_spurious_hazard_count | mean_latency_seconds | mean_token_usage |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| multi_agent_orchestration | 5 | 100 | 500 | 0.734 | 0.043 | 0.106 | 5.514 | 0.214 | 3.312 | 11.833 | 2273.060 |
| single_agent | 5 | 100 | 500 | 0.810 | 0.081 | 0.131 | 1.526 | 0.144 | 0.150 | 2.320 | 457.938 |

## Table 2. Scenario-level performance by architecture
| scenario_id | architecture_type | runs | expected_action | modal_recommended_action | decision_accuracy | mean_exact_hazard_f1 | mean_semantic_hazard_f1 | mean_canonical_hazard_coverage | mean_spurious_hazard_count | mean_latency_seconds |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR-001 | multi_agent_orchestration | 5 | proceed | proceed | 1.000 | 0.000 | 0.000 | 0.000 | 2.000 | 10.471 |
| MR-001 | single_agent | 5 | proceed | proceed | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 4.225 |
| MR-002 | multi_agent_orchestration | 5 | reroute | pause | 0.000 | 0.040 | 0.040 | 0.067 | 2.800 | 14.190 |
| MR-002 | single_agent | 5 | reroute | pause | 0.000 | 0.000 | 0.286 | 0.333 | 0.000 | 2.130 |
| MR-003 | multi_agent_orchestration | 5 | pause | pause | 1.000 | 0.000 | 0.413 | 1.000 | 2.000 | 10.812 |
| MR-003 | single_agent | 5 | pause | pause | 1.000 | 0.400 | 1.000 | 1.000 | 0.000 | 2.121 |
| MR-004 | multi_agent_orchestration | 5 | request_human_review | proceed | 0.200 | 0.000 | 0.106 | 0.200 | 2.800 | 14.348 |
| MR-004 | single_agent | 5 | request_human_review | pause | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 2.641 |
| MR-005 | multi_agent_orchestration | 5 | reroute | proceed | 0.200 | 0.295 | 0.295 | 0.500 | 2.800 | 10.598 |
| MR-005 | single_agent | 5 | reroute | reroute | 1.000 | 0.900 | 0.900 | 0.900 | 0.000 | 1.978 |
| MR-006 | multi_agent_orchestration | 5 | pause | pause | 1.000 | 0.000 | 0.000 | 0.000 | 1.600 | 10.877 |
| MR-006 | single_agent | 5 | pause | pause | 1.000 | 0.400 | 0.400 | 0.500 | 0.000 | 2.303 |
| MR-007 | multi_agent_orchestration | 5 | proceed | proceed | 1.000 | 0.000 | 0.000 | 0.000 | 3.200 | 10.675 |
| MR-007 | single_agent | 5 | proceed | proceed | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 2.451 |
| MR-008 | multi_agent_orchestration | 5 | request_human_review | pause | 0.000 | 0.345 | 0.518 | 0.600 | 1.000 | 13.309 |
| MR-008 | single_agent | 5 | request_human_review | request_human_review | 0.800 | 0.250 | 0.250 | 0.200 | 0.000 | 2.464 |
| MR-009 | multi_agent_orchestration | 5 | proceed | proceed | 1.000 | 0.000 | 0.000 | 0.000 | 2.400 | 10.064 |
| MR-009 | single_agent | 5 | proceed | proceed | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 2.579 |
| MR-010 | multi_agent_orchestration | 5 | proceed | proceed | 1.000 | 0.000 | 0.000 | 0.000 | 2.000 | 10.891 |
| MR-010 | single_agent | 5 | proceed | proceed | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 2.923 |
| MR-011 | multi_agent_orchestration | 5 | proceed | proceed | 1.000 | 0.000 | 0.000 | 0.000 | 2.800 | 10.499 |
| MR-011 | single_agent | 5 | proceed | proceed | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 2.624 |
| MR-012 | multi_agent_orchestration | 5 | proceed | proceed | 1.000 | 0.000 | 0.000 | 0.000 | 2.600 | 10.277 |
| MR-012 | single_agent | 5 | proceed | proceed | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 2.490 |
| MR-013 | multi_agent_orchestration | 5 | proceed | proceed | 1.000 | 0.000 | 0.000 | 0.000 | 2.800 | 11.200 |
| MR-013 | single_agent | 5 | proceed | proceed | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 2.336 |
| MR-014 | multi_agent_orchestration | 5 | proceed | proceed | 1.000 | 0.000 | 0.000 | 0.000 | 2.400 | 9.171 |
| MR-014 | single_agent | 5 | proceed | proceed | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 2.108 |
| MR-015 | multi_agent_orchestration | 5 | proceed | proceed | 1.000 | 0.000 | 0.000 | 0.000 | 2.200 | 11.187 |
| MR-015 | single_agent | 5 | proceed | proceed | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 2.478 |
| MR-016 | multi_agent_orchestration | 5 | proceed | proceed | 1.000 | 0.000 | 0.000 | 0.000 | 2.400 | 11.343 |
| MR-016 | single_agent | 5 | proceed | proceed | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 2.776 |
| MR-017 | multi_agent_orchestration | 5 | proceed | proceed | 1.000 | 0.000 | 0.000 | 0.000 | 2.800 | 9.906 |
| MR-017 | single_agent | 5 | proceed | proceed | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 2.377 |
| MR-018 | multi_agent_orchestration | 5 | proceed | proceed | 1.000 | 0.000 | 0.000 | 0.000 | 3.000 | 10.125 |
| MR-018 | single_agent | 5 | proceed | proceed | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 2.524 |
| MR-019 | multi_agent_orchestration | 5 | proceed | proceed | 1.000 | 0.000 | 0.000 | 0.000 | 3.000 | 10.804 |
| MR-019 | single_agent | 5 | proceed | proceed | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 2.581 |
| MR-020 | multi_agent_orchestration | 5 | proceed | proceed | 1.000 | 0.000 | 0.000 | 0.000 | 2.000 | 10.036 |
| MR-020 | single_agent | 5 | proceed | proceed | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 2.239 |
| MR-021 | multi_agent_orchestration | 5 | proceed | proceed | 1.000 | 0.000 | 0.000 | 0.000 | 2.000 | 10.044 |
| MR-021 | single_agent | 5 | proceed | proceed | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 2.753 |
| MR-022 | multi_agent_orchestration | 5 | proceed | proceed | 1.000 | 0.000 | 0.000 | 0.000 | 3.000 | 12.517 |
| MR-022 | single_agent | 5 | proceed | proceed | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 3.159 |
| MR-023 | multi_agent_orchestration | 5 | proceed | proceed | 1.000 | 0.000 | 0.000 | 0.000 | 3.000 | 10.200 |
| MR-023 | single_agent | 5 | proceed | proceed | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 3.196 |
| MR-024 | multi_agent_orchestration | 5 | proceed | proceed | 1.000 | 0.000 | 0.000 | 0.000 | 2.000 | 9.356 |
| MR-024 | single_agent | 5 | proceed | proceed | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 2.616 |
| MR-025 | multi_agent_orchestration | 5 | proceed | proceed | 1.000 | 0.000 | 0.000 | 0.000 | 3.000 | 9.722 |
| MR-025 | single_agent | 5 | proceed | proceed | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 2.501 |
| MR-026 | multi_agent_orchestration | 5 | proceed | proceed | 1.000 | 0.000 | 0.000 | 0.000 | 2.600 | 12.981 |
| MR-026 | single_agent | 5 | proceed | proceed | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 2.191 |
| MR-027 | multi_agent_orchestration | 5 | proceed | proceed | 1.000 | 0.000 | 0.000 | 0.000 | 2.800 | 10.775 |
| MR-027 | single_agent | 5 | proceed | proceed | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 2.422 |
| MR-028 | multi_agent_orchestration | 5 | proceed | proceed | 1.000 | 0.000 | 0.000 | 0.000 | 2.600 | 11.588 |
| MR-028 | single_agent | 5 | proceed | proceed | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 2.749 |
| MR-029 | multi_agent_orchestration | 5 | proceed | proceed | 1.000 | 0.000 | 0.000 | 0.000 | 2.400 | 9.096 |
| MR-029 | single_agent | 5 | proceed | proceed | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 2.348 |
| MR-030 | multi_agent_orchestration | 5 | proceed | proceed | 1.000 | 0.000 | 0.000 | 0.000 | 2.200 | 10.398 |
| MR-030 | single_agent | 5 | proceed | proceed | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 2.419 |
| MR-031 | multi_agent_orchestration | 5 | proceed | proceed | 1.000 | 0.000 | 0.000 | 0.000 | 3.200 | 11.099 |
| MR-031 | single_agent | 5 | proceed | proceed | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 2.911 |
| MR-032 | multi_agent_orchestration | 5 | reroute | proceed | 0.000 | 0.156 | 0.156 | 0.400 | 5.800 | 12.370 |
| MR-032 | single_agent | 5 | reroute | pause | 0.000 | 0.000 | 0.400 | 0.500 | 0.000 | 2.495 |
| MR-033 | multi_agent_orchestration | 5 | reroute | proceed | 0.000 | 0.000 | 0.000 | 0.000 | 4.400 | 11.694 |
| MR-033 | single_agent | 5 | reroute | proceed | 0.000 | 0.000 | 0.000 | 0.000 | 0.600 | 2.277 |
| MR-034 | multi_agent_orchestration | 5 | reroute | proceed | 0.400 | 0.244 | 0.244 | 0.500 | 1.200 | 12.253 |
| MR-034 | single_agent | 5 | reroute | reroute | 1.000 | 0.400 | 0.400 | 0.500 | 0.200 | 2.388 |
| MR-035 | multi_agent_orchestration | 5 | reroute | reroute | 1.000 | 0.000 | 0.274 | 0.500 | 3.200 | 11.537 |
| MR-035 | single_agent | 5 | reroute | reroute | 1.000 | 0.000 | 0.500 | 0.500 | 0.000 | 2.195 |
| MR-036 | multi_agent_orchestration | 5 | reroute | reroute | 1.000 | 0.000 | 0.000 | 0.000 | 5.200 | 12.531 |
| MR-036 | single_agent | 5 | reroute | reroute | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 2.181 |
| MR-037 | multi_agent_orchestration | 5 | reroute | proceed | 0.000 | 0.000 | 0.000 | 0.000 | 5.400 | 12.473 |
| MR-037 | single_agent | 5 | reroute | reroute | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 2.022 |
| MR-038 | multi_agent_orchestration | 5 | reroute | reroute | 1.000 | 0.279 | 0.279 | 0.600 | 1.200 | 13.487 |
| MR-038 | single_agent | 5 | reroute | reroute | 1.000 | 0.800 | 0.800 | 1.000 | 0.000 | 2.756 |
| MR-039 | multi_agent_orchestration | 5 | reroute | reroute | 1.000 | 0.000 | 0.000 | 0.000 | 4.400 | 11.353 |
| MR-039 | single_agent | 5 | reroute | reroute | 1.000 | 0.000 | 0.000 | 0.000 | 1.000 | 3.080 |
| MR-040 | multi_agent_orchestration | 5 | reroute | proceed | 0.200 | 0.000 | 0.228 | 0.500 | 4.800 | 10.940 |
| MR-040 | single_agent | 5 | reroute | pause | 0.000 | 0.400 | 0.400 | 0.500 | 0.000 | 1.901 |
| MR-041 | multi_agent_orchestration | 5 | reroute | proceed | 0.000 | 0.000 | 0.160 | 0.400 | 3.800 | 10.585 |
| MR-041 | single_agent | 5 | reroute | reroute | 0.800 | 0.000 | 0.000 | 0.000 | 0.800 | 2.164 |
| MR-042 | multi_agent_orchestration | 5 | reroute | reroute | 1.000 | 0.000 | 0.000 | 0.000 | 2.200 | 10.865 |
| MR-042 | single_agent | 5 | reroute | reroute | 1.000 | 0.000 | 0.000 | 0.000 | 0.400 | 2.095 |
| MR-043 | multi_agent_orchestration | 5 | reroute | reroute | 1.000 | 0.000 | 0.000 | 0.000 | 5.200 | 11.507 |
| MR-043 | single_agent | 5 | reroute | reroute | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 2.105 |
| MR-044 | multi_agent_orchestration | 5 | reroute | pause | 0.400 | 0.116 | 0.116 | 0.300 | 5.600 | 11.901 |
| MR-044 | single_agent | 5 | reroute | pause | 0.000 | 0.160 | 0.480 | 0.600 | 0.000 | 2.125 |
| MR-045 | multi_agent_orchestration | 5 | reroute | proceed | 0.000 | 0.000 | 0.084 | 0.200 | 3.800 | 13.065 |
| MR-045 | single_agent | 5 | reroute | proceed | 0.400 | 0.000 | 0.000 | 0.000 | 0.600 | 2.966 |
| MR-046 | multi_agent_orchestration | 5 | reroute | proceed | 0.400 | 0.050 | 0.233 | 0.500 | 2.400 | 12.124 |
| MR-046 | single_agent | 5 | reroute | reroute | 1.000 | 0.400 | 0.400 | 0.500 | 1.000 | 2.362 |
| MR-047 | multi_agent_orchestration | 5 | reroute | reroute | 1.000 | 0.000 | 0.309 | 0.500 | 2.200 | 10.361 |
| MR-047 | single_agent | 5 | reroute | reroute | 1.000 | 0.000 | 0.500 | 0.500 | 0.000 | 2.087 |
| MR-048 | multi_agent_orchestration | 5 | reroute | reroute | 1.000 | 0.000 | 0.044 | 0.067 | 2.800 | 10.223 |
| MR-048 | single_agent | 5 | reroute | reroute | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 1.956 |
| MR-049 | multi_agent_orchestration | 5 | reroute | proceed | 0.000 | 0.000 | 0.000 | 0.000 | 6.800 | 12.329 |
| MR-049 | single_agent | 5 | reroute | proceed | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 1.946 |
| MR-050 | multi_agent_orchestration | 5 | reroute | reroute | 1.000 | 0.373 | 0.373 | 0.900 | 1.000 | 11.835 |
| MR-050 | single_agent | 5 | reroute | reroute | 1.000 | 0.800 | 0.800 | 1.000 | 0.000 | 2.282 |
| MR-051 | multi_agent_orchestration | 5 | reroute | reroute | 1.000 | 0.000 | 0.000 | 0.000 | 3.200 | 11.307 |
| MR-051 | single_agent | 5 | reroute | reroute | 1.000 | 0.000 | 0.000 | 0.000 | 1.000 | 2.619 |
| MR-052 | multi_agent_orchestration | 5 | reroute | reroute | 0.600 | 0.000 | 0.113 | 0.300 | 5.600 | 25.110 |
| MR-052 | single_agent | 5 | reroute | pause | 0.000 | 0.400 | 0.400 | 0.500 | 0.000 | 2.002 |
| MR-053 | multi_agent_orchestration | 5 | reroute | proceed | 0.000 | 0.000 | 0.156 | 0.400 | 3.800 | 11.150 |
| MR-053 | single_agent | 5 | reroute | reroute | 1.000 | 0.000 | 0.000 | 0.000 | 1.000 | 1.846 |
| MR-054 | multi_agent_orchestration | 5 | reroute | reroute | 1.000 | 0.000 | 0.036 | 0.067 | 2.200 | 9.671 |
| MR-054 | single_agent | 5 | reroute | reroute | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 2.269 |
| MR-055 | multi_agent_orchestration | 5 | pause | pause | 1.000 | 0.000 | 0.500 | 1.000 | 1.000 | 10.098 |
| MR-055 | single_agent | 5 | pause | pause | 1.000 | 0.000 | 1.000 | 1.000 | 0.000 | 1.852 |
| MR-056 | multi_agent_orchestration | 5 | pause | pause | 1.000 | 0.000 | 0.050 | 0.100 | 4.600 | 11.892 |
| MR-056 | single_agent | 5 | pause | pause | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 1.740 |
| MR-057 | multi_agent_orchestration | 5 | pause | pause | 1.000 | 0.000 | 0.000 | 0.000 | 4.000 | 10.268 |
| MR-057 | single_agent | 5 | pause | pause | 1.000 | 0.000 | 0.000 | 0.000 | 1.000 | 2.447 |
| MR-058 | multi_agent_orchestration | 5 | pause | pause | 1.000 | 0.000 | 0.000 | 0.000 | 2.800 | 11.618 |
| MR-058 | single_agent | 5 | pause | pause | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 1.751 |
| MR-059 | multi_agent_orchestration | 5 | pause | pause | 1.000 | 0.000 | 0.000 | 0.000 | 2.600 | 12.627 |
| MR-059 | single_agent | 5 | pause | pause | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 2.022 |
| MR-060 | multi_agent_orchestration | 5 | pause | pause | 1.000 | 0.070 | 0.170 | 0.400 | 4.800 | 11.674 |
| MR-060 | single_agent | 5 | pause | pause | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 2.028 |
| MR-061 | multi_agent_orchestration | 5 | pause | pause | 1.000 | 0.000 | 0.324 | 1.000 | 3.200 | 9.432 |
| MR-061 | single_agent | 5 | pause | pause | 1.000 | 0.000 | 0.000 | 0.000 | 1.000 | 2.000 |
| MR-062 | multi_agent_orchestration | 5 | pause | pause | 1.000 | 0.250 | 0.410 | 0.600 | 1.400 | 11.307 |
| MR-062 | single_agent | 5 | pause | pause | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 3.336 |
| MR-063 | multi_agent_orchestration | 5 | pause | pause | 1.000 | 0.000 | 0.000 | 0.000 | 2.400 | 9.715 |
| MR-063 | single_agent | 5 | pause | pause | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 2.362 |
| MR-064 | multi_agent_orchestration | 5 | pause | pause | 1.000 | 0.000 | 0.000 | 0.000 | 5.600 | 11.374 |
| MR-064 | single_agent | 5 | pause | pause | 1.000 | 0.000 | 0.000 | 0.000 | 0.400 | 1.963 |
| MR-065 | multi_agent_orchestration | 5 | pause | pause | 1.000 | 0.000 | 0.000 | 0.000 | 4.400 | 11.215 |
| MR-065 | single_agent | 5 | pause | pause | 1.000 | 0.000 | 0.000 | 0.000 | 1.000 | 2.417 |
| MR-066 | multi_agent_orchestration | 5 | pause | pause | 1.000 | 0.000 | 0.000 | 0.000 | 2.000 | 12.913 |
| MR-066 | single_agent | 5 | pause | pause | 1.000 | 0.000 | 0.000 | 0.000 | 0.200 | 1.962 |
| MR-067 | multi_agent_orchestration | 5 | pause | pause | 1.000 | 0.000 | 0.440 | 1.000 | 2.200 | 10.864 |
| MR-067 | single_agent | 5 | pause | pause | 1.000 | 0.000 | 1.000 | 1.000 | 0.000 | 2.360 |
| MR-068 | multi_agent_orchestration | 5 | pause | pause | 1.000 | 0.000 | 0.000 | 0.000 | 3.800 | 11.127 |
| MR-068 | single_agent | 5 | pause | pause | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 1.959 |
| MR-069 | multi_agent_orchestration | 5 | pause | pause | 1.000 | 0.000 | 0.000 | 0.000 | 3.200 | 10.292 |
| MR-069 | single_agent | 5 | pause | pause | 1.000 | 0.000 | 0.000 | 0.000 | 1.000 | 2.933 |
| MR-070 | multi_agent_orchestration | 5 | pause | pause | 1.000 | 0.000 | 0.000 | 0.000 | 1.400 | 11.587 |
| MR-070 | single_agent | 5 | pause | pause | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 1.933 |
| MR-071 | multi_agent_orchestration | 5 | pause | pause | 1.000 | 0.000 | 0.000 | 0.000 | 2.600 | 9.826 |
| MR-071 | single_agent | 5 | pause | pause | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 1.983 |
| MR-072 | multi_agent_orchestration | 5 | pause | pause | 1.000 | 0.040 | 0.040 | 0.100 | 5.600 | 11.956 |
| MR-072 | single_agent | 5 | pause | pause | 1.000 | 0.000 | 0.000 | 0.000 | 0.200 | 2.394 |
| MR-073 | multi_agent_orchestration | 5 | pause | pause | 1.000 | 0.000 | 0.314 | 1.000 | 3.000 | 11.870 |
| MR-073 | single_agent | 5 | pause | pause | 1.000 | 0.000 | 0.000 | 0.000 | 1.000 | 2.134 |
| MR-074 | multi_agent_orchestration | 5 | pause | pause | 1.000 | 0.107 | 0.246 | 0.500 | 2.600 | 12.621 |
| MR-074 | single_agent | 5 | pause | pause | 1.000 | 0.000 | 0.400 | 0.400 | 0.000 | 2.041 |
| MR-075 | multi_agent_orchestration | 5 | pause | pause | 1.000 | 0.000 | 0.000 | 0.000 | 2.800 | 11.091 |
| MR-075 | single_agent | 5 | pause | pause | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 2.036 |
| MR-076 | multi_agent_orchestration | 5 | pause | pause | 1.000 | 0.000 | 0.000 | 0.000 | 5.800 | 12.097 |
| MR-076 | single_agent | 5 | pause | pause | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 1.909 |
| MR-077 | multi_agent_orchestration | 5 | pause | pause | 1.000 | 0.000 | 0.000 | 0.000 | 4.200 | 10.153 |
| MR-077 | single_agent | 5 | pause | pause | 1.000 | 0.000 | 0.000 | 0.000 | 1.000 | 2.062 |
| MR-078 | multi_agent_orchestration | 5 | request_human_review | pause | 0.000 | 0.167 | 0.333 | 0.667 | 1.800 | 12.533 |
| MR-078 | single_agent | 5 | request_human_review | pause | 0.200 | 0.286 | 0.286 | 0.333 | 0.000 | 2.028 |
| MR-079 | multi_agent_orchestration | 5 | request_human_review | request_human_review | 1.000 | 0.271 | 0.271 | 0.467 | 4.000 | 13.501 |
| MR-079 | single_agent | 5 | request_human_review | request_human_review | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 2.008 |
| MR-080 | multi_agent_orchestration | 5 | request_human_review | pause | 0.000 | 0.000 | 0.000 | 0.000 | 5.000 | 14.255 |
| MR-080 | single_agent | 5 | request_human_review | pause | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 2.106 |
| MR-081 | multi_agent_orchestration | 5 | request_human_review | pause | 0.200 | 0.149 | 0.335 | 0.600 | 4.000 | 14.382 |
| MR-081 | single_agent | 5 | request_human_review | request_human_review | 1.000 | 0.333 | 0.333 | 0.333 | 0.000 | 2.101 |
| MR-082 | multi_agent_orchestration | 5 | request_human_review | request_human_review | 0.800 | 0.000 | 0.000 | 0.000 | 2.000 | 12.542 |
| MR-082 | single_agent | 5 | request_human_review | request_human_review | 0.600 | 0.000 | 0.000 | 0.000 | 0.000 | 2.035 |
| MR-083 | multi_agent_orchestration | 5 | request_human_review | request_human_review | 0.600 | 0.000 | 0.192 | 0.333 | 4.600 | 12.269 |
| MR-083 | single_agent | 5 | request_human_review | request_human_review | 1.000 | 0.000 | 0.000 | 0.000 | 0.400 | 2.825 |
| MR-084 | multi_agent_orchestration | 5 | request_human_review | pause | 0.000 | 0.067 | 0.239 | 0.467 | 2.800 | 11.848 |
| MR-084 | single_agent | 5 | request_human_review | pause | 0.200 | 0.250 | 0.250 | 0.333 | 0.000 | 2.453 |
| MR-085 | multi_agent_orchestration | 5 | request_human_review | request_human_review | 1.000 | 0.120 | 0.120 | 0.200 | 3.200 | 14.995 |
| MR-085 | single_agent | 5 | request_human_review | request_human_review | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 2.255 |
| MR-086 | multi_agent_orchestration | 5 | request_human_review | request_human_review | 0.600 | 0.000 | 0.000 | 0.000 | 6.200 | 14.722 |
| MR-086 | single_agent | 5 | request_human_review | pause | 0.000 | 0.000 | 0.000 | 0.000 | 0.200 | 2.626 |
| MR-087 | multi_agent_orchestration | 5 | request_human_review | request_human_review | 1.000 | 0.140 | 0.312 | 0.600 | 5.600 | 13.494 |
| MR-087 | single_agent | 5 | request_human_review | request_human_review | 1.000 | 0.333 | 0.333 | 0.333 | 1.000 | 1.931 |
| MR-088 | multi_agent_orchestration | 5 | request_human_review | pause | 0.000 | 0.000 | 0.031 | 0.067 | 4.400 | 12.282 |
| MR-088 | single_agent | 5 | request_human_review | pause | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 2.258 |
| MR-089 | multi_agent_orchestration | 5 | request_human_review | pause | 0.400 | 0.000 | 0.157 | 0.266 | 3.200 | 14.814 |
| MR-089 | single_agent | 5 | request_human_review | request_human_review | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 2.105 |
| MR-090 | multi_agent_orchestration | 5 | request_human_review | pause | 0.000 | 0.167 | 0.334 | 0.667 | 2.400 | 14.005 |
| MR-090 | single_agent | 5 | request_human_review | pause | 0.200 | 0.286 | 0.286 | 0.333 | 0.000 | 2.247 |
| MR-091 | multi_agent_orchestration | 5 | request_human_review | request_human_review | 1.000 | 0.211 | 0.211 | 0.400 | 5.000 | 15.250 |
| MR-091 | single_agent | 5 | request_human_review | request_human_review | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 2.341 |
| MR-092 | multi_agent_orchestration | 5 | request_human_review | pause | 0.000 | 0.000 | 0.000 | 0.000 | 5.600 | 13.028 |
| MR-092 | single_agent | 5 | request_human_review | pause | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 1.944 |
| MR-093 | multi_agent_orchestration | 5 | request_human_review | request_human_review | 0.800 | 0.116 | 0.273 | 0.467 | 4.000 | 13.057 |
| MR-093 | single_agent | 5 | request_human_review | request_human_review | 1.000 | 0.333 | 0.333 | 0.333 | 0.000 | 1.932 |
| MR-094 | multi_agent_orchestration | 5 | request_human_review | pause | 0.200 | 0.000 | 0.000 | 0.000 | 2.200 | 11.520 |
| MR-094 | single_agent | 5 | request_human_review | pause | 0.200 | 0.286 | 0.286 | 0.333 | 0.000 | 1.822 |
| MR-095 | multi_agent_orchestration | 5 | request_human_review | request_human_review | 0.600 | 0.000 | 0.179 | 0.333 | 5.200 | 11.978 |
| MR-095 | single_agent | 5 | request_human_review | request_human_review | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 2.364 |
| MR-096 | multi_agent_orchestration | 5 | request_human_review | pause | 0.000 | 0.167 | 0.334 | 0.667 | 1.400 | 12.508 |
| MR-096 | single_agent | 5 | request_human_review | request_human_review | 0.600 | 0.250 | 0.250 | 0.333 | 0.000 | 2.780 |
| MR-097 | multi_agent_orchestration | 5 | request_human_review | request_human_review | 0.800 | 0.164 | 0.164 | 0.266 | 3.000 | 16.818 |
| MR-097 | single_agent | 5 | request_human_review | request_human_review | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 1.990 |
| MR-098 | multi_agent_orchestration | 5 | request_human_review | pause | 0.400 | 0.000 | 0.000 | 0.000 | 6.600 | 12.064 |
| MR-098 | single_agent | 5 | request_human_review | pause | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 2.180 |
| MR-099 | multi_agent_orchestration | 5 | request_human_review | request_human_review | 0.600 | 0.205 | 0.450 | 0.734 | 3.600 | 12.415 |
| MR-099 | single_agent | 5 | request_human_review | request_human_review | 1.000 | 0.400 | 0.400 | 0.333 | 0.000 | 1.906 |
| MR-100 | multi_agent_orchestration | 5 | request_human_review | pause | 0.000 | 0.000 | 0.000 | 0.000 | 5.800 | 12.150 |
| MR-100 | single_agent | 5 | request_human_review | pause | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 2.389 |

## Table 3. Incorrect decisions
| scenario_id | run_id | architecture_type | expected_action | recommended_action | semantic_hazard_f1 | latency_seconds | confidence_score |
| --- | --- | --- | --- | --- | --- | --- | --- |
| MR-002 | 1 | single_agent | reroute | pause | 0.286 | 2.248 | 0.850 |
| MR-002 | 1 | multi_agent_orchestration | reroute | pause | 0.000 | 13.896 | 0.850 |
| MR-004 | 1 | single_agent | request_human_review | pause | 0.000 | 2.259 | 0.850 |
| MR-004 | 1 | multi_agent_orchestration | request_human_review | proceed | 0.182 | 12.373 | 0.850 |
| MR-008 | 1 | multi_agent_orchestration | request_human_review | pause | 0.500 | 10.663 | 0.850 |
| MR-032 | 1 | single_agent | reroute | pause | 0.400 | 2.047 | 0.850 |
| MR-032 | 1 | multi_agent_orchestration | reroute | proceed | 0.200 | 10.021 | 0.850 |
| MR-033 | 1 | single_agent | reroute | proceed | 0.000 | 2.017 | 0.900 |
| MR-033 | 1 | multi_agent_orchestration | reroute | proceed | 0.000 | 14.150 | 0.850 |
| MR-034 | 1 | multi_agent_orchestration | reroute | proceed | 0.222 | 9.691 | 0.850 |
| MR-037 | 1 | multi_agent_orchestration | reroute | proceed | 0.000 | 12.873 | 0.850 |
| MR-040 | 1 | single_agent | reroute | pause | 0.400 | 2.094 | 0.850 |
| MR-041 | 1 | multi_agent_orchestration | reroute | proceed | 0.200 | 9.059 | 0.850 |
| MR-044 | 1 | single_agent | reroute | pause | 0.800 | 1.962 | 0.850 |
| MR-044 | 1 | multi_agent_orchestration | reroute | pause | 0.182 | 11.146 | 0.850 |
| MR-045 | 1 | single_agent | reroute | proceed | 0.000 | 2.050 | 0.900 |
| MR-045 | 1 | multi_agent_orchestration | reroute | proceed | 0.000 | 12.903 | 0.850 |
| MR-046 | 1 | multi_agent_orchestration | reroute | proceed | 0.250 | 11.779 | 0.850 |
| MR-049 | 1 | single_agent | reroute | proceed | 0.000 | 1.665 | 0.900 |
| MR-049 | 1 | multi_agent_orchestration | reroute | proceed | 0.000 | 11.609 | 0.850 |
| MR-052 | 1 | single_agent | reroute | pause | 0.400 | 2.002 | 0.850 |
| MR-053 | 1 | multi_agent_orchestration | reroute | proceed | 0.200 | 12.518 | 0.850 |
| MR-078 | 1 | single_agent | request_human_review | pause | 0.286 | 2.397 | 0.850 |
| MR-078 | 1 | multi_agent_orchestration | request_human_review | reroute | 0.333 | 12.159 | 0.850 |
| MR-080 | 1 | single_agent | request_human_review | pause | 0.000 | 2.637 | 0.850 |
| MR-080 | 1 | multi_agent_orchestration | request_human_review | pause | 0.000 | 21.795 | 0.850 |
| MR-084 | 1 | multi_agent_orchestration | request_human_review | pause | 0.333 | 12.222 | 0.850 |
| MR-086 | 1 | single_agent | request_human_review | pause | 0.000 | 2.689 | 0.850 |
| MR-086 | 1 | multi_agent_orchestration | request_human_review | reroute | 0.000 | 13.490 | 0.850 |
| MR-088 | 1 | single_agent | request_human_review | pause | 0.000 | 2.479 | 0.850 |
| MR-088 | 1 | multi_agent_orchestration | request_human_review | proceed | 0.000 | 11.339 | 0.800 |
| MR-089 | 1 | multi_agent_orchestration | request_human_review | pause | 0.222 | 10.988 | 0.850 |
| MR-090 | 1 | single_agent | request_human_review | pause | 0.286 | 1.935 | 0.850 |
| MR-090 | 1 | multi_agent_orchestration | request_human_review | pause | 0.364 | 15.472 | 0.850 |
| MR-092 | 1 | single_agent | request_human_review | pause | 0.000 | 1.911 | 0.850 |
| MR-092 | 1 | multi_agent_orchestration | request_human_review | pause | 0.000 | 14.853 | 0.850 |
| MR-093 | 1 | multi_agent_orchestration | request_human_review | pause | 0.182 | 14.288 | 0.850 |
| MR-094 | 1 | single_agent | request_human_review | pause | 0.286 | 1.992 | 0.850 |
| MR-094 | 1 | multi_agent_orchestration | request_human_review | pause | 0.000 | 10.750 | 0.850 |
| MR-096 | 1 | multi_agent_orchestration | request_human_review | pause | 0.333 | 12.469 | 0.850 |
| MR-098 | 1 | single_agent | request_human_review | pause | 0.000 | 1.862 | 0.850 |
| MR-100 | 1 | single_agent | request_human_review | pause | 0.000 | 2.097 | 0.850 |
| MR-100 | 1 | multi_agent_orchestration | request_human_review | pause | 0.000 | 11.161 | 0.850 |
| MR-002 | 2 | single_agent | reroute | pause | 0.286 | 1.527 | 0.850 |
| MR-002 | 2 | multi_agent_orchestration | reroute | pause | 0.000 | 13.837 | 0.850 |
| MR-004 | 2 | single_agent | request_human_review | pause | 0.000 | 3.567 | 0.850 |
| MR-004 | 2 | multi_agent_orchestration | request_human_review | pause | 0.000 | 13.416 | 0.850 |
| MR-005 | 2 | multi_agent_orchestration | reroute | proceed | 0.286 | 11.777 | 0.850 |
| MR-008 | 2 | multi_agent_orchestration | request_human_review | pause | 0.500 | 20.478 | 0.850 |
| MR-032 | 2 | single_agent | reroute | pause | 0.400 | 2.867 | 0.850 |
| MR-032 | 2 | multi_agent_orchestration | reroute | proceed | 0.000 | 14.128 | 0.850 |
| MR-033 | 2 | single_agent | reroute | proceed | 0.000 | 2.969 | 0.900 |
| MR-033 | 2 | multi_agent_orchestration | reroute | proceed | 0.000 | 13.007 | 0.850 |
| MR-034 | 2 | multi_agent_orchestration | reroute | proceed | 0.250 | 11.160 | 0.850 |
| MR-037 | 2 | multi_agent_orchestration | reroute | proceed | 0.000 | 14.597 | 0.880 |
| MR-040 | 2 | single_agent | reroute | pause | 0.400 | 1.945 | 0.850 |
| MR-040 | 2 | multi_agent_orchestration | reroute | proceed | 0.222 | 10.524 | 0.850 |
| MR-041 | 2 | multi_agent_orchestration | reroute | proceed | 0.200 | 11.983 | 0.850 |
| MR-044 | 2 | single_agent | reroute | pause | 0.400 | 2.431 | 0.850 |
| MR-045 | 2 | multi_agent_orchestration | reroute | proceed | 0.222 | 12.695 | 0.850 |
| MR-049 | 2 | single_agent | reroute | proceed | 0.000 | 2.411 | 0.850 |
| MR-049 | 2 | multi_agent_orchestration | reroute | proceed | 0.000 | 10.873 | 0.850 |
| MR-052 | 2 | single_agent | reroute | pause | 0.400 | 2.213 | 0.850 |
| MR-053 | 2 | multi_agent_orchestration | reroute | proceed | 0.200 | 10.456 | 0.850 |
| MR-078 | 2 | single_agent | request_human_review | pause | 0.286 | 2.054 | 0.850 |
| MR-078 | 2 | multi_agent_orchestration | request_human_review | pause | 0.333 | 11.743 | 0.850 |
| MR-080 | 2 | single_agent | request_human_review | pause | 0.000 | 1.839 | 0.850 |
| MR-080 | 2 | multi_agent_orchestration | request_human_review | pause | 0.000 | 13.206 | 0.850 |
| MR-081 | 2 | multi_agent_orchestration | request_human_review | pause | 0.400 | 14.173 | 0.850 |
| MR-082 | 2 | multi_agent_orchestration | request_human_review | pause | 0.000 | 17.724 | 0.850 |
| MR-083 | 2 | multi_agent_orchestration | request_human_review | pause | 0.222 | 9.518 | 0.850 |
| MR-084 | 2 | single_agent | request_human_review | pause | 0.250 | 2.459 | 0.850 |
| MR-084 | 2 | multi_agent_orchestration | request_human_review | pause | 0.182 | 10.946 | 0.850 |
| MR-086 | 2 | single_agent | request_human_review | pause | 0.000 | 2.463 | 0.850 |
| MR-086 | 2 | multi_agent_orchestration | request_human_review | pause | 0.000 | 13.714 | 0.850 |
| MR-088 | 2 | single_agent | request_human_review | pause | 0.000 | 1.814 | 0.850 |
| MR-088 | 2 | multi_agent_orchestration | request_human_review | proceed | 0.000 | 10.851 | 0.800 |
| MR-089 | 2 | multi_agent_orchestration | request_human_review | pause | 0.000 | 12.296 | 0.800 |
| MR-090 | 2 | single_agent | request_human_review | pause | 0.286 | 2.025 | 0.850 |
| MR-090 | 2 | multi_agent_orchestration | request_human_review | pause | 0.333 | 12.635 | 0.850 |
| MR-092 | 2 | single_agent | request_human_review | pause | 0.000 | 1.958 | 0.850 |
| MR-092 | 2 | multi_agent_orchestration | request_human_review | pause | 0.000 | 13.212 | 0.850 |
| MR-095 | 2 | multi_agent_orchestration | request_human_review | pause | 0.182 | 11.438 | 0.850 |
| MR-096 | 2 | multi_agent_orchestration | request_human_review | pause | 0.308 | 11.982 | 0.850 |
| MR-097 | 2 | multi_agent_orchestration | request_human_review | pause | 0.200 | 18.282 | 0.850 |
| MR-098 | 2 | single_agent | request_human_review | pause | 0.000 | 2.591 | 0.850 |
| MR-098 | 2 | multi_agent_orchestration | request_human_review | pause | 0.000 | 13.737 | 0.850 |
| MR-100 | 2 | single_agent | request_human_review | pause | 0.000 | 2.032 | 0.850 |
| MR-100 | 2 | multi_agent_orchestration | request_human_review | pause | 0.000 | 12.679 | 0.850 |
| MR-002 | 3 | single_agent | reroute | pause | 0.286 | 2.696 | 0.850 |
| MR-002 | 3 | multi_agent_orchestration | reroute | pause | 0.200 | 11.325 | 0.850 |
| MR-004 | 3 | single_agent | request_human_review | pause | 0.000 | 1.840 | 0.850 |
| MR-004 | 3 | multi_agent_orchestration | request_human_review | reroute | 0.167 | 17.215 | 0.850 |
| MR-005 | 3 | multi_agent_orchestration | reroute | proceed | 0.286 | 11.278 | 0.850 |
| MR-008 | 3 | single_agent | request_human_review | pause | 0.250 | 2.384 | 0.850 |
| MR-008 | 3 | multi_agent_orchestration | request_human_review | pause | 0.500 | 10.641 | 0.800 |
| MR-032 | 3 | single_agent | reroute | pause | 0.400 | 2.789 | 0.850 |
| MR-032 | 3 | multi_agent_orchestration | reroute | proceed | 0.200 | 14.175 | 0.850 |
| MR-033 | 3 | single_agent | reroute | proceed | 0.000 | 2.447 | 0.900 |
| MR-033 | 3 | multi_agent_orchestration | reroute | proceed | 0.000 | 10.996 | 0.850 |
| MR-037 | 3 | multi_agent_orchestration | reroute | proceed | 0.000 | 12.138 | 0.880 |
| MR-040 | 3 | single_agent | reroute | pause | 0.400 | 1.535 | 0.850 |
| MR-040 | 3 | multi_agent_orchestration | reroute | proceed | 0.222 | 10.242 | 0.850 |
| MR-041 | 3 | multi_agent_orchestration | reroute | proceed | 0.200 | 10.651 | 0.850 |
| MR-044 | 3 | single_agent | reroute | pause | 0.400 | 2.048 | 0.850 |
| MR-044 | 3 | multi_agent_orchestration | reroute | pause | 0.200 | 10.815 | 0.850 |
| MR-045 | 3 | single_agent | reroute | proceed | 0.000 | 2.291 | 0.900 |
| MR-045 | 3 | multi_agent_orchestration | reroute | proceed | 0.000 | 14.641 | 0.850 |
| MR-049 | 3 | single_agent | reroute | proceed | 0.000 | 1.652 | 0.850 |
| MR-049 | 3 | multi_agent_orchestration | reroute | proceed | 0.000 | 12.964 | 0.850 |
| MR-052 | 3 | single_agent | reroute | pause | 0.400 | 2.046 | 0.850 |
| MR-052 | 3 | multi_agent_orchestration | reroute | proceed | 0.000 | 12.488 | 0.850 |
| MR-053 | 3 | multi_agent_orchestration | reroute | proceed | 0.182 | 9.613 | 0.850 |
| MR-078 | 3 | multi_agent_orchestration | request_human_review | pause | 0.333 | 13.685 | 0.850 |
| MR-080 | 3 | single_agent | request_human_review | pause | 0.000 | 2.073 | 0.850 |
| MR-080 | 3 | multi_agent_orchestration | request_human_review | pause | 0.000 | 11.493 | 0.850 |
| MR-081 | 3 | multi_agent_orchestration | request_human_review | pause | 0.364 | 14.253 | 0.850 |
| MR-084 | 3 | single_agent | request_human_review | pause | 0.250 | 2.671 | 0.850 |
| MR-084 | 3 | multi_agent_orchestration | request_human_review | pause | 0.182 | 10.424 | 0.850 |
| MR-086 | 3 | single_agent | request_human_review | pause | 0.000 | 2.563 | 0.850 |
| MR-088 | 3 | single_agent | request_human_review | pause | 0.000 | 2.449 | 0.850 |
| MR-088 | 3 | multi_agent_orchestration | request_human_review | pause | 0.000 | 14.030 | 0.850 |
| MR-090 | 3 | single_agent | request_human_review | pause | 0.286 | 1.720 | 0.850 |
| MR-090 | 3 | multi_agent_orchestration | request_human_review | reroute | 0.308 | 11.677 | 0.850 |
| MR-092 | 3 | single_agent | request_human_review | pause | 0.000 | 1.921 | 0.850 |
| MR-092 | 3 | multi_agent_orchestration | request_human_review | pause | 0.000 | 11.187 | 0.850 |
| MR-094 | 3 | single_agent | request_human_review | pause | 0.286 | 1.843 | 0.850 |
| MR-094 | 3 | multi_agent_orchestration | request_human_review | pause | 0.000 | 11.566 | 0.850 |
| MR-096 | 3 | single_agent | request_human_review | pause | 0.250 | 3.172 | 0.850 |
| MR-096 | 3 | multi_agent_orchestration | request_human_review | pause | 0.364 | 12.700 | 0.850 |
| MR-098 | 3 | single_agent | request_human_review | pause | 0.000 | 1.739 | 0.850 |
| MR-100 | 3 | single_agent | request_human_review | pause | 0.000 | 3.434 | 0.850 |
| MR-100 | 3 | multi_agent_orchestration | request_human_review | pause | 0.000 | 12.081 | 0.850 |
| MR-002 | 4 | single_agent | reroute | pause | 0.286 | 1.694 | 0.850 |
| MR-002 | 4 | multi_agent_orchestration | reroute | pause | 0.000 | 19.091 | 0.850 |
| MR-004 | 4 | single_agent | request_human_review | pause | 0.000 | 3.178 | 0.850 |
| MR-005 | 4 | multi_agent_orchestration | reroute | proceed | 0.333 | 9.002 | 0.850 |
| MR-008 | 4 | multi_agent_orchestration | request_human_review | pause | 0.545 | 11.061 | 0.800 |
| MR-032 | 4 | single_agent | reroute | pause | 0.400 | 2.048 | 0.850 |
| MR-032 | 4 | multi_agent_orchestration | reroute | proceed | 0.182 | 10.978 | 0.850 |
| MR-033 | 4 | single_agent | reroute | proceed | 0.000 | 2.058 | 0.850 |
| MR-033 | 4 | multi_agent_orchestration | reroute | proceed | 0.000 | 10.430 | 0.850 |
| MR-037 | 4 | multi_agent_orchestration | reroute | proceed | 0.000 | 10.339 | 0.850 |
| MR-040 | 4 | single_agent | reroute | pause | 0.400 | 1.886 | 0.850 |
| MR-040 | 4 | multi_agent_orchestration | reroute | proceed | 0.222 | 11.193 | 0.850 |
| MR-041 | 4 | single_agent | reroute | proceed | 0.000 | 2.460 | 0.900 |
| MR-041 | 4 | multi_agent_orchestration | reroute | proceed | 0.000 | 12.326 | 0.850 |
| MR-044 | 4 | single_agent | reroute | pause | 0.400 | 1.929 | 0.850 |
| MR-044 | 4 | multi_agent_orchestration | reroute | pause | 0.000 | 11.027 | 0.850 |
| MR-045 | 4 | multi_agent_orchestration | reroute | proceed | 0.200 | 10.955 | 0.850 |
| MR-046 | 4 | multi_agent_orchestration | reroute | proceed | 0.250 | 10.786 | 0.850 |
| MR-049 | 4 | single_agent | reroute | proceed | 0.000 | 1.857 | 0.900 |
| MR-049 | 4 | multi_agent_orchestration | reroute | proceed | 0.000 | 13.809 | 0.850 |
| MR-052 | 4 | single_agent | reroute | pause | 0.400 | 2.045 | 0.850 |
| MR-052 | 4 | multi_agent_orchestration | reroute | pause | 0.000 | 12.284 | 0.850 |
| MR-053 | 4 | multi_agent_orchestration | reroute | proceed | 0.200 | 13.641 | 0.850 |
| MR-078 | 4 | single_agent | request_human_review | pause | 0.286 | 1.947 | 0.850 |
| MR-078 | 4 | multi_agent_orchestration | request_human_review | pause | 0.333 | 13.580 | 0.850 |
| MR-080 | 4 | single_agent | request_human_review | pause | 0.000 | 1.951 | 0.850 |
| MR-080 | 4 | multi_agent_orchestration | request_human_review | pause | 0.000 | 14.052 | 0.850 |
| MR-081 | 4 | multi_agent_orchestration | request_human_review | pause | 0.182 | 13.702 | 0.850 |
| MR-082 | 4 | single_agent | request_human_review | pause | 0.000 | 2.326 | 0.850 |
| MR-084 | 4 | single_agent | request_human_review | pause | 0.250 | 2.047 | 0.850 |
| MR-084 | 4 | multi_agent_orchestration | request_human_review | pause | 0.333 | 13.829 | 0.850 |
| MR-086 | 4 | single_agent | request_human_review | pause | 0.000 | 3.455 | 0.850 |
| MR-088 | 4 | single_agent | request_human_review | pause | 0.000 | 1.853 | 0.850 |
| MR-088 | 4 | multi_agent_orchestration | request_human_review | pause | 0.154 | 9.862 | 0.800 |
| MR-089 | 4 | multi_agent_orchestration | request_human_review | pause | 0.182 | 21.152 | 0.800 |
| MR-090 | 4 | single_agent | request_human_review | pause | 0.286 | 3.134 | 0.850 |
| MR-090 | 4 | multi_agent_orchestration | request_human_review | pause | 0.333 | 15.038 | 0.850 |
| MR-092 | 4 | single_agent | request_human_review | pause | 0.000 | 2.142 | 0.850 |
| MR-092 | 4 | multi_agent_orchestration | request_human_review | pause | 0.000 | 14.159 | 0.850 |
| MR-094 | 4 | single_agent | request_human_review | pause | 0.286 | 1.838 | 0.850 |
| MR-094 | 4 | multi_agent_orchestration | request_human_review | pause | 0.000 | 13.165 | 0.850 |
| MR-096 | 4 | multi_agent_orchestration | request_human_review | pause | 0.333 | 11.962 | 0.850 |
| MR-098 | 4 | single_agent | request_human_review | pause | 0.000 | 2.302 | 0.850 |
| MR-098 | 4 | multi_agent_orchestration | request_human_review | reroute | 0.000 | 10.582 | 0.850 |
| MR-099 | 4 | multi_agent_orchestration | request_human_review | pause | 0.444 | 11.635 | 0.850 |
| MR-100 | 4 | single_agent | request_human_review | pause | 0.000 | 2.413 | 0.850 |
| MR-100 | 4 | multi_agent_orchestration | request_human_review | pause | 0.000 | 12.231 | 0.850 |
| MR-002 | 5 | single_agent | reroute | pause | 0.286 | 2.483 | 0.850 |
| MR-002 | 5 | multi_agent_orchestration | reroute | pause | 0.000 | 12.803 | 0.850 |
| MR-004 | 5 | single_agent | request_human_review | pause | 0.000 | 2.361 | 0.850 |
| MR-004 | 5 | multi_agent_orchestration | request_human_review | proceed | 0.182 | 12.970 | 0.850 |
| MR-005 | 5 | multi_agent_orchestration | reroute | proceed | 0.286 | 10.489 | 0.850 |
| MR-008 | 5 | multi_agent_orchestration | request_human_review | pause | 0.545 | 13.703 | 0.850 |
| MR-032 | 5 | single_agent | reroute | pause | 0.400 | 2.723 | 0.850 |
| MR-032 | 5 | multi_agent_orchestration | reroute | proceed | 0.200 | 12.549 | 0.850 |
| MR-033 | 5 | single_agent | reroute | proceed | 0.000 | 1.892 | 0.900 |
| MR-033 | 5 | multi_agent_orchestration | reroute | proceed | 0.000 | 9.887 | 0.850 |
| MR-034 | 5 | multi_agent_orchestration | reroute | proceed | 0.250 | 10.824 | 0.850 |
| MR-037 | 5 | multi_agent_orchestration | reroute | proceed | 0.000 | 12.420 | 0.880 |
| MR-040 | 5 | single_agent | reroute | pause | 0.400 | 2.045 | 0.850 |
| MR-040 | 5 | multi_agent_orchestration | reroute | proceed | 0.222 | 11.477 | 0.850 |
| MR-041 | 5 | multi_agent_orchestration | reroute | proceed | 0.200 | 8.907 | 0.850 |
| MR-044 | 5 | single_agent | reroute | pause | 0.400 | 2.253 | 0.850 |
| MR-045 | 5 | single_agent | reroute | proceed | 0.000 | 1.947 | 0.900 |
| MR-045 | 5 | multi_agent_orchestration | reroute | proceed | 0.000 | 14.132 | 0.850 |
| MR-046 | 5 | multi_agent_orchestration | reroute | proceed | 0.222 | 12.393 | 0.850 |
| MR-049 | 5 | single_agent | reroute | proceed | 0.000 | 2.147 | 0.850 |
| MR-049 | 5 | multi_agent_orchestration | reroute | proceed | 0.000 | 12.391 | 0.850 |
| MR-052 | 5 | single_agent | reroute | pause | 0.400 | 1.705 | 0.850 |
| MR-053 | 5 | multi_agent_orchestration | reroute | proceed | 0.000 | 9.523 | 0.850 |
| MR-078 | 5 | single_agent | request_human_review | pause | 0.286 | 1.691 | 0.850 |
| MR-078 | 5 | multi_agent_orchestration | request_human_review | reroute | 0.333 | 11.496 | 0.850 |
| MR-080 | 5 | single_agent | request_human_review | pause | 0.000 | 2.029 | 0.850 |
| MR-080 | 5 | multi_agent_orchestration | request_human_review | pause | 0.000 | 10.731 | 0.850 |
| MR-081 | 5 | multi_agent_orchestration | request_human_review | pause | 0.364 | 13.381 | 0.850 |
| MR-082 | 5 | single_agent | request_human_review | pause | 0.000 | 1.786 | 0.850 |
| MR-083 | 5 | multi_agent_orchestration | request_human_review | pause | 0.200 | 16.590 | 0.850 |
| MR-084 | 5 | single_agent | request_human_review | pause | 0.250 | 2.359 | 0.850 |
| MR-084 | 5 | multi_agent_orchestration | request_human_review | pause | 0.167 | 11.820 | 0.850 |
| MR-086 | 5 | single_agent | request_human_review | pause | 0.000 | 1.962 | 0.850 |
| MR-088 | 5 | single_agent | request_human_review | pause | 0.000 | 2.696 | 0.850 |
| MR-088 | 5 | multi_agent_orchestration | request_human_review | pause | 0.000 | 15.328 | 0.850 |
| MR-090 | 5 | multi_agent_orchestration | request_human_review | pause | 0.333 | 15.204 | 0.850 |
| MR-092 | 5 | single_agent | request_human_review | pause | 0.000 | 1.787 | 0.850 |
| MR-092 | 5 | multi_agent_orchestration | request_human_review | pause | 0.000 | 11.728 | 0.850 |
| MR-094 | 5 | single_agent | request_human_review | pause | 0.286 | 1.486 | 0.850 |
| MR-094 | 5 | multi_agent_orchestration | request_human_review | pause | 0.000 | 11.004 | 0.850 |
| MR-095 | 5 | multi_agent_orchestration | request_human_review | pause | 0.167 | 10.805 | 0.850 |
| MR-096 | 5 | single_agent | request_human_review | pause | 0.250 | 2.349 | 0.850 |
| MR-096 | 5 | multi_agent_orchestration | request_human_review | pause | 0.333 | 13.425 | 0.850 |
| MR-098 | 5 | single_agent | request_human_review | pause | 0.000 | 2.404 | 0.850 |
| MR-098 | 5 | multi_agent_orchestration | request_human_review | pause | 0.000 | 13.392 | 0.850 |
| MR-099 | 5 | multi_agent_orchestration | request_human_review | pause | 0.600 | 13.514 | 0.850 |
| MR-100 | 5 | single_agent | request_human_review | pause | 0.000 | 1.970 | 0.850 |
| MR-100 | 5 | multi_agent_orchestration | request_human_review | pause | 0.000 | 12.598 | 0.850 |

## Table 4. Pairwise statistical comparisons
| architecture_a | architecture_b | metric | test_name | test_statistic_name | test_statistic_value | architecture_a_mean | architecture_b_mean | difference_b_minus_a | bootstrap_ci_low | bootstrap_ci_high | effect_size_name | effect_size | effect_size_ci_low | effect_size_ci_high | cohens_dz | cohens_dz_ci_low | cohens_dz_ci_high | exact_p_value | holm_adjusted_p_value | sign_test_p_value | favored_architecture |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| multi_agent_orchestration | single_agent | decision_correct | exact McNemar test | discordant_pairs | 66 | 0.734 | 0.810 | 0.076 | 0.044 | 0.108 | rank_biserial_correlation | 0.576 | 0.367 | 0.758 | 0.214 | 0.129 | 0.290 | 0.000 | 0.000 | 0.000 | single_agent |
| multi_agent_orchestration | single_agent | exact_hazard_f1 | exact paired sign test | positive_differences | 88 | 0.043 | 0.081 | 0.038 | 0.024 | 0.052 | rank_biserial_correlation | 0.397 | 0.227 | 0.554 | 0.235 | 0.161 | 0.302 | 0.000 | 0.000 | 0.000 | single_agent |
| multi_agent_orchestration | single_agent | semantic_hazard_f1 | exact paired sign test | positive_differences | 96 | 0.106 | 0.131 | 0.025 | 0.008 | 0.042 | rank_biserial_correlation | -0.040 | -0.173 | 0.103 | 0.126 | 0.040 | 0.205 | 0.621 | 0.621 | 0.621 | single_agent |
| multi_agent_orchestration | single_agent | canonical_hazard_coverage | exact paired sign test | positive_differences | 31 | 0.214 | 0.144 | -0.070 | -0.092 | -0.048 | rank_biserial_correlation | -0.554 | -0.691 | -0.413 | -0.281 | -0.360 | -0.204 | 0.000 | 0.000 | 0.000 | multi_agent_orchestration |
| multi_agent_orchestration | single_agent | plausible_noncanonical_hazard_count | exact paired sign test | positive_differences | 74 | 2.202 | 1.376 | -0.826 | -0.932 | -0.722 | rank_biserial_correlation | -0.604 | -0.686 | -0.524 | -0.665 | -0.762 | -0.580 | 0.000 | 0.000 | 0.000 | single_agent |
| multi_agent_orchestration | single_agent | spurious_hazard_count | exact paired sign test | positive_differences | 0 | 3.312 | 0.150 | -3.162 | -3.304 | -3.032 | rank_biserial_correlation | -1.000 | -1.000 | -1.000 | -2.031 | -2.149 | -1.924 | 0.000 | 0.000 | 0.000 | single_agent |
| multi_agent_orchestration | single_agent | hazard_false_positive_count | exact paired sign test | positive_differences | 1 | 5.514 | 1.526 | -3.988 | -4.120 | -3.860 | rank_biserial_correlation | -0.996 | -1.000 | -0.988 | -2.771 | -3.001 | -2.582 | 0.000 | 0.000 | 0.000 | single_agent |
| multi_agent_orchestration | single_agent | hazard_false_negative_count | exact paired sign test | positive_differences | 108 | 1.468 | 1.642 | 0.174 | 0.126 | 0.222 | rank_biserial_correlation | 0.554 | 0.412 | 0.691 | 0.313 | 0.232 | 0.394 | 0.000 | 0.000 | 0.000 | multi_agent_orchestration |
| multi_agent_orchestration | single_agent | latency_seconds | exact paired sign test | positive_differences | 0 | 11.833 | 2.320 | -9.513 | -9.896 | -9.212 | rank_biserial_correlation | -1.000 | -1.000 | -1.000 | -2.459 | -4.190 | -1.668 | 0.000 | 0.000 | 0.000 | single_agent |
| multi_agent_orchestration | single_agent | token_usage | exact paired sign test | positive_differences | 0 | 2273.060 | 457.938 | -1815.122 | -1828.488 | -1801.522 | rank_biserial_correlation | -1.000 | -1.000 | -1.000 | -11.757 | -12.447 | -11.180 | 0.000 | 0.000 | 0.000 | single_agent |
| multi_agent_orchestration | single_agent | confidence_score | exact paired sign test | positive_differences | 121 | 0.868 | 0.878 | 0.010 | 0.008 | 0.012 | rank_biserial_correlation | 0.862 | 0.771 | 0.942 | 0.429 | 0.339 | 0.524 | 0.000 | 0.000 | 0.000 | single_agent |

These tables are generated automatically from `outputs/results.json` and are intended for direct reuse in drafts, appendices, or supplementary materials.