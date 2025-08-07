import numpy as np
from numpy import empty, arange, sqrt, sin, cos, pi, exp, linspace, log
from pylab import imshow, show, gray, plot, scatter, axhline, loglog
from scipy.special import roots_legendre
from scipy.constants import k, hbar, c, epsilon_0

#(a)
def electric_potential (charge, seperation, scale, resolution):

    func = lambda r : charge / (4 * pi * epsilon_0 * r)
    distant = lambda a, b : np.linalg.norm(np.array(a) - np.array(b))
    
    charge_1 = (-seperation / 2, 0) #negative
    charge_2 = (seperation / 2, 0) #postive

    epsilon = 1e-2
    x_coordinate = linspace(-scale / 2, scale / 2, resolution)
    y_coordinate = linspace(-scale / 2, scale / 2, resolution)

    grid = np.empty((resolution, resolution), float)

    for y_index, y in enumerate(y_coordinate):
        for x_index, x in enumerate(x_coordinate):
            
            sample_location = (x, y)
            dis_1 = distant(sample_location, charge_1)
            dis_2 = distant(sample_location, charge_2)

            if(dis_1 < epsilon):
                dis_1 = epsilon
            elif(dis_2 < epsilon):
                dis_2 = epsilon

            potential = log(func(dis_2)) * charge - log(func(dis_1)) * charge # avoid the plot explode
            grid[y_index, x_index] = potential

    return grid


def main ():

    charge = 1
    seperation = 0.1
    scale = 1
    resolution = 100

    distribution = electric_potential(charge, seperation, scale, resolution)

    imshow(distribution, extent = [-scale / 2, scale / 2, -scale / 2, scale / 2]) #, vmax = 1.2, vmin = -1.2 for show clearly
    gray()
    show()

main()
