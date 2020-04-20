#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 30 22:10:53 2020

@author: suman
"""

import matplotlib.pyplot as plt
import numpy as np

def f(t,y):
    return (y/t)-(y/t)*(y/t) #y' of the differential equation
h=0.1 #stepsize
t_sol=np.array(1) #initial value of t 
y_sol=np.array(1) #initial value of y 
t=1
y=1
while t<2:
    y=y+h*f(t,y) #formula for euler method
    t=t+h
    t_sol=np.append(t_sol,t) #appending the value of t after each step
    y_sol=np.append(y_sol,y) #appending the value of y after each step
plt.plot(t_sol, y_sol,label='solution of differential eq') #plotting of solution
def g(t):
    return t/(1+np.log(t)) #analytical sol of differential eq
x = np.arange(1, 2+h, h)
a_e=np.average(abs(g(x)-y_sol)) #absolute error
r_e=np.average(abs((g(x)-y_sol)/g(x))) #relative error
print('The absolute error is',a_e)
print('The relative error is',r_e)
plt.xlabel('t', fontsize=15)
plt.ylabel('y', fontsize=15)
plt.title('t vs y graph')
plt.legend()
plt.show()
