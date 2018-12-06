#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd


''' Logistic Regression 
It is a Machine Learning classification algorithm 
that is used to predict the probability of a categorical 
dependent variable. In logistic regression, the dependent 
variable is a binary variable that contains data coded 
as 1 (yes, success, etc.) or 0 (no, failure, etc.). 
In other words, the logistic regression model predicts 
P(Y=1) as a function of X.
'''
                           
''' data preparation '''
total_samples    = 20
train_sample_cnt = 12
base_path        = '/home/imademethink/prg06_scikitlearn/'
file_raw_data    = base_path + 'employee_data.csv'
emp_date_df      = pd.read_csv(file_raw_data,
                                  header='infer',sep=',',index_col=False,
                                  dtype = 'object')

''' converting categorical variables to a dummy indicators '''
emp_date_df      = pd.get_dummies(emp_date_df)
emp_date_values  = emp_date_df.values

x_samples_train, x_samples_test = np.split(
                                     emp_date_values[:,:-1],[train_sample_cnt,])
y_samples_train, y_samples_test = np.split(
                                     emp_date_values[:,-1], [train_sample_cnt,])

''' model fitting '''
from sklearn.linear_model import LogisticRegression
logisticRegr     = LogisticRegression()
logisticRegr.fit(x_samples_train, y_samples_train)

''' preditions '''
predictions      = logisticRegr.predict(x_samples_test)
print(predictions)

''' preditions score'''
score            = logisticRegr.score(x_samples_test, y_samples_test)
score            = score * 100
print("Prediction accuracy precentage : ", score)
