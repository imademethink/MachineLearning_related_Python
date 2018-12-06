#!/usr/bin/env python3
# -*- coding: utf-8 -*-


''' basic example '''
import numpy as np
import matplotlib.pyplot as plt
from scipy import interpolate

x = np.arange(0,10)
y = np.exp(-x/3.0)
f = interpolate.interp1d(x, y, fill_value='extrapolate')

print (f(9))
print (f(15)) # extrapolated value got here


import numpy as np
import scipy.interpolate as interpolate

'''
Extrapolation is the process of 
finding a value outside two points 
on a line or a curve.
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
new_x = np.linspace(0.0, 19.0, 25)

''' extrapolation for kind = 'nearest' '''
new_y = interpolate.interp1d(x,y,kind='nearest',fill_value='extrapolate')(new_x)
plt.plot(new_x, new_y, color='C1', linewidth=1)

''' extrapolation for kind = 'zero' does not work and not applicable '''
#new_y = interpolate.interp1d(x,y,kind='zero',fill_value='extrapolate')(new_x)
#plt.plot(new_x, new_y, color='C2', linewidth=1)

''' extrapolation for kind = 'linear' '''
new_y = interpolate.interp1d(x,y,kind='linear',fill_value='extrapolate')(new_x)
plt.plot(new_x, new_y, color='C3', linewidth=1)

''' extrapolation for kind = 'slinear' does not work and not applicable '''
#new_y = interpolate.interp1d(x,y,kind='slinear',fill_value='extrapolate')(new_x)
#plt.plot(new_x, new_y, color='C4', linewidth=1)

''' extrapolation for kind = 'cubic' does not work and not applicable '''
#new_y = interpolate.interp1d(x,y,kind='cubic',fill_value='extrapolate')(new_x)
#plt.plot(new_x, new_y, color='C5', linewidth=1)

plt.legend(['original','nearest','linear'])
plt.show()



''' Extrapolation using InterpolatedUnivariateSpline and custom order type '''
import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import InterpolatedUnivariateSpline

# given values
xi = np.array([0.2, 0.5, 0.7, 0.9])
yi = np.array([0.3, 0.1, 0.2, 0.1])
# expand x values
x = np.linspace(0, 1.5, 50)
# spline order: 1=linear, 2=quadratic, 3=cubic ... 
order = 1
# do inter/extrapolation
s = InterpolatedUnivariateSpline(xi, yi, k=order)
y = s(x)

# example showing the interpolation for following kind
# linear, quadratic and cubic interpolation
#plt.figure()
plt.plot(xi, yi)


for order_new in range(1, 4):
    s = InterpolatedUnivariateSpline(xi, yi, k=order_new)
    y = s(x)
    plt.plot(x, y)
plt.legend(['linear','quadratic','cubic'])
plt.show()

