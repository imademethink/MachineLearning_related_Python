#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
import scipy.interpolate as interpolate


'''
Interpolation is the process of 
finding a value between two points on a line 
or a curve.
'''

kinds = ('nearest', 
         'zero', 
         'linear', 
         'slinear', 
         'quadratic', 
         'cubic')

''' x- axis values '''
x = np.array([0.0,1.0,2.0,3.0,
              4.0,5.0,6.0,7.0,
              8.0,9.0])

''' y- axis values '''
y = np.array([10,5,39,3,6,9,41,73,57,88])

''' plot original values '''
plt.plot(x, y, 'o')

''' new x-axis values to be interpolated '''
new_x = np.linspace(0.0, 9.0, 25)

''' interpolate for kind = 'nearest' '''
new_y = interpolate.interp1d(x,y,kind='nearest')(new_x)
plt.plot(new_x, new_y, color='C1', linewidth=1)

''' interpolate for kind = 'zero' '''
new_y = interpolate.interp1d(x,y,kind='zero')(new_x)
plt.plot(new_x, new_y, color='C2', linewidth=1)

''' interpolate for kind = 'linear' '''
new_y = interpolate.interp1d(x,y,kind='linear')(new_x)
plt.plot(new_x, new_y, color='C3', linewidth=1)

''' interpolate for kind = 'slinear' '''
new_y = interpolate.interp1d(x,y,kind='slinear')(new_x)
plt.plot(new_x, new_y, color='C4', linewidth=1)

''' interpolate for kind = 'cubic' '''
new_y = interpolate.interp1d(x,y,kind='cubic')(new_x)
plt.plot(new_x, new_y, color='C5', linewidth=1)

plt.legend(['original','nearest','zero',
            'linear','slinear','cubic'])
plt.show()




''' plotting all types in single graph '''
fig, axs = plt.subplots(
        nrows=len(kinds)+1, 
        sharex=True)
axs[0].plot(x, y, 'bo-')
axs[0].set_title('raw')
for ax, kind in zip(axs[1:], kinds):
    new_y = interpolate.interp1d(
            x, 
            y, 
            kind=kind)(new_x)
    ax.plot(new_x, new_y, 'ro-')
    ax.set_title(kind)
plt.show()



''' spliners '''
''' to draw smooth curves through data points '''
from scipy.interpolate import UnivariateSpline

''' x- axis values '''
x = np.array([0.0,1.0,2.0,3.0,
              4.0,5.0,6.0,7.0,
              8.0,9.0])

''' y- axis values '''
y = np.array([10,25,39,58,16,91,41,73,57,88])
''' plot original values '''
plt.plot(x, y, 'o')

new_x = np.linspace(0.0, 9.0, 25)
new_y = interpolate.interp1d(x,y,kind='nearest')(new_x)
spl = UnivariateSpline(new_x, new_y)
spl.set_smoothing_factor(0.001)
plt.plot(new_x, spl(new_x), color='C6', linewidth=2)

