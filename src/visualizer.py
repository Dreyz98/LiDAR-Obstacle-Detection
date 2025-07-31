import numpy as np
import matplotlib.pyplot as plt

def plot_lidar_scan(angles, distances):
    x = distances * np.cos(np.radians(angles))
    y = distances * np.sin(np.radians(angles))

    plt.figure(figsize=(6, 6))
    plt.plot(x, y, 'r.')
    plt.title("LiDAR Obstacle Detection")
    plt.xlabel("X (units)")
    plt.ylabel("Y (units)")
    plt.grid(True)
    plt.axis('equal')
    plt.show()
