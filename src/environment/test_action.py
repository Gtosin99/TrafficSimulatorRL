import os
import sys

import traci


if "SUMO_HOME" in os.environ:
    tools = os.path.join(os.environ["SUMO_HOME"], "tools")
    sys.path.append(tools)
else:
    raise EnvironmentError("SUMO_HOME is not set.")


from actions import apply_action
from traffic_signal import get_current_phase


SUMO_CONFIG = "../../simulation/intersection/config/intersection.sumocfg"


sumo_cmd = [
    "sumo-gui",
    "-c",
    SUMO_CONFIG,
    "--delay",
    "100",
]


traci.start(sumo_cmd)


print(f"Initial phase: {get_current_phase()}")


for step in range(10):

    traci.simulationStep()

    current_phase = get_current_phase()

    print(
        f"Time: {traci.simulation.getTime():.1f}s | "
        f"Phase before action: {current_phase}"
    )

    # Switch every 5 simulation steps.
    if step % 5 == 0:
        print("Action: SWITCH")
        apply_action(1)

    else:
        print("Action: KEEP")
        apply_action(0)


traci.close()

print("Action test complete.")