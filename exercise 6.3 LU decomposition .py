import numpy as np
import matplotlib.pyplot as plt
from pylab import show
from mpl_toolkits.mplot3d import Axes3D
from numpy import sqrt, linspace, sin, cos
from scipy.constants import epsilon_0, pi

def LU_decomposition(arr, v):

    row, col = arr.shape
    order = row
    lower_arr = np.empty([order, order], float)

    for i in range (order):
        
        lower_arr[i:order, i] = arr[i:order, i]

        div = arr[i, i]
        arr[i, :] = arr[i, :] / div
        v[i] = v[i] / div

        for m in range (i + 1, order):
            
            multi = arr[m, i]
            arr[m, :] -= multi * arr[i, :]
            v[m] -= multi * v[i]

    upper_arr = arr

    return lower_arr, upper_arr, v, order


def back_substitution(arr, v, order):

    x = np.empty(order, float)

    for i in range(order - 1, -1, -1):
        x[i] = v[i]

        for m in range (i + 1, order):
            
            x[i] -= x[m] * arr[i, m]
    
    return x

def main():
    
    A_i = np.array([[2, 1, 4, 1],
                 [3, 4, -1, -1],
                 [1, -4, 1, 5],
                 [2, -2, 1, 3]], float)
    
    v_i = np.array([-4, 3, 9, 7], float)

    L, U, v_f, order = LU_decomposition(A_i, v_i) 
    x = back_substitution(U, v_f, order)
    y = L * U * v_i

    print(x, y)

main()
