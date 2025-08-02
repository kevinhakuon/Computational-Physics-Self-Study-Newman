import numpy as np
from numpy import empty, arange, sqrt, sin, cos, pi, exp, linspace
from pylab import imshow, show, gray, plot, scatter, axhline, loglog, legend
from scipy.special import roots_legendre, factorial
from scipy.constants import k, hbar, c

#(a) plot wave func

def Hermite_ploynomial (n, x):

    if(n == 0):
        return 1
    elif(n == 1):
        return 2 * x
    else:

        H_mid = 2 * x
        H_min = 1
        for index in range (1, n ):
            H_max = 2 * x * H_mid - 2 * index * H_min
            H_min , H_mid = H_mid, H_max

        return H_max

def plotting(x_lower_bound = -4, x_upper_bound = 4, n_index = 4, sample_point = 100):
    
    wave_func = lambda n, x : (1/ sqrt(2**n * factorial(n) * sqrt(pi))) * exp(-x**2 / 2) * Hermite_ploynomial(n, x)

    x_list = linspace(x_lower_bound, x_upper_bound, sample_point)

    for index in range(n_index + 1):
        H_list = wave_func(index, x_list)
        plot(x_list, H_list, label = f"{index} order quantum harmonic oscillator wave function")

    legend(loc = 'upper right', fontsize = 4, ncol = 3)
    show()

plotting()



(c)
import numpy as np
from numpy import empty, arange, sqrt, sin, cos, tan, pi, exp, linspace
from pylab import imshow, show, gray, plot, scatter, axhline, loglog
from scipy.special import roots_legendre, factorial
from scipy.constants import k, hbar, c


def Hermite_ploynomial (n, x):

    if(n == 0):
        return 1
    elif(n == 1):
        return 2 * x
    else:
        H_mid = 2 * x
        H_min = 1
        for index in range (1, n):
            H_max = 2 * x * H_mid - 2 * index * H_min
            H_min , H_mid = H_min, H_max

        return H_max



class GaussIntegrator:

    def __init__(self, N = 500):
        self.N = N
        self.x, self.w = roots_legendre(N)

    def Gauss_quadrature (self, lower_bound, upper_bound, func ):

        if(lower_bound == upper_bound):
            return  0 

        x_value = (upper_bound - lower_bound) * self.x / 2 + (upper_bound + lower_bound) / 2
        weight = (upper_bound - lower_bound) * self.w / 2

        integral = sum(weight * func(x_value))

        return integral
        

def root_mean_square(n = 5, sample_point = 100):

    wave_func = lambda n, x : (1/ sqrt(2 * factorial(n) * sqrt(pi))) * exp(-x**2 / 2) * Hermite_ploynomial(n, x)

    func = lambda x : (1/ cos(x)**2) * tan(x)**2 * abs(wave_func(n, tan(x)))**2
    
    integral = GaussIntegrator()
    mean_square = integral.Gauss_quadrature(lower_bound = -pi / 2, upper_bound = pi / 2, func = func)

    return sqrt(mean_square)


print(root_mean_square())
