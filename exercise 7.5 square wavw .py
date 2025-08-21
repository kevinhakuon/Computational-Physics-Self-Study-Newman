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

    t_list = np.linspace(0, 1, 1000)
    data = np.floor(2 * t_list)
    #data -= np.mean(data)

    spectrum = FFT(data)
    spectrum[10:] = 0
    
    p_data = IFFT(spectrum)
    #p_data += np.mean(p_data)

    plt.plot(t_list, data)
    plt.plot(t_list, p_data, '--')
    #plt.xlim(0, 100)
    plt.show()


main()
