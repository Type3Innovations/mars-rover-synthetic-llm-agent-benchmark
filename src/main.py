"""Command-line entrypoint for the Mars rover benchmark."""

from __future__ import annotations

import argparse
import json
import time
from datetime import datetime
from pathlib import Path
from typing import Any, Callable

from agents import multi_agent_orchestration, single_agent
from evaluator import build_evaluation_record, save_results, save_summary_statistics
from openai_client import LLMResult, get_model_name


PROJECT_ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = PROJECT_ROOT / "data" / "mars_rover_scenarios.json"
OUTPUT_DIR = PROJECT_ROOT / "outputs"


def _sanitize_for_path(value: str) -> str:
    """Convert a free-form string into a filesystem-safe path segment."""

    safe_chars = []
    for char in value:
        if char.isalnum() or char in {"-", "_", "."}:
            safe_chars.append(char)
        else:
            safe_chars.append("-")
    return "".join(safe_chars).strip("-") or "run"


def load_scenarios(path: Path = DATA_PATH) -> list[dict[str, Any]]:
    """Load benchmark scenarios from JSON."""

    with path.open("r", encoding="utf-8") as file:
        return json.load(file)


def parse_args() -> argparse.Namespace:
    """Parse command-line arguments for repeatable benchmark runs."""

    parser = argparse.ArgumentParser(
        description="Run the Mars rover agent benchmark and export summary tables."
    )
    parser.add_argument(
        "--repeats",
        type=int,
        default=1,
        help="Number of repeated runs per scenario and architecture.",
    )
    parser.add_argument(
        "--scenario-limit",
        type=int,
        default=None,
        help="Optional limit on the number of scenarios to run for pilot tests.",
    )
    parser.add_argument(
        "--model",
        type=str,
        default=None,
        help="Override the model name from OPENAI_MODEL.",
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=None,
        help=(
            "Base output directory for benchmark artifacts. "
            "If --versioned-output is enabled, a run-specific subfolder is created here."
        ),
    )
    parser.add_argument(
        "--versioned-output",
        dest="versioned_output",
        action="store_true",
        default=True,
        help="Create a timestamped run subfolder containing model and repeat metadata.",
    )
    parser.add_argument(
        "--no-versioned-output",
        dest="versioned_output",
        action="store_false",
        help="Write directly into --output-dir (or outputs/) without creating a run subfolder.",
    )
    parser.add_argument(
        "--run-tag",
        type=str,
        default=None,
        help="Optional short tag appended to versioned run folder names (for notes like baseline or ablation).",
    )
    args = parser.parse_args()
    if args.repeats < 1:
        parser.error("--repeats must be at least 1")
    if args.scenario_limit is not None and args.scenario_limit < 1:
        parser.error("--scenario-limit must be at least 1 when provided")
    return args


def run_pipeline(
    *,
    scenario: dict[str, Any],
    architecture_type: str,
    pipeline: Callable[[dict[str, Any], str | None], LLMResult],
    model: str,
    run_id: int,
) -> dict[str, Any]:
    """Run one pipeline for one scenario and return an evaluation record."""

    start_time = time.perf_counter()
    result = pipeline(scenario, model)
    latency_seconds = time.perf_counter() - start_time
    return build_evaluation_record(
        scenario=scenario,
        architecture_type=architecture_type,
        model_output=result.data,
        latency_seconds=latency_seconds,
        token_usage=result.token_usage,
        run_id=run_id,
        model_name=model,
    )


def resolve_output_dir(args: argparse.Namespace, model: str) -> Path:
    """Resolve the final output path with optional per-run versioning."""

    base_dir = args.output_dir or OUTPUT_DIR
    if not args.versioned_output:
        return base_dir

    timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    model_slug = _sanitize_for_path(model)
    suffix = f"_{_sanitize_for_path(args.run_tag)}" if args.run_tag else ""
    run_folder = f"{timestamp}_{model_slug}_r{args.repeats}{suffix}"
    return base_dir / run_folder


def save_run_metadata(
    *,
    output_dir: Path,
    model: str,
    repeats: int,
    scenario_count: int,
    scenario_limit: int | None,
    versioned_output: bool,
    run_tag: str | None,
) -> None:
    """Write metadata to make run provenance explicit for publication workflows."""

    metadata = {
        "created_at_utc": datetime.utcnow().isoformat(timespec="seconds") + "Z",
        "model": model,
        "repeats": repeats,
        "scenario_count": scenario_count,
        "scenario_limit": scenario_limit,
        "versioned_output": versioned_output,
        "run_tag": run_tag,
    }
    metadata_path = output_dir / "run_metadata.json"
    metadata_path.write_text(json.dumps(metadata, indent=2) + "\n", encoding="utf-8")


def main() -> None:
    """Run both benchmark architectures across all scenarios."""

    args = parse_args()
    scenarios = load_scenarios()
    if args.scenario_limit is not None:
        scenarios = scenarios[: args.scenario_limit]

    model = args.model or get_model_name()
    output_dir = resolve_output_dir(args, model)
    records: list[dict[str, Any]] = []

    print(f"Running Mars rover benchmark with model: {model}")
    print(f"Loaded {len(scenarios)} scenarios")
    print(f"Repeats per condition: {args.repeats}")
    print(f"Writing outputs to: {output_dir}")

    for run_id in range(1, args.repeats + 1):
        print(f"Starting repeat {run_id}/{args.repeats}")
        for scenario in scenarios:
            scenario_id = scenario["scenario_id"]
            print(f"Evaluating {scenario_id} with single-agent pipeline (run {run_id})")
            records.append(
                run_pipeline(
                    scenario=scenario,
                    architecture_type="single_agent",
                    pipeline=single_agent,
                    model=model,
                    run_id=run_id,
                )
            )

            print(
                "Evaluating "
                f"{scenario_id} with multi-agent orchestration pipeline (run {run_id})"
            )
            records.append(
                run_pipeline(
                    scenario=scenario,
                    architecture_type="multi_agent_orchestration",
                    pipeline=multi_agent_orchestration,
                    model=model,
                    run_id=run_id,
                )
            )

    save_results(records, output_dir)
    save_summary_statistics(records, output_dir)
    save_run_metadata(
        output_dir=output_dir,
        model=model,
        repeats=args.repeats,
        scenario_count=len(scenarios),
        scenario_limit=args.scenario_limit,
        versioned_output=args.versioned_output,
        run_tag=args.run_tag,
    )
    print(f"Saved {len(records)} records to {output_dir / 'results.csv'}")
    print(f"Saved {len(records)} records to {output_dir / 'results.json'}")
    print(
        "Saved summary artifacts to "
        f"{output_dir / 'summary_statistics.json'}, "
        f"{output_dir / 'summary_by_architecture.csv'}, "
        f"{output_dir / 'summary_by_scenario.csv'}, "
        f"{output_dir / 'decision_errors.csv'}, "
        f"{output_dir / 'statistical_tests.csv'}, and "
        f"{output_dir / 'paper_tables.md'}"
    )
    print(f"Saved run metadata to {output_dir / 'run_metadata.json'}")


if __name__ == "__main__":
    main()
