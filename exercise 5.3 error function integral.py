from math import sqrt, sin, pi
import numpy as np
from numpy import empty, arange, exp
from pylab import imshow, show, gray, plot, scatter

def func(x):
    y = exp(-x**2)
    return y

def Simpson_integral (lower_bound, upper_bound, slices = 1000):
    width = (upper_bound - lower_bound) / slices
    result = func(lower_bound) + func(upper_bound)
    for i in range(1, slices, 2):
        x = lower_bound + i * width
        result += 4 * func(x)
    for i in range(2, slices, 2):
        x = lower_bound + i * width
        result += 2 * func(x)
    
    result = result * width /3
    
    return result

def storedata(lower_bound, upper_bound, slices = 1000):
    x_list = list(np.linspace(lower_bound, upper_bound, slices + 1))
    y_list = []
    for i in range (len(x_list)):
        y_list.append(Simpson_integral(0, x_list[i], slices))
    
    plot(x_list, y_list)
    show()

storedata(0, 10)
