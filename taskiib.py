# -*- coding: utf-8 -*-
"""
Created on Wed Jan 22 11:43:16 2020

@author: Ching Hoe Lee
"""

import complexity as com
import numpy as np
import matplotlib.pyplot as plt
#t_xover=time when first grain added induce a loss in grain in the system

steps=300000
add=[1]*steps
L=np.array([4,8,16,32,64,128,256])
results=[]
for i in L:
   model=com.oslo(i)
   t_x_sample=[]
   t_xocer_i=np.asarray(range(1,i+1))
   for j in range(0,len(add)):
      t_xover=np.multiply(model.all_slope(1),t_xocer_i)
      t_x=np.sum(t_xover)
      t_x_sample.append(t_x)
   t_x_avg_L=np.mean(t_x_sample)
   results.append(t_x_avg_L)
np.savetxt('task2b.txt',results,delimiter=',')

'''
for k in range(0, len(results)):
   plt.plot(t, results[k], 'x', label=f'L={L[k]}')


plt.legend()
plt.show()
'''