#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 21:07:56 2020

@author: suman
"""

import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import solve_ivp

def f(t,y):
    return 1-(t-y)**2 #y' of differential equation
time = np.linspace(2,3,100)
Y = solve_ivp(f,(2,3),[1],t_eval=time) #solve using scipy function
plt.plot(Y.t,Y.y[0,:],label='numerical solution') #plotting of numerical solution
def g(t):
    return (1-3*t+t*t)/(t-3) #analytical solution
t = np.arange(2, 3, 0.01)
plt.plot(t, g(t),label='analytical solution') #plotting analytical solution
plt.xlabel('t', fontsize=15)
plt.ylabel('y', fontsize=15)
plt.title('t vs y graph')
plt.legend()
plt.show()