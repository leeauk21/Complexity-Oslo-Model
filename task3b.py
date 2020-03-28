# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 11:06:56 2020

@author: Ching Hoe Lee
"""
from logbin230119 import logbin
import scipy as sp
import numpy as np
import matplotlib.pyplot as plt
a_size_list=np.loadtxt('avalanche_size.txt', delimiter=',')
L=np.array([4,8,16,32,64,128,256])
i=0
while i<=6:
   x_3a,y_3a=logbin(np.asarray(a_size_list[i], dtype=np.int64), scale=1.5)
   y=y_3a*x_3a**(1.55)
   x=x_3a/L[i]**(2.25)
   plt.plot(x,y,label=f'L={L[i]}')
   plt.loglog()
   i+=1
plt.xlabel('s/L^(D)')
plt.ylabel('Probability')
plt.legend()
plt.savefig('task3b.png')
plt.show()