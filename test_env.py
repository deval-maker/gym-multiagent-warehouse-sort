import gym
import time
import gym_multigrid
import numpy as np

def main():

    env = gym.make('MultiGrid-WarehouseSort-n2-v1')

    obs = env.reset()

    n_agents = len(env.agents)

    debug = True
    if debug:
        mode = 'human'
        print("Action Space:" , env.action_space)
        print("Observation Space:" , env.observation_space)

    else:
        mode = 'rgb-array'

    while True:

        env.render(mode=mode, highlight=False)
        ac = [env.action_space.sample() for _ in range(n_agents)]

        if debug:
            time.sleep(0.01)
            print(env)
            print("Observations:", obs.shape)

            ac = input('cmd >')
            ac = [int(ac)]

            print("Past Actions:", ac)
            print(env.step_count)
        
        ac = np.array(ac)
        obs, rewards, done, _ = env.step(ac)

        if debug: 
            print("Rewards:", rewards)

        if done:
            print(env.step_count)
            break

if __name__ == "__main__":
    main()