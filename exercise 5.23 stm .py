import numpy as np
import matplotlib.pyplot as plt
from pylab import show
from mpl_toolkits.mplot3d import Axes3D
from numpy import sqrt, linspace, sin, cos
from scipy.constants import epsilon_0, pi


# I think there's something werid appear in the altitude.txt so I only do the stm
def loaddata(name):
    data = np.loadtxt(name)
    return data

def derivative(data, scale):

    dx = scale
    dy = scale
    grad_y, grad_x = np.gradient(data, dy, dx)

    return grad_y, grad_x

def Intensity(grad_x, grad_y, phi):

    intensity = - (cos(phi) * grad_x + sin(phi) * grad_y) / (sqrt(grad_x**2 + grad_y**2 + 1))
    return intensity

def main():

    file = "stm.txt"
    scale_btw_grid = 2.5

    surface = loaddata(file)
    grad_surface_y, grad_surface_x = derivative(surface, scale_btw_grid)
    intensity = Intensity(grad_surface_x, grad_surface_y, pi / 4)

    row, column = surface.shape
    x = np.arange(column)
    y = np.arange(row)
    x_coordinate, y_coordinate = np.meshgrid(x, y)

    fig = plt.figure()
    ax = fig.add_subplot(111, projection = '3d')
    ax.plot_surface(x_coordinate, y_coordinate, intensity, cmap = 'viridis')
    show()

main()
