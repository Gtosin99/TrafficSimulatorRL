import os
import sys
import traci


if "SUMO_HOME" in os.environ:
    tools = os.path.join(os.environ["SUMO_HOME"], "tools")
    sys.path.append(tools)
else:
    raise EnvironmentError("SUMO_HOME is not set.")


SUMO_CONFIG = "simulation/intersection/config/intersection.sumocfg"


sumo_cmd = [
    "sumo-gui",
    "-c",
    SUMO_CONFIG,
    "--delay",
    "100",
]


traci.start(sumo_cmd)


next_change = 30


while traci.simulation.getTime() < 120:

    traci.simulationStep()

    current_time = traci.simulation.getTime()

    if current_time >= next_change:

        current_phase = traci.trafficlight.getPhase("center")

        print(
            f"Time: {current_time:.1f}s | "
            f"Current phase: {current_phase}"
        )

        # Switch between the two green phases.
        if current_phase == 0:
            traci.trafficlight.setPhase("center", 2)

        elif current_phase == 2:
            traci.trafficlight.setPhase("center", 0)

        next_change += 30


traci.close()

print("Simulation complete.")