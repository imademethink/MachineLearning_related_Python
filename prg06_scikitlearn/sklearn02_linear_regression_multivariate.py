#!/usr/bin/env python3
# -*- coding: utf-8 -*-

''' https://www.desmos.com/calculator '''
''' linear regression using Ordinary Least Squares '''

import numpy as np
import pandas as pd
from sklearn import linear_model
import random
import matplotlib.pyplot as plt

''' multi variable linear equation '''
''' t = 12x -0.5y + 9z + 24
'''
constant     = 24
error_induce = 0.01

def fx(x):
    res   = (12.0  * x)
    error = 0.0
    error = res * random.uniform(-error_induce, error_induce)
    return res + error
def fy(y):
    res   = (-05.0 * y)
    error = 0.0
    error = res * random.uniform(-error_induce, error_induce)
    return res + error
def fz(z):
    res   = (09.0 * z)
    error = 0.0
    error = res * random.uniform(-error_induce, error_induce)
    return res + error

''' data preparation '''
max_sample_value = 50
total_samples    = 100
train_sample_cnt = int((total_samples * 80.0 / 100.0))
test_sample_cnt  = total_samples - train_sample_cnt

random_array     = np.random.randint (
                       max_sample_value,
                       size=total_samples).astype(float)
x_samples        = fx(random_array)
y_samples        = fy(random_array)
z_samples        = fz(random_array)

t_samples        = x_samples + y_samples + z_samples
t_samples        = t_samples + constant

''' splitting samples into train data and test data '''
x_samples_train, x_samples_test = np.split(
                                     x_samples, [train_sample_cnt,])
y_samples_train, y_samples_test = np.split(
                                     y_samples, [train_sample_cnt,])
z_samples_train, z_samples_test = np.split(
                                     z_samples, [train_sample_cnt,])
t_samples_train, t_samples_test = np.split(
                                     t_samples, [train_sample_cnt,])

''' combining all variables in column structure '''
xyz_samples_train   = {'colx': x_samples_train,
                       'coly': y_samples_train,
                       'colz': z_samples_train}
dfxyz_samples_train = pd.DataFrame(data=xyz_samples_train)
dft_samples_train   = pd.DataFrame(data=t_samples_train)

xyz_samples_test    = {'colx': x_samples_test,
                       'coly': y_samples_test,
                       'colz': z_samples_test}
dfxyz_samples_test  = pd.DataFrame(data=xyz_samples_test)
dft_samples_test    = pd.DataFrame(data=t_samples_test)

''' finally using linear model to fit '''
lm                  = linear_model.LinearRegression()
model               = lm.fit(dfxyz_samples_train,
                             dft_samples_train)

''' predictions and other calculations '''
predictions         = lm.predict(dfxyz_samples_test)
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
plt.title('Multi variable linear regression - difference between actual and expected', fontsize=16)
plt.xlabel('test sample count', fontsize=14)
plt.ylabel('difference value' , fontsize=14)

plt.plot(np.arange(prediced_difference.size), 
         prediced_difference,
         color='b')
plt.show()

