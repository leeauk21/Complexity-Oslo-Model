# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 11:15:35 2020

@author: Ching Hoe Lee
"""
import scipy as sp
import numpy as np
import random as ran

"i dont understand this"

class oslo:

   def __init__(self,L):
      self.L=L
      self.h=0
      self.a=[]
      self.boo=()
      self.pos=np.array([])
      self.z=np.zeros(self.L)
      i=0
      self.z_th=[]
      while i < L:
         self.z_th=np.append(self.z_th,np.array(ran.choice([1,2])))
         i+=1
            
   def drive(self):
      self.z[0]+=1
         
      
      
   def indiv_relax(self,j):
      self.z_th[j]=ran.choice([1,2])
      if j ==0:
         self.z[0]-=2
         self.z[1]+=1
       
      elif j == self.L-1:
         self.z[self.L-1]-=1
         self.z[self.L-2]+=1
      else:
         self.z[j]-=2
         self.z[j+1]+=1
         self.z[j-1]+=1

   """     
   def check(self):
        i=0
        self.a=[]
        #self.a returns postion where needs relaxing
        while i < self.L:
           if self.z[i]>self.z_th[i]:
              self.a.append(i)
           i+=1
   """
   def new_check(self):
       self.boo=self.z>self.z_th
       self.pos=np.where(self.boo==True)[0]
        #pos return all the position that need relaxing
        
   def new_total_relax(self):
      self.new_check()
      while len(self.pos)>=1:
         for i in self.pos:
            self.indiv_relax(i)
         self.new_check()

      
   """              
   def total_relax(self):
        self.check()
        while len(self.a)>0:
           for i in self.a:
              self.indiv_relax(i)
           self.check()
   """
   def iteration(self,t):
        i=0
        while i < t:
          self.drive()
          self.new_total_relax()
          i+=1
          
   def height(self,t):
        self.iteration(t)
        self.h=np.sum(self.z)
        return(self.h)
        
   def all_slope(self,t):
       self.iteration(t)
       return self.z

   def avalanche_size(self,t):
      time=0
      s_list=[]
      while time < t:
         self.drive()
         self.new_check()
         s=0
         while len(self.pos)>=1:
            for i in self.pos:
               self.indiv_relax(i)
            s+=len(self.pos)
            self.new_check()
         s_list.append(s)            
         time+=1
      return s_list
      
         
      
      
        
        
        
            
        
        
        
            
            
            
        
    
            


        
       
        