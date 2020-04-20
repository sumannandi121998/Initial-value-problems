#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 30 20:14:07 2020

@author: suman
"""

import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import newton

def f(x,y):
    return -9*y #y' of first differential equation
def g(x,y):
    return -20*(y-x)*(y-x)+2*x #y' of second differential equation
h=0.01  #stepsize
x_sol=np.array(0) #initial value of x in both eq
y_sol1=np.array(np.exp(1)) #initial value of y in 1st eq
y_sol2=np.array(1/3) #initial value of y in 2nd eq
x=0
y1=np.exp(1)
y2=1/3
while x<1:
    def f1(y):
        return (y-y1-h*f(x,y))
    def g1(y):
        return (y-y2-h*g(x,y))
    y1 = newton(f1,1) #solution by Newton Raphson method
    y2 = newton(g1,1)
    x=x+h 
    x_sol=np.append(x_sol,x) #appending the value of x after each step
    y_sol1=np.append(y_sol1,y1) #appending the value of y1 after each step
    y_sol2=np.append(y_sol2,y2) #appending the value of y2 after each step

plt.plot(x_sol, y_sol1, 'r',label='solution of 1st eq') #plotting of sol of 1st eq
plt.plot(x_sol, y_sol2, 'g',label='solution of 2nd eq') #plotting of sol of 2nd eq

plt.xlabel('x', fontsize=15)
plt.ylabel('y', fontsize=15)
plt.title('x vs y graph')
plt.legend()
plt.show()
