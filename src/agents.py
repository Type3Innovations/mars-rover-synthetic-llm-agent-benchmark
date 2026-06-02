"""Single-agent and multi-agent benchmark pipelines."""

from __future__ import annotations

from typing import Any

from openai_client import LLMResult, call_json_model


ACTIONS = ["proceed", "pause", "reroute", "request_human_review"]
RISK_LEVELS = ["low", "medium", "high", "critical"]


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


def single_agent(scenario: dict[str, Any], model: str | None = None) -> LLMResult:
    """Pipeline A: one generalized agent receives the complete scenario."""

    system_prompt = (
        "You are a Mars rover decision-support agent. Analyze the full mission "
        "scenario and recommend exactly one action. Prioritize rover safety, "
        "mission continuity, and science value. Return only valid JSON."
    )
    result = call_json_model(
        system_prompt=system_prompt,
        user_payload={"scenario": scenario, "allowed_actions": ACTIONS},
        response_schema=DECISION_SCHEMA,
        model=model,
    )
    if result.error:
        result.data = _fallback_decision(result.error)
    return result


def telemetry_agent(scenario: dict[str, Any], model: str | None = None) -> LLMResult:
    """Analyze rover health, power, thermal, radiation, and communications."""

    payload = {
        "scenario_id": scenario["scenario_id"],
        "battery_level": scenario["battery_level"],
        "wheel_temperature": scenario["wheel_temperature"],
        "radiation_level": scenario["radiation_level"],
        "communication_delay_minutes": scenario["communication_delay_minutes"],
        "mission_log": scenario["mission_log"],
    }
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

    payload = {
        "scenario_id": scenario["scenario_id"],
        "terrain_slope": scenario["terrain_slope"],
        "terrain_description": scenario["terrain_description"],
        "mission_log": scenario["mission_log"],
    }
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

    payload = {
        "scenario_id": scenario["scenario_id"],
        "sol": scenario["sol"],
        "battery_level": scenario["battery_level"],
        "wheel_temperature": scenario["wheel_temperature"],
        "terrain_slope": scenario["terrain_slope"],
        "radiation_level": scenario["radiation_level"],
        "communication_delay_minutes": scenario["communication_delay_minutes"],
        "mission_log": scenario["mission_log"],
    }
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

    payload = {
        "scenario_id": scenario["scenario_id"],
        "science_objective": scenario["science_objective"],
        "mission_log": scenario["mission_log"],
        "battery_level": scenario["battery_level"],
        "communication_delay_minutes": scenario["communication_delay_minutes"],
    }
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

    payload = {
        "scenario": scenario,
        "specialist_outputs": specialist_outputs,
        "allowed_actions": ACTIONS,
    }
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


def multi_agent_orchestration(
    scenario: dict[str, Any], model: str | None = None
) -> LLMResult:
    """Pipeline B: specialist agents followed by a final orchestrator."""

    specialists = {
        "telemetry_agent": telemetry_agent(scenario, model=model),
        "terrain_agent": terrain_agent(scenario, model=model),
        "risk_agent": risk_agent(scenario, model=model),
        "mission_planner_agent": mission_planner_agent(scenario, model=model),
    }
    specialist_outputs = {
        name: result.data if not result.error else {"error": result.error}
        for name, result in specialists.items()
    }
    orchestrated = orchestrator_agent(scenario, specialist_outputs, model=model)
    token_usage = sum(
        result.token_usage or 0 for result in specialists.values()
    ) + (orchestrated.token_usage or 0)
    orchestrated.token_usage = token_usage or None
    return orchestrated
