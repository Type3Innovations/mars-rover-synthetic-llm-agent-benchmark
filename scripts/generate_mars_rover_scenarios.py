"""Generate a 100-scenario Mars rover benchmark dataset."""

from __future__ import annotations

import json
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]
OUTPUT_PATH = PROJECT_ROOT / "data" / "mars_rover_scenarios.json"


BASE_SCENARIOS = [
    {
        "scenario_id": "MR-001",
        "sol": 48,
        "battery_level": 82,
        "wheel_temperature": 41,
        "terrain_slope": 7,
        "terrain_description": "Compact regolith plain with scattered pebble fields and clear wheel tracks from prior traversal.",
        "radiation_level": 0.21,
        "communication_delay_minutes": 11,
        "science_objective": "Image layered sediment deposits near a shallow ridge.",
        "mission_log": "Navigation cameras show stable footing. Power margin is high and thermal readings are nominal.",
        "expected_action": "proceed",
        "expected_hazards": ["minor pebble field"],
    },
    {
        "scenario_id": "MR-002",
        "sol": 73,
        "battery_level": 34,
        "wheel_temperature": 68,
        "terrain_slope": 18,
        "terrain_description": "Loose sand drift leading into a sloped crater rim with visible slip marks.",
        "radiation_level": 0.27,
        "communication_delay_minutes": 14,
        "science_objective": "Reach crater rim to collect panoramic imagery.",
        "mission_log": "Recent drive segment showed elevated wheel slip and rising actuator temperature.",
        "expected_action": "reroute",
        "expected_hazards": ["loose sand", "steep slope", "wheel overheating"],
    },
    {
        "scenario_id": "MR-003",
        "sol": 112,
        "battery_level": 19,
        "wheel_temperature": 44,
        "terrain_slope": 4,
        "terrain_description": "Flat basaltic surface with low obstacle density.",
        "radiation_level": 0.23,
        "communication_delay_minutes": 9,
        "science_objective": "Run overnight atmospheric sampling sequence.",
        "mission_log": "Battery is below reserve threshold after an extended instrument warmup.",
        "expected_action": "pause",
        "expected_hazards": ["low battery"],
    },
    {
        "scenario_id": "MR-004",
        "sol": 139,
        "battery_level": 57,
        "wheel_temperature": 49,
        "terrain_slope": 11,
        "terrain_description": "Fractured bedrock with sharp embedded rocks and narrow passable channels.",
        "radiation_level": 0.31,
        "communication_delay_minutes": 21,
        "science_objective": "Approach exposed vein material for spectrometer analysis.",
        "mission_log": "Autonav identified multiple wheel-clearance warnings near high-priority science target.",
        "expected_action": "request_human_review",
        "expected_hazards": ["sharp rocks", "wheel damage risk", "long communication delay"],
    },
    {
        "scenario_id": "MR-005",
        "sol": 167,
        "battery_level": 61,
        "wheel_temperature": 53,
        "terrain_slope": 14,
        "terrain_description": "Moderately sloped terrain with rippled sand patches beside a safer bedrock bench.",
        "radiation_level": 0.24,
        "communication_delay_minutes": 12,
        "science_objective": "Traverse to clay-bearing outcrop before local dusk.",
        "mission_log": "Sand ripples are avoidable with a longer route. Battery supports a delayed traverse.",
        "expected_action": "reroute",
        "expected_hazards": ["sand ripples", "moderate slope"],
    },
    {
        "scenario_id": "MR-006",
        "sol": 203,
        "battery_level": 46,
        "wheel_temperature": 39,
        "terrain_slope": 6,
        "terrain_description": "Stable terrain, but orbital weather feed reports a regional dust opacity increase.",
        "radiation_level": 0.62,
        "communication_delay_minutes": 16,
        "science_objective": "Deploy arm-mounted camera for close inspection of surface crust.",
        "mission_log": "Radiation and dust readings rose sharply over the last two sols. Visibility may degrade.",
        "expected_action": "pause",
        "expected_hazards": ["elevated radiation", "dust opacity"],
    },
    {
        "scenario_id": "MR-007",
        "sol": 244,
        "battery_level": 76,
        "wheel_temperature": 47,
        "terrain_slope": 9,
        "terrain_description": "Hard-packed traverse corridor around a dune margin.",
        "radiation_level": 0.22,
        "communication_delay_minutes": 10,
        "science_objective": "Collect multispectral observations of dune stratification from stand-off distance.",
        "mission_log": "Hazard cameras show adequate clearance and no recent slip events.",
        "expected_action": "proceed",
        "expected_hazards": ["nearby dune margin"],
    },
    {
        "scenario_id": "MR-008",
        "sol": 301,
        "battery_level": 52,
        "wheel_temperature": 72,
        "terrain_slope": 22,
        "terrain_description": "Narrow gully entrance with shadowed rocks, steep cross-slope, and uncertain exit route.",
        "radiation_level": 0.29,
        "communication_delay_minutes": 24,
        "science_objective": "Investigate hydrated mineral signatures inside the gully.",
        "mission_log": "Planner notes high science value, but terrain model confidence is low and communications are delayed.",
        "expected_action": "request_human_review",
        "expected_hazards": ["steep slope", "shadowed rocks", "wheel overheating", "uncertain exit route", "long communication delay"],
    },
]


PROCEED_TERRAINS = [
    "Firm basaltic pavement with isolated pebble clusters and shallow wheel ruts from a prior safe traverse.",
    "Hard-packed regolith corridor skirting a low dune edge with stable traction indicators.",
    "Broad sediment bench with compact surface crust and sparse cobble obstacles.",
    "Shallow ridge approach with exposed bedrock plates and predictable wheel contact.",
    "Flat ejecta apron with minor gravel scatter and high slip-margin confidence.",
    "Layered outcrop access path with gentle undulations and no deep sink zones.",
]
PROCEED_OBJECTIVES = [
    "Acquire multispectral imagery of a nearby sediment contact.",
    "Capture context panorama for a previously sampled vein exposure.",
    "Image ripple cross-bedding from a stable stand-off location.",
    "Collect close-range stereo imagery of weathered basalt fragments.",
    "Survey a shallow ridge crest for stratigraphic continuity.",
    "Map surface texture around a low-relief fracture network.",
]
PROCEED_LOGS = [
    "Hazard cameras report consistent traction and nominal steering loads.",
    "Recent autonav segment completed without slip alarms or thermal excursions.",
    "Power margin remains strong and wheel currents are within expected range.",
    "Localization quality is high and terrain confidence remains stable.",
]
PROCEED_HAZARD_SETS = [
    ["minor pebble field"],
    ["nearby dune margin"],
    ["scattered cobbles"],
    ["shallow wheel rut"],
    ["low ridge crest"],
    ["gravel patch"],
]

REROUTE_TERRAINS = [
    "Loose sand apron leading toward a steeper bench with visible slip streaks.",
    "Rippled drift field adjacent to a safer bedrock shoulder.",
    "Moderately sloped channel floor with soft regolith pockets and embedded rocks.",
    "Crater-wall approach where compact terrain exists only along a longer lateral path.",
    "Dust-coated traverse lane with unstable edges beside a firmer bypass route.",
    "Mixed sand-and-gravel surface trending upward toward a sharper cross-slope.",
]
REROUTE_OBJECTIVES = [
    "Reach an imaging point for crater-wall mineral mapping.",
    "Traverse toward a clay-bearing exposure before lighting conditions degrade.",
    "Move to a ridge overlook for panoramic science observations.",
    "Position the rover for arm deployment near a layered outcrop.",
    "Approach a sediment fan for context imaging and follow-on sampling.",
    "Relocate to a bench with improved access to sulfate-bearing rock.",
]
REROUTE_LOGS = [
    "Drive telemetry indicates intermittent slip spikes near the current heading.",
    "Planner identified a longer but safer path with improved traction confidence.",
    "Wheel currents are acceptable, but terrain risk increases along the shortest route.",
    "Navigation assessment recommends avoiding the soft shoulder on the direct path.",
]
REROUTE_HAZARD_SETS = [
    ["loose sand", "steep slope"],
    ["sand ripples", "moderate slope"],
    ["traction loss risk", "embedded rocks"],
    ["soft shoulder", "cross-slope hazard"],
    ["wheel overheating", "loose sand", "steep slope"],
    ["dust-covered ground", "unstable edge"],
]

PAUSE_TERRAINS = [
    "Stable flat terrain with no major mobility obstacles.",
    "Low-relief basalt plain suitable for holding position.",
    "Compact regolith bench with good stow posture and minimal immediate terrain risk.",
    "Level surface near a prior drill site with adequate communications geometry.",
]
PAUSE_OBJECTIVES = [
    "Hold for an atmospheric sampling window after systems stabilize.",
    "Delay arm deployment until environmental conditions improve.",
    "Preserve vehicle health before resuming a planned traverse.",
    "Pause surface operations until power or environmental margins recover.",
]
PAUSE_LOGS = [
    "Battery reserve has trended downward after extended instrument usage.",
    "Environmental telemetry shows worsening conditions over the last two planning cycles.",
    "Thermal margin is narrowing and a cooldown pause would protect actuators.",
    "Dust or radiation conditions exceed the nominal comfort range for current activities.",
]
PAUSE_HAZARD_SETS = [
    ["low battery"],
    ["elevated radiation", "dust opacity"],
    ["wheel overheating"],
    ["instrument thermal stress"],
    ["low power margin", "communication risk"],
    ["dust accumulation", "reduced visibility"],
]

REVIEW_TERRAINS = [
    "Narrow fractured corridor with sharp rocks, blind turns, and uncertain wheel clearance.",
    "Steep gully entrance with shadowed obstacles and no confirmed exit route.",
    "Broken bedrock ledge network with narrow channels and limited escape options.",
    "Crater-rim notch containing sharp ejecta blocks and ambiguous traction estimates.",
    "Rocky slope above a confined basin with uncertain turnaround space.",
    "Shadowed ravine approach where terrain model confidence drops sharply.",
]
REVIEW_OBJECTIVES = [
    "Approach a high-value mineral vein for spectrometer analysis.",
    "Investigate hydrated signatures inside a partially shadowed gully.",
    "Reach a fractured outcrop that may preserve alteration textures.",
    "Inspect bright clasts exposed near a rim breach.",
    "Evaluate a steep access route to a scientifically valuable ledge.",
    "Approach subsurface exposure revealed by recent erosion.",
]
REVIEW_LOGS = [
    "Autonav flags repeated wheel-clearance concerns and route confidence remains low.",
    "Science value is high, but the operations team would benefit from a deliberate review.",
    "Communications delay and terrain ambiguity increase the consequence of an autonomous mistake.",
    "Recent planning products disagree on the safest entry angle into the target zone.",
]
REVIEW_HAZARD_SETS = [
    ["sharp rocks", "wheel damage risk", "long communication delay"],
    ["steep slope", "uncertain exit route", "shadowed rocks"],
    ["terrain model uncertainty", "blind turn", "limited escape path"],
    ["sharp ejecta blocks", "long communication delay", "cross-slope hazard"],
    ["confined turning space", "wheel damage risk", "steep slope"],
    ["shadowed rocks", "route ambiguity", "long communication delay"],
]


def build_generated_scenarios() -> list[dict[str, object]]:
    scenarios: list[dict[str, object]] = []

    for index in range(23):
        scenarios.append(
            {
                "sol": 320 + index * 3,
                "battery_level": 70 + (index % 6) * 4,
                "wheel_temperature": 39 + (index % 5) * 3,
                "terrain_slope": 4 + (index % 6),
                "terrain_description": PROCEED_TERRAINS[index % len(PROCEED_TERRAINS)],
                "radiation_level": round(0.18 + (index % 5) * 0.02, 2),
                "communication_delay_minutes": 8 + (index % 6),
                "science_objective": PROCEED_OBJECTIVES[index % len(PROCEED_OBJECTIVES)],
                "mission_log": PROCEED_LOGS[index % len(PROCEED_LOGS)],
                "expected_action": "proceed",
                "expected_hazards": PROCEED_HAZARD_SETS[index % len(PROCEED_HAZARD_SETS)],
            }
        )

    for index in range(23):
        scenarios.append(
            {
                "sol": 420 + index * 4,
                "battery_level": 48 + (index % 7) * 3,
                "wheel_temperature": 52 + (index % 6) * 3,
                "terrain_slope": 12 + (index % 8),
                "terrain_description": REROUTE_TERRAINS[index % len(REROUTE_TERRAINS)],
                "radiation_level": round(0.24 + (index % 4) * 0.03, 2),
                "communication_delay_minutes": 10 + (index % 7),
                "science_objective": REROUTE_OBJECTIVES[index % len(REROUTE_OBJECTIVES)],
                "mission_log": REROUTE_LOGS[index % len(REROUTE_LOGS)],
                "expected_action": "reroute",
                "expected_hazards": REROUTE_HAZARD_SETS[index % len(REROUTE_HAZARD_SETS)],
            }
        )

    for index in range(23):
        scenarios.append(
            {
                "sol": 540 + index * 5,
                "battery_level": 18 + (index % 8) * 4,
                "wheel_temperature": 41 + (index % 7) * 5,
                "terrain_slope": 3 + (index % 5),
                "terrain_description": PAUSE_TERRAINS[index % len(PAUSE_TERRAINS)],
                "radiation_level": round(0.28 + (index % 6) * 0.07, 2),
                "communication_delay_minutes": 9 + (index % 8),
                "science_objective": PAUSE_OBJECTIVES[index % len(PAUSE_OBJECTIVES)],
                "mission_log": PAUSE_LOGS[index % len(PAUSE_LOGS)],
                "expected_action": "pause",
                "expected_hazards": PAUSE_HAZARD_SETS[index % len(PAUSE_HAZARD_SETS)],
            }
        )

    for index in range(23):
        scenarios.append(
            {
                "sol": 680 + index * 6,
                "battery_level": 38 + (index % 6) * 5,
                "wheel_temperature": 50 + (index % 6) * 4,
                "terrain_slope": 11 + (index % 10),
                "terrain_description": REVIEW_TERRAINS[index % len(REVIEW_TERRAINS)],
                "radiation_level": round(0.26 + (index % 5) * 0.05, 2),
                "communication_delay_minutes": 18 + (index % 8),
                "science_objective": REVIEW_OBJECTIVES[index % len(REVIEW_OBJECTIVES)],
                "mission_log": REVIEW_LOGS[index % len(REVIEW_LOGS)],
                "expected_action": "request_human_review",
                "expected_hazards": REVIEW_HAZARD_SETS[index % len(REVIEW_HAZARD_SETS)],
            }
        )

    return scenarios


def assign_ids(scenarios: list[dict[str, object]]) -> list[dict[str, object]]:
    """Attach sequential scenario IDs after the preserved base scenarios."""

    with_ids: list[dict[str, object]] = []
    for index, scenario in enumerate(scenarios, start=9):
        record = dict(scenario)
        record["scenario_id"] = f"MR-{index:03d}"
        with_ids.append(record)
    return with_ids


def main() -> None:
    generated = assign_ids(build_generated_scenarios())
    all_scenarios = BASE_SCENARIOS + generated
    if len(all_scenarios) != 100:
        raise RuntimeError(f"Expected 100 scenarios, found {len(all_scenarios)}")
    OUTPUT_PATH.write_text(json.dumps(all_scenarios, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote {len(all_scenarios)} scenarios to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
