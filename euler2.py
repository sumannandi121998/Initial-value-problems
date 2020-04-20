#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 20:55:35 2020

@author: suman
"""

import matplotlib.pyplot as plt
import numpy as np

def f(t,y): #a function which return an array
    y1=y[0] #here y1=y
    y2=y[1] #y2=y'
    return np.array([y2,(2*t*y2-2*y1+(t**3)*np.log(t))/(t*t)]) #we devide the eq in two part ie y'=y2 and y2'=(2ty2-2y1+(t^3)log(t))/(t^2)
h=0.01 #stepsize
t_sol=np.array(1) #initial value of t 
y_sol=np.array([[1.0,0.0]]) #1st and 2nd element of the array are initial value of y and y' respectively 
t=1
y=np.array([1.0,0.0])
while t<2:
    y=y+h*f(t,y) #formula for euler method
    t=t+h
    t_sol=np.append(t_sol,t) #appending the value of t after each step
    y_sol=np.vstack([y_sol,y]) #appending the vector y after each step
plt.plot(t_sol, y_sol[:,0],label='numerical solution') #plotting of solution

def g(t):
    return 7*t/4+(t**3)*np.log(t)/2-3*t**3/4 #analytical sol of differential eq
x = np.linspace(1, 2, 100)
plt.plot(x, g(x),label='analytical solution') #plotting analytical solution
plt.xlabel('t', fontsize=15)
plt.ylabel('y', fontsize=15)
plt.title('t vs y graph')
plt.legend()
plt.show()