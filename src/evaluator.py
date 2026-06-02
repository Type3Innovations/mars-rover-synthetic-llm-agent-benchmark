"""Evaluation helpers for the Mars rover benchmark."""

from __future__ import annotations

import csv
import json
import math
import random
from collections import Counter, defaultdict
from itertools import combinations
from pathlib import Path
from statistics import median
from typing import Any, Callable


def normalize_text(value: str) -> str:
    """Normalize labels for simple exact and set-based scoring."""

    return value.strip().lower().replace("_", " ")


def _deduplicate_preserving_order(values: list[str]) -> list[str]:
    """Deduplicate string values while preserving original order."""

    seen: set[str] = set()
    deduplicated: list[str] = []
    for value in values:
        normalized = normalize_text(value)
        if normalized in seen:
            continue
        seen.add(normalized)
        deduplicated.append(normalized)
    return deduplicated


def _match_hazards(
    expected: list[str],
    detected: list[str],
    matcher: Callable[[str, str], bool],
) -> tuple[int, int, int]:
    """Match expected and detected hazards with one-to-one assignment."""

    expected_items = _deduplicate_preserving_order(expected)
    unmatched_detected = _deduplicate_preserving_order(detected)
    true_positives = 0

    for expected_item in expected_items:
        for index, detected_item in enumerate(unmatched_detected):
            if matcher(expected_item, detected_item):
                true_positives += 1
                unmatched_detected.pop(index)
                break

    false_negatives = len(expected_items) - true_positives
    false_positives = len(unmatched_detected)
    return true_positives, false_positives, false_negatives


def _precision_recall_f1(
    *, true_positives: int, false_positives: int, false_negatives: int
) -> dict[str, float]:
    """Compute precision, recall, and F1 from confusion counts."""

    if true_positives == 0 and false_positives == 0 and false_negatives == 0:
        return {"precision": 1.0, "recall": 1.0, "f1": 1.0}

    precision_denominator = true_positives + false_positives
    recall_denominator = true_positives + false_negatives
    precision = (
        true_positives / precision_denominator if precision_denominator else 0.0
    )
    recall = true_positives / recall_denominator if recall_denominator else 0.0
    f1_denominator = precision + recall
    f1 = (2 * precision * recall / f1_denominator) if f1_denominator else 0.0
    return {
        "precision": round(precision, 3),
        "recall": round(recall, 3),
        "f1": round(f1, 3),
    }


def exact_hazard_metrics(expected: list[str], detected: list[str]) -> dict[str, float | int]:
    """Compute strict exact-match hazard metrics."""

    true_positives, false_positives, false_negatives = _match_hazards(
        expected,
        detected,
        lambda expected_item, detected_item: expected_item == detected_item,
    )
    metrics = _precision_recall_f1(
        true_positives=true_positives,
        false_positives=false_positives,
        false_negatives=false_negatives,
    )
    metrics.update(
        {
            "true_positives": true_positives,
            "false_positives": false_positives,
            "false_negatives": false_negatives,
        }
    )
    return metrics


def semantic_hazard_metrics(
    expected: list[str], detected: list[str]
) -> dict[str, float | int]:
    """Compute substring-tolerant hazard metrics for semantic overlap."""

    true_positives, false_positives, false_negatives = _match_hazards(
        expected,
        detected,
        lambda expected_item, detected_item: expected_item in detected_item
        or detected_item in expected_item,
    )
    metrics = _precision_recall_f1(
        true_positives=true_positives,
        false_positives=false_positives,
        false_negatives=false_negatives,
    )
    metrics.update(
        {
            "true_positives": true_positives,
            "false_positives": false_positives,
            "false_negatives": false_negatives,
        }
    )
    return metrics


def hazard_match_score(expected: list[str], detected: list[str]) -> float:
    """Backward-compatible semantic recall score for hazards."""

    return float(semantic_hazard_metrics(expected, detected)["recall"])


def build_evaluation_record(
    *,
    scenario: dict[str, Any],
    architecture_type: str,
    model_output: dict[str, Any],
    latency_seconds: float,
    token_usage: int | None,
    run_id: int,
    model_name: str,
) -> dict[str, Any]:
    """Create one benchmark result row for CSV and JSON outputs."""

    expected_action = scenario["expected_action"]
    recommended_action = model_output.get("recommended_action", "")
    expected_hazards = scenario.get("expected_hazards", [])
    detected_hazards = model_output.get("detected_hazards", [])

    exact_metrics = exact_hazard_metrics(expected_hazards, detected_hazards)
    semantic_metrics = semantic_hazard_metrics(expected_hazards, detected_hazards)

    return {
        "scenario_id": scenario["scenario_id"],
        "run_id": run_id,
        "architecture_type": architecture_type,
        "model": model_name,
        "expected_action": expected_action,
        "recommended_action": recommended_action,
        "decision_correct": expected_action == recommended_action,
        "expected_hazards": expected_hazards,
        "detected_hazards": detected_hazards,
        "hazard_match_score": semantic_metrics["recall"],
        "exact_hazard_precision": exact_metrics["precision"],
        "exact_hazard_recall": exact_metrics["recall"],
        "exact_hazard_f1": exact_metrics["f1"],
        "semantic_hazard_precision": semantic_metrics["precision"],
        "semantic_hazard_recall": semantic_metrics["recall"],
        "semantic_hazard_f1": semantic_metrics["f1"],
        "hazard_false_positive_count": semantic_metrics["false_positives"],
        "hazard_false_negative_count": semantic_metrics["false_negatives"],
        "latency_seconds": round(latency_seconds, 3),
        "token_usage": token_usage,
        "reasoning": model_output.get("reasoning", ""),
        "confidence_score": model_output.get("confidence_score", 0),
    }


def save_results(records: list[dict[str, Any]], output_dir: Path) -> None:
    """Write benchmark records to outputs/results.json and outputs/results.csv."""

    output_dir.mkdir(parents=True, exist_ok=True)
    json_path = output_dir / "results.json"
    csv_path = output_dir / "results.csv"

    with json_path.open("w", encoding="utf-8") as file:
        json.dump(records, file, indent=2)

    csv_fields = [
        "scenario_id",
        "run_id",
        "architecture_type",
        "model",
        "expected_action",
        "recommended_action",
        "decision_correct",
        "expected_hazards",
        "detected_hazards",
        "hazard_match_score",
        "exact_hazard_precision",
        "exact_hazard_recall",
        "exact_hazard_f1",
        "semantic_hazard_precision",
        "semantic_hazard_recall",
        "semantic_hazard_f1",
        "hazard_false_positive_count",
        "hazard_false_negative_count",
        "latency_seconds",
        "token_usage",
        "reasoning",
        "confidence_score",
    ]
    with csv_path.open("w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=csv_fields)
        writer.writeheader()
        for record in records:
            csv_record = record.copy()
            csv_record["expected_hazards"] = json.dumps(record["expected_hazards"])
            csv_record["detected_hazards"] = json.dumps(record["detected_hazards"])
            writer.writerow(csv_record)


def _safe_mean(values: list[float | int | None]) -> float | None:
    """Compute a rounded mean while ignoring null values."""

    filtered = [float(value) for value in values if value is not None]
    if not filtered:
        return None
    return round(sum(filtered) / len(filtered), 3)


def _safe_median(values: list[float | int | None]) -> float | None:
    """Compute a rounded median while ignoring null values."""

    filtered = [float(value) for value in values if value is not None]
    if not filtered:
        return None
    return round(median(filtered), 3)


def _most_common_action(records: list[dict[str, Any]]) -> str:
    """Return a deterministic modal recommendation for a group of records."""

    counts = Counter(record.get("recommended_action", "") for record in records)
    return sorted(counts.items(), key=lambda item: (-item[1], item[0]))[0][0]


def _prepare_record(record: dict[str, Any]) -> dict[str, Any]:
    """Backfill missing fields so legacy result files still analyze correctly."""

    normalized_record = record.copy()
    normalized_record.setdefault("run_id", 1)
    normalized_record.setdefault("model", "unknown")
    normalized_record.setdefault("expected_hazards", [])
    normalized_record.setdefault("detected_hazards", [])
    normalized_record.setdefault(
        "decision_correct",
        normalized_record.get("expected_action")
        == normalized_record.get("recommended_action"),
    )
    normalized_record.setdefault("confidence_score", 0.0)

    exact_metrics = exact_hazard_metrics(
        normalized_record["expected_hazards"],
        normalized_record["detected_hazards"],
    )
    semantic_metrics = semantic_hazard_metrics(
        normalized_record["expected_hazards"],
        normalized_record["detected_hazards"],
    )

    normalized_record.setdefault("hazard_match_score", semantic_metrics["recall"])
    normalized_record.setdefault("exact_hazard_precision", exact_metrics["precision"])
    normalized_record.setdefault("exact_hazard_recall", exact_metrics["recall"])
    normalized_record.setdefault("exact_hazard_f1", exact_metrics["f1"])
    normalized_record.setdefault(
        "semantic_hazard_precision", semantic_metrics["precision"]
    )
    normalized_record.setdefault("semantic_hazard_recall", semantic_metrics["recall"])
    normalized_record.setdefault("semantic_hazard_f1", semantic_metrics["f1"])
    normalized_record.setdefault(
        "hazard_false_positive_count", semantic_metrics["false_positives"]
    )
    normalized_record.setdefault(
        "hazard_false_negative_count", semantic_metrics["false_negatives"]
    )
    return normalized_record


def _prepare_records(records: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """Normalize all records for summary and statistical analysis."""

    return [_prepare_record(record) for record in records]


def summarize_by_architecture(records: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """Aggregate benchmark metrics at the architecture level."""

    records = _prepare_records(records)
    grouped: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for record in records:
        grouped[record["architecture_type"]].append(record)

    summary: list[dict[str, Any]] = []
    for architecture_type, architecture_records in sorted(grouped.items()):
        decision_accuracy = round(
            sum(record["decision_correct"] for record in architecture_records)
            / len(architecture_records),
            3,
        )
        summary.append(
            {
                "architecture_type": architecture_type,
                "model": architecture_records[0].get("model", "unknown"),
                "runs": len(
                    {record.get("run_id", 1) for record in architecture_records}
                ),
                "scenarios": len(
                    {record["scenario_id"] for record in architecture_records}
                ),
                "evaluations": len(architecture_records),
                "decision_accuracy": decision_accuracy,
                "mean_hazard_match_score": _safe_mean(
                    [record["hazard_match_score"] for record in architecture_records]
                ),
                "mean_exact_hazard_precision": _safe_mean(
                    [record["exact_hazard_precision"] for record in architecture_records]
                ),
                "mean_exact_hazard_recall": _safe_mean(
                    [record["exact_hazard_recall"] for record in architecture_records]
                ),
                "mean_exact_hazard_f1": _safe_mean(
                    [record["exact_hazard_f1"] for record in architecture_records]
                ),
                "mean_semantic_hazard_precision": _safe_mean(
                    [record["semantic_hazard_precision"] for record in architecture_records]
                ),
                "mean_semantic_hazard_recall": _safe_mean(
                    [record["semantic_hazard_recall"] for record in architecture_records]
                ),
                "mean_semantic_hazard_f1": _safe_mean(
                    [record["semantic_hazard_f1"] for record in architecture_records]
                ),
                "mean_hazard_false_positive_count": _safe_mean(
                    [record["hazard_false_positive_count"] for record in architecture_records]
                ),
                "mean_hazard_false_negative_count": _safe_mean(
                    [record["hazard_false_negative_count"] for record in architecture_records]
                ),
                "mean_latency_seconds": _safe_mean(
                    [record["latency_seconds"] for record in architecture_records]
                ),
                "median_latency_seconds": _safe_median(
                    [record["latency_seconds"] for record in architecture_records]
                ),
                "mean_token_usage": _safe_mean(
                    [record["token_usage"] for record in architecture_records]
                ),
                "total_token_usage": sum(
                    record["token_usage"] or 0 for record in architecture_records
                ),
                "mean_confidence_score": _safe_mean(
                    [record.get("confidence_score") for record in architecture_records]
                ),
            }
        )
    return summary


def summarize_by_scenario(records: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """Aggregate benchmark metrics at the scenario-by-architecture level."""

    records = _prepare_records(records)
    grouped: dict[tuple[str, str], list[dict[str, Any]]] = defaultdict(list)
    for record in records:
        key = (record["scenario_id"], record["architecture_type"])
        grouped[key].append(record)

    summary: list[dict[str, Any]] = []
    for (scenario_id, architecture_type), scenario_records in sorted(grouped.items()):
        decision_accuracy = round(
            sum(record["decision_correct"] for record in scenario_records)
            / len(scenario_records),
            3,
        )
        summary.append(
            {
                "scenario_id": scenario_id,
                "architecture_type": architecture_type,
                "runs": len(scenario_records),
                "expected_action": scenario_records[0].get("expected_action", ""),
                "modal_recommended_action": _most_common_action(scenario_records),
                "decision_accuracy": decision_accuracy,
                "mean_exact_hazard_f1": _safe_mean(
                    [record["exact_hazard_f1"] for record in scenario_records]
                ),
                "mean_semantic_hazard_f1": _safe_mean(
                    [record["semantic_hazard_f1"] for record in scenario_records]
                ),
                "mean_hazard_false_positive_count": _safe_mean(
                    [record["hazard_false_positive_count"] for record in scenario_records]
                ),
                "mean_hazard_false_negative_count": _safe_mean(
                    [record["hazard_false_negative_count"] for record in scenario_records]
                ),
                "mean_latency_seconds": _safe_mean(
                    [record["latency_seconds"] for record in scenario_records]
                ),
                "mean_token_usage": _safe_mean(
                    [record["token_usage"] for record in scenario_records]
                ),
                "mean_confidence_score": _safe_mean(
                    [record.get("confidence_score") for record in scenario_records]
                ),
            }
        )
    return summary


def decision_error_records(records: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """Return only records where the model's decision mismatched the gold label."""

    normalized_records: list[dict[str, Any]] = []
    for record in _prepare_records(records):
        if record["decision_correct"]:
            continue
        normalized_records.append(record)
    return normalized_records


def _write_csv_records(
    *, file_path: Path, fieldnames: list[str], records: list[dict[str, Any]]
) -> None:
    """Write a list of dictionaries to CSV with JSON serialization for lists."""

    with file_path.open("w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for record in records:
            csv_record = {
                key: json.dumps(value) if isinstance(value, list) else value
                for key, value in record.items()
            }
            writer.writerow(csv_record)


def _format_markdown_value(value: Any) -> str:
    """Format summary values for markdown tables."""

    if value is None:
        return "NA"
    if isinstance(value, float):
        return f"{value:.3f}"
    return str(value)


def _render_markdown_table(rows: list[dict[str, Any]], columns: list[str]) -> str:
    """Render a markdown table from dictionaries using selected columns."""

    if not rows:
        return "No rows available."

    header = "| " + " | ".join(columns) + " |"
    separator = "| " + " | ".join("---" for _ in columns) + " |"
    body = [
        "| "
        + " | ".join(_format_markdown_value(row.get(column)) for column in columns)
        + " |"
        for row in rows
    ]
    return "\n".join([header, separator, *body])


def _exact_two_sided_binomial_p_value(successes: int, trials: int) -> float | None:
    """Compute an exact two-sided binomial p-value for p=0.5."""

    if trials == 0:
        return None
    tail_probability = sum(
        math.comb(trials, index) for index in range(0, successes + 1)
    ) / (2**trials)
    return round(min(1.0, 2 * tail_probability), 6)


def _paired_sign_test(values_a: list[float], values_b: list[float]) -> dict[str, int | float | None]:
    """Run an exact paired sign test on non-tied paired observations."""

    positive_differences = 0
    negative_differences = 0
    ties = 0

    for value_a, value_b in zip(values_a, values_b):
        if value_b > value_a:
            positive_differences += 1
        elif value_b < value_a:
            negative_differences += 1
        else:
            ties += 1

    non_tied = positive_differences + negative_differences
    p_value = _exact_two_sided_binomial_p_value(
        min(positive_differences, negative_differences),
        non_tied,
    )
    return {
        "positive_differences": positive_differences,
        "negative_differences": negative_differences,
        "ties": ties,
        "p_value": p_value,
    }


def _mcnemar_exact_p_value(values_a: list[float], values_b: list[float]) -> dict[str, int | float | None]:
    """Compute exact McNemar statistics for paired binary outcomes."""

    a_correct_b_incorrect = 0
    b_correct_a_incorrect = 0

    for value_a, value_b in zip(values_a, values_b):
        if value_a == value_b:
            continue
        if value_a > value_b:
            a_correct_b_incorrect += 1
        else:
            b_correct_a_incorrect += 1

    discordant_pairs = a_correct_b_incorrect + b_correct_a_incorrect
    p_value = _exact_two_sided_binomial_p_value(
        min(a_correct_b_incorrect, b_correct_a_incorrect),
        discordant_pairs,
    )
    return {
        "a_correct_b_incorrect": a_correct_b_incorrect,
        "b_correct_a_incorrect": b_correct_a_incorrect,
        "discordant_pairs": discordant_pairs,
        "p_value": p_value,
    }


def _bootstrap_mean_difference(
    values_a: list[float],
    values_b: list[float],
    *,
    iterations: int = 2000,
    seed: int = 42,
) -> tuple[float, float]:
    """Bootstrap the mean paired difference `b - a` to form a confidence interval."""

    if not values_a or len(values_a) != len(values_b):
        return (float("nan"), float("nan"))

    differences = [value_b - value_a for value_a, value_b in zip(values_a, values_b)]
    generator = random.Random(seed)
    bootstrapped_means: list[float] = []
    for _ in range(iterations):
        sampled = [
            differences[generator.randrange(len(differences))]
            for _ in range(len(differences))
        ]
        bootstrapped_means.append(sum(sampled) / len(sampled))
    bootstrapped_means.sort()
    lower_index = int(0.025 * (iterations - 1))
    upper_index = int(0.975 * (iterations - 1))
    return (
        round(bootstrapped_means[lower_index], 3),
        round(bootstrapped_means[upper_index], 3),
    )


def _favored_architecture(
    *,
    architecture_a: str,
    architecture_b: str,
    difference_b_minus_a: float,
    higher_is_better: bool,
) -> str:
    """Determine which architecture is favored by a paired metric difference."""

    if difference_b_minus_a == 0:
        return "tie"
    if higher_is_better:
        return architecture_b if difference_b_minus_a > 0 else architecture_a
    return architecture_b if difference_b_minus_a < 0 else architecture_a


def significance_analysis(records: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """Run pairwise significance-style analyses across architectures."""

    records = _prepare_records(records)
    architecture_types = sorted({record["architecture_type"] for record in records})
    pair_index: dict[tuple[str, int, str], dict[str, dict[str, Any]]] = defaultdict(dict)
    for record in records:
        key = (
            record["scenario_id"],
            record.get("run_id", 1),
            record.get("model", "unknown"),
        )
        pair_index[key][record["architecture_type"]] = record

    metric_specs = [
        ("decision_correct", True),
        ("exact_hazard_f1", True),
        ("semantic_hazard_f1", True),
        ("hazard_false_positive_count", False),
        ("hazard_false_negative_count", False),
        ("latency_seconds", False),
        ("token_usage", False),
        ("confidence_score", True),
    ]

    results: list[dict[str, Any]] = []
    for architecture_a, architecture_b in combinations(architecture_types, 2):
        paired_records = [
            (entry[architecture_a], entry[architecture_b])
            for entry in pair_index.values()
            if architecture_a in entry and architecture_b in entry
        ]
        if not paired_records:
            continue

        for metric_name, higher_is_better in metric_specs:
            values_a = [float(record_a.get(metric_name) or 0.0) for record_a, _ in paired_records]
            values_b = [float(record_b.get(metric_name) or 0.0) for _, record_b in paired_records]
            mean_a = round(sum(values_a) / len(values_a), 3)
            mean_b = round(sum(values_b) / len(values_b), 3)
            difference_b_minus_a = round(mean_b - mean_a, 3)
            ci_lower, ci_upper = _bootstrap_mean_difference(values_a, values_b)
            sign_test = _paired_sign_test(values_a, values_b)

            result = {
                "architecture_a": architecture_a,
                "architecture_b": architecture_b,
                "metric": metric_name,
                "paired_observations": len(paired_records),
                "architecture_a_mean": mean_a,
                "architecture_b_mean": mean_b,
                "difference_b_minus_a": difference_b_minus_a,
                "bootstrap_ci_low": ci_lower,
                "bootstrap_ci_high": ci_upper,
                "sign_test_p_value": sign_test["p_value"],
                "positive_differences": sign_test["positive_differences"],
                "negative_differences": sign_test["negative_differences"],
                "ties": sign_test["ties"],
                "higher_is_better": higher_is_better,
                "favored_architecture": _favored_architecture(
                    architecture_a=architecture_a,
                    architecture_b=architecture_b,
                    difference_b_minus_a=difference_b_minus_a,
                    higher_is_better=higher_is_better,
                ),
            }

            if metric_name == "decision_correct":
                mcnemar = _mcnemar_exact_p_value(values_a, values_b)
                result.update(
                    {
                        "mcnemar_p_value": mcnemar["p_value"],
                        "a_correct_b_incorrect": mcnemar["a_correct_b_incorrect"],
                        "b_correct_a_incorrect": mcnemar["b_correct_a_incorrect"],
                        "discordant_pairs": mcnemar["discordant_pairs"],
                    }
                )

            results.append(result)
    return results


def _build_paper_tables_markdown(
    *,
    architecture_summary: list[dict[str, Any]],
    scenario_summary: list[dict[str, Any]],
    decision_errors: list[dict[str, Any]],
    significance_results: list[dict[str, Any]],
) -> str:
    """Create a markdown report with paper-ready benchmark tables."""

    aggregate_columns = [
        "architecture_type",
        "runs",
        "scenarios",
        "evaluations",
        "decision_accuracy",
        "mean_exact_hazard_f1",
        "mean_semantic_hazard_f1",
        "mean_hazard_false_positive_count",
        "mean_latency_seconds",
        "mean_token_usage",
    ]
    scenario_columns = [
        "scenario_id",
        "architecture_type",
        "runs",
        "expected_action",
        "modal_recommended_action",
        "decision_accuracy",
        "mean_exact_hazard_f1",
        "mean_semantic_hazard_f1",
        "mean_latency_seconds",
    ]
    error_columns = [
        "scenario_id",
        "run_id",
        "architecture_type",
        "expected_action",
        "recommended_action",
        "semantic_hazard_f1",
        "latency_seconds",
        "confidence_score",
    ]
    significance_columns = [
        "architecture_a",
        "architecture_b",
        "metric",
        "architecture_a_mean",
        "architecture_b_mean",
        "difference_b_minus_a",
        "bootstrap_ci_low",
        "bootstrap_ci_high",
        "sign_test_p_value",
        "favored_architecture",
    ]

    parts = [
        "# Paper-Ready Tables",
        "",
        "## Table 1. Aggregate architecture comparison",
        _render_markdown_table(architecture_summary, aggregate_columns),
        "",
        "## Table 2. Scenario-level performance by architecture",
        _render_markdown_table(scenario_summary, scenario_columns),
        "",
        "## Table 3. Incorrect decisions",
        _render_markdown_table(decision_errors, error_columns),
        "",
        "## Table 4. Pairwise statistical comparisons",
        _render_markdown_table(significance_results, significance_columns),
        "",
        "These tables are generated automatically from `outputs/results.json` and are intended for direct reuse in drafts, appendices, or supplementary materials.",
    ]
    return "\n".join(parts)


def save_summary_statistics(records: list[dict[str, Any]], output_dir: Path) -> None:
    """Write aggregate benchmark summaries for analysis and paper drafting."""

    output_dir.mkdir(parents=True, exist_ok=True)

    architecture_summary = summarize_by_architecture(records)
    scenario_summary = summarize_by_scenario(records)
    decision_errors = decision_error_records(records)
    significance_results = significance_analysis(records)

    summary_json = output_dir / "summary_statistics.json"
    architecture_csv = output_dir / "summary_by_architecture.csv"
    scenario_csv = output_dir / "summary_by_scenario.csv"
    errors_csv = output_dir / "decision_errors.csv"
    significance_json = output_dir / "significance_analysis.json"
    significance_csv = output_dir / "statistical_tests.csv"
    paper_tables_md = output_dir / "paper_tables.md"

    with summary_json.open("w", encoding="utf-8") as file:
        json.dump(
            {
                "architecture_summary": architecture_summary,
                "scenario_summary": scenario_summary,
                "decision_errors": decision_errors,
                "significance_analysis": significance_results,
            },
            file,
            indent=2,
        )

    with significance_json.open("w", encoding="utf-8") as file:
        json.dump(significance_results, file, indent=2)

    if architecture_summary:
        _write_csv_records(
            file_path=architecture_csv,
            fieldnames=list(architecture_summary[0].keys()),
            records=architecture_summary,
        )
    if scenario_summary:
        _write_csv_records(
            file_path=scenario_csv,
            fieldnames=list(scenario_summary[0].keys()),
            records=scenario_summary,
        )
    if decision_errors:
        _write_csv_records(
            file_path=errors_csv,
            fieldnames=list(decision_errors[0].keys()),
            records=decision_errors,
        )
    else:
        _write_csv_records(
            file_path=errors_csv,
            fieldnames=[
                "scenario_id",
                "run_id",
                "architecture_type",
                "expected_action",
                "recommended_action",
                "semantic_hazard_f1",
                "latency_seconds",
                "confidence_score",
            ],
            records=[],
        )

    if significance_results:
        _write_csv_records(
            file_path=significance_csv,
            fieldnames=list(significance_results[0].keys()),
            records=significance_results,
        )
    else:
        _write_csv_records(
            file_path=significance_csv,
            fieldnames=[
                "architecture_a",
                "architecture_b",
                "metric",
                "paired_observations",
                "architecture_a_mean",
                "architecture_b_mean",
                "difference_b_minus_a",
                "bootstrap_ci_low",
                "bootstrap_ci_high",
                "sign_test_p_value",
                "favored_architecture",
            ],
            records=[],
        )

    with paper_tables_md.open("w", encoding="utf-8") as file:
        file.write(
            _build_paper_tables_markdown(
                architecture_summary=architecture_summary,
                scenario_summary=scenario_summary,
                decision_errors=decision_errors,
                significance_results=significance_results,
            )
        )
