#!/usr/bin/env python3
# -*- coding: utf-8 -*-

''' lasso regression
Least Absolute Shrinkage and Selection Operator.
It is a regression method that involves penalizing 
the absolute size of the regression coefficients.

It is a penalized regression type.

By penalizing (or equivalently constraining the 
sum of the absolute values of the estimates) 
you end up in a situation where some of the parameter 
estimates may be exactly zero. 

The larger the penalty applied, the further estimates 
are shrunk towards zero.

This is convenient when we want some automatic 
feature/variable selection, or when dealing with highly 
correlated predictors, where standard regression will 
usually have regression coefficients that are 'too large'.
'''

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

def fx1(x):
    res   = (12.0  * x)
    error = 0.0
    error = res * random.uniform(-error_induce, error_induce)
    return res + error
def fx2(x2):
    res   = (-05.0 * x2)
    error = 0.0
    error = res * random.uniform(-error_induce, error_induce)
    return res + error
def fx3(x3):
    res   = (09.0 * x3)
    error = 0.0
    error = res * random.uniform(-error_induce, error_induce)
    return res + error
def fx4(x4):
    res   = (29.0 * x4)
    error = 0.0
    error = res * random.uniform(-error_induce, error_induce)
    return res + error
def fx5(x5):
    res   = (8.0 * x5)
    error = 0.0
    error = res * random.uniform(-error_induce, error_induce)
    return res + error
def fx6(x6):
    res   = (2.0 * x6)
    error = 0.0
    error = res * random.uniform(-error_induce, error_induce)
    return res + error
def fx7(x7):
    res   = (52.0 * x7)
    error = 0.0
    error = res * random.uniform(-error_induce, error_induce)
    return res + error
def fx8(x8):
    res   = (16.0 * x8)
    error = 0.0
    error = res * random.uniform(-error_induce, error_induce)
    return res + error
def fx9(x9):
    res   = (6.0 * x9)
    error = 0.0
    error = res * random.uniform(-error_induce, error_induce)
    return res + error
def fx10(x10):
    res   = (09.0 * x10)
    error = 0.0
    error = res * random.uniform(-error_induce, error_induce)
    return res + error
def fx11(x11):
    res   = (11.0 * x11)
    error = 0.0
    error = res * random.uniform(-error_induce, error_induce)
    return res + error
def fx12(x12):
    res   = (-12.0 * x12)
    error = 0.0
    error = res * random.uniform(-error_induce, error_induce)
    return res + error

''' data preparation '''
max_sample_value = 50
total_samples    = 800
train_sample_cnt = int((total_samples * 60.0 / 100.0))
test_sample_cnt  = total_samples - train_sample_cnt

random_array     = np.random.randint (
                       max_sample_value,
                       size=total_samples).astype(float)
x1_samples       = fx1(random_array)
x2_samples       = fx2(random_array)
x3_samples       = fx3(random_array)
x4_samples       = fx4(random_array)
x5_samples       = fx5(random_array)
x6_samples       = fx6(random_array)
x7_samples       = fx7(random_array)
x8_samples       = fx8(random_array)
x9_samples       = fx9(random_array)
x10_samples      = fx10(random_array)
x11_samples      = fx11(random_array)
x12_samples      = fx12(random_array)

t_samples        =  x1_samples 
+ x2_samples + x3_samples + x4_samples 
+ x5_samples + x6_samples + x7_samples 
+ x8_samples + x9_samples + x10_samples 
+ x11_samples+ x12_samples

t_samples        = t_samples + constant

''' splitting samples into train data and test data '''
x1_samples_train, x1_samples_test = np.split(
                                     x1_samples, [train_sample_cnt,])
x2_samples_train, x2_samples_test = np.split(
                                     x2_samples, [train_sample_cnt,])
x3_samples_train, x3_samples_test = np.split(
                                     x3_samples, [train_sample_cnt,])
x4_samples_train, x4_samples_test = np.split(
                                     x4_samples, [train_sample_cnt,])
x5_samples_train, x5_samples_test = np.split(
                                     x5_samples, [train_sample_cnt,])
x6_samples_train, x6_samples_test = np.split(
                                     x6_samples, [train_sample_cnt,])
x7_samples_train, x7_samples_test = np.split(
                                     x7_samples, [train_sample_cnt,])
x8_samples_train, x8_samples_test = np.split(
                                     x8_samples, [train_sample_cnt,])
x9_samples_train, x9_samples_test = np.split(
                                     x9_samples, [train_sample_cnt,])
x10_samples_train,x10_samples_test= np.split(
                                     x10_samples, [train_sample_cnt,])
x11_samples_train,x11_samples_test= np.split(
                                     x11_samples, [train_sample_cnt,])
x12_samples_train,x12_samples_test= np.split(
                                     x12_samples, [train_sample_cnt,])
t_samples_train, t_samples_test   = np.split(
                                     t_samples, [train_sample_cnt,])

''' combining all variables in column structure '''
xyz_samples_train   = {'colx1' : x1_samples_train,
                       'colx2' : x2_samples_train,
                       'colx3' : x3_samples_train,
                       'colx4' : x4_samples_train,
                       'colx5' : x5_samples_train,
                       'colx6' : x6_samples_train,
                       'colx7' : x7_samples_train,
                       'colx8' : x8_samples_train,
                       'colx9' : x9_samples_train,
                       'colx10': x10_samples_train,
                       'colx11': x11_samples_train,
                       'colx12': x12_samples_train}
dfxyz_samples_train = pd.DataFrame(data=xyz_samples_train)
dft_samples_train   = pd.DataFrame(data=t_samples_train)

xyz_samples_test    = {'colx1' : x1_samples_test,
                       'colx2' : x2_samples_test,
                       'colx3' : x3_samples_test,
                       'colx4' : x4_samples_test,
                       'colx5' : x5_samples_test,
                       'colx6' : x6_samples_test,
                       'colx7' : x7_samples_test,
                       'colx8' : x8_samples_test,
                       'colx9' : x9_samples_test,
                       'colx10': x10_samples_test,
                       'colx11': x11_samples_test,
                       'colx12': x12_samples_test}

dfxyz_samples_test  = pd.DataFrame(data=xyz_samples_test)
dft_samples_test    = pd.DataFrame(data=t_samples_test)

''' finally using lasso regression to fit '''
lasso_regr          = linear_model.Lasso(alpha = .01)
lasso_model         = lasso_regr.fit(dfxyz_samples_train,
                                     dft_samples_train)

''' predictions and other calculations '''
predictions         = lasso_model.predict(dfxyz_samples_test)
print("predictions   = ", predictions)
print("lasso_model.score(X,y) = ", lasso_model.score(dfxyz_samples_test,
                                   dft_samples_test))
print("lasso_model.coef_      = ")
for single_coeff in lasso_model.coef_:
    print (single_coeff)
print("lasso_model.intercept_ = %.2f" %lasso_model.intercept_)

''' now we are going to plot the points 
    just the difference between actual and expected '''
prediced_difference = np.subtract(
                            dft_samples_test.values, 
                            predictions.reshape(
                                    dft_samples_test.values.size,
                                    1))
plt.title('LASSO regression - difference between actual and expected', fontsize=16)
plt.xlabel('test sample count', fontsize=14)
plt.ylabel('difference value' , fontsize=14)

plt.plot(np.arange(prediced_difference.size), 
         prediced_difference,
         color='b')
plt.show()

''' also try this 
https://gist.github.com/yoavram/378777660e13b77d6daf
'''
