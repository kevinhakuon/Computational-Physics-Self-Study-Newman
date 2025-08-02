import numpy as np
from numpy import empty, arange, sqrt, sin, pi, exp
from pylab import imshow, show, gray, plot, scatter, axhline, loglog
from scipy.special import roots_legendre
from scipy.constants import k



func = lambda a, x : sqrt(8) / sqrt(a**4 - x**4)

def Gauss_quadrature (lower_bound, upper_bound, N = 20, func = func):

    if(lower_bound == upper_bound):
        return  
    else:
        x, w = roots_legendre(N)

        x_value = (upper_bound - lower_bound) * x / 2 + (upper_bound + lower_bound) / 2
        weight = (upper_bound - lower_bound) * w / 2

        a = upper_bound
        integral = sum(weight * func(a, x_value))

        return integral

def plot_Harmonic_Oscillator (amplitude, N = 500):

    a_list = np.linspace (0.01, 2, N) 
    period_list = []

    for amplitude in a_list:
        period_list.append(Gauss_quadrature(0.01, amplitude))

    scatter(a_list, period_list, s = 1)
    show()


plot_Harmonic_Oscillator(2)
