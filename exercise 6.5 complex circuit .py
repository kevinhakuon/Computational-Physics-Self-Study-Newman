import numpy as np
import matplotlib.pyplot as plt
from pylab import show
from mpl_toolkits.mplot3d import Axes3D
from numpy import sqrt, linspace, sin, cos
from scipy.constants import epsilon_0, pi


def main():

    R_1 = R_3 = R_5 = 1e3
    R_2 = R_4 = R_6 = 2e3
    C_1 = 1e-6
    C_2 = 0.5e-6
    x_postive = 3
    frequency = 1e3


    
    arr = np.array([[(1 / R_1 + 1 / R_4 + frequency * C_1 * 1j), -frequency * C_1 * 1j, 0],
                    [-frequency * C_1 * 1j, (1 / R_2 + 1 / R_5 + frequency * (C_1 + C_2) * 1j), -frequency * C_2 * 1j],
                    [0, -frequency * C_2 * 1j, (1 / R_3 + 1 / R_6 + frequency * C_2 * 1j)]])

    
    v = x_postive * np.array([1/ R_1, 1/R_2, 1/R_3])

    x = np.linalg.solve(arr, v)

    r = np.abs(x)
    theta = np.angle(x)

    print(r, theta)

main()
