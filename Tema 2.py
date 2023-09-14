import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np


def potential_field(p0, p1, obstacles, destination):
    sum = 0
    for ci in obstacles:
        dist_ci = np.sqrt((abs(p0 - ci[0])) ** 2 + (abs(p1 - ci[1])) ** 2)
        sum = sum + 1 / (1 + dist_ci)

    dist_dest = np.sqrt((abs(p0 - destination[0])) ** 2 + (abs(p1 - destination[1])) ** 2)

    potential_field = dist_dest + sum

    return potential_field


def apply_command(p0, p1, obstacles, destination):
    command = [-((p0 - destination[0]) / np.sqrt((abs(p0 - destination[0])) ** 2 + (abs(p1 - destination[1])) ** 2)),
               -((p1 - destination[1]) / np.sqrt((abs(p0 - destination[0])) ** 2 + (abs(p1 - destination[1])) ** 2))]
    for ci in obstacles:
        dist_ci = np.sqrt((abs(p0 - ci[0])) ** 2 + (abs(p1 - ci[1])) ** 2)
        sum = -1 / (1 + dist_ci) ** 2
        command[0] += sum * (p0 - ci[0]) / dist_ci
        command[1] += sum * (p1 - ci[1]) / dist_ci
    return command


if __name__ == '__main__':

    # 1
    fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
    X = np.arange(-10, 15, 0.2)
    Y = np.arange(-12, 2, 0.3)
    X, Y = np.meshgrid(X, Y)
    Z = potential_field(X, Y, [[-4, 2]], (12, 10))

    graph = ax.plot_surface(X, Y, Z, cmap=cm.coolwarm, linewidth=0, antialiased=False)

    plt.show()
