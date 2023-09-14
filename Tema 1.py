import math
import sympy as sp
import matplotlib.pyplot as plt
import numpy as np
import scipy.special


def curba_bezier(puncte_control, n_points=50):
    traj = []
    for t in np.linspace(0, 1, n_points):
        traj.append(bezier(t, puncte_control))
    return np.array(traj)


def bezier(t, puncte_control):  # (5)
    n = len(puncte_control)
    return np.sum([puncte_control[i] * bernstein(i, n-1, t) for i in range(n)], axis=0)


def bernstein(i, n, t):  # (7)
    return scipy.special.comb(n, i) * (1-t)**(n-i) * t**i


if __name__ == '__main__':
    # 1)
    puncte_control = np.array(
        [[5., 1.], [-2.78, 1.], [-10, 2], [-11.5, -4.5], [-6., -8.], [10, -10], [-10, -12], [10, -13], [-10, -15]])
    graf = curba_bezier(puncte_control)

    fig, ax = plt.subplots()
    ax.plot(graf.T[0], graf.T[1], label="Curba Bezier")
    ax.plot(puncte_control.T[0], puncte_control.T[1], '--o', label="Puncte de Control")
    ax.legend()
    ax.grid(True)
    plt.show()

    # 3)
    uv = math.sqrt(z1**2 + z2**2)
    uo = np.arctan(L * (sp.diff(z2)*z1 - z2*sp.diff(z1)) / (z1**2 + z2**2)**(3/2))
    tau = np.arctan(z2/z1)
