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

def fft2D(y):

    c = fft.fft2(y)

    return c

def ifft2D(c):

    y = fft.ifft2(c)

    return y

def main():

    sigma = 25
    data = loaddata("blur.txt")
    row, col = data.shape

    sample_num = row

    gauss = lambda x, y : exp(-0.5 * (x**2 + y**2) / sigma**2)

    x_list = np.linspace(-row // 2, row // 2, sample_num)
    y_list = np.linspace(-col // 2, col // 2, sample_num)

    X, Y = np.meshgrid(x_list, y_list)

    gauss_list = gauss(X, Y)
    gauss_list /= gauss_list.sum()

    g_k = fft2D(fft.ifftshift(gauss_list))
    b_k = fft2D(data)

    a_k = b_k / (g_k * row * col)

    a = ifft2D(a_k)

    plt.imshow(gauss_list)
    plt.show()
    plt.imshow(np.abs(a), cmap='gray')
    plt.show()

main()
