from math import sqrt, sin, pi
from numpy import empty, arange
from pylab import imshow, show, gray, plot, scatter

trial = 100
side = 2
point = 500
spacing = side / point

Mandelbrot = empty([2 * point, 2 * point], bool)

for i in arange (-side, side, spacing):
    x = int((i + side) / spacing)
    for k in arange (-side, side, spacing):
        y = int((k + side) / spacing)
        complex_constant = complex(i, k)
        inside_set = True
        z = complex(0, 0)
        for m in range (trial):
            z = z**2 + complex_constant
            if(abs(z) > 2):
                inside_set = False
                break
        Mandelbrot[x, y] = inside_set

imshow(Mandelbrot,  extent = [-side, side, -side, side])
show()

#use chatGPT simplify
from numpy import empty, linspace
from pylab import imshow, show

trial = 100
side = 2
point = 500

x_vals = linspace(-side, side, 2 * point)
y_vals = linspace(-side, side, 2 * point)

Mandelbrot = empty([2 * point, 2 * point], bool)

for ix, x in enumerate(x_vals):
    for iy, y in enumerate(y_vals):
        c = complex(x, y)
        z = 0
        for t in range(trial):
            z = z*z + c
            if abs(z) > 2:
                Mandelbrot[ix, iy] = False
                break
        else:
            Mandelbrot[ix, iy] = True

imshow(Mandelbrot, extent=[-side, side, -side, side])
show()
