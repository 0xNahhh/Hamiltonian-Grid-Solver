from stable_baselines3.common.env_checker import check_env
from hamiltonian_grid_game import HamiltonianGrid

env = HamiltonianGrid([[0,5], [1,2], [1,7], [6,3]])
env.reset()
actions = [3, 3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 2, 1, 2, 2, 2, 2, 2, 3, 2, 2, 3, 3, 3, 3, 3]

for action in actions:
  env.step(action)

# episodes = 1

# for episode in range(episodes):
#   done = False
#   obs = env.reset()
#   while True:
#     random_action = env.action_space.sample()
#     print("action: ", random_action)
#     obs, reward, done, info = env.step(random_action) 
#     print("reward: ", reward) 
#     if (done == True):
#       env.reset()
		