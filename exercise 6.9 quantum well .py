import numpy as np
import matplotlib.pyplot as plt
import scipy
from pylab import show
from mpl_toolkits.mplot3d import Axes3D
from numpy import sqrt, linspace, sin, cos, pi
from scipy.constants import epsilon_0, pi, hbar

def H_mn(m, n, width, height, e_mass):

    if(m == n):
        kinetic = (pi**2 * n**2 * hbar**2) / (2 * e_mass * width**2)
        potential = height / 2
    elif((m%2) != (n%2)):
        kinetic = 0
        potential = - (8 * height / pi**2) * (m * n) / (m**2 - n**2)**2
    else:
        kinetic = 0
        potential = 0

    energy = kinetic + potential
    return energy

def construct_metric(scale,  width, height, e_mass):

    hamilton = np.empty([scale, scale])
    for row in range (scale):
        for col in range(scale):

            hamilton[row, col] = H_mn(row + 1, col + 1, width, height, e_mass)

    return hamilton


def main():

    scale = 100
    width = 5e-10
    e_mass = 9.1094e-31
    e_charge = 1.6022e-19
    height = 10 * e_charge

    hamilton = construct_metric(scale, width, height, e_mass)
    energy = np.linalg.eigvalsh(hamilton) / e_charge

    print(energy)

main()
