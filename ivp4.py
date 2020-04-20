#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 21:21:36 2020

@author: suman
"""

import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import solve_ivp

def f(t,y):
    return np.cos(2*t)+np.sin(3*t) #y' of differential equation
time = np.linspace(0,1,100)
Y = solve_ivp(f,(0,1),[1],t_eval=time) #solve using scipy function
plt.plot(Y.t,Y.y[0,:],label='numerical solution') #plotting of numerical solution
def g(t):
    return (1/6) *(8 - 2 *np.cos(3 *t) + 3 *np.sin(2* t)) #analytical solution
t = np.linspace(0, 1, 100)
plt.plot(t, g(t),label='analytical solution') #plotting analytical solution
plt.xlabel('t', fontsize=15)
plt.ylabel('y', fontsize=15)
plt.title('t vs y graph')
plt.legend()
plt.show()