# -*- coding: utf-8 -*-
"""
Created on Mon Feb 10 16:43:16 2020

@author: Ching Hoe Lee
"""
import scipy as sp
import numpy as np
import matplotlib.pyplot as plt
num=np.array([80,140,600,2000,8000,30000,120000])
L=np.array([4,8,16,32,64,128,256])
data_2g=[]
unique_h_list=[]
counts_h_list=[]
data_2g.append(np.loadtxt('taskiig_one.csv',delimiter=','))
data_2g.append(np.loadtxt('taskiig_two.csv',delimiter=','))
data_2g.append(np.loadtxt('taskiig_three.csv',delimiter=','))
data_2g.append(np.loadtxt('taskiig_four.csv',delimiter=','))
data_2g.append(np.loadtxt('taskiig_five.csv',delimiter=','))
data_2g.append(np.loadtxt('taskiig_six.csv',delimiter=','))
data_2g.append(np.loadtxt('taskiig_seven.csv',delimiter=','))

for i in data_2g:
   unique_h,counts_h=np.unique(i,return_counts=True)
   unique_h_list.append(unique_h)
   counts_h_list.append(counts_h)
j=0
while j <=6:
   x=unique_h_list[j]
   y=counts_h_list[j]/num[j]
   plt.plot(x, y, label=f'L={L[j]}',linewidth=0.5)
   j+=1
plt.xlabel('height')
plt.xlabel('probability')
