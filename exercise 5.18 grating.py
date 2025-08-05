import numpy as np
from numpy import empty, arange, sqrt, sin, cos, pi, exp, linspace
from pylab import imshow, show, gray, plot, scatter, axhline, loglog
from scipy.special import roots_legendre
from scipy.constants import k, hbar, c


def intensity_tran_func (u, seperation = 20e-6):
    
    alpha = pi / seperation

    intensity_rate = sin(alpha * u)**2

    return(intensity_rate)

class GaussIntegrator:

    def __init__(self, N = 1000):
        self.N = N
        self.x, self.w = roots_legendre(N)

    def Gauss_quadrature (self, lower_bound, upper_bound, func, parameter):

        if(lower_bound == upper_bound):
            return  0 

        x_value = (upper_bound - lower_bound) * self.x / 2 + (upper_bound + lower_bound) / 2
        weight = (upper_bound - lower_bound) * self.w / 2

        integral = sum(weight[i] * func(parameter, x_value[i]) for i in range (len(x_value)))

        return integral
        
def Intensity (wavelength = 500e-9, seperation = 20e-6, slit_num = 6,
               screen_wide = 10e-2, focal_length = 1, sample_point = 1000):
    
    total_width = seperation * (slit_num - 1)

    intensity_integrand = lambda x, u : (sqrt(intensity_tran_func(u)) * exp(2 * pi * x * u * 1j / (wavelength * focal_length)))

    x_list = linspace(-screen_wide / 2, screen_wide / 2, sample_point)

    integral = GaussIntegrator()
    intensity_list = abs(integral.Gauss_quadrature(-total_width / 2, total_width / 2, intensity_integrand, x_list)) ** 2

    plot(x_list, intensity_list / np.max(intensity_list))
    show()

    return x_list, intensity_list

def density_plot(x_list, intensity_list):

    density_distribution = empty([100, len(x_list)], float)
    intensity_maxi = np.max(intensity_list)
    for i in range (len(x_list)):
        density_distribution[:, i] = intensity_list[i]  / intensity_maxi


    imshow((density_distribution), vmin = 0)# if u want to clearly see the pattern, u need to set vmax = 0.17
    show()


density_plot(*Intensity())
# I'm not sure about the graph is correct or not, but the number of pattern would not changed with different slit_number so I think there's might be something wrong.

import numpy as np
from numpy import empty, arange, sqrt, sin, cos, pi, exp, linspace
from pylab import imshow, show, gray, plot, scatter, axhline, loglog
from scipy.special import roots_legendre
from scipy.constants import k, hbar, c


def intensity_tran_func (u, seperation = 20e-6):
    
    if(u >= -45e-6 and u<=-35e-6):
        intensity_rate = 1
    elif(u <= 45e-6 and u>= 1e-6):
        intensity_rate = 1
    else:
        intensity_rate = 0

    return(intensity_rate)

class GaussIntegrator:

    def __init__(self, N = 1000):
        self.N = N
        self.x, self.w = roots_legendre(N)

    def Gauss_quadrature (self, lower_bound, upper_bound, func, parameter):

        if(lower_bound == upper_bound):
            return  0 

        x_value = (upper_bound - lower_bound) * self.x / 2 + (upper_bound + lower_bound) / 2
        weight = (upper_bound - lower_bound) * self.w / 2

        integral = sum(weight[i] * func(parameter, x_value[i]) for i in range (len(x_value)))

        return integral
        
def Intensity (wavelength = 500e-9, seperation = 20e-6, slit_num = 4,
               screen_wide = 10e-2, focal_length = 1, sample_point = 1000):
    
    total_width = 90e-6

    intensity_integrand = lambda x, u : (sqrt(intensity_tran_func(u)) * exp(2 * pi * x * u * 1j / (wavelength * focal_length)))

    x_list = linspace(-screen_wide / 2, screen_wide / 2, sample_point)

    integral = GaussIntegrator()
    intensity_list = abs(integral.Gauss_quadrature(-total_width / 2, total_width / 2, intensity_integrand, x_list)) ** 2

    plot(x_list, intensity_list) #/ np.max(intensity_list))
    show()

    return x_list, intensity_list

def density_plot(x_list, intensity_list):

    density_distribution = empty([100, len(x_list)], float)
    intensity_maxi = np.max(intensity_list)
    for i in range (len(x_list)):
        density_distribution[:, i] = intensity_list[i]  / intensity_maxi


    imshow((density_distribution), vmin = 0)# if u want to clearly see the pattern, u need to set vmax = 0.17
    show()


density_plot(*Intensity())
# I'm not sure about the graph is correct or not, but the number of pattern would not changed with different slit_number evidently, so I think there's might be something wrong.
