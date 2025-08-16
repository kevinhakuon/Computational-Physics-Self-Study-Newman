import numpy as np
import matplotlib.pyplot as plt
import scipy
from mpl_toolkits.mplot3d import Axes3D
from numpy import sqrt, linspace, sin, cos, tan, pi, exp
from scipy.constants import epsilon_0, pi, hbar, h, c, k
from scipy.special import roots_legendre


def DFT(y):

    N = len(y)
    c = np.zeros(N // 2 + 1, dtype = complex)

    for k in range (N//2 + 1):
        for n in range (N):

            c[k] += y[n] * np.exp(-2j * pi * k * n / N)

    return c


def main():

    data = np.loadtxt("sunspots.txt")
    month = data[:, 0]
    sunspots = data[:, 1]

    sunspots -= sunspots.mean()

    power_spectrum = (abs(DFT(sunspots)))**2

    plt.plot(power_spectrum)
    plt.xlim(0, 100)
    plt.show()


main()
