# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 16:20:27 2020

@author: Ching Hoe Lee
"""

from logbin230119 import logbin
import scipy as sp
import numpy as np
import matplotlib.pyplot as plt
a_size_list=np.loadtxt('avalanche_size.txt', delimiter=',')
L=np.array([4,8,16,32,64,128,256])
a=0
for i in a_size_list:
   x_3a,y_3a=logbin(np.asarray(i, dtype=np.int64), scale=1.5)
   plt.plot(x_3a,y_3a,label=f'L={L[a]}')
   plt.loglog()
   a+=1
plt.xlabel('avalanche size')
plt.ylabel('probability')
plt.legend()
plt.show()