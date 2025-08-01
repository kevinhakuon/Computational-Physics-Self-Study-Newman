import numpy as np
from numpy import empty, arange, sqrt, sin, pi
from pylab import imshow, show, gray, plot, scatter


lower_bound = 0
upper_bound = 1
tolerance = 1e-6

func = lambda x : sin(sqrt(100 * x))**2

def Adaptive_Simpson_integral ( lower_bound, upper_bound, S_sum = 0, T_sum = 0, integral = 0
                               , slices = 2, func = func, tolerance = tolerance):

    width = (upper_bound - lower_bound) / slices

    if(integral == 0):
        S_sum = (func(lower_bound) + func(upper_bound)) / 3
        T_sum = func(lower_bound + width) * 2 /3
        
        integral = (S_sum + T_sum * 2) * width

        return Adaptive_Simpson_integral(lower_bound, upper_bound, S_sum, T_sum,
                                          integral, 2 * slices)
    else:
        S_sum = S_sum + T_sum
        T_sum = 0

        for i in range(1, slices, 2):
            x = lower_bound + i * width
            T_sum += 2 * func(x) / 3


    previous_integral = integral
    integral = (S_sum + T_sum * 2) * width

    error = abs(integral - previous_integral) / 15
    if(error > tolerance):
        return Adaptive_Simpson_integral(lower_bound, upper_bound, S_sum, T_sum,
                                            integral, 2 * slices) 
    else:
        return integral, error
            

print(Adaptive_Simpson_integral(0, 1))
