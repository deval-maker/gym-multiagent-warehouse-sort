import gym
from gym.envs.registration import register

from stable_baselines3 import PPO
from stable_baselines3.common.env_util import make_vec_env
from stable_baselines3.ppo.policies import MlpPolicy

from datetime import datetime
import time
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--file', type=str, help='Model file to load')
args = parser.parse_args()

class CustomPolicy(MlpPolicy):
    def __init__(self, *args, **kwargs):
        super(CustomPolicy, self).__init__(*args, **kwargs,
                                           net_arch=[64, 64, dict(pi=[64, 64], vf=[64, 64])])

    def _get_torch_save_params(self):
        state_dicts = ["policy", "policy.optimizer", "policy.lr_scheduler"]

        return state_dicts, []

register(
    id='warehouse-sort-v0', 
    entry_point='gym_multigrid.envs:WarehouseSortEnvN1'
)

env = gym.make('warehouse-sort-v0')

model = PPO(CustomPolicy, env, verbose=1)
model = PPO.load(args.file)

obs = env.reset()
while True:
    time.sleep(0.1)
    action, _states = model.predict(obs)
    obs, rewards, dones, info = env.step(action)
    print(action)
    print(obs)
    print("Reward:", rewards)
    env.render()
    
    if dones:
        env.reset()
    
