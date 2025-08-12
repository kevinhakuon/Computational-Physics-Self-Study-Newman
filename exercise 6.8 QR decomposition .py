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

        for index in range (0, column, 1):
            
            u_arr[:, column] -= (arr[:, column] @ q_arr[:, index]) * q_arr[:, index]

        u_i = u_arr[:, column]
        q_arr[:, column] = u_i / np.linalg.norm(u_i)
        r_arr[column, column] = np.linalg.norm(u_i)


    for i in range(row):

        for j in range(i + 1, col, 1):

            r_arr[i, j] = q_arr[:, i] @ arr[:, j]

    return(q_arr, r_arr)

def find_eigen(A_i, row, column, tolerance):

    V = np.eye(row)
    A = A_i.copy()
    diagonal = False

    while(diagonal == False):

        Q, R = QR_decomp(A)
        A = R @ Q
        V = V @ Q

        diagonal = True

        for i in range (row):
            for j in range(column):

                if(i != j and A[i, j] > tolerance):
                    diagonal = False

    eigenvalue = A.diagonal()

    return(eigenvalue, V)
        


def main():

    tolerance = 1e-6
    A = np.array([[1, 4, 8, 4],
                  [4, 2, 3, 7],
                  [8, 3, 6, 9],
                  [4, 7, 9, 2]])
    
    row, col = A.shape
    eigenval, eignefunc = find_eigen(A, row, col, tolerance)

    print(eigenval)
    print(eignefunc)


main()
