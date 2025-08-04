import numpy as np
from numpy import empty, arange, sqrt, sin, cos, pi, exp, linspace
from pylab import imshow, show, gray, plot, scatter, axhline, loglog
from scipy.special import roots_legendre
from scipy.constants import k, hbar, c

#(c), (d)

func = lambda a, x : (a - 1) * np.log(x) - x
func_exp = lambda a, x : exp(func(a, x))
variation = lambda  a, z : func_exp(a, (z * (a - 1) / (1 - z))) * ((a - 1) / (1 - z)**2)

class GaussIntegrator:

    def __init__(self, N = 100):
        self.N = N
        self.x, self.w = roots_legendre(N)

    def Gauss_quadrature (self, order, lower_bound, upper_bound, func = variation):

        if(lower_bound == upper_bound):
            return  0 

        x_value = (upper_bound - lower_bound) * self.x / 2 + (upper_bound + lower_bound) / 2
        weight = (upper_bound - lower_bound) * self.w / 2

        integral = sum(weight * func(order, x_value))

        return integral
        


def Gamma_func (order = 3/2, x_lower_bound = 0 + 1e-5, x_upper_bound = 1 - 1e-5, sample_point = 500):

    x_list = linspace(x_lower_bound, x_upper_bound, sample_point)

    integral = GaussIntegrator()

    h = 1e-7

    
    #for order in range (2, a + 1):
        # #(a)
        # integrand = func(order, x_list)
        # plot(x_list, integrand)


        # #(b)
        # derivative = abs((func(order, x_list + (h / 2)) - func(order, x_list - (h / 2))) / h)
        # mini_x = np.argmin(derivative)
        # print(x_list[mini_x])

    #e
    #gamma_func = integral.Gauss_quadrature(order, x_lower_bound, x_upper_bound)

    #f
    for i in [3, 6, 10]:
        gamma_func = integral.Gauss_quadrature(i, x_lower_bound, x_upper_bound)
        print(gamma_func)

    #show()

    return(gamma_func)


Gamma_func()
