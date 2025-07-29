from math import sqrt, sin, pi
import numpy as np
from numpy import empty, arange
from pylab import imshow, show, gray, plot, scatter

N = 10000

def f(x):
    y = sqrt(1 - x**2)
    return y

def approx (trial_time, function, lower_bound, upper_bound):
    result = 0.0
    width = (upper_bound - lower_bound) / trial_time
    for i in arange (lower_bound, upper_bound, width):
        height = function(i)
        result += width * height
    print(result)

approx(N, f, -1, 1)

