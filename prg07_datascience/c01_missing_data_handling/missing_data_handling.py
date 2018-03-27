#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
from sklearn.preprocessing import Imputer
import matplotlib.pyplot as plt

base_path = '/home/imademethink/prg_datascience/c01_missing_data_handling/'
file_missing_data_NaN       = base_path + 'missing_data_NaN.csv'
file_missing_data_blank     = base_path + 'missing_data_blank.csv'
file_missing_data_selected  = base_path + 'missing_data_selected.csv'


# ----------------------------------------------------------                   
# Handle blank values
# Replace blank or NaN values with mean of all all values
input_missing_data_blank = pd.read_csv(file_missing_data_blank,
                                       header='infer',sep=',',index_col=False,
                                       dtype = 'float32')
print (input_missing_data_blank)
# plotting raw values
plt.plot(np.arange(input_missing_data_blank.size), input_missing_data_blank)
plt.xticks(np.arange(0, input_missing_data_blank.size, 1.0))
plt.ylabel('input raw data')
plt.show()


imputer_blank            = Imputer( missing_values = 'NaN',  strategy = 'mean')
imputer_blank            = imputer_blank.fit(input_missing_data_blank)
input_missing_data_blank = imputer_blank.transform(input_missing_data_blank)
print(input_missing_data_blank)
plt.plot(np.arange(input_missing_data_blank.size), input_missing_data_blank)
plt.xticks(np.arange(0, input_missing_data_blank.size, 1.0))
plt.ylabel('input raw data')
plt.show()


# ----------------------------------------------------------                   
# Handle selected or intended values
# First replace intended values by np.NaN
# Then follow the normal process
input_missing_data_selected = pd.read_csv(file_missing_data_selected,
                                          header='infer',sep=',',index_col=False,
                                          dtype = 'float32')
print (input_missing_data_selected)
# plotting raw values
plt.plot(input_missing_data_selected)
plt.xticks(np.arange(0, input_missing_data_selected.size, 1.0))
plt.ylabel('input raw data')
plt.show()

input_missing_data_selected = input_missing_data_selected.replace(0.0, np.NaN)
print (input_missing_data_selected)
# plotting selected data
plt.plot(input_missing_data_selected)
plt.xticks(np.arange(0, input_missing_data_selected.size, 1.0))
plt.ylabel('input selected selected')
plt.show()


imputer_selected            = Imputer( missing_values = 'NaN',  strategy = 'mean')
imputer_selected            = imputer_selected.fit(input_missing_data_selected)
input_missing_data_selected = imputer_selected.transform(input_missing_data_selected)
print(input_missing_data_selected)
# plotting selected data
plt.plot(input_missing_data_selected)
plt.xticks(np.arange(0, input_missing_data_selected.size, 1.0))
plt.ylabel('input data with mean values')
plt.show()

# ----------------------------------------------------------                   
# Remove missing data lines
# Remove particular row where corresponding column valus is NaN
input_missing_data_NaN = pd.read_csv(file_missing_data_NaN,
                                     header='infer',sep=',',index_col=False,
                                     dtype = 'float32')
print (input_missing_data_NaN)
# plotting raw values
plt.plot(input_missing_data_NaN)
plt.xticks(np.arange(0, input_missing_data_NaN.size, 1.0))
plt.ylabel('input raw data')
plt.show()

# remove all coloumns with missing data
input_missing_data_NaN = input_missing_data_NaN.dropna(axis=0, how='all')
print (input_missing_data_NaN)
# plotting removed values
plt.plot(input_missing_data_NaN)
plt.xticks(np.arange(0, input_missing_data_NaN.size, 1.0))
plt.ylabel('input data with removed columns')
plt.show()

