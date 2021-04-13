import gym
from gym.envs.registration import register

from stable_baselines3 import PPO
from stable_baselines3.common.env_util import make_vec_env
from stable_baselines3.ppo.policies import MlpPolicy

from datetime import datetime

now = datetime.now()
current_time = now.strftime("%d_%m_%Y_%H_%M_%S")
filename = "ppo_warehouse_sort_"+ str(current_time)
print("Model will be saved at ", filename)
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
model.learn(total_timesteps=120000)
model.save(filename)

obs = env.reset()
while True:
    action, _states = model.predict(obs)
    obs, rewards, dones, info = env.step(action)
    env.render()

    if dones:
        env.reset()