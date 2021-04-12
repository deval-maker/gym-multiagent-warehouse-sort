import gym
import time
from gym.envs.registration import register
import argparse

parser = argparse.ArgumentParser(description=None)
parser.add_argument('-e', '--env', default='soccer', type=str)

args = parser.parse_args()

def main():

    if args.env == 'soccer':
        register(
            id='multigrid-soccer-v0',
            entry_point='gym_multigrid.envs:WarehouseSortEnvN1',
        )
        env = gym.make('multigrid-soccer-v0')

    else:
        register(
            id='multigrid-collect-v0',
            entry_point='gym_multigrid.envs:CollectGame4HEnv10x10N2',
        )
        env = gym.make('multigrid-collect-v0')

    _ = env.reset()

    nb_agents = len(env.agents)

    while True:
        env.render(mode='human', highlight=True)
        time.sleep(0.1)

        ac = [env.action_space.sample() for _ in range(nb_agents)]

        ac = input('Enter')
        print(ac)
        ac = [int(ac)]
        obs, _, done, _ = env.step(ac)

        if done:
            break

if __name__ == "__main__":
    main()