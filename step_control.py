#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 21:19:02 2020

@author: suman
"""

import matplotlib.pyplot as plt
import numpy as np

t_sol=np.array(1) #initial value of t 
y_sol=np.array(-2) #initial value of y
def f(t,y):
    return (y*y+y)/t #y' of the differential equation
def RK(t,y,h): #a function which compute one iteration using RK4 method for stepsize h
    k1=h*f(t,y)
    k2=h*f(t+h/2,y+k1/2)
    k3=h*f(t+h/2,y+k2/2)
    k4=h*f(t+h,y+k3)
    y1=y+(1/6)*(k1+2*k2+2*k3+k4)
    return y1
t=1
y=-2
h=0.01 #initial stepsize
e=0.0001 #minimum accuracy
while t<3.0:
    y1=RK(t,y,2*h) #calculate the value of y for stepsize 2h
    y2=RK(t,y,h) #calculate the value of y for stepsize h
    y3=RK(t+h,y2,h) #calculate the value of y for stepsize h after calculating y2
    eps=np.abs(y3-y1)/30
    h=h*(e*h/eps)**0.25 #calculate the perfect stepsize
    y=RK(t,y,h)  #calculate the value of y using perfect stepsize
    t=t+h
    t_sol=np.append(t_sol,t) #appending the value of t after each step
    y_sol=np.append(y_sol,y) #appending the value of y after each step
print('The mesh points are',t_sol) #printing mesh points
plt.plot(t_sol, y_sol, 'o',label='meshpoints') #plotting the solution
plt.xlabel('t', fontsize=15)
plt.ylabel('y', fontsize=15)
plt.title('t vs y graph')
plt.legend()
plt.show()
