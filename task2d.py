# -*- coding: utf-8 -*-
"""
Created on Sun Feb 16 21:30:45 2020

@author: Ching Hoe Lee
"""
import complexity as com
import numpy as np
import matplotlib.pyplot as plt
results_array=np.loadtxt('task2d.txt',delimiter=',')
L=np.array([4,8,16,32,64,128,256])
steps=10000
t=range(1,steps+1)
i=0
while i<=6:   
   y=results_array[i]/L[i]
   x=np.asarray(t)/L[i]**2
   plt.loglog(x,y,'x',label=f'L={L[i]}')
   i+=1


plt.title('log(h^(j)/L vs t/L^(2))') 
plt.legend()
plt.savefig('task2d.png')
plt.show()
   