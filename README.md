# Single-Agent Versus Multi-Agent Orchestration for Simulated Mars Rover Decision Support

This repository contains a small reproducible Python benchmark for comparing a single generalized LLM agent against a coordinated multi-agent orchestration architecture on simulated Mars rover mission scenarios.

The repository now includes a deterministic synthetic dataset of 100 labeled rover scenarios for publication-oriented experiments.

Research question:

> Does multi-agent orchestration improve decision quality and risk detection compared with a single-agent architecture in simulated Mars rover mission scenarios?

## Project Structure

```text
.
├── data/
│   └── mars_rover_scenarios.json
├── docs/
│   └── publication_study_plan.md
├── outputs/
│   └── .gitkeep
├── scripts/
│   └── generate_mars_rover_scenarios.py
├── src/
│   ├── agents.py
│   ├── evaluator.py
│   ├── main.py
│   └── openai_client.py
├── .env.example
├── README.md
└── requirements.txt
```

## Setup

Create a virtual environment and install dependencies:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Create a `.env` file:

```bash
cp .env.example .env
```

Then edit `.env`:

```bash
OPENAI_API_KEY=your_api_key_here
OPENAI_MODEL=gpt-4o-mini
```

`OPENAI_MODEL` is optional. If omitted, the project defaults to `gpt-4o-mini`.

## Run

```bash
python src/main.py
```

Run repeated evaluations for a publication-style benchmark:

```bash
python src/main.py --repeats 5
```

By default, each run now writes to a unique timestamped subfolder under `outputs/` (including model and repeat count in the folder name) so results are never overwritten.

Example with a different model:

```bash
python src/main.py --model gpt-5.5 --repeats 5
```

Example with a custom label for the run folder:

```bash
python src/main.py --model gpt-5.5 --repeats 5 --run-tag camera-ready
```

Run a smaller pilot benchmark on the first 3 scenarios:

```bash
python src/main.py --repeats 3 --scenario-limit 3
```

Regenerate the 100-scenario dataset:

```bash
python scripts/generate_mars_rover_scenarios.py
```

The benchmark writes:

- `outputs/results.csv`
- `outputs/results.json`
- `outputs/summary_statistics.json`
- `outputs/summary_by_architecture.csv`
- `outputs/summary_by_scenario.csv`
- `outputs/decision_errors.csv`
- `outputs/significance_analysis.json`
- `outputs/statistical_tests.csv`
- `outputs/paper_tables.md`

For versioned runs, these files are written into a run-specific folder under `outputs/` and include:

- `run_metadata.json` (model, repeats, scenario count, timestamp, and run tag)

## Benchmark Design

Pipeline A, `single_agent`, sends the full scenario to one LLM call and asks for:

- `recommended_action`
- `risk_level`
- `detected_hazards`
- `reasoning`
- `confidence_score`

Pipeline B, `multi_agent_orchestration`, runs four specialist agents:

- `telemetry_agent`
- `terrain_agent`
- `risk_agent`
- `mission_planner_agent`

An `orchestrator_agent` then combines their outputs into the same final decision format used by the single-agent pipeline.

## Evaluation Fields

Each pipeline run logs:

- `scenario_id`
- `run_id`
- `architecture_type`
- `model`
- `expected_action`
- `recommended_action`
- `decision_correct`
- `expected_hazards`
- `detected_hazards`
- `hazard_match_score`
- `exact_hazard_precision`
- `exact_hazard_recall`
- `exact_hazard_f1`
- `semantic_hazard_precision`
- `semantic_hazard_recall`
- `semantic_hazard_f1`
- `hazard_false_positive_count`
- `hazard_false_negative_count`
- `latency_seconds`
- `token_usage`
- `reasoning`
- `confidence_score`

`hazard_match_score` remains as a backward-compatible semantic recall metric. The benchmark now also reports stricter exact-match and semantic precision/recall/F1 hazard metrics, plus false-positive and false-negative counts for over-detection analysis.

## Publication Workflow

- Use repeated runs (`--repeats N`) to measure consistency and operational variance.
- Use `outputs/summary_by_architecture.csv` for aggregate results tables.
- Use `outputs/summary_by_scenario.csv` to report scenario-level comparisons.
- Use `outputs/decision_errors.csv` for qualitative error analysis.
- Use `outputs/statistical_tests.csv` and `outputs/significance_analysis.json` for paired significance analysis.
- Use `outputs/paper_tables.md` as a draft-ready appendix or manuscript table source.
- See `docs/publication_study_plan.md` for a publication-grade experiment plan.

Tip: if you need legacy behavior and want to overwrite a fixed folder, pass `--no-versioned-output --output-dir outputs`.

## Statistical Analysis

- Pairwise comparisons are computed across matched `(scenario_id, run_id, model)` observations.
- Decision correctness includes an exact McNemar test summary.
- Continuous and score-based metrics include paired sign tests and bootstrap confidence intervals for mean differences.

## Notes for Future Extensions

- Add human or expert annotation validation for a subset of scenarios.
- Add stricter semantic hazard matching beyond substring overlap.
- Add a Streamlit UI for browsing scenario-level outputs.
- Compare multiple model backends under the same benchmark harness.
# Mars_Synthetic_Dataset_SingleVsMulti
