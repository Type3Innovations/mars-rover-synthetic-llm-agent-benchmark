from __future__ import annotations

import csv
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1] / "src"))
from evaluator import save_summary_statistics  # noqa: E402

BOOL_FIELDS = {"decision_correct", "canonical_hazards_all_detected"}
FLOAT_FIELDS = {
    "hazard_match_score",
    "exact_hazard_precision",
    "exact_hazard_recall",
    "exact_hazard_f1",
    "semantic_hazard_precision",
    "semantic_hazard_recall",
    "semantic_hazard_f1",
    "hazard_false_positive_count",
    "hazard_false_negative_count",
    "canonical_hazard_coverage",
    "plausible_noncanonical_hazard_count",
    "spurious_hazard_count",
    "latency_seconds",
    "token_usage",
    "confidence_score",
}
INT_FIELDS = {"run_id"}


def parse_record(row: dict[str, str]) -> dict[str, object]:
    out: dict[str, object] = dict(row)
    for key in BOOL_FIELDS:
        if key in out:
            out[key] = str(out[key]).strip().lower() == "true"
    for key in INT_FIELDS:
        value = out.get(key)
        if value not in ("", None):
            out[key] = int(float(str(value)))
    for key in FLOAT_FIELDS:
        value = out.get(key)
        if value not in ("", None):
            out[key] = float(str(value))
    return out


def regenerate(run_dir: Path) -> None:
    results_path = run_dir / "results.csv"
    records = [parse_record(r) for r in csv.DictReader(results_path.open())]
    save_summary_statistics(records, run_dir)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        raise SystemExit("Usage: python scripts/regenerate_statistics_from_results.py <run_dir> [<run_dir> ...]")

    for arg in sys.argv[1:]:
        path = Path(arg)
        if not path.exists():
            raise SystemExit(f"Run directory not found: {path}")
        regenerate(path)
        print(f"Regenerated summaries for: {path}")
