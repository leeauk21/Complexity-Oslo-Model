# -*- coding: utf-8 -*-
"""
Created on Sat Feb 15 17:24:18 2020

@author: Ching Hoe Lee
"""
import numpy as np
import matplotlib.pyplot as plt
steps=70000
t=range(0,steps)
results_2a=np.loadtxt('task2a.txt',delimiter=',')
L=np.array([4,8,16,32,64,128,256])
for k in range(0, len(results_2a)):
   plt.plot(t, results_2a[k], 'x', label=f'L={L[k]}')
plt.xlabel('time')
plt.ylabel('height')
plt.title('height vs time')
plt.legend()
plt.savefig('task2a.png')
plt.show()