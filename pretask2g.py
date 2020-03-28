# -*- coding: utf-8 -*-
"""
Created on Sat Feb  8 19:57:02 2020

@author: Ching Hoe Lee
"""

import scipy as sp
import numpy as np
import matplotlib.pyplot as plt
data=np.loadtxt('taskiie.csv',delimiter=',')
unique_h_list=[]
counts_h_list=[]
L=np.array([4,8,16,32,64,128,256])
std_height=np.std(data,axis=1)
for i in data:
   unique_h,counts_h=np.unique(i,return_counts=True)
   unique_h_list.append(unique_h)
   counts_h_list.append(counts_h)
scale_y_list=[]
j=0
while j <=6:
   x=unique_h_list[j]
   y=counts_h_list[j]/100000
   scale_y=np.std(unique_h_list[j])*counts_h_list[j]/100000
   scale_y_list.append(scale_y)
   plt.plot(x, y, label=f'L={L[j]}')
   j+=1
plt.legend()
plt.ylabel('probability')
plt.xlabel('height')
plt.savefig('probability.png')
plt.figure()

k=0
while k<=6:
   new_y=scale_y_list[k]
   quan=unique_h_list[k]-np.mean(unique_h_list[k])
   new_x=quan*(np.std(unique_h_list[k]))**(-1)
   plt.plot(new_x,new_y,label=f'L={L[k]}')
   plt.legend()
   plt.savefig('datacollapse.png')
   k+=1

plt.legend()
plt.show()