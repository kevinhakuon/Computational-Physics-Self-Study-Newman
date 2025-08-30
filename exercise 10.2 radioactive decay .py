import numpy as np
import matplotlib.pyplot as plt
import random as rd
from scipy import fft

N_213Bi = []
N_209Tl = []
N_209Pb = []
N_209Bi = []

ht_Bi = 46 * 60
ht_Tl = 2.2 * 60
ht_Pb = 3.3 * 60

Bi213_num = 10000
Tl209_num = 0
Pb209_num = 0
Bi209_num = 0

end_time = 20000
time_list = np.arange(0.0, end_time, 1.0)

p = lambda t, ht : 1 - 2**(- t / ht)

for t in time_list:

    N_213Bi.append(Bi213_num)
    N_209Tl.append(Tl209_num)
    N_209Pb.append(Pb209_num)
    N_209Bi.append(Bi209_num)

    decay_Bi213 = 0
    decay_Tl209 = 0
    decay_Pb209 = 0
    decay_Bi209 = 0

    for i in range(Pb209_num):
        if(rd.random() < p(1, ht_Pb)):
            decay_Pb209 += 1
            decay_Bi209 -= 1

    for i in range(Tl209_num):
        if(rd.random() < p(1, ht_Tl)):
            decay_Tl209 += 1
            decay_Pb209 -= 1
        
    for i in range (Bi213_num):
        if (rd.random() < p(1, ht_Bi)):
            decay_Bi213 += 1

            if (rd.random() < 0.0209):
                decay_Tl209 -= 1
            else:
                decay_Pb209 -= 1


    Bi213_num -= decay_Bi213
    Tl209_num -= decay_Tl209
    Pb209_num -= decay_Pb209
    Bi209_num -= decay_Bi209

plt.plot(time_list, N_213Bi, label="213Bi")
plt.plot(time_list, N_209Pb, label="209Pb")
plt.plot(time_list, N_209Tl, label="209Tl")
plt.plot(time_list, N_209Bi, label="209Bi")

plt.xlabel("time (s)")
plt.ylabel("number of atoms")
plt.legend()
plt.show()
