# Publication-Grade Study Plan

## Study Objective

Evaluate whether multi-agent orchestration improves Mars rover decision support compared with a single-agent baseline under simulated mission scenarios, while accounting for decision accuracy, hazard detection quality, latency, cost, and run-to-run consistency.

## Core Research Questions

1. Does multi-agent orchestration improve action-selection accuracy relative to a single-agent baseline?
2. Does multi-agent orchestration improve hazard detection coverage or semantic quality?
3. What latency and token-cost tradeoffs are introduced by multi-agent decomposition?
4. How stable are the architectures across repeated runs and model backends?

## Recommended Hypotheses

- `H1`: Multi-agent orchestration improves hazard detection quality on complex scenarios.
- `H2`: Multi-agent orchestration incurs higher latency and token cost than the single-agent baseline.
- `H3`: Single-agent performance is more efficient, but multi-agent reasoning is more informative on ambiguous, high-risk scenarios.

## Experimental Design

## Agent Prompt Guide

The model-facing prompts are intentionally limited to operational scenario details. The scoring-only fields `expected_action` and `expected_hazards` are excluded from all prompts and are used only by the evaluator after the model returns a recommendation.

Plain-language summary of each agent prompt:

- `single_agent`: Review the complete mission situation, weigh rover safety against mission progress, and choose one final action.
- `telemetry_agent`: Focus on rover health signals such as battery, wheel temperature, radiation, and communications delays to identify health-related risks.
- `terrain_agent`: Focus on terrain slope, terrain description, and mission context to identify mobility, traction, obstacle, and wheel-damage risks.
- `risk_agent`: Combine the main operational signals into one overall safety assessment and highlight the highest-priority hazards.
- `mission_planner_agent`: Consider the science objective, timing, battery state, and communications delay to judge whether the mission should continue or pause.
- `orchestrator_agent`: Read the specialist summaries, resolve disagreements, and produce the safest final recommendation.

This keeps the benchmark interpretable for reviewers while preventing label leakage into the model input.

## Conditions

- `single_agent`
- `multi_agent_orchestration`

## Recommended Dataset Scope

- Minimum for a serious submission: 100 scenarios.
- Stronger target: 150 to 250 scenarios.
- Balance easy, medium, and hard cases.
- Include multiple hazard families: terrain, thermal, communications, battery, radiation, uncertainty, and multi-hazard combinations.

## Labeling Protocol

- Define `expected_action` using a documented rubric.
- Define `expected_hazards` from the same rubric.
- If possible, use two independent annotators and resolve disagreements with adjudication.
- Report inter-annotator agreement if multiple human labelers are used.

## Repetition Strategy

- Run each scenario under each architecture at least 3 to 5 times.
- Record `run_id`, model name, and timestamped outputs.
- If multiple models are used, repeat the full benchmark for each model.

## Metrics to Report

## Primary Metrics

- Decision accuracy
- Hazard recall
- Hazard precision or over-detection rate
- Hazard F1 or semantic overlap metric
- Inclusion-based canonical hazard coverage (coverage not penalized by additional detected hazards)
- Spurious hazard count separated from plausible non-canonical hazard observations

## Efficiency Metrics

- Mean latency
- Median latency
- Mean token usage
- Total token usage

## Reliability Metrics

- Run-to-run agreement rate
- Per-scenario variance in action selection
- Failure rate due to API or schema errors

## Statistical Analysis Plan

- Report means with confidence intervals.
- Use paired comparisons by scenario.
- For binary decision correctness, report an exact McNemar test with an exact p-value.
- For other paired metrics, report an exact paired sign test, a rank-biserial effect size, Cohen's $d_z$, and bootstrap confidence intervals.
- Apply Holm-Bonferroni correction across the family of pairwise metric tests.
- For latency and token usage, keep paired confidence intervals and explicitly state that repeats are not independent samples.
- Pre-register the primary endpoint if the work is intended for a formal empirical venue.

## Reproducibility Notes

- Record the exact model name, repeat count, run tag, timestamp, Python version, git commit, and sampling settings for every run.
- Keep the full prompt guide and scenario-field map alongside the code so reviewers can verify that `expected_action` and `expected_hazards` are never passed to the model.

## Recommended Result Tables

1. Aggregate performance by architecture.
2. Per-scenario summary by architecture.
3. Incorrect-decision cases for qualitative analysis.
4. Cost-latency tradeoff table.
5. Ablation table removing one specialist at a time.

## Error Analysis

Include a qualitative section that categorizes failures such as:

- Overly conservative decisions
- Missed hazards
- Hallucinated hazards
- Planner-specialist disagreement
- Ambiguous-label cases

Also include directional transition counts (for example `expected reroute -> recommended proceed` vs `expected reroute -> recommended pause`) to test conservative-vs-risk-tolerant error hypotheses explicitly.

## Ablation and Robustness Studies

- Remove one specialist agent at a time.
- Compare different orchestrator prompts.
- Compare at least two model backends if budget allows.
- Evaluate sensitivity to scenario difficulty and hazard count.

## Threats to Validity

- Small synthetic datasets may not reflect real operations.
- Gold labels may encode one policy choice rather than an absolute truth.
- Exact-match action scoring may under-credit reasonable alternatives.
- Hazard string matching may under- or over-estimate semantic correctness.

## Minimum Recommended Execution Plan

1. Expand the scenario set to at least 100 cases.
2. Run `python src/main.py --repeats 5`.
3. Export aggregate and scenario-level tables from `outputs/`.
4. Review `decision_errors.csv` for qualitative coding.
5. Add stricter hazard metrics and an ablation study before submission.

## Current Repository Support

This repository now supports repeated runs, aggregate summaries, and manuscript-ready markdown tables. The next highest-value additions are larger scenario coverage, stronger hazard metrics, and statistical significance analysis.