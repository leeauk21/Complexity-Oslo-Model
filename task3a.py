# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 14:13:44 2020

@author: Ching Hoe Lee
"""
from logbin230119 import logbin
import scipy as sp
import numpy as np
import matplotlib.pyplot as plt
import complexity as com
L=np.array([4,8,16,32,64,128,256])
attractor_t=np.array([40,70,300,1000,4000,15000,60000])
num=10000
a=0
a_size_list=[]
list_x_3a=[]
list_y_3a=[]
while a <=6:
   model_3a=com.oslo(L[a])
   model_3a.iteration(attractor_t[a])   
   a_size=model_3a.avalanche_size(num)
   a_size_list.append(a_size)
   x_3a,y_3a=logbin(a_size, scale=1.5)
   list_x_3a.append(x_3a)
   list_x_3a.append(y_3a)
   plt.plot(x_3a,y_3a,label=f'L={L[a]}')
   a+=1
   plt.loglog()
plt.xlabel('avalanche size')
plt.ylabel('probability')
plt.legend()
plt.savefig('task3a.png')
plt.show()
np.savetxt('avalanche_size.txt',a_size_list,delimiter=',')
