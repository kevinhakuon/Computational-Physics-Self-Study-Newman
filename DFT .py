import numpy as np
import matplotlib.pyplot as plt
import scipy
from mpl_toolkits.mplot3d import Axes3D
from numpy import sqrt, linspace, sin, cos, tan, pi, exp
from scipy.constants import epsilon_0, pi, hbar, h, c, k
from scipy.special import roots_legendre


def DFT(y):

    N = len(y)
    c = np.zeros(N // 2 + 1, complex)

    for k in range (N//2 + 1):
        for n in range (N):

            c[k] += y[n] * exp(-2j * pi * k * n / N)

    return c


def main():

    y = np.zeros(1000)
    for i in range(len(y)):
        y[i] = i
    c = DFT(y)

    #plt.plot(y)
    plt.plot(abs(c))
    plt.show()


main()
