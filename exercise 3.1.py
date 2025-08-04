#3.1.a
import numpy as np
from pylab import plot, show, ylim, xlabel, ylabel
data = np.loadtxt("sunspots.txt", float)
x = data[:, 0]
y = data[:, 1]
plot(x, y)
show()
#3.1.b
import numpy as np
from pylab import plot, show, ylim, xlabel, ylabel
data = np.loadtxt("sunspots.txt", float)
x = data[:1000, 0]
y = data[:1000, 1]
plot(x, y)
show()
#3.1.c
import numpy as np
from pylab import plot, show, ylim, xlabel, ylabel
r = 5
data = np.loadtxt("sunspots.txt", float)
x = data[:1001, 0]
y = data[:1001, 1]
running_avg = []
for k in range (990):
    avg = 0.0
    for m in range (-r, r + 1):
        avg += y[(k + r) + m]
    avg = avg/(2*r+1)
    running_avg.append(avg)
print(len(running_avg))
time_avg = x[5:995]
plot(x, y, "k-")
plot(time_avg, running_avg, "c--")
show()
