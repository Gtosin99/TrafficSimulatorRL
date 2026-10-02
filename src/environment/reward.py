def calculate_reward(previous_waiting, current_waiting):
    """
    Calculate the reward based on the change in total waiting time.

    Positive reward:
        Waiting time decreased.

    Negative reward:
        Waiting time increased.

    Zero reward:
        Waiting time stayed the same.
    """

    reward = previous_waiting - current_waiting

    return reward