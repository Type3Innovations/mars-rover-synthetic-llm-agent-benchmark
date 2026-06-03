from __future__ import annotations

import sys
import unittest
from pathlib import Path
from unittest.mock import patch

PROJECT_ROOT = Path(__file__).resolve().parents[1]
SRC_DIR = PROJECT_ROOT / "src"
if str(SRC_DIR) not in sys.path:
    sys.path.insert(0, str(SRC_DIR))

from agents import (  # type: ignore  # noqa: E402
    _assert_no_scoring_fields,
    multi_agent_orchestration,
    sanitize_scenario_for_model,
    single_agent,
)
from openai_client import LLMResult  # type: ignore  # noqa: E402


class AgentPayloadSanitizationTests(unittest.TestCase):
    def setUp(self) -> None:
        self.scenario = {
            "scenario_id": "scenario-001",
            "sol": 17,
            "science_objective": "Analyze soil composition",
            "battery_level": 63,
            "wheel_temperature": 19,
            "terrain_slope": 11,
            "radiation_level": 2.1,
            "communication_delay_minutes": 14,
            "terrain_description": "Loose gravel near a ridge",
            "mission_log": ["Initial scan complete"],
            "expected_action": "pause",
            "expected_hazards": ["low battery", "slippery slope"],
        }

    def test_sanitize_scenario_for_model_removes_scoring_fields(self) -> None:
        sanitized = sanitize_scenario_for_model(self.scenario)

        self.assertNotIn("expected_action", sanitized)
        self.assertNotIn("expected_hazards", sanitized)
        self.assertIn("expected_action", self.scenario)
        self.assertIn("expected_hazards", self.scenario)

    def test_single_agent_payload_excludes_scoring_fields(self) -> None:
        with patch("agents.call_json_model", return_value=LLMResult(data={})) as mock_call:
            single_agent(self.scenario, model="test-model")

        payload = mock_call.call_args.kwargs["user_payload"]
        _assert_no_scoring_fields(payload)

    def test_multi_agent_payloads_exclude_scoring_fields(self) -> None:
        with patch("agents.call_json_model", return_value=LLMResult(data={})) as mock_call:
            multi_agent_orchestration(self.scenario, model="test-model")

        for call in mock_call.call_args_list:
            payload = call.kwargs["user_payload"]
            _assert_no_scoring_fields(payload)


if __name__ == "__main__":
    unittest.main()
