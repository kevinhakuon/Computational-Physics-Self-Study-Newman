import numpy as np
import matplotlib.pyplot as plt
import scipy
from mpl_toolkits.mplot3d import Axes3D
from numpy import sqrt, linspace, sin, cos, tan, pi, exp
from scipy import fft
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

def DCT(y):

    z = fft.dct(y)

    return z

def IDCT(z):

    y = fft.idct(z)

    return y

def main():

    data = loaddata("dow2.txt")
    #data -= np.mean(data)

    spectrum_f = FFT(data)
    spectrum_c = DCT(data)

    threshold_1 = int(0.02 * len(spectrum_f))
    threshold_2 = int(0.02 * len(spectrum_c))
    spectrum_f[threshold_1 :] = 0
    spectrum_c[threshold_2 :] = 0


    p_data_f = IFFT(spectrum_f)
    p_data_c = IDCT(spectrum_c)
    

    plt.plot(data)
    plt.plot(p_data_f, '--')
    plt.plot(p_data_c, '--')
    #plt.xlim(0, 100)
    plt.show()


main()
