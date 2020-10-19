import numpy as np
from matplotlib import pyplot as plt
trials = 5000
N= 200
ar2= []
for j in range(1,N+1):
    sum1=0
    for i in range(0,trials):
        maxim=np.amax(np.random.normal(0,1.0,j))
        sum1+=maxim
    ave_maxim_value= sum1/trials
    ar2.append(ave_maxim_value)
plt.plot(np.arange(1,201),ar2)
plt.xlabel('N ',fontsize=20)
plt.ylabel('Average Maximum value',fontsize=20)
plt.show()
