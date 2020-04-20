#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 11:17:58 2020

@author: suman
"""

import matplotlib.pyplot as plt
import numpy as np

def f(x,y,z):
    return z #we have taken y'=z
def g(x,y,z):
    return 2*z-y+x*np.exp(x)-x #The diff eq become z'=2z-y+x.exp(x)-x
h=0.01
x_sol=np.array(0) #initial value of x
y_sol=np.array(0) #value of y at x=0
x=0
y=0
z=0 #value of y' at x=0
while x<1:
    k1=h*f(x,y,z)
    l1=h*g(x,y,z)
    k2=h*f(x+h/2,y+k1/2,z+l1/2)
    l2=h*g(x+h/2,y+k1/2,z+l1/2)
    k3=h*f(x+h/2,y+k2/2,z+l2/2)
    l3=h*g(x+h/2,y+k2/2,z+l2/2)
    k4=h*f(x+h,y+k3,z+l3)
    l4=h*g(x+h,y+k3,z+l3)
    y=y+(1/6)*(k1+2*k2+2*k3+k4) #value of y after each step
    z=z+(1/6)*(l1+2*l2+2*l3+l4) #value of y' after each step
    x=x+h
    x_sol=np.append(x_sol,x) #appending the value of x after each step
    y_sol=np.append(y_sol,y) #appending the value of y after each step
plt.plot(x_sol, y_sol,label='solution of differential eq') #plotting of solution
plt.xlabel('x', fontsize=15)
plt.ylabel('y', fontsize=15)
plt.title('x vs y graph')
plt.legend()
plt.show()