import numpy as np
import matplotlib.pyplot as plt
import scipy
from pylab import show, scatter, plot, ylim
from mpl_toolkits.mplot3d import Axes3D
from numpy import sqrt, linspace, sin, cos, tan, pi, exp
from scipy.constants import epsilon_0, pi, hbar, h, c, k


def Newton_method(func_1, func_1d, func_2, func_2d, func_12, func_21, V, tolerance):
    
    delta = [1.0, 1.0]
    Jacobian = np.empty([2, 2])
    
    while(delta[0] > tolerance or delta[1] > tolerance):
        
        Jacobian = [[func_1d(V[0], V[1]), func_12(V[0], V[1])],
                    [func_21(V[0], V[1]), func_2d(V[0], V[1])]]

        v = [func_1(V[0], V[1]), func_2(V[0], V[1])]
        delta = np.linalg.solve(Jacobian, v)

        V -= delta

    return V
    


                
def main():

    tolerance = 1e-7
    V_postive = 5
    R_1 = 1e3
    R_2 = 4e3
    R_3 = 3e3
    R_4 = 2e3
    I_0 = 3e-9
    V_T = 0.05


    func_1 = lambda V_1, V_2 : (V_1 - V_postive) / R_1 + V_1 / R_2 + I_0 * (exp((V_1 - V_2) / V_T) - 1)
    func_1d = lambda V_1, V_2 : 1 / R_1 + 1 / R_2 + (I_0 / V_T) * (exp((V_1 - V_2) / V_T))
    func_2 = lambda V_1, V_2 : (V_2 - V_postive) / R_3 + V_2 / R_4 - I_0 * (exp((V_1 - V_2) / V_T) - 1)
    func_2d = lambda V_1, V_2 : 1 / R_3 + 1 / R_4 + (I_0 / V_T) * (exp((V_1 - V_2) / V_T))
    func_12 = lambda V_1, V_2 : -(I_0 / V_T) * (exp((V_1 - V_2) / V_T))
    func_21 = lambda V_1, V_2 : -(I_0 / V_T) * (exp((V_1 - V_2) / V_T))
    

    V = [3.5, 2.9]
    Voltage = Newton_method(func_1, func_1d, func_2, func_2d, func_12, func_21, V, tolerance)
    print(Voltage)
    

main()
