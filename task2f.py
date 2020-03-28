# -*- coding: utf-8 -*-
"""
Created on Sat Feb  8 14:08:03 2020

@author: Ching Hoe Lee
"""
import scipy as sp
import numpy as np
import matplotlib.pyplot as plt
data=np.loadtxt('taskiie.csv',delimiter=',')
mean_height=np.mean(data,axis=1)
std_height=np.std(data,axis=1)
L=np.array([4,8,16,32,64,128,256])
plt.figure()
x=np.log(L)
y=np.log(std_height)
plt.plot(x,y,'x')
slope, intercept, r_value, p_value, std_err = stats.linregress(x,y)
x_reg=np.array([0,1,2,3,4,5])
y_reg=x_reg*slope+intercept
plt.plot(x_reg,y_reg)
plt.title('ln(L) against ln(standard deviation)')
plt.xlabel('ln(L)')
plt.ylabel('ln(standard deviation)')
plt.savefig('lnstd.png')
plt.figure()
plt.title('L against standard deviation')
plt.plot(L,std_height,'x')
plt.xlabel('L')
plt.ylabel('standard deviation')
plt.savefig('std.png')
plt.figure()
plt.plot(L,mean_height,'x')
plt.xlabel('L')
plt.ylabel('mean height')

plt.show()
#average height linear with L
#std oscillate when L>>1