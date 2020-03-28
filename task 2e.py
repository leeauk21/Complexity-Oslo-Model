# -*- coding: utf-8 -*-
"""
Created on Fri Feb  7 15:23:04 2020

@author: Ching Hoe Lee
"""
import numpy as np
import complexity as com
L=np.array([4,8,16,32,64,128,256])
attractor_t=np.array([40,70,300,1000,4000,15000,60000])
num_sample=10000
avg_attractor_t_h_list=[]
height_sample=[]
sample=[]
i=0
while i<=len(L)-1:
   model=com.oslo(L[i])
   model.height(attractor_t[i])
   height_sample=[]
   for j in range(0,num_sample):
      h=model.height(1)
      height_sample.append(h)
      
   avg_attractor_t_h=np.mean(height_sample)
   avg_attractor_t_h_list.append(avg_attractor_t_h)
   sample.append(height_sample)
   i+=1
sample=np.asarray(sample)
std=np.std(sample,axis=1)
np.savetxt('taskiie.csv',sample,delimiter=',')

      
#task 2d
#estimate_a_knot_list=avg_attractor_t_h_list/L
#a_knot=estimate_a_knot_list[-1]
#y=1-avg_attractor_t_h_list
