import traci


TRAFFIC_LIGHT_ID = "center"


def get_current_phase():
    """
    Return the current traffic-light phase.
    """

    return traci.trafficlight.getPhase(TRAFFIC_LIGHT_ID)


def keep_phase():
    """
    Keep the traffic light in its current phase.
    """

    current_phase = get_current_phase()

    traci.trafficlight.setPhase(
        TRAFFIC_LIGHT_ID,
        current_phase,
    )


def switch_phase():
    """
    Switch to the opposite green phase.

    Phase 0 -> Phase 1 -> Phase 2
    Phase 2 -> Phase 3 -> Phase 0
    """

    current_phase = get_current_phase()

    if current_phase == 0:
        # Begin the yellow transition toward East/West green.
        traci.trafficlight.setPhase(
            TRAFFIC_LIGHT_ID,
            1,
        )

    elif current_phase == 2:
        # Begin the yellow transition toward North/South green.
        traci.trafficlight.setPhase(
            TRAFFIC_LIGHT_ID,
            3,
        )