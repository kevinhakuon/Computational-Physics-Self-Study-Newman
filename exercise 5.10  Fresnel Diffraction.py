import numpy as np
from numpy import empty, arange, sqrt, sin, cos, pi, exp, linspace
from pylab import imshow, show, gray, plot, scatter, axhline, loglog
from scipy.special import roots_legendre
from scipy.constants import k

C_func = lambda t : cos(pi * t**2 / 2)
S_func = lambda t : sin(pi * t**2 / 2)

N = 1500
x, w = roots_legendre(N)

class GaussIntegrator:

    def __init__(self, N):
        self.N = N
        self.x, self.w = roots_legendre(N)

    def Gauss_quadrature (self, lower_bound, upper_bound, func):

        if(lower_bound == upper_bound):
            return  0 

        x_value = (upper_bound - lower_bound) * x / 2 + (upper_bound + lower_bound) / 2
        weight = (upper_bound - lower_bound) * w / 2

        integral = sum(weight * func(x_value))

        return integral
        


def near_field_diffraction (x_lower_bound = -30, x_upper_bound = 30, z_location = 3, wavelength = 1, N = 2000):
    
    u = lambda x, z : x * sqrt(2 / (wavelength * z))

    x_list = linspace(x_lower_bound, x_upper_bound, N)
    u_list = u(x_list, z_location)

    Intensity = []

    G = GaussIntegrator(N=100)
    
    for u_value in u_list:
        Intensity.append(((2 * G.Gauss_quadrature(0, u_value, C_func) + 1)**2 +
                        (2 * G.Gauss_quadrature(0, u_value, S_func) + 1)**2) / 8)
    
    plot(x_list, Intensity)
    show()


near_field_diffraction()
