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

def IFFT(z):

    y = fft.irfft(z)

    return y

def main():

    data = loaddata("dow.txt")
    data -= np.mean(data)


    spectrum = FFT(data)
    threshold = int(len(spectrum) * 0.1)
    p_spectrum = np.zeros(len(spectrum), complex)
    p_spectrum[:threshold] = True

    p_spectrum = np.where(p_spectrum, spectrum, 0)
    
    p_data = IFFT(p_spectrum)

    plt.plot(data)
    plt.plot(p_data, '--')
    #plt.xlim(0, 100)
    plt.show()


main()
