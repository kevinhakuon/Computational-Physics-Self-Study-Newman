from math import sqrt, sin, cos, pi
import numpy as np
import pylab
from numpy import empty, arange, exp, linspace
from pylab import imshow, show, gray, plot, scatter, savefig


def Simpson_integral (func, lower_bound, upper_bound, slices = 1000):
    width = (upper_bound - lower_bound) / slices
    result = func(lower_bound) + func(upper_bound)
    for i in range(1, slices, 2):
        x = lower_bound + i * width
        result += 4 * func(x)
    for i in range(2, slices, 2):
        x = lower_bound + i * width
        result += 2 * func(x)
    
    result = result * width /3
    
    return result

def Bessel_func (x, order = 1):
    func = lambda theta : cos(order * theta - x * sin(theta))
    J_m = (1 / pi) * Simpson_integral(func, 0, pi)
    return J_m

def storedata(lower_bound, upper_bound, slices = 1000):
    x_list = list(np.linspace(lower_bound, upper_bound, slices + 1))
    y_list = []
    for i in range (len(x_list)):
        y_list.append(Bessel_func(x_list[i]))
    
    return x_list, y_list

def plotting(x_list, y_list, name):
    fig, ax = pylab.subplots()
    ax.plot(x_list, y_list)
    ax.spines['left'].set_position('zero')
    ax.spines['bottom'].set_position('zero')
    savefig(name, dpi = 100)
    show()

wavelength = 500e-9
wavenumber = 2 * pi / wavelength

intensity = lambda r : (Bessel_func(wavenumber * r) / (wavenumber * r))

def Diffraction (edge, resolution):
    
    intensity = lambda r : (Bessel_func(wavenumber * r) / (wavenumber * r))
    intensity_distribution = empty([resolution, resolution], float)

    pixel = edge / resolution

    x_coordinate = linspace(-resolution / 2, resolution / 2, resolution)
    y_coordinate = linspace(-resolution / 2, resolution / 2, resolution)

    for x, i in enumerate (x_coordinate):
        for y, j in enumerate (y_coordinate):
            intensity_distribution[x, y] = intensity(sqrt(i **2 + j**2) * pixel)

    return intensity_distribution

def density_fig (edge = 1e-6, resolution = 1000):
    imshow(Diffraction(edge, resolution), extent = [-resolution / 2, resolution / 2, -resolution / 2, resolution / 2])
    show()

density_fig()
