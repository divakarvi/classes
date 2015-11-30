import numpy as np
from matplotlib import pyplot as plt

data = np.genfromtxt('htwt.txt')
ht = data[:,1]
wt = data[:,2]
plt.plot(ht, wt, 'ro')
plt.show()

htavg = np.mean(ht)
wtavg = np.mean(wt)
cov = np.mean((ht-htavg)*(wt-wtavg))
r = cov/np.std(ht)/np.std(wt)
print("Pearson's R = ", r)
