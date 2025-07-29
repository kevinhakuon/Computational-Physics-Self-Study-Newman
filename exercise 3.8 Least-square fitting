from math import sqrt, sin, pi
import numpy as np
from numpy import empty, arange
from pylab import imshow, show, gray, plot, scatter

charge = 1.602 * 10**(-19)
data = np.loadtxt("millikan.txt", float)
x_list = data[:, 0]
y_list = data[:, 1]

E_xx = 0
E_xy = 0
E_x = 0
E_y = 0
for i in range (len(x_list)):
    E_xx += x_list[i]**2 / len(x_list)
    E_xy += y_list[i]*x_list[i] / len(y_list)
    E_x += x_list[i] / len(x_list)
    E_y += y_list[i] / len(y_list)

slope = (E_xy - E_x * E_y) / (E_xx - E_x**2)
intercept = (E_xx * E_y - E_x * E_xy)/ (E_xx - E_x**2)
print(slope * charge)

def best_fitting(x_value):
    y = slope * x_value + intercept
    return y

plot(x_list, best_fitting(x_list), "c--")

scatter(x_list, y_list)
show()


#chatGPT improve the capsulation
import numpy as np
import matplotlib.pyplot as plt

# 常數
CHARGE = 1.602e-19

def load_data(filename):
    data = np.loadtxt(filename, float)
    return data[:, 0], data[:, 1]

def linear_regression(x, y):
    Ex = np.mean(x)
    Ey = np.mean(y)
    Exx = np.mean(x**2)
    Exy = np.mean(x * y)

    slope = (Exy - Ex * Ey) / (Exx - Ex**2)
    intercept = (Exx * Ey - Ex * Exy) / (Exx - Ex**2)
    return slope, intercept

def plot_fit(x, y, slope, intercept):
    plt.scatter(x, y, label='Data')
    plt.plot(x, slope * x + intercept, 'c--', label='Best fit')
    plt.xlabel("x")
    plt.ylabel("y")
    plt.legend()
    plt.grid(True)
    plt.show()

def main():
    x_data, y_data = load_data("millikan.txt")
    slope, intercept = linear_regression(x_data, y_data)

    print(f"Estimated slope × e = {slope * CHARGE:.4e} C")
    plot_fit(x_data, y_data, slope, intercept)

if __name__ == "__main__":
    main()
