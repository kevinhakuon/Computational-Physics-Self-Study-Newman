import numpy as np
from numpy import empty, arange, sqrt, sin, cos, pi, exp, linspace
from pylab import imshow, show, gray, plot, scatter, axhline, loglog
from scipy.special import roots_legendre
from scipy.constants import k, hbar, c


tolerance = 1e-4
func = lambda x : sin(x)**2 / x**2
x_list = []

def adaptive_trapezoidal (x_list, lower_bound, upper_bound, f_lower, f_upper,
                        tolerance = tolerance, func = func):   

        width = upper_bound - lower_bound
        width_d = width / 2
        mid = (upper_bound + lower_bound) / 2
        x_list.append(mid)
        f_mid = func(mid)

        integral_single = (f_lower + f_upper) * width / 2
        integral_double = integral_single / 2 + f_mid * width_d

        error = abs((integral_single - integral_double)) / 3

        if(error > tolerance):

            integral_fixed = (adaptive_trapezoidal(x_list, lower_bound, mid, f_lower, f_mid,
            tolerance = tolerance / 2)+ adaptive_trapezoidal(x_list, mid, upper_bound,
            f_mid, f_upper, tolerance = tolerance / 2))

            return integral_fixed
        else:
            return integral_double
    
print(adaptive_trapezoidal(x_list, 0 + tolerance, 10, func(0 + tolerance), func(10)))
x_list.append(0 + tolerance)
x_list.append(10)
x_list.sort()
y_list = func(np.array(x_list))
scatter(x_list, y_list, s = 0.5)
show()

