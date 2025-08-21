import numpy as np
import matplotlib.pyplot as plt
import scipy
from mpl_toolkits.mplot3d import Axes3D
from numpy import sqrt, linspace, sin, cos, tan, pi, exp
from numpy import fft
from scipy.constants import epsilon_0, pi, hbar, h, c, k
from scipy.special import roots_legendre

def loaddata(name):

    data = np.loadtxt(name)
    return data

def FFT(y):

    z = fft.rfft(y)

    return z


def main():

    data = loaddata("piano.txt")


    spectrum = FFT(data)

    plt.plot(abs(spectrum))
    plt.xlim(1000, 2000)
    plt.show()


main()
