#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 11:57:19 2020

@author: suman
"""

import matplotlib.pyplot as plt
import numpy as np
def f(t,u): #a function which return an array of u1',u2' and u3'
    u1=u[0]
    u2=u[1]
    u3=u[2]
    return np.array([u1+2*u2-2*u3+np.exp(-t),u2+u3-2*np.exp(-t),u1+2*u2+np.exp(-t)])
t_sol=np.array(0) #initial value of t 
u_sol=np.array([[3.0,-1.0,1.0]]) #initial value of u1,u2 and u3 in an array 
h=0.01 #stepsize
t=0
u=np.array([3.0,-1.0,1.0]) 
k1=k2=k3=k4=np.zeros(3) #k1,k2,k3,k4 are arrays of three elements
while t<1:
    k1=h*f(t,u)
    k2=h*f(t+h/2,np.array([u[0]+k1[0]/2,u[1]+k1[1]/2,u[2]+k1[2]/2]))
    k3=h*f(t+h/2,np.array([u[0]+k2[0]/2,u[1]+k2[1]/2,u[2]+k2[2]/2]))
    k4=h*f(t+h,np.array([u[0]+k3[0],u[1]+k3[1],u[2]+k3[2]]))
    u=u+(1/6)*(k1+2*k2+2*k3+k4) #u vector that contains u1,u2,u3 after each step
    t=t+h
    t_sol=np.append(t_sol,t) #appending the value of x after each step
    u_sol=np.vstack([u_sol,u]) #appending the vector u after each step
plt.plot(t_sol, u_sol[:,0],label='u1') #plotting the graph u1 vs t
plt.plot(t_sol, u_sol[:,1],label='u2') #plotting the graph u2 vs t
plt.plot(t_sol, u_sol[:,2],label='u3') #plotting the graph u3 vs t
plt.axhline(color='k')
plt.xlim(0, 1)
plt.xlabel('t', fontsize=15)
plt.title('t vs u1,u2,u3 graph')
plt.legend()
plt.show()

