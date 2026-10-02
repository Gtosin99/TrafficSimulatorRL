import os
import sys

import traci


if "SUMO_HOME" in os.environ:
    tools = os.path.join(os.environ["SUMO_HOME"], "tools")
    sys.path.append(tools)
else:
    raise EnvironmentError("SUMO_HOME is not set.")


from traffic_state import get_state, get_total_waiting_time
from reward import calculate_reward
from actions import apply_action


SUMO_CONFIG = "../../simulation/intersection/config/intersection.sumocfg"

SIMULATION_END = 120

ACTION_DURATION = 5


class TrafficEnvironment:

    def __init__(self):

        self.current_time = 0

        self.previous_waiting = 0

    def reset(self):

        sumo_cmd = [
            "sumo",
            "-c",
            SUMO_CONFIG,
        ]

        traci.start(sumo_cmd)

        self.current_time = traci.simulation.getTime()

        self.previous_waiting = get_total_waiting_time()

        state = get_state()

        return state

    def step(self, action):

        apply_action(action)

        for _ in range(ACTION_DURATION):

            traci.simulationStep()

        self.current_time = traci.simulation.getTime()

        current_waiting = get_total_waiting_time()

        reward = calculate_reward(
            self.previous_waiting,
            current_waiting,
        )

        state = get_state()

        self.previous_waiting = current_waiting

        done = self.current_time >= SIMULATION_END

        return state, reward, done

    def close(self):

        traci.close()