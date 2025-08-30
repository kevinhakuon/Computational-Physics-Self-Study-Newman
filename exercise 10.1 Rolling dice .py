import numpy as np
import matplotlib.pyplot as plt
import random as rd
from scipy import fft

N = 1000000
double_six = 0

for i in range(N):
    a = rd.randrange(1, 7)
    b = rd.randrange(1, 7)

    if(a == 6 and b == 6):
        double_six += 1


print(double_six)
print(double_six / N)
print(1 / 36)
