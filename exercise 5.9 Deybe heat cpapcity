import numpy as np
from numpy import empty, arange, sqrt, sin, pi, exp
from pylab import imshow, show, gray, plot, scatter
from scipy.special import roots_legendre
from scipy.constants import k



func = lambda x : x**4 * exp(x) / (exp(x) - 1)**2

def Gauss_quadrature (lower_bound, upper_bound, N = 50, func = func):
    
    x, w = roots_legendre(N)

    x_value = (upper_bound - lower_bound) * x / 2 + (upper_bound + lower_bound) / 2
    weight = (upper_bound - lower_bound) * w / 2

    integral = sum(weight + func(x_value))

    return integral

def Debye_Heat_Capacity (temperature, volume = 1000e-6,
                          rho = 6.022e28, Deybe_temperature = 428, func = func):
    
    heat_capacity = 9 * volume * rho * k * (temperature / Deybe_temperature)**3 * Gauss_quadrature(0, (Deybe_temperature / temperature))

    return heat_capacity

def plot_capacity(lower_bound, upper_bound, N):

    temperature_list = np.linspace(lower_bound, upper_bound, N)
    heat_capacity = []

    for temperature in temperature_list:
        heat_capacity.append(Debye_Heat_Capacity(temperature))

    plot(temperature_list, heat_capacity)
    show()


plot_capacity(5, 500, 500)
