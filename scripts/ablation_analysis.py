"""
Ablation Analysis Script
Compares all 4 ablation conditions against the gpt-4o r5 baseline.
Covers: accuracy drop, hazard quality, canonical coverage, error-mode shifts,
        efficiency (latency/tokens), confidence, and agent contribution ranking.

Output files (in outputs/ablation_analysis/):
  - ablation_comparison.csv          — consolidated metrics for all conditions
  - ablation_per_scenario_delta.csv  — per-scenario accuracy deltas
  - agent_contribution_ranking.csv   — ranked importance of each specialist
  - ablation_error_mode_shift.csv    — error category counts per condition
  - ablation_summary.json            — machine-readable summary
"""

import csv
import json
import math
import statistics
from pathlib import Path

BASELINE_DIR = Path("outputs/20260602-153013_gpt-4o_r5")
ABLATION_DIRS = {
    "drop_telemetry": Path("outputs/20260603-091702_gpt-4o_r5_drop_telemetry"),
    "drop_terrain": Path("outputs/20260603-104151_gpt-4o_r5_drop_terrain"),
    "drop_risk": Path("outputs/20260603-125453_gpt-4o_r5_drop_risk"),
    "drop_mission_planner": Path("outputs/20260603-140945_gpt-4o_r5_drop_mission_planner"),
}
DROPPED_AGENT = {
    "drop_telemetry": "telemetry_agent",
    "drop_terrain": "terrain_agent",
    "drop_risk": "risk_agent",
    "drop_mission_planner": "mission_planner_agent",
}
MULTI_ARCH = "multi_agent_orchestration"
OUT = Path("outputs/ablation_analysis")
OUT.mkdir(exist_ok=True)


# ── helpers ───────────────────────────────────────────────────────────────────

def load_results(p: Path):
    return list(csv.DictReader((p / "results.csv").open()))


def float_col(rows, col):
    return [float(r[col]) for r in rows if r.get(col) not in ("", None)]


def pct(v):
    return round(v * 100, 2)


def fmt(v, digits=4):
    if v != v:  # NaN check
        return None
    return round(v, digits)


def safe_int(v):
    if v != v or v is None:
        return None
    return int(round(v))


def mean(lst):
    return statistics.mean(lst) if lst else float("nan")


def _exact_two_sided_binomial_p_value(successes: int, trials: int):
    """Compute an exact two-sided binomial p-value for p=0.5."""
    if trials == 0:
        return 1.0
    tail_probability = sum(
        math.comb(trials, index) for index in range(0, successes + 1)
    ) / (2**trials)
    return min(1.0, 2 * tail_probability)


def exact_mcnemar_from_rows(rows_a, rows_b):
    """Exact McNemar statistics for paired decision correctness.

    rows_a and rows_b are paired by (scenario_id, run_id) for MULTI_ARCH rows.
    """
    index_a = {
        (r["scenario_id"], r["run_id"]): r
        for r in rows_a
        if r.get("architecture_type") == MULTI_ARCH
    }
    index_b = {
        (r["scenario_id"], r["run_id"]): r
        for r in rows_b
        if r.get("architecture_type") == MULTI_ARCH
    }

    paired_keys = sorted(set(index_a) & set(index_b))
    a_correct_b_incorrect = 0
    b_correct_a_incorrect = 0

    for key in paired_keys:
        a_correct = index_a[key]["decision_correct"] == "True"
        b_correct = index_b[key]["decision_correct"] == "True"
        if a_correct == b_correct:
            continue
        if a_correct:
            a_correct_b_incorrect += 1
        else:
            b_correct_a_incorrect += 1

    discordant_pairs = a_correct_b_incorrect + b_correct_a_incorrect
    exact_p_value = _exact_two_sided_binomial_p_value(
        min(a_correct_b_incorrect, b_correct_a_incorrect),
        discordant_pairs,
    )
    return {
        "paired_observations": len(paired_keys),
        "a_correct_b_incorrect": a_correct_b_incorrect,
        "b_correct_a_incorrect": b_correct_a_incorrect,
        "discordant_pairs": discordant_pairs,
        "exact_p_value": exact_p_value,
    }


# ── summarise one condition ────────────────────────────────────────────────────

def summarise(rows, tag):
    multi = [r for r in rows if r["architecture_type"] == MULTI_ARCH]
    n = len(multi)
    acc = mean([1 if r["decision_correct"] == "True" else 0 for r in multi])
    return {
        "condition": tag,
        "n": n,
        "decision_accuracy": acc,
        "mean_exact_hazard_f1": mean(float_col(multi, "exact_hazard_f1")),
        "mean_semantic_hazard_f1": mean(float_col(multi, "semantic_hazard_f1")),
        "mean_canonical_coverage": mean(float_col(multi, "canonical_hazard_coverage")),
        "mean_spurious_hazards": mean(float_col(multi, "spurious_hazard_count")),
        "mean_false_positives": mean(float_col(multi, "hazard_false_positive_count")),
        "mean_false_negatives": mean(float_col(multi, "hazard_false_negative_count")),
        "mean_latency_s": mean(float_col(multi, "latency_seconds")),
        "mean_tokens": mean(float_col(multi, "token_usage")),
        "mean_confidence": mean(float_col(multi, "confidence_score")),
        "_rows": multi,
    }


# ── load ──────────────────────────────────────────────────────────────────────

baseline_rows = load_results(BASELINE_DIR)
condition_rows = {"baseline_full": baseline_rows}
summaries = [summarise(baseline_rows, "baseline_full")]
for name, d in ABLATION_DIRS.items():
    rows = load_results(d)
    condition_rows[name] = rows
    summaries.append(summarise(rows, name))

base = summaries[0]
base_n = base["n"]
base_acc = base["decision_accuracy"]


# ── 1. Consolidated comparison table ──────────────────────────────────────────

cmp_rows = []
for s in summaries:
    mcnemar = {
        "paired_observations": s["n"],
        "a_correct_b_incorrect": 0,
        "b_correct_a_incorrect": 0,
        "discordant_pairs": 0,
        "exact_p_value": 1.0,
    }
    if s["condition"] != "baseline_full":
        mcnemar = exact_mcnemar_from_rows(
            condition_rows["baseline_full"],
            condition_rows[s["condition"]],
        )
    delta_acc = s["decision_accuracy"] - base_acc
    delta_f1 = s["mean_exact_hazard_f1"] - base["mean_exact_hazard_f1"]
    delta_cov = s["mean_canonical_coverage"] - base["mean_canonical_coverage"]
    cmp_rows.append({
        "condition": s["condition"],
        "dropped_agent": DROPPED_AGENT.get(s["condition"], "—"),
        "n_evaluations": s["n"],
        "decision_accuracy": pct(s["decision_accuracy"]),
        "delta_accuracy_pp": round(delta_acc * 100, 2),
        "exact_hazard_f1": fmt(s["mean_exact_hazard_f1"]),
        "delta_f1": fmt(delta_f1),
        "semantic_hazard_f1": fmt(s["mean_semantic_hazard_f1"]),
        "canonical_coverage": pct(s["mean_canonical_coverage"]),
        "delta_coverage_pp": round(delta_cov * 100, 2),
        "mean_spurious_hazards": fmt(s["mean_spurious_hazards"]),
        "mean_false_positives": fmt(s["mean_false_positives"]),
        "mean_false_negatives": fmt(s["mean_false_negatives"]),
        "mean_latency_s": fmt(s["mean_latency_s"]),
        "mean_tokens": safe_int(s["mean_tokens"]),
        "mean_confidence": fmt(s["mean_confidence"]),
        "paired_test": "exact McNemar test",
        "paired_observations": mcnemar["paired_observations"],
        "baseline_correct_ablation_incorrect": mcnemar["a_correct_b_incorrect"],
        "ablation_correct_baseline_incorrect": mcnemar["b_correct_a_incorrect"],
        "discordant_pairs": mcnemar["discordant_pairs"],
        "p_value_vs_baseline": mcnemar["exact_p_value"],
    })

with (OUT / "ablation_comparison.csv").open("w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=list(cmp_rows[0].keys()))
    w.writeheader()
    w.writerows(cmp_rows)
print("ablation_comparison.csv written")


# ── 2. Per-scenario accuracy delta ────────────────────────────────────────────

all_scenarios = sorted(set(r["scenario_id"] for r in baseline_rows))


def scenario_acc(rows, scenarios):
    m = {s: [] for s in scenarios}
    for r in rows:
        if r["architecture_type"] == MULTI_ARCH:
            m[r["scenario_id"]].append(1 if r["decision_correct"] == "True" else 0)
    return {s: mean(v) for s, v in m.items()}


base_scen_acc = scenario_acc(baseline_rows, all_scenarios)
scen_delta_by_ablation = {}
for name, d in ABLATION_DIRS.items():
    ab_acc = scenario_acc(load_results(d), all_scenarios)
    scen_delta_by_ablation[name] = {s: ab_acc[s] - base_scen_acc[s] for s in all_scenarios}

scen_impact_rows = []
for s in all_scenarios:
    row = {"scenario_id": s, "baseline_accuracy": pct(base_scen_acc[s])}
    for name in ABLATION_DIRS:
        row[f"delta_{name}"] = round(scen_delta_by_ablation[name][s] * 100, 2)
    scen_impact_rows.append(row)

scen_impact_rows.sort(key=lambda r: min(r[f"delta_{n}"] for n in ABLATION_DIRS))

with (OUT / "ablation_per_scenario_delta.csv").open("w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=list(scen_impact_rows[0].keys()))
    w.writeheader()
    w.writerows(scen_impact_rows)
print("ablation_per_scenario_delta.csv written")


# ── 3. Agent contribution ranking ─────────────────────────────────────────────

rank_rows = []
for name, d in ABLATION_DIRS.items():
    s = next(x for x in summaries if x["condition"] == name)
    acc_drop = (base_acc - s["decision_accuracy"]) * 100
    f1_drop = base["mean_exact_hazard_f1"] - s["mean_exact_hazard_f1"]
    cov_drop = (base["mean_canonical_coverage"] - s["mean_canonical_coverage"]) * 100
    conf_drop = base["mean_confidence"] - s["mean_confidence"]
    fp_change = s["mean_false_positives"] - base["mean_false_positives"]
    fn_change = s["mean_false_negatives"] - base["mean_false_negatives"]
    # Composite importance score: acc 40%, f1 30%, cov 20%, conf 10%
    importance = 0.4 * acc_drop + 0.3 * (f1_drop * 100) + 0.2 * cov_drop + 0.1 * (conf_drop * 100)
    rank_rows.append({
        "dropped_agent": DROPPED_AGENT[name],
        "ablation_condition": name,
        "accuracy_drop_pp": round(acc_drop, 2),
        "exact_f1_drop": fmt(f1_drop),
        "canonical_coverage_drop_pp": round(cov_drop, 2),
        "confidence_drop": fmt(conf_drop),
        "false_positive_change": fmt(fp_change),
        "false_negative_change": fmt(fn_change),
        "latency_reduction_s": fmt(base["mean_latency_s"] - s["mean_latency_s"]),
        "token_reduction": safe_int(base["mean_tokens"] - s["mean_tokens"]),
        "importance_score": round(importance, 3),
    })

rank_rows.sort(key=lambda r: r["importance_score"], reverse=True)
for i, r in enumerate(rank_rows, 1):
    r["contribution_rank"] = i

fields = [
    "contribution_rank", "dropped_agent", "ablation_condition", "importance_score",
    "accuracy_drop_pp", "exact_f1_drop", "canonical_coverage_drop_pp",
    "confidence_drop", "false_positive_change", "false_negative_change",
    "latency_reduction_s", "token_reduction",
]
with (OUT / "agent_contribution_ranking.csv").open("w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=fields)
    w.writeheader()
    w.writerows(rank_rows)
print("agent_contribution_ranking.csv written")


# ── 4. Error-mode shift analysis ──────────────────────────────────────────────

def load_errors(p: Path):
    ep = p / "decision_errors.csv"
    if not ep.exists():
        return []
    return list(csv.DictReader(ep.open()))


error_cats = {}
for label, p in [("baseline_full", BASELINE_DIR)] + list(ABLATION_DIRS.items()):
    errs = [r for r in load_errors(p) if r.get("architecture_type") == MULTI_ARCH]
    cat_counts = {}
    for r in errs:
        cat = r.get("error_category") or r.get("error_type") or "unknown"
        cat_counts[cat] = cat_counts.get(cat, 0) + 1
    error_cats[label] = cat_counts

all_cats = sorted(set(c for d in error_cats.values() for c in d))
error_rows = []
for label, counts in error_cats.items():
    row = {"condition": label, "total_errors": sum(counts.values())}
    for c in all_cats:
        row[c] = counts.get(c, 0)
    error_rows.append(row)

with (OUT / "ablation_error_mode_shift.csv").open("w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=["condition", "total_errors"] + all_cats)
    w.writeheader()
    w.writerows(error_rows)
print("ablation_error_mode_shift.csv written")


# ── 5. Summary JSON ───────────────────────────────────────────────────────────

summary_json = {
    "baseline": {
        "run_dir": str(BASELINE_DIR),
        "n": base_n,
        "decision_accuracy": fmt(base_acc),
        "exact_hazard_f1": fmt(base["mean_exact_hazard_f1"]),
        "canonical_coverage": fmt(base["mean_canonical_coverage"]),
        "mean_latency_s": fmt(base["mean_latency_s"]),
        "mean_tokens": safe_int(base["mean_tokens"]),
    },
    "ablations": {
        s["condition"]: {
            "dropped_agent": DROPPED_AGENT.get(s["condition"], "—"),
            "decision_accuracy": fmt(s["decision_accuracy"]),
            "accuracy_drop_pp": round((base_acc - s["decision_accuracy"]) * 100, 2),
            "exact_hazard_f1": fmt(s["mean_exact_hazard_f1"]),
            "canonical_coverage": fmt(s["mean_canonical_coverage"]),
            "mean_latency_s": fmt(s["mean_latency_s"]),
            "mean_tokens": safe_int(s["mean_tokens"]),
            "discordant_pairs": next(r["discordant_pairs"] for r in cmp_rows if r["condition"] == s["condition"]),
            "p_value_vs_baseline": next(r["p_value_vs_baseline"] for r in cmp_rows if r["condition"] == s["condition"]),
        }
        for s in summaries[1:]
    },
    "agent_contribution_ranking": [
        {"rank": r["contribution_rank"], "agent": r["dropped_agent"], "importance_score": r["importance_score"]}
        for r in sorted(rank_rows, key=lambda x: x["contribution_rank"])
    ],
}
(OUT / "ablation_summary.json").write_text(json.dumps(summary_json, indent=2))
print("ablation_summary.json written")


# ── 6. Terminal summary ───────────────────────────────────────────────────────

print()
print("=" * 70)
print("ABLATION ANALYSIS — QUICK SUMMARY")
print("=" * 70)
print(f"{'Condition':<26} {'Acc%':>6} {'ΔAcc pp':>8} {'F1':>6} {'Cov%':>6} {'p-val':>10}")
print("-" * 70)
for r in cmp_rows:
    f1_str = f"{r['exact_hazard_f1']:>6}" if r['exact_hazard_f1'] is not None else "   N/A"
    cov_str = f"{r['canonical_coverage']:>6}" if r['canonical_coverage'] is not None else "   N/A"
    print(
        f"{r['condition']:<26} {r['decision_accuracy']:>6} "
        f"{r['delta_accuracy_pp']:>+8.2f} {f1_str} "
        f"{cov_str} {r['p_value_vs_baseline']:>10}"
    )
print("-" * 70)
print("\nAgent Contribution Ranking (composite score = 40%·acc + 30%·F1 + 20%·cov + 10%·conf):")
for r in sorted(rank_rows, key=lambda x: x["contribution_rank"]):
    fn = r['false_negative_change']
    fn_str = f"{fn:>+.4f}" if fn is not None else "   N/A"
    print(
        f"  #{r['contribution_rank']} {r['dropped_agent']:<28} "
        f"score={r['importance_score']:>7.3f}  "
        f"acc_drop={r['accuracy_drop_pp']:>+6.2f}pp  "
        f"fn_change={fn_str}"
    )
print(f"\nAll files written to: {OUT}/")
