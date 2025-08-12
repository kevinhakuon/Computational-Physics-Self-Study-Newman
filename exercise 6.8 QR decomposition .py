import numpy as np
import matplotlib.pyplot as plt
import scipy
from pylab import show
from mpl_toolkits.mplot3d import Axes3D
from numpy import sqrt, linspace, sin, cos
from scipy.constants import epsilon_0, pi

def QR_decomp (arr):

    row, col = arr.shape

    u_arr = np.zeros([row, col], float)
    q_arr = np.zeros([row, col], float)
    r_arr = np.zeros([row, col], float)

    for column in range(col):

        u_arr[:, column] = arr[:, column]

        for index in range (column, 0, -1):
            
            u_arr[:, index] = (arr[:, index] @ q_arr[:, column - index]) * q_arr[:, column - index]

        u_i = u_arr[:, column]
        q_arr[:, column] = u_i / np.linalg.norm(u_i)
        r_arr[column, column] = np.linalg.norm(u_i)


    for i in range(row):

        for j in range(i + 1, col, 1):

            r_arr[i, j] = q_arr[:, i] @ arr[:, j]

    print(r_arr)
    return(q_arr, r_arr)


def main():

    A = np.array([[1, 4, 8, 4],
                  [4, 2, 3, 7],
                  [8, 3, 6, 9],
                  [4, 7, 9, 2]])
    
    Q, R = QR_decomp(A)
    print(Q @ R)


main()
