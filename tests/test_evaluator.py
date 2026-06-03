from __future__ import annotations

import sys
import unittest
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
SRC_DIR = PROJECT_ROOT / "src"
if str(SRC_DIR) not in sys.path:
    sys.path.insert(0, str(SRC_DIR))

from evaluator import significance_analysis  # type: ignore  # noqa: E402


class SignificanceAnalysisTests(unittest.TestCase):
    def test_reports_exact_test_metadata_and_adjustment(self) -> None:
        records = [
            {
                "scenario_id": "scenario-001",
                "run_id": 1,
                "model": "test-model",
                "architecture_type": "single_agent",
                "decision_correct": 1,
                "exact_hazard_f1": 0.5,
                "semantic_hazard_f1": 0.6,
                "hazard_false_positive_count": 2,
                "hazard_false_negative_count": 1,
                "latency_seconds": 1.0,
                "token_usage": 100,
                "confidence_score": 0.7,
            },
            {
                "scenario_id": "scenario-001",
                "run_id": 1,
                "model": "test-model",
                "architecture_type": "multi_agent_orchestration",
                "decision_correct": 0,
                "exact_hazard_f1": 0.2,
                "semantic_hazard_f1": 0.3,
                "hazard_false_positive_count": 4,
                "hazard_false_negative_count": 3,
                "latency_seconds": 2.0,
                "token_usage": 150,
                "confidence_score": 0.5,
            },
            {
                "scenario_id": "scenario-002",
                "run_id": 1,
                "model": "test-model",
                "architecture_type": "single_agent",
                "decision_correct": 0,
                "exact_hazard_f1": 0.4,
                "semantic_hazard_f1": 0.5,
                "hazard_false_positive_count": 1,
                "hazard_false_negative_count": 2,
                "latency_seconds": 1.2,
                "token_usage": 110,
                "confidence_score": 0.6,
            },
            {
                "scenario_id": "scenario-002",
                "run_id": 1,
                "model": "test-model",
                "architecture_type": "multi_agent_orchestration",
                "decision_correct": 1,
                "exact_hazard_f1": 0.6,
                "semantic_hazard_f1": 0.7,
                "hazard_false_positive_count": 3,
                "hazard_false_negative_count": 1,
                "latency_seconds": 2.2,
                "token_usage": 140,
                "confidence_score": 0.8,
            },
        ]

        results = significance_analysis(records)

        self.assertGreater(len(results), 0)
        row = results[0]
        self.assertIn("test_name", row)
        self.assertIn("test_statistic_name", row)
        self.assertIn("test_statistic_value", row)
        self.assertIn("exact_p_value", row)
        self.assertIn("holm_adjusted_p_value", row)
        self.assertIn("effect_size", row)
        self.assertIn("effect_size_ci_low", row)
        self.assertIn("effect_size_ci_high", row)
        self.assertIn("cohens_dz", row)
        self.assertIn("null_hypothesis", row)
        self.assertIn("alternative_hypothesis", row)
        self.assertIsNotNone(row["exact_p_value"])
        self.assertIsNotNone(row["holm_adjusted_p_value"])


if __name__ == "__main__":
    unittest.main()
