import numpy as np
from numpy import empty, arange, sqrt, sin, cos, pi, exp, linspace
from pylab import imshow, show, gray, plot, scatter, axhline, loglog
from scipy.special import roots_legendre
from scipy.constants import k, hbar, c


tolerance = 1e-4
func = lambda x : sin(x)**2 / x**2

def adaptive_trapezoidal (lower_bound, upper_bound,
                        tolerance = tolerance, func = func):   

        width = upper_bound - lower_bound
        width_d = width / 2
        mid = (upper_bound + lower_bound) / 2

        integral_single = (func(lower_bound) + func(upper_bound)) * width / 2
        integral_double = integral_single / 2 + func(mid) * width_d

        error = abs((integral_single - integral_double)) / 3

        if(error > tolerance):

            integral_fixed = adaptive_trapezoidal(lower_bound, mid, tolerance = tolerance / 2)
            + adaptive_trapezoidal(mid, upper_bound, tolerance = tolerance / 2)

            return integral_fixed
        else:
            return integral_double
    

print(adaptive_trapezoidal(0 + tolerance, 10))
