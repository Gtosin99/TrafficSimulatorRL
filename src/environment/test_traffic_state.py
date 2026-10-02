import os
import sys

import traci


if "SUMO_HOME" in os.environ:
    tools = os.path.join(os.environ["SUMO_HOME"], "tools")
    sys.path.append(tools)
else:
    raise EnvironmentError("SUMO_HOME is not set.")


from traffic_state import (get_vehicle_counts, get_stopped_vehicle_counts, get_waiting_time, get_state)


SUMO_CONFIG = "../../simulation/intersection/config/intersection.sumocfg"


sumo_cmd = [
    "sumo",
    "-c",
    SUMO_CONFIG,
]


traci.start(sumo_cmd)


for step in range(30):

    traci.simulationStep()

    state = get_state()
    counts = get_vehicle_counts()
    stopped_counts = get_stopped_vehicle_counts()
    waiting_times = get_waiting_time()

    print(f"\nTime: {traci.simulation.getTime():.1f}s")
    print("-" * 60)

    for edge in counts:
        print(
            f"{edge:<20} "
            f"Vehicles: {counts[edge]:<3} "
            f"Stopped: {stopped_counts[edge]:<3} "
            f"Waiting: {waiting_times[edge]:.1f}s"
        )
    print(f"State: {state}")  


traci.close()