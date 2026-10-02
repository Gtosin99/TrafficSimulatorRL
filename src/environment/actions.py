from traffic_signal import keep_phase, switch_phase


KEEP_PHASE = 0
SWITCH_PHASE = 1


def apply_action(action):
    """
    Apply an RL action to the traffic light.

    Action 0:
        Keep the current phase.

    Action 1:
        Switch to the opposite green phase.
    """

    if action == KEEP_PHASE:
        keep_phase()

    elif action == SWITCH_PHASE:
        switch_phase()

    else:
        raise ValueError(
            f"Invalid action: {action}. "
            "Action must be 0 or 1."
        )