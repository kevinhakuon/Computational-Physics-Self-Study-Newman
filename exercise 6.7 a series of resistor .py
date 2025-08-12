import numpy as np
import matplotlib.pyplot as plt
import scipy
from pylab import show
from mpl_toolkits.mplot3d import Axes3D
from numpy import sqrt, linspace, sin, cos
from scipy.constants import epsilon_0, pi


def main():

    N = 100000
    V_postive = 5

    banded_metric = np.zeros([5, N], float)

    banded_metric[0, 2:] = -1
    banded_metric[1, 1:] = -1
    banded_metric[3, :-1] = -1
    banded_metric[4, 0:-2] = -1
    banded_metric[2, :] = 4
    banded_metric[2, 0] = 3
    banded_metric[2, N - 1] = 3
    print(banded_metric)

    v = np.zeros(N, float)
    v[0] = V_postive
    v[1] = V_postive

    V = scipy.linalg.solve_banded((2, 2), banded_metric, v)
    print(V)


main()
