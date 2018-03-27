#!/usr/bin/env python3
# -*- coding: utf-8 -*-





#       some images in download folder





import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
np.set_printoptions(precision=3)


'''
read input data from csv file
'''
base_path               = '/home/imademethink/prg_datascience/c04_data_split_train_test/'
file_emp_data           = base_path + 'employee_data.csv'
emp_data_values_df      = pd.read_csv(file_emp_data,
                                  header='infer',
                                  sep=',',
                                  index_col=False,
                                  dtype = 'object')

nparray_unsplit_values  = emp_data_values_df.values
print('original unsplit values \n',nparray_unsplit_values)
print(type(nparray_unsplit_values))
print(nparray_unsplit_values.shape)
print(nparray_unsplit_values)



'''
simple split (default split size (test_size  = 0.25 or 25%))
split without label data
'''
from sklearn.cross_validation import train_test_split
data_df                 = nparray_unsplit_values[:,:-1]
data_train, data_test   = train_test_split(data_df)

print('original data set row x col            ', data_df.shape)
print('train data set after split row x col   ', data_train.shape)
print('test data set after split row x col    ', data_test.shape)




'''
simple split (default split size (test_size  = 0.25 or 25%))
'''
from sklearn.cross_validation import train_test_split
data_df                 = nparray_unsplit_values[:,:-1]
nparr_labels            = nparray_unsplit_values[:,-1:]
data_train, data_test, 
nparr_labels_train, nparr_labels_test = train_test_split(
        data_df, 
        nparr_labels)

print('original data set row x col            ', data_df.shape)
print('original lablels set row x col         ', nparr_labels.shape)
print('train data set after split row x col   ', data_train.shape)
print('train data set after split row x col   ', nparr_labels_train.shape)
print('test data set after split row x col    ', data_test.shape)
print('test data set after split row x col    ', nparr_labels_test.shape)




'''
simple split (custom split size (test_size  = 0.25 or 25%))
'''
from sklearn.cross_validation import train_test_split
data_df                 = nparray_unsplit_values[:,:-1]
nparr_labels            = nparray_unsplit_values[:,-1:]
data_train, data_test, 
nparr_labels_train, nparr_labels_test = train_test_split(data_df, nparr_labels, test_size=0.1)

print('original data set: row x col            ', data_df.shape)
print('original lablels set: row x col         ', nparr_labels.shape)
print('train data set after split: row x col   ', data_train.shape)
print('train data set after split: row x col   ', nparr_labels_train.shape)
print('test data set after split: row x col    ', data_test.shape)
print('test data set after split: row x col    ', nparr_labels_test.shape)




'''
split into test_data, train_data, split_data
'''
X_train, X_test, y_train, y_test 
    = train_test_split(X, y, test_size=0.2, random_state=1)

X_train, X_val, y_train, y_val 
    = train_test_split(X_train, y_train, test_size=0.2, random_state=1)



'''
split with get to know index of original data which was split
'''
from sklearn.cross_validation import train_test_split
import numpy as np
data = np.array([[11,22], 
                 [33,44], 
                 [55,66], 
                 [77,88], 
                 [99,99], 
                 [12,23], 
                 [34,45], 
                 [56,78], 
                 [89,10], 
                 [98,87],], np.int32)
labels = np.array([41,42,43,44,45,46,47,48,49,50], np.int32)
indices = np.arange(10)
data_train, data_test, nparr_labels_train, nparr_labels_test, data_train_index, data_test_index = train_test_split(
        data, labels, indices, test_size=0.2, random_state=1)


