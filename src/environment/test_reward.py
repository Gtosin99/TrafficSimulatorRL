import os
import sys

import traci


if "SUMO_HOME" in os.environ:
    tools = os.path.join(os.environ["SUMO_HOME"], "tools")
    sys.path.append(tools)
else:
    raise EnvironmentError("SUMO_HOME is not set.")


from traffic_state import get_total_waiting_time
from reward import calculate_reward


SUMO_CONFIG = "../../simulation/intersection/config/intersection.sumocfg"


sumo_cmd = [
    "sumo",
    "-c",
    SUMO_CONFIG,
]


traci.start(sumo_cmd)


previous_waiting = get_total_waiting_time()


for step in range(30):

    traci.simulationStep()

    current_waiting = get_total_waiting_time()

    reward = calculate_reward(
        previous_waiting,
        current_waiting,
    )

    print(
        f"Time: {traci.simulation.getTime():.1f}s | "
        f"Previous waiting: {previous_waiting:.1f}s | "
        f"Current waiting: {current_waiting:.1f}s | "
        f"Reward: {reward:.1f}"
    )

    previous_waiting = current_waiting


traci.close()