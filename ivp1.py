#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 12:09:18 2020

@author: suman
"""

import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import solve_ivp

def f(t,y):
    return t*np.exp(3*t)-2*y #y' of differential equation
time = np.linspace(0,1,100)
Y = solve_ivp(f,(0,1),[0],t_eval=time) #solve using scipy function
plt.plot(Y.t,Y.y[0,:],label='numerical solution') #plotting of numerical solution
def g(t):
    return (1/25)*np.exp(-2*t)*(1 -np.exp(5 *t) + 5* np.exp(5* t)* t) #analytical solution
t = np.linspace(0, 1, 100)
plt.plot(t, g(t),label='analytical solution') #plotting analytical solution
plt.xlabel('t', fontsize=15)
plt.ylabel('y', fontsize=15)
plt.title('t vs y graph')
plt.legend()
plt.show()