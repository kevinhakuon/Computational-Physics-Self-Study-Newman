from math import sqrt, sin, pi
import numpy as np
from numpy import empty, arange
from pylab import imshow, show, gray, plot, scatter

def loaddata(filename):
    data = np.loadtxt(filename, float)
    time = data[:, 0]
    x_velocity = data[:, 1]
    return time, x_velocity


def trapezoidal(t_final, x_velocity):
    displacement = 0.0
    displacement += x_velocity[t_final] / 2

    for i in range (t_final):
        displacement += x_velocity[i]

    return displacement

time, x_velocity = loaddata("velocities.txt")
x_displacement = []
for i in range(len(time)):
    x_displacement.append(trapezoidal(i, x_velocity))

def plotting (x_list, y_list, z_list):
    plot(x_list, y_list, "k-")
    plot(x_list, z_list, "b--")
    show()

plotting(time, x_velocity, x_displacement)
