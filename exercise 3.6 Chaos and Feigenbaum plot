from math import sqrt, sin, pi
from numpy import empty, arange
from pylab import imshow, show, gray, plot, scatter

# use different initial x to determine the edge and fixed point
def plotting(x_list, y_list, z_list):
    scatter(x_list, y_list, s = 0.4)
    scatter(x_list, z_list, s = 0.4)
    show()

loop_time = 1000
x_list = []
y_list = []

r_list = arange(1, 5.01, 0.01)
for i in r_list:
    x_ele = 1/2
    y_ele = 1/3
    for j in range (loop_time):
        x_ele = i * x_ele * (1 - x_ele)
        y_ele = i * y_ele * (1 - y_ele)
    x_list.append(x_ele)
    y_list.append(y_ele)

plotting(r_list, x_list, y_list)
