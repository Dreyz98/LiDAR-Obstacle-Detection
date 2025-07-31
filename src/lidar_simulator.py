import numpy as np

def simulate_lidar(environment, angle_resolution=1):
    """
    Simulate LiDAR readings in a 2D grid environment.
    :param environment: 2D numpy array where 1=obstacle, 0=free
    :param angle_resolution: degrees between beams
    :return: distances array
    """
    center = (environment.shape[0] // 2, environment.shape[1] // 2)
    max_range = min(environment.shape) // 2
    angles = np.arange(0, 360, angle_resolution)
    distances = []

    for angle in angles:
        rad = np.deg2rad(angle)
        for r in range(1, max_range):
            x = int(center[0] + r * np.cos(rad))
            y = int(center[1] + r * np.sin(rad))
            if (0 <= x < environment.shape[0]) and (0 <= y < environment.shape[1]):
                if environment[x, y] == 1:
                    distances.append(r)
                    break
        else:
            distances.append(max_range)
    
    return angles, distances
