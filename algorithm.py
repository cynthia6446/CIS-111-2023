# -*- coding: utf-8 -*-
"""
Created on Thu Jun 15 17:22:39 2023

@author: chenriquez4
"""
import numpy as np

import matplotlib.pyplot as plt



def f(x):
    
    """
    f(x) = exp(x) - x**2
    Parameters
    ----------
    x : TYPE flaot
        DESCRIPTION. input to the function f(x)

    Returns
    -------
    y : output of the function, f(x)

    """

    #y = np.exp(x) - x**2
    y= x**2-3*x+1
    return y

## find x so that f(x) = 0


xAxis = np.linspace(-3,1)
y = f(xAxis)

plt.plot(xAxis, y)
plt.axhline(y=0, color='red', ls=':')

xLow = 1
xHigh = -1

for i in range(25):
    
        xTry = (xLow+xHigh)/2
        if f(xTry) > 0:
            xHigh = xTry
        else:
            xLow = xTry
            
        #print(f"x = {xTry}, f(x) = {f(xTry)}")
        
print(f"final ans= {xTry}, f = {f(xTry): 0.5f}")
        
    
    