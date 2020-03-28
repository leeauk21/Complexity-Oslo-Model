# -*- coding: utf-8 -*-
"""
Created on Mon Feb 10 16:00:18 2020

@author: Ching Hoe Lee
"""

import scipy as sp
import numpy as np
import matplotlib.pyplot as plt
import complexity as com
L=np.array([4,8,16,32,64,128,256])
num=np.array([80,140,600,2000,8000,30000,120000])
sample_2g=[]
k=0
while k<=6:
   model=com.oslo(L[k])
   height_sample_2g=[]
   for j in range(0,num[k]):
      h_2g=model.height(1)
      height_sample_2g.append(h_2g)
   sample_2g.append(height_sample_2g)
   k+=1
np.savetxt('taskiig_one.csv',sample_2g[0])
np.savetxt('taskiig_two.csv',sample_2g[1])
np.savetxt('taskiig_three.csv',sample_2g[2])
np.savetxt('taskiig_four.csv',sample_2g[3])
np.savetxt('taskiig_five.csv',sample_2g[4])
np.savetxt('taskiig_six.csv',sample_2g[5])
np.savetxt('taskiig_seven.csv',sample_2g[6])

for i in sa
  
