import numpy as np
import matplotlib.pyplot as plt
import random

inp2 = [1.0,1.5,1.43,2.3,5.44,2.5,3.0,255.0,2.9,2.75]
inp5 = [1.0,3.0,4.0,5.0,4.0,255.0,5.0,6.0,7.0,4.0,5.0,4.0,6.0,7.0]
inp = [random.uniform(14.0,18.0) for i in range(0,100)]
inp[30] = inp[43]=inp[76]=255
temp = inp[:]
pos = 0
smoothedVal = inp[0]
print(inp)
while pos < len(inp):
    inp[pos] = (inp[pos] * (1 - .95)) + (inp[pos-1]  *  .95);
    pos=pos+1
print(inp)
plt.plot([i for i in range(0,len(inp))],inp,'r-',[i for i in range(0,len(inp))],temp)
plt.show()
