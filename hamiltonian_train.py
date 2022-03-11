from stable_baselines3 import PPO
import os
from hamiltonian_grid_game import HamiltonianGrid
import time

models_dir = f"models/{int(time.time())}/"
logdir = f"logs/{int(time.time())}/"

if not os.path.exists(models_dir):
	os.makedirs(models_dir)

if not os.path.exists(logdir):
	os.makedirs(logdir)

env = HamiltonianGrid([[0,5], [1,2], [1,7], [6,3]])
env.reset()

model = PPO('MlpPolicy', env, verbose=1, learning_rate=0.001, ent_coef=0.1, tensorboard_log=logdir)

TIMESTEPS = 10000
iters = 0
while True:
	iters += 1
	model.learn(total_timesteps=TIMESTEPS, reset_num_timesteps=False, tb_log_name=f"PPO")
	model.save(f"{models_dir}/{TIMESTEPS*iters}")