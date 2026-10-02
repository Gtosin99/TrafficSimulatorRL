import traci


# Incoming roads leading toward the intersection
INCOMING_EDGES = [
    "north_to_center",
    "south_to_center",
    "east_to_center",
    "west_to_center",
]


def get_vehicle_counts():
    """
    Return the number of vehicles currently on each incoming road.
    """

    vehicle_counts = {}

    for edge in INCOMING_EDGES:
        vehicle_counts[edge] = traci.edge.getLastStepVehicleNumber(edge)

    return vehicle_counts

def get_stopped_vehicle_counts():
    """
    Return the number of stopped vehicles on each incoming road.
    """

    stopped_counts = {}

    for edge in INCOMING_EDGES:

        vehicle_ids = traci.edge.getLastStepVehicleIDs(edge)

        stopped_count = 0

        for vehicle_id in vehicle_ids:

            speed = traci.vehicle.getSpeed(vehicle_id)

            if speed < 0.1:
                stopped_count += 1

        stopped_counts[edge] = stopped_count

    return stopped_counts

def get_waiting_time():
    """
    Return the accumulated waiting time on each incoming road.
    """

    waiting_times = {}

    for edge in INCOMING_EDGES:
        waiting_times[edge] = traci.edge.getWaitingTime(edge)

    return waiting_times

def get_total_waiting_time():
    """
    Return the total waiting time across all incoming roads.
    """

    waiting_times = get_waiting_time()

    total_waiting = sum(waiting_times.values())

    return total_waiting

def get_state():
    """
    Return the current traffic state as a list.
    """

    vehicle_counts = get_vehicle_counts()
    stopped_counts = get_stopped_vehicle_counts()
    waiting_times = get_waiting_time()

    current_phase = traci.trafficlight.getPhase("center")

    state = [
        vehicle_counts["north_to_center"],
        vehicle_counts["south_to_center"],
        vehicle_counts["east_to_center"],
        vehicle_counts["west_to_center"],

        stopped_counts["north_to_center"],
        stopped_counts["south_to_center"],
        stopped_counts["east_to_center"],
        stopped_counts["west_to_center"],

        waiting_times["north_to_center"],
        waiting_times["south_to_center"],
        waiting_times["east_to_center"],
        waiting_times["west_to_center"],

        current_phase,
    ]

    return state