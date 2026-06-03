"""Single-agent and multi-agent benchmark pipelines."""

from __future__ import annotations

from typing import Any

from openai_client import LLMResult, call_json_model


ACTIONS = ["proceed", "pause", "reroute", "request_human_review"]
RISK_LEVELS = ["low", "medium", "high", "critical"]

SCORING_ONLY_FIELDS = {"expected_action", "expected_hazards"}


DECISION_SCHEMA: dict[str, Any] = {
    "type": "object",
    "additionalProperties": False,
    "properties": {
        "recommended_action": {"type": "string", "enum": ACTIONS},
        "risk_level": {"type": "string", "enum": RISK_LEVELS},
        "detected_hazards": {"type": "array", "items": {"type": "string"}},
        "reasoning": {"type": "string"},
        "confidence_score": {"type": "number", "minimum": 0, "maximum": 1},
    },
    "required": [
        "recommended_action",
        "risk_level",
        "detected_hazards",
        "reasoning",
        "confidence_score",
    ],
}


SPECIALIST_SCHEMA: dict[str, Any] = {
    "type": "object",
    "additionalProperties": False,
    "properties": {
        "summary": {"type": "string"},
        "risk_level": {"type": "string", "enum": RISK_LEVELS},
        "detected_hazards": {"type": "array", "items": {"type": "string"}},
        "recommendation": {"type": "string"},
        "confidence_score": {"type": "number", "minimum": 0, "maximum": 1},
    },
    "required": [
        "summary",
        "risk_level",
        "detected_hazards",
        "recommendation",
        "confidence_score",
    ],
}


def _fallback_decision(error: str) -> dict[str, Any]:
    """Return a valid decision record when an LLM call fails."""

    return {
        "recommended_action": "request_human_review",
        "risk_level": "critical",
        "detected_hazards": ["llm_call_failed"],
        "reasoning": f"API call failed; conservative fallback used. Error: {error}",
        "confidence_score": 0.0,
    }


def sanitize_scenario_for_model(scenario: dict[str, Any]) -> dict[str, Any]:
    """Remove scoring-only fields before sending a scenario to any model."""

    sanitized = scenario.copy()
    for field in SCORING_ONLY_FIELDS:
        sanitized.pop(field, None)
    return sanitized


def _assert_no_scoring_fields(payload: Any) -> None:
    """Fail fast if a model payload contains scoring-only fields."""

    if isinstance(payload, dict):
        for field in SCORING_ONLY_FIELDS:
            assert field not in payload, f"{field} leaked into a model payload"
        for value in payload.values():
            _assert_no_scoring_fields(value)
    elif isinstance(payload, list):
        for item in payload:
            _assert_no_scoring_fields(item)


def single_agent(scenario: dict[str, Any], model: str | None = None) -> LLMResult:
    """Pipeline A: one generalized agent receives the complete scenario."""

    sanitized_scenario = sanitize_scenario_for_model(scenario)

    system_prompt = (
        "You are a Mars rover decision-support agent. Analyze the full mission "
        "scenario and recommend exactly one action. Prioritize rover safety, "
        "mission continuity, and science value. Return only valid JSON."
    )
    user_payload = {"scenario": sanitized_scenario, "allowed_actions": ACTIONS}
    _assert_no_scoring_fields(user_payload)
    result = call_json_model(
        system_prompt=system_prompt,
        user_payload=user_payload,
        response_schema=DECISION_SCHEMA,
        model=model,
    )
    if result.error:
        result.data = _fallback_decision(result.error)
    return result


def telemetry_agent(scenario: dict[str, Any], model: str | None = None) -> LLMResult:
    """Analyze rover health, power, thermal, radiation, and communications."""

    sanitized_scenario = sanitize_scenario_for_model(scenario)

    payload = {
        "scenario_id": sanitized_scenario["scenario_id"],
        "battery_level": sanitized_scenario["battery_level"],
        "wheel_temperature": sanitized_scenario["wheel_temperature"],
        "radiation_level": sanitized_scenario["radiation_level"],
        "communication_delay_minutes": sanitized_scenario[
            "communication_delay_minutes"
        ],
        "mission_log": sanitized_scenario["mission_log"],
    }
    _assert_no_scoring_fields(payload)
    return call_json_model(
        system_prompt=(
            "You are a rover telemetry specialist. Assess vehicle health and "
            "communications risk. Return only valid JSON."
        ),
        user_payload=payload,
        response_schema=SPECIALIST_SCHEMA,
        model=model,
    )


def terrain_agent(scenario: dict[str, Any], model: str | None = None) -> LLMResult:
    """Analyze mobility hazards from slope and terrain description."""

    sanitized_scenario = sanitize_scenario_for_model(scenario)

    payload = {
        "scenario_id": sanitized_scenario["scenario_id"],
        "terrain_slope": sanitized_scenario["terrain_slope"],
        "terrain_description": sanitized_scenario["terrain_description"],
        "mission_log": sanitized_scenario["mission_log"],
    }
    _assert_no_scoring_fields(payload)
    return call_json_model(
        system_prompt=(
            "You are a Mars terrain and mobility specialist. Identify slope, "
            "traction, obstacle, and wheel-damage hazards. Return only valid JSON."
        ),
        user_payload=payload,
        response_schema=SPECIALIST_SCHEMA,
        model=model,
    )


def risk_agent(scenario: dict[str, Any], model: str | None = None) -> LLMResult:
    """Analyze aggregate operational risk for the scenario."""

    sanitized_scenario = sanitize_scenario_for_model(scenario)

    payload = {
        "scenario_id": sanitized_scenario["scenario_id"],
        "sol": sanitized_scenario["sol"],
        "battery_level": sanitized_scenario["battery_level"],
        "wheel_temperature": sanitized_scenario["wheel_temperature"],
        "terrain_slope": sanitized_scenario["terrain_slope"],
        "radiation_level": sanitized_scenario["radiation_level"],
        "communication_delay_minutes": sanitized_scenario[
            "communication_delay_minutes"
        ],
        "mission_log": sanitized_scenario["mission_log"],
    }
    _assert_no_scoring_fields(payload)
    return call_json_model(
        system_prompt=(
            "You are a mission risk specialist. Assess combined operational risk "
            "and identify hazards that could compromise rover safety. Return only valid JSON."
        ),
        user_payload=payload,
        response_schema=SPECIALIST_SCHEMA,
        model=model,
    )


def mission_planner_agent(scenario: dict[str, Any], model: str | None = None) -> LLMResult:
    """Analyze science objective tradeoffs and operational priority."""

    sanitized_scenario = sanitize_scenario_for_model(scenario)

    payload = {
        "scenario_id": sanitized_scenario["scenario_id"],
        "science_objective": sanitized_scenario["science_objective"],
        "mission_log": sanitized_scenario["mission_log"],
        "battery_level": sanitized_scenario["battery_level"],
        "communication_delay_minutes": sanitized_scenario[
            "communication_delay_minutes"
        ],
    }
    _assert_no_scoring_fields(payload)
    return call_json_model(
        system_prompt=(
            "You are a Mars mission planner. Balance science value, time, safety, "
            "and need for human review. Return only valid JSON."
        ),
        user_payload=payload,
        response_schema=SPECIALIST_SCHEMA,
        model=model,
    )


def orchestrator_agent(
    scenario: dict[str, Any],
    specialist_outputs: dict[str, dict[str, Any]],
    model: str | None = None,
) -> LLMResult:
    """Combine specialist reports into a final decision."""

    sanitized_scenario = sanitize_scenario_for_model(scenario)

    payload = {
        "scenario": sanitized_scenario,
        "specialist_outputs": specialist_outputs,
        "allowed_actions": ACTIONS,
    }
    _assert_no_scoring_fields(payload)
    result = call_json_model(
        system_prompt=(
            "You are the final Mars rover orchestration agent. Combine specialist "
            "reports into one decision. Resolve conflicts explicitly and choose "
            "the safest action that still preserves mission value. Return only valid JSON."
        ),
        user_payload=payload,
        response_schema=DECISION_SCHEMA,
        model=model,
    )
    if result.error:
        result.data = _fallback_decision(result.error)
    return result


ABLATION_AGENTS = {
    "drop_telemetry": "telemetry_agent",
    "drop_terrain": "terrain_agent",
    "drop_risk": "risk_agent",
    "drop_mission_planner": "mission_planner_agent",
}


def multi_agent_orchestration(
    scenario: dict[str, Any],
    model: str | None = None,
    ablation: str | None = None,
) -> LLMResult:
    """Pipeline B: specialist agents followed by a final orchestrator.

    Args:
        ablation: If set, must be one of the keys in ABLATION_AGENTS. The
            corresponding specialist is omitted from the orchestrator inputs.
    """

    sanitized_scenario = sanitize_scenario_for_model(scenario)
    skip = ABLATION_AGENTS.get(ablation) if ablation else None

    all_specialists: dict[str, Any] = {}
    if skip != "telemetry_agent":
        all_specialists["telemetry_agent"] = telemetry_agent(sanitized_scenario, model=model)
    if skip != "terrain_agent":
        all_specialists["terrain_agent"] = terrain_agent(sanitized_scenario, model=model)
    if skip != "risk_agent":
        all_specialists["risk_agent"] = risk_agent(sanitized_scenario, model=model)
    if skip != "mission_planner_agent":
        all_specialists["mission_planner_agent"] = mission_planner_agent(sanitized_scenario, model=model)
    specialists = all_specialists
    specialist_outputs = {
        name: result.data if not result.error else {"error": result.error}
        for name, result in specialists.items()
    }
    orchestrated = orchestrator_agent(
        sanitized_scenario, specialist_outputs, model=model
    )
    token_usage = sum(
        result.token_usage or 0 for result in specialists.values()
    ) + (orchestrated.token_usage or 0)
    orchestrated.token_usage = token_usage or None
    return orchestrated
