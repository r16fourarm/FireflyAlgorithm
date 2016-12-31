# -*- coding: utf-8 -*-
"""
Created on Fri Dec 30 23:43:39 2016

@author: R16
"""
import math
import numpy as np
def fitness(x):
  return np.sum(x**2)
  
def fitnessF(popF):
  return [fitness(k) for k in popF]
  
#dim = 3
nFirefly = 30
maxEP = 1000
totPosisi = 300

ub = 5.12
lb = -5.12

dim = 1

#init populasi kunang2
popF=np.random.uniform(0,1,(nFirefly,dim)) *(ub-lb)+lb

#init parameter
betamin = 0.2
gamma = 1.0
alpha = 0.5
#print(popF)

#running algo
for e  in range(maxEP): 
  print("epo ke - ",e)
  #evaluasi fitness/intensitass cahaya
  light = fitnessF(popF)
#  print(light)
  idx = np.argsort(light,axis=0)
#  print(idx)
  popF = popF[idx,:]
#  print(popF)
  
  
#  break
  light_ = light
  popF_ = popF
  #inisiasi vektor untuk stepsize
  scale=np.ones(dim)*abs(ub-lb)
  for i in range (nFirefly):
      for j in range(nFirefly):
        #hitung untuk setiap kunang2
          r=np.sqrt(np.sum((popF[i,:]-popF[j,:])**2));
          #r=1
          # update pergerakan/lokasi kunang2
          if light[i]>light_[j]: # kunang2 yg redup bergerak ke yang terang
             beta0=1
             beta=(beta0-betamin)*math.exp(-gamma*r**2)+betamin
             tmpf=alpha*(np.random.rand(dim)-0.5)*scale
             #update setiap nilai/dim pada kunang2 
             popF[i,:]=popF[i,:]*(1-beta)+popF_[j,:]*beta+tmpf
    
  light = fitnessF(popF)
#  print(light)
  idx = np.argsort(light,axis=0)
#  print(idx)
  popF = popF[idx,:]
  print(popF[0]," ",light[0])
#  print(popF)
             
#  break