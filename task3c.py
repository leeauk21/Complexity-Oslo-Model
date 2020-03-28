# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 19:23:51 2020

@author: Ching Hoe Lee
"""
import scipy as sp
from scipy import stats
import numpy as np
import matplotlib.pyplot as plt
L=np.array([4,8,16,32,64,128,256])
a_size_list=np.loadtxt('avalanche_size.txt', delimiter=',')
mean_list=[]
slope_list=[]
for b in range (1,5):
   abc=np.power(a_size_list,b)
   mean=np.mean(abc,axis=1)
   mean_list.append(mean)

for c in mean_list:
   x=np.log(L)
   y=np.log(c)
   plt.plot(x,y,'x')
   slope, intercept, r_value, p_value, std_err = stats.linregress(x, y)
   plt.plot(x, intercept + slope*x)
   slope_list.append(slope)


plt.legend()
plt.ylabel('log(mean avalanche size moment')
plt.xlabel('log(L)')
plt.savefig('task3c.png')
plt.show()

k=[1,2,3,4]
plt.plot(k,slope_list,'x')
slpe, intercept, r_value, p_value, std_err = stats.linregress(k, slope_list)
plt.plot(k, intercept + slpe*np.asarray(k))
plt.savefig('task3cc.png')
plt.figure()
    
   