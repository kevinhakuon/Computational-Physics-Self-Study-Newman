import numpy as np
import matplotlib.pyplot as plt
import random as rd
from matplotlib.animation import FuncAnimation


N_208Tl = 1000
ht = 3.053 * 60
decay_time = []
Tl208_num = []

p = lambda z : -ht * np.log2(1 - z)


for i in range(N_208Tl):

    z = rd.random()
    decay = p(z)
    decay_time.append(decay)


decay_time = np.sort(decay_time)
t_sorted = np.sort(decay_time)               # shape = (N0,)
t_sorted = np.r_[0.0, t_sorted]                     # 加入 t=0 起點
Tl208_num = N_208Tl - np.arange(0, N_208Tl + 1)              # N0, N0-1, ..., 1, 0
plt.step(t_sorted, Tl208_num, where="post")

plt.show()
