from stable_baselines3.common.env_checker import check_env
from hamiltonian_grid_game import HamiltonianGrid

env = HamiltonianGrid()
check_env(env)
