# -*- coding: utf-8 -*-
"""
Created on Tue Jan 21 17:28:25 2020

@author: Ching Hoe Lee
"""
"task 2a"
import complexity as com
import numpy as np
import matplotlib.pyplot as plt
# height vs time(for different L)
steps=70000
L=np.array([4,8,16,32,64,128,256])
add=[1]*steps
t=range(0,steps)
results=[]
for i in L:
   h=[]
   model=com.oslo(i)
   for j in range(0,len(add)):
      height_t=model.height(1)
      h.append(height_t)
   results.append(h)
np.savetxt('task2a.txt',results,delimiter=',')
for k in range(0, len(results)):
   plt.plot(t, results[k], 'x', label=f'L={L[k]}')

plt.legend()
plt.show()
   

#do 70000 for results
   

   
   