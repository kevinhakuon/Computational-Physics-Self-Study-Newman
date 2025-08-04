import numpy as np
from numpy import cos, sin
from pylab import plot, show, ylim, xlabel, ylabel
split = 1000
def plotting(x_list, y_list):
    plot(x_list, y_list)
    show()

def deltoid_curve():
    x_deltoid = []
    y_deltoid = []
    for i in range (split):
        theta = 2 * np.pi * i / split
        x_deltoid.append(2 * cos(theta) + cos(theta*2))
        y_deltoid.append(2 * sin(theta) - sin(theta*2))
    return x_deltoid, y_deltoid

def Galilean_Spiral ():
    x_spiral = []
    y_spiral = []
    for i in range (split):
        theta = 10 * np.pi * i / split
        x_spiral.append(cos(theta) * theta**2)
        y_spiral.append(sin(theta) * theta**2)
    return x_spiral, y_spiral

def Feys_func():
    x_fey = []
    y_fey = []
    for i in range (split):
        theta = 24 * np.pi * i / split
        x_fey.append(np.e**(cos(theta)) * cos(theta) - 2 * cos(theta * 4) * cos(theta) + sin(theta/12)**5 * cos(theta))
        y_fey.append(np.e**(cos(theta)) * sin(theta) - 2 * cos(theta * 4) * sin(theta) + sin(theta/12)**5 * sin(theta))
    return x_fey, y_fey

plotting(*deltoid_curve())
plotting(*Galilean_Spiral())
plotting(*Feys_func())
