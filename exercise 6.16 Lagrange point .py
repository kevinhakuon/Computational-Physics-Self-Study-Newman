import numpy as np
import matplotlib.pyplot as plt
import scipy
from pylab import show, scatter, plot, ylim
from mpl_toolkits.mplot3d import Axes3D
from numpy import sqrt, linspace, sin, cos, tan, pi, exp
from scipy.constants import epsilon_0, pi, hbar, h, c, k


def secant_method(func, initial_point, tolerance):

    x_1 = initial_point
    delta = 1e8
    x_2 = initial_point + delta
    val_1 = func(x_1)
    val_2 = func(x_2)

    while(abs(delta) > tolerance):

        delta = (val_2) * (x_2 - x_1) / (val_2 - val_1)

        x_1 = x_2
        val_1 = val_2
        x_2 -= delta
        val_2 = func(x_2)

    return x_2
                
def main():

    tolerance = 1e-5 # I finally found that the tolerance(accuracy) does not need to be 1e-10, for this kind of big scale, 1e-3 to 1e-5 is enough
    G = 6.674e-11
    M = 5.974e24
    m = 7.348e22
    R = 3.844e8
    omega = 2.662e-6


    func = lambda r : (G * M / r**2) - (G * m / (R - r)**2) - omega**2 * r
    
    
    r_list = linspace(2.5e8, 3.8e8, 10000)
    arr = np.array(r_list)
    l_list = (func(arr))
    y = np.zeros(10000)
              
    plot(r_list, l_list)
    plot(r_list, y)
    ylim = (-10, 10)
    show()

    lagrange_point = secant_method(func, 2.5e8, tolerance)
    print(lagrange_point)
    

main()
