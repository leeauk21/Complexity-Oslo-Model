# -*- coding: utf-8 -*-
"""
Created on Fri Feb  7 17:03:53 2020

@author: Ching Hoe Lee
"""
import scipy as sp
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

data=np.loadtxt('taskiie.csv',delimiter=',')
mean_height=np.mean(data,axis=1)
std_height=np.std(data,axis=1)
L=np.array([4,8,16,32,64,128,256])

#task2e
#mean_height/L approx= a_0 when L>>1
k=np.divide(mean_height,L)
a=k[-1]
b=1-k/a
y=np.log(b[0:6])
x=np.log(L[0:6])
plt.plot(x,y,'x')
plt.xlabel('ln(L)')
plt.ylabel('ln(y)')
slope, intercept, r_value, p_value, std_err = stats.linregress(x,y)
x_reg=np.array([0,1,2,3,4,5])
y_reg=x_reg*slope+intercept
plt.plot(x_reg,y_reg)
print(slope)
plt.show()
#omega=0.84045
#a=1.720
