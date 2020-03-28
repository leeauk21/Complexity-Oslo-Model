# -*- coding: utf-8 -*-
"""
Created on Tue Jan 28 11:06:15 2020

@author: Ching Hoe Lee
"""

import complexity as com
import numpy as np
import matplotlib.pyplot as plt
L=np.array([4,8,16,32,64,128,256])
steps=10000
t=range(1,steps+1)
num_sample=10
results=[]
b=0
a=0
for a in L:
   sample=[]
   for i in range(0,num_sample):
      model=com.oslo(a)
      height=[]
      for j in range(0,steps):
         h=model.height(1)
         height.append(h)
         #height stores all the h in one model
      sample.append(height)
   avg_h_t=np.mean(sample,axis=0)
   results.append(avg_h_t)
   
results_array=np.asarray(results)
np.savetxt('task2d.txt',results_array,delimiter=',')
#results stores all the average height at different steps
'''
for k in range(0, len(results_array)):
   plt.plot(t, results_array[k], 'x', label=f'L={L[k]}')
plt.legend()
plt.show()
'''
#plot log h/L against log t/L**2
#y=h/L
i=0
while i<=6:   
   y=results_array[i]/L[i]
   x=np.asarray(t)/L[i]**2
   plt.plot(x,y,'x',label=f'L={L[i]}')
   i+=1


plt.title('log(h^(j)/L vs t/L^(2))') 
plt.legend()
plt.savefig('task2d.png')
plt.show()
   
      

