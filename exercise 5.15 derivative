import numpy as np
from numpy import empty, arange, sqrt, sin, cos, tan, pi, exp, linspace
from pylab import imshow, show, gray, plot, scatter, axhline, loglog, tanh
from scipy.special import roots_legendre, factorial
from scipy.constants import k, hbar, c


func = lambda x : 1 + tanh(2 * x) / 2

def derivative (x_lower_bound = -2, x_upper_bound = 2, sample_point = 100, func = func, h = 1e-4):

    x_list = linspace(x_lower_bound, x_upper_bound, sample_point)

    f_list = func(x_list)

    f_derivative = (func(x_list + h / 2) - func(x_list - h / 2)) / h

    plot(x_list, f_list)
    plot(x_list, f_derivative)
    show()


derivative()
