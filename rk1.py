#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 21:16:43 2020

@author: suman
"""

def f(x,t):
    return 1/(x*x+t*t) #y' of the differential equation
h=0.1 #stepsize
t=0 #initial value of t
x=1 #initial value of x
while t<3.5*10**6:
    k1=h*f(t,x)
    k2=h*f(t+h/2,x+k1/2)
    k3=h*f(t+h/2,x+k2/2)
    k4=h*f(t+h,x+k3)
    x=x+(1/6)*(k1+2*k2+2*k3+k4) #value of x at each iteration
    t=t+h
print('The value of x at t=3.5*10^6 is',x)
