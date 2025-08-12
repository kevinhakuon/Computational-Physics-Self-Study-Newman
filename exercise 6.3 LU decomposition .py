import numpy as np
import matplotlib.pyplot as plt
from pylab import show
from mpl_toolkits.mplot3d import Axes3D
from numpy import sqrt, linspace, sin, cos
from scipy.constants import epsilon_0, pi

def LU_decomposition(arr, v):

    row, col = arr.shape
    order = row
    lower_arr = np.zeros([order, order], float)

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


def upper_back_substitution(arr, v, order):

    x = np.empty(order, float)

    for i in range(order - 1, -1, -1):
        x[i] = v[i]

        for m in range (i + 1, order):
            
            x[i] -= x[m] * arr[i, m]
    
    return x

def lower_back_substitution(arr, v, order):

    x = np.zeros(order, float)
    print(v)


    for i in range(order):

        x[i] = v[i]
        print(x)

        for m in range (0, i, 1):
            
            x[i] -= x[m] * arr[i, m]
        
        x[i] = x[i] / arr[i, i]
        arr[i, i] /= arr[i, i]

    return x

def main():
    
    A_i = np.array([[2, 1, 4, 1],
                 [3, 4, -1, -1],
                 [1, -4, 1, 5],
                 [2, -2, 1, 3]], float)
    
    v_i = np.array([-4, 3, 9, 7], float)
    v = v_i.copy()

    L, U, v_f, order = LU_decomposition(A_i, v) 
    y = lower_back_substitution(L, v_i, order)
    x = upper_back_substitution(U, y, order)

    result = np.linalg.solve(A_i, v)

    print(x, y)
    print(result)

main()
