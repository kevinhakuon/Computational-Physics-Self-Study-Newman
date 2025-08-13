import numpy as np
import matplotlib.pyplot as plt
import scipy
from pylab import show
from mpl_toolkits.mplot3d import Axes3D
from numpy import sqrt, linspace, sin, cos, pi, exp
from scipy.constants import epsilon_0, pi, hbar, h, c, k

def binary_search(x_1, x_2, func, tolerance):

    val_1, val_2 = func(x_1), func(x_2)

    if(val_1 * val_2 > 0):
        print(val_1, val_2)
        return "error"
    else:

        while(abs(x_1 - x_2) > tolerance):

            mid = (x_1 + x_2) / 2
            val_mid = func(mid)
                

            if((val_mid * val_1) > 0):
                x_1 = mid
                val_1 = val_mid
            else:
                x_2 = mid
                val_2 = val_mid
            
    return mid
                
def main():

    tolerance = 1e-6
    func = lambda x : 5 * exp(-x) + x - 5
    approx = binary_search(1, 100, func, tolerance)
    print(approx)
    wavelength = 502e-9
    print(h * c / (k * approx * wavelength))

    
main()
