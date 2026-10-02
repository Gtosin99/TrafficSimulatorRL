from traffic_environment import TrafficEnvironment


environment = TrafficEnvironment()


state = environment.reset()

print("\nInitial state:")
print(state)


for step in range(10):

    # For now, alternate between KEEP and SWITCH.
    if step % 2 == 0:
        action = 0
    else:
        action = 1

    next_state, reward, done = environment.step(action)

    print(
        f"\nStep: {step + 1}"
        f"\nAction: {action}"
        f"\nReward: {reward:.2f}"
        f"\nNext state: {next_state}"
        f"\nDone: {done}"
    )

    if done:
        break


environment.close()

print("\nEnvironment test complete.")