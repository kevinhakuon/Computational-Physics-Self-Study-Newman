import numpy as np
import matplotlib.pyplot as plt
from numpy import sqrt, linspace
from scipy.special import factorial
from scipy.constants import epsilon_0, pi

def contour_integral(order, resolution):

    
    z_k = lambda k : np.exp(1j * 2 * pi * k / resolution)
    func = lambda z : np.exp(2 * z)
    
    
    k_list = linspace(0, resolution - 1, 1)
    approx = sum(factorial(order) / resolution * (func(z_k(k)) * np.exp(-1j * 2 * pi * k * order / resolution)) for k in range(0, resolution -))

    return approx

def main ():
    
    resolution = 10000
    k = 21
    for order in range(1, k):
        print(contour_integral(order, resolution))


main()
