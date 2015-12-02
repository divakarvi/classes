import numpy as np
from matplotlib import pyplot as plt

data = np.genfromtxt('htwt.txt')
ht = data[:,1]
wt = data[:,2]
plt.plot(ht, wt, 'ro')
htavg = np.mean(ht)
wtavg = np.mean(wt)
cov = np.mean((ht-htavg)*(wt-wtavg))
r = cov/np.std(ht)/np.std(wt)
plt.title("Pearson's R = {0:.5f}".format(r))
plt.show()
