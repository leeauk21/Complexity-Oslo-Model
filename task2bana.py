# -*- coding: utf-8 -*-
"""
Created on Sat Feb 15 18:18:06 2020

@author: Ching Hoe Lee
"""
from scipy import stats
import complexity as com
import numpy as np
import matplotlib.pyplot as plt
results_2b=np.loadtxt('task2b.txt',delimiter=',')
L=np.array([4,8,16,32,64,128,256])
steps=300000
t=range(0,steps)

plt.plot(L, results_2b, 'x')
plt.title('Average Cross Over Time vs System Size')
plt.ylabel('Average Cross Over Time')
plt.xlabel('System Size')
plt.savefig('task2b.png')
plt.figure()
plt.loglog(L, results_2b, 'x')
plt.title('ln(Average Cross Over Time) vs ln(System Size)')
plt.ylabel('ln(Average Cross Over Time)')
plt.xlabel('ln(System Size)')
plt.savefig('task2bb.png')
plt.legend()
plt.show()

