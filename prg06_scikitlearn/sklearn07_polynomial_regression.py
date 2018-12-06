#!/usr/bin/env python3
# -*- coding: utf-8 -*-

''' polynomial regression using numpy.polyfit
It is a form of regression analysis in which 
the relationship between the independent variable x 
and the dependent variable y is modelled as an 
nth degree polynomial in x.

y = c0 * x^0 + c1 * x^1 +
    c2 * x^2 + c3 * x^3 + ..... + cn * x ^n
n = degree


numpy.polyfit
Least squares polynomial fit
Returns a vector of coefficients p 
    that minimises the squared error
'''

import random
import numpy as np
import matplotlib.pyplot as plt

''' sample polynomial equation with degree=3'''
''' t =    24.0 * x^0
         + 12.0 * x^1
         -  0.5 * x^2
         +  9.0 * x^3
'''

constant     = 24
error_induce = 0.01

def fx1(x1):
    res   = (12.0  * x1)
    error = 0.0
    error = res * random.uniform(-error_induce, error_induce)
    return res + error
def fx2(x2):
    res   = (-0.50 * x2 * x2)
    error = 0.0
    error = res * random.uniform(-error_induce, error_induce)
    return res + error
def fx3(x3):
    res   = (09.0 * x3 * x3 * x3)
    error = 0.0
    error = res * random.uniform(-error_induce, error_induce)
    return res + error

''' data preparation '''
max_sample_value = 50
total_samples    = 800
train_sample_cnt = int((total_samples * 60.0 / 100.0))
test_sample_cnt  = total_samples - train_sample_cnt
train_sample     = np.linspace(1,train_sample_cnt,train_sample_cnt)
test_sample      = np.linspace(train_sample_cnt,total_samples,test_sample_cnt)

y1_samples       = fx1(np.arange(total_samples))
y2_samples       = fx2(np.arange(total_samples))
y3_samples       = fx3(np.arange(total_samples))

t_samples        = y1_samples + y2_samples + y3_samples

t_samples        = t_samples + constant

''' splitting samples into train data and test data '''
t_samples_train, t_samples_test   = np.split(
                                     t_samples, 
                                     [train_sample_cnt,])

''' use numpy.polyfit for fitting data '''
coefs   = np.polyfit(np.arange(train_sample_cnt),
                       t_samples_train,
                       3)

print("intercept_ = ", coefs[3])
print("coef_      = ", coefs[2],coefs[1],coefs[0])

''' fit a polynomial with above coefficients'''
ffit = np.poly1d(coefs)

plt.title('Polynomial Regression using numpy.polyfit', fontsize=16)
plt.plot(train_sample,t_samples_train)
plt.plot(test_sample,ffit(test_sample))
plt.show()


plt.title('Polynomial Regression using numpy.polyfit: Difference between actual and expected', fontsize=16)
plt.plot(np.linspace(1,test_sample_cnt,test_sample_cnt),
         (ffit(test_sample) - t_samples_test))
plt.show()

