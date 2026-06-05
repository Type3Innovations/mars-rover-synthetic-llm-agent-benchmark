from __future__ import annotations

import argparse
import csv
import json
import math
import random
from collections import defaultdict
from pathlib import Path
from typing import Any

SINGLE_ARCH = "single_agent"
MULTI_ARCH = "multi_agent_orchestration"

METRICS: list[tuple[str, tuple[str, ...]]] = [
    ("decision_correct", ("decision_correct",)),
    ("exact_hazard_f1", ("exact_hazard_f1",)),
    ("semantic_hazard_f1", ("semantic_hazard_f1",)),
    ("latency_seconds", ("latency_seconds",)),
    ("total_tokens", ("total_tokens", "token_usage")),
]


def _parse_bool(value: str) -> float:
    return 1.0 if str(value).strip().lower() == "true" else 0.0


def _safe_float(value: Any) -> float | None:
    if value in (None, ""):
        return None
    try:
        return float(value)
    except (TypeError, ValueError):
        return None


def _resolve_metric_value(row: dict[str, str], candidate_columns: tuple[str, ...]) -> float | None:
    for column in candidate_columns:
        if column not in row:
            continue
        if column == "decision_correct":
            return _parse_bool(row[column])
        value = _safe_float(row[column])
        if value is not None:
            return value
    return None


def _mean(values: list[float]) -> float:
    return sum(values) / len(values)


def _sample_sd(values: list[float]) -> float | None:
    if len(values) < 2:
        return None
    mean_value = _mean(values)
    variance = sum((value - mean_value) ** 2 for value in values) / (len(values) - 1)
    return math.sqrt(variance)


def _cohens_dz(differences: list[float]) -> float | None:
    sd = _sample_sd(differences)
    if sd is None or sd == 0:
        return None
    return _mean(differences) / sd


def _exact_two_sided_binomial_p_value(successes: int, trials: int) -> float | None:
    if trials <= 0:
        return None
    probability = 0.0
    for k in range(0, successes + 1):
        probability += math.comb(trials, k) * (0.5 ** trials)
    return min(1.0, 2.0 * probability)


def _paired_sign_test_p_value(differences: list[float]) -> float | None:
    positive = sum(1 for value in differences if value > 0)
    negative = sum(1 for value in differences if value < 0)
    return _exact_two_sided_binomial_p_value(min(positive, negative), positive + negative)


def _bootstrap_mean_difference_ci(
    differences: list[float],
    *,
    iterations: int = 5000,
    seed: int = 42,
) -> tuple[float, float]:
    rng = random.Random(seed)
    n = len(differences)
    samples: list[float] = []
    for _ in range(iterations):
        drawn = [differences[rng.randrange(n)] for _ in range(n)]
        samples.append(_mean(drawn))
    samples.sort()
    low_idx = int(0.025 * (iterations - 1))
    high_idx = int(0.975 * (iterations - 1))
    return round(samples[low_idx], 3), round(samples[high_idx], 3)


def _bootstrap_cohens_dz_ci(
    differences: list[float],
    *,
    iterations: int = 5000,
    seed: int = 42,
) -> tuple[float | None, float | None]:
    rng = random.Random(seed)
    n = len(differences)
    samples: list[float] = []

    for _ in range(iterations):
        drawn = [differences[rng.randrange(n)] for _ in range(n)]
        dz = _cohens_dz(drawn)
        if dz is not None and math.isfinite(dz):
            samples.append(dz)

    if not samples:
        return None, None

    samples.sort()
    low_idx = int(0.025 * (len(samples) - 1))
    high_idx = int(0.975 * (len(samples) - 1))
    return round(samples[low_idx], 3), round(samples[high_idx], 3)


def _round_or_none(value: float | None, decimals: int = 3) -> float | None:
    return None if value is None else round(value, decimals)


def _format_p_value(p_value: float | None) -> str:
    if p_value is None:
        return "NA"
    if p_value < 0.001:
        return "p < 0.001"
    return f"p = {p_value:.3f}"


def _holm_adjust(rows: list[dict[str, Any]]) -> None:
    indexed = [(i, row["p_value_numeric"]) for i, row in enumerate(rows) if row.get("p_value_numeric") is not None]
    if not indexed:
        return

    sorted_values = sorted(indexed, key=lambda x: x[1])
    m = len(sorted_values)
    running_max = 0.0
    adjusted: dict[int, float] = {}

    for rank, (idx, p_val) in enumerate(sorted_values, start=1):
        adj = min(1.0, (m - rank + 1) * float(p_val))
        running_max = max(running_max, adj)
        adjusted[idx] = running_max

    for idx, adj in adjusted.items():
        rows[idx]["holm_adjusted_p_value_numeric"] = adj
        rows[idx]["holm_adjusted_p_value"] = _format_p_value(adj)


def _aggregate_scenario_means(records: list[dict[str, str]]) -> dict[tuple[str, str, str], dict[str, float]]:
    # key: (model, architecture, scenario_id)
    bucket: dict[tuple[str, str, str], dict[str, list[float]]] = defaultdict(lambda: defaultdict(list))

    for row in records:
        model = row.get("model", "")
        architecture = row.get("architecture_type", "")
        scenario_id = row.get("scenario_id", "")
        key = (model, architecture, scenario_id)

        for metric_name, candidates in METRICS:
            value = _resolve_metric_value(row, candidates)
            if value is not None:
                bucket[key][metric_name].append(value)

    aggregated: dict[tuple[str, str, str], dict[str, float]] = {}
    for key, metric_lists in bucket.items():
        aggregated[key] = {metric: _mean(values) for metric, values in metric_lists.items() if values}
    return aggregated


def _read_results(run_dir: Path) -> list[dict[str, str]]:
    path = run_dir / "results.csv"
    with path.open("r", encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))


def run_scenario_level_analysis(run_dir: Path) -> list[dict[str, Any]]:
    records = _read_results(run_dir)
    scenario_means = _aggregate_scenario_means(records)

    models = sorted({key[0] for key in scenario_means.keys()})
    rows: list[dict[str, Any]] = []

    for model in models:
        single_by_scenario = {
            scenario: values
            for (m, arch, scenario), values in scenario_means.items()
            if m == model and arch == SINGLE_ARCH
        }
        multi_by_scenario = {
            scenario: values
            for (m, arch, scenario), values in scenario_means.items()
            if m == model and arch == MULTI_ARCH
        }

        paired_scenarios = sorted(set(single_by_scenario.keys()) & set(multi_by_scenario.keys()))

        for metric_name, _ in METRICS:
            single_values: list[float] = []
            multi_values: list[float] = []

            for scenario_id in paired_scenarios:
                single_metric = single_by_scenario[scenario_id].get(metric_name)
                multi_metric = multi_by_scenario[scenario_id].get(metric_name)
                if single_metric is None or multi_metric is None:
                    continue
                single_values.append(single_metric)
                multi_values.append(multi_metric)

            if not single_values:
                continue

            differences = [single - multi for single, multi in zip(single_values, multi_values)]
            mean_diff = _mean(differences)
            ci_low, ci_high = _bootstrap_mean_difference_ci(differences)
            dz = _cohens_dz(differences)
            dz_low, dz_high = _bootstrap_cohens_dz_ci(differences)
            p_val = _paired_sign_test_p_value(differences)

            row = {
                "model": model,
                "metric": metric_name,
                "paired_scenarios": len(single_values),
                "single_agent_scenario_mean": round(_mean(single_values), 3),
                "multi_agent_scenario_mean": round(_mean(multi_values), 3),
                "paired_mean_difference_single_minus_multi": round(mean_diff, 3),
                "paired_mean_difference_ci_low": ci_low,
                "paired_mean_difference_ci_high": ci_high,
                "cohens_dz": _round_or_none(dz, 3),
                "cohens_dz_ci_low": dz_low,
                "cohens_dz_ci_high": dz_high,
                "p_value_numeric": p_val,
                "p_value": _format_p_value(p_val),
                "holm_adjusted_p_value_numeric": None,
                "holm_adjusted_p_value": "NA",
                "test_name": "Exact paired sign test on scenario-level means",
                "notes": "Bootstrap CIs resample scenarios (paired units), not individual runs.",
            }
            rows.append(row)

    _holm_adjust(rows)
    return rows


def _write_csv(path: Path, rows: list[dict[str, Any]]) -> None:
    if not rows:
        return
    fieldnames = [
        "model",
        "metric",
        "paired_scenarios",
        "single_agent_scenario_mean",
        "multi_agent_scenario_mean",
        "paired_mean_difference_single_minus_multi",
        "paired_mean_difference_ci_low",
        "paired_mean_difference_ci_high",
        "cohens_dz",
        "cohens_dz_ci_low",
        "cohens_dz_ci_high",
        "p_value",
        "holm_adjusted_p_value",
        "p_value_numeric",
        "holm_adjusted_p_value_numeric",
        "test_name",
        "notes",
    ]

    with path.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def _write_json(path: Path, rows: list[dict[str, Any]]) -> None:
    with path.open("w", encoding="utf-8") as f:
        json.dump(rows, f, indent=2)


def _write_markdown(path: Path, rows: list[dict[str, Any]]) -> None:
    by_model: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for row in rows:
        by_model[row["model"]].append(row)

    lines: list[str] = [
        "# Scenario-level statistical tests",
        "",
        "Repeated runs were aggregated to scenario-level means (100 paired scenario units per model) before paired testing.",
        "Bootstrap confidence intervals resample scenarios, not individual runs.",
        "",
    ]

    for model, model_rows in sorted(by_model.items()):
        lines.append(f"## {model}")
        lines.append("")
        lines.append("| Metric | Single mean | Multi mean | Diff (single-multi) | 95% CI (diff) | Cohen's dz | 95% CI (dz) | p-value | Holm-adjusted |")
        lines.append("|---|---:|---:|---:|---|---:|---|---|---|")
        for row in model_rows:
            diff_ci = f"[{row['paired_mean_difference_ci_low']}, {row['paired_mean_difference_ci_high']}]"
            dz_ci = (
                f"[{row['cohens_dz_ci_low']}, {row['cohens_dz_ci_high']}]"
                if row["cohens_dz_ci_low"] is not None and row["cohens_dz_ci_high"] is not None
                else "NA"
            )
            lines.append(
                "| "
                + " | ".join(
                    [
                        str(row["metric"]),
                        str(row["single_agent_scenario_mean"]),
                        str(row["multi_agent_scenario_mean"]),
                        str(row["paired_mean_difference_single_minus_multi"]),
                        diff_ci,
                        str(row["cohens_dz"]) if row["cohens_dz"] is not None else "NA",
                        dz_ci,
                        str(row["p_value"]),
                        str(row["holm_adjusted_p_value"]),
                    ]
                )
                + " |"
            )
        lines.append("")

    path.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Generate scenario-level paired statistical tests from results.csv"
    )
    parser.add_argument(
        "run_dirs",
        nargs="+",
        help="One or more run directories that contain results.csv",
    )
    args = parser.parse_args()

    for run_dir_arg in args.run_dirs:
        run_dir = Path(run_dir_arg)
        if not run_dir.exists():
            raise SystemExit(f"Run directory not found: {run_dir}")

        rows = run_scenario_level_analysis(run_dir)

        _write_csv(run_dir / "scenario_level_statistical_tests.csv", rows)
        _write_json(run_dir / "scenario_level_statistical_tests.json", rows)
        _write_markdown(run_dir / "scenario_level_statistical_summary.md", rows)

        print(f"Wrote scenario-level outputs for: {run_dir}")


if __name__ == "__main__":
    main()
