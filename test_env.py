import gym
import time
from gym.envs.registration import register
import argparse


def main():

    register(
        id='warehouse-sort-v0', 
        entry_point='gym_multigrid.envs:WarehouseSortEnvN1'
    )
    
    env = gym.make('warehouse-sort-v0')

    obs = env.reset()

    nb_agents = len(env.agents)
    
    debug = False
    if debug:
        mode = 'human'
    else:
        mode = 'rgb-array'

    while True:

        env.render(mode=mode, highlight=False)
        ac = [env.action_space.sample() for _ in range(nb_agents)]

        if debug:
            time.sleep(0.01)
            print(env)
            print("Goal Positions:", obs[0])
            print("Agent Positions:", obs[1])

            ac = input('cmd >')
            ac = [int(ac)]

            print("Past Actions:", ac)
            print(env.step_count)
        
        obs, rewards, done, _ = env.step(ac)

        if debug: 
            print("Rewards:", rewards)

        if done:
            print(env.step_count)
            break

if __name__ == "__main__":
    main()