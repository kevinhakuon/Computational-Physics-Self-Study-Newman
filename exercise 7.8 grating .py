import numpy as np
import matplotlib.pyplot as plt
import scipy
import math as mt
from mpl_toolkits.mplot3d import Axes3D
from numpy import sqrt, linspace, sin, cos, tan, pi, exp
from scipy import fft
from scipy.constants import epsilon_0, pi, hbar, h, c, k
from scipy.special import roots_legendre

def loaddata(name):

    data = np.loadtxt(name)
    return data

def main():

    sample_point = 4096

    fraction_width = 200e-6
    W = 10 * fraction_width
    wavelength = 500e-9
    f = 1
    screen_width = 0.1

    alpha = np.pi / 20e-6

    q = lambda u : np.sin(alpha * u)**2
    y = lambda u : np.sqrt(q(u))

    y_list = np.zeros(sample_point, float)
    u_list = (np.linspace(-W / 2, W / 2, sample_point))
    mask = (np.abs(u_list) <= fraction_width / 2)
    y_list[mask] = y(u_list[mask])

    c_list = scipy.fft.fft(y_list)
    c_shift = fft.fftshift(c_list)

    k_list = fft.fftfreq(sample_point, d = 1.0) * sample_point
    k_shift = fft.fftshift(k_list)

    x_list = wavelength * f / W * k_shift

    I_list = W**2 / sample_point**2 * np.abs(c_shift)**2

    mask_x = (np.abs(x_list) <= 0.05)
    plt.plot(x_list[mask_x], I_list[mask_x])
    plt.show()

main()
