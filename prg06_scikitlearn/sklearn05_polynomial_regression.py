#!/usr/bin/env python3
# -*- coding: utf-8 -*-

''' polynomial regression
It is a form of regression analysis in which 
the relationship between the independent variable x 
and the dependent variable y is modelled as an 
nth degree polynomial in x.

y = c0 * x^0 + c1 * x^1 +
    c2 * x^2 + c3 * x^3 + ..... + cn * x ^n
n = degree
'''


import random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

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

y1_samples       = fx1(np.arange(total_samples))
y2_samples       = fx2(np.arange(total_samples))
y3_samples       = fx3(np.arange(total_samples))

t_samples        = y1_samples + y2_samples + y3_samples

t_samples        = t_samples + constant

''' splitting samples into train data and test data '''
y1_samples_train, y1_samples_test = np.split(
                                     y1_samples, [train_sample_cnt,])
y2_samples_train, y2_samples_test = np.split(
                                     y2_samples, [train_sample_cnt,])
y3_samples_train, y3_samples_test = np.split(
                                     y3_samples, [train_sample_cnt,])
t_samples_train, t_samples_test   = np.split(
                                     t_samples, [train_sample_cnt,])

''' combining all variables in column structure '''
xyz_samples_train   = {'colx1' : y1_samples_train,
                       'colx2' : y2_samples_train,
                       'colx3' : y3_samples_train}
dfxyz_samples_train = pd.DataFrame(data=xyz_samples_train)
dft_samples_train   = pd.DataFrame(data=t_samples_train)

xyz_samples_test    = {'colx1' : y1_samples_test,
                       'colx2' : y2_samples_test,
                       'colx3' : y3_samples_test}

dfxyz_samples_test  = pd.DataFrame(data=xyz_samples_test)
dft_samples_test    = pd.DataFrame(data=t_samples_test)

''' use PolynomialFeatures to fit and transform a model'''
poly     = PolynomialFeatures(degree=3, include_bias=False)
poly_fit = poly.fit_transform(
            np.arange(train_sample_cnt)[:, np.newaxis])

''' prepare a linear regression model finally for prediction '''
lm            = LinearRegression().fit(poly_fit, dft_samples_train)
#predictions   = lm.predict(poly_fit)
predictions   = lm.predict(dfxyz_samples_test)

print("predictions   = ", predictions)
print("lm.score(X,y) = ", lm.score(dfxyz_samples_test,
                                   dft_samples_test))
print("lm.coef_      = ", lm.coef_)
print("lm.intercept_ = %.2f" %lm.intercept_)

''' now we are going to plot the points 
    just the difference between actual and expected '''
prediced_difference = np.subtract(
                            dft_samples_test.values, 
                            predictions)
plt.title('Polynomial Regression - difference between actual and expected', fontsize=16)
plt.xlabel('test sample count', fontsize=14)
plt.ylabel('difference value' , fontsize=14)

plt.plot(np.arange(prediced_difference.size), 
         prediced_difference,
         color='b')
plt.show()

