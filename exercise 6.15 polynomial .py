import numpy as np
import matplotlib.pyplot as plt
import scipy
from pylab import show, scatter, plot, ylim
from mpl_toolkits.mplot3d import Axes3D
from numpy import sqrt, linspace, sin, cos, tan, pi, exp
from scipy.constants import epsilon_0, pi, hbar, h, c, k


def polynomial(func, func_deri, initial_point, tolerance):

    x = initial_point
    delta = 1.0

    while(abs(delta) > tolerance):

        delta = (func(x)) / func_deri(x)
        x -=delta


    return x
                
def main():

    tolerance = 1e-10
    func = lambda x : 924 * x**6 - 2772 * x**5 + 3150 * x**4 - 1680 * x**3 + 420 * x**2 - 42 * x + 1
    func_derivative = lambda x : 6 * 924 * x**5 - 5 * 2772 * x**4 + 4 * 3150 * x**3 - 3 * 1680 * x**2 + 840 * x - 42

    x = [0.0, 0.2, 0.4, 0.6, 0.8, 1.0]
    y = np.empty(6)

    for x_index, x_val in enumerate(x):
        y[x_index] = (polynomial(func, func_derivative, x_val, tolerance))

    print(y)

    x_list = linspace(0, 1, 100)
    y_list = func(x_list)
    horizon = np.zeros(100)

    plot(x_list, y_list)
    plot(x_list, horizon)
    show()
    
    

main()
