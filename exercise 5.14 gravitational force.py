import numpy as np
from numpy import empty, arange, sqrt, sin, cos, tan, pi, exp, linspace
from pylab import imshow, show, gray, plot, scatter, axhline, loglog
from scipy.special import roots_legendre, factorial
from scipy.constants import k, hbar, c


G = 6.674e-11
mass_area_density = 1e4 / 100
func = lambda x, y, z : z / (x**2 + y**2 + z**2)**(3/2)

class GaussIntegrator:

    def __init__(self, N = 100):
        self.N = N
        self.x, self.w_x = roots_legendre(N)
        self.y, self.w_y = roots_legendre(N)

    def Gauss_quadrature (self, x_lower_bound, x_upper_bound,
                          y_lower_bound, y_upper_bound, z_value, func = func):

        if(x_lower_bound == x_upper_bound):
            x_integral = 0 
        if(y_lower_bound == y_upper_bound):
            y_integral = 0

        x_value = (x_upper_bound - x_lower_bound) * self.x / 2 + (x_upper_bound + x_lower_bound) / 2
        x_weight = (x_upper_bound - x_lower_bound) * self.w_x / 2

        y_value = (y_upper_bound - y_lower_bound) * self.y / 2 + (y_upper_bound + y_lower_bound) / 2
        y_weight = (y_upper_bound - y_lower_bound) * self.w_y / 2

        integral = sum(sum(x_weight[i] * y_weight[j] * func(x_value[i], y_value[j], z_value) for i in range (len(x_value)))
                       for j in range (len(y_value)) )
        
        print(integral)

        return integral
        

def gravitational_force (z_lower_bound = 0 + 5e-1, z_upper_bound = 10, z_sample_point = 100,
                         x_lower_bound = -5, x_upper_bound = 5,
                         y_lower_bound = -5, y_upper_bound = 5):
    

    z_list = linspace(z_lower_bound, z_upper_bound, z_sample_point)

    integral = GaussIntegrator()

    force_list = integral.Gauss_quadrature(x_lower_bound, x_upper_bound, y_lower_bound, y_upper_bound, z_list)

    scatter(z_list, force_list, s = 0.5)

    show()


gravitational_force()
