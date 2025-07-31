import numpy as np
from lidar_simulator import simulate_lidar
from visualizer import plot_lidar_scan

# Create an environment: 100x100 grid with obstacles
env = np.zeros((100, 100))
env[50, 80] = 1
env[30:35, 40:45] = 1
env[70:75, 20:25] = 1
import os

data_dir = os.path.join(os.path.dirname(__file__), '..', 'data')
os.makedirs(data_dir, exist_ok=True)

env_path = os.path.join(data_dir, 'sample_environment.npy')
np.save(env_path, env)


# Simulate
angles, distances = simulate_lidar(env)

# Visualize
plot_lidar_scan(angles, distances)
