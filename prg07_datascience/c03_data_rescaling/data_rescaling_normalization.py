#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import Binarizer
import matplotlib.pyplot as plt
np.set_printoptions(precision=3)

base_path               = '/home/imademethink/prg_datascience/c03_data_rescaling/'
file_unscaled_data      = base_path + 'unscaled_data.csv'
unscaled_values_df      = pd.read_csv(file_unscaled_data,
                                  header='infer',sep=',',index_col=False,
                                  dtype = 'object')
nparray_unscaled_values = unscaled_values_df.values
# extract required column - bonus (amount)
nparr_bonus             = nparray_unscaled_values[:,1:].astype(float)
print('original values \n',nparr_bonus)
# plotting raw values
plt.plot(nparr_bonus)
plt.xticks(np.arange(0, nparr_bonus.size, 1.0))
plt.ylabel('original values')
plt.show()

#===============================================================
# min-max scaler
# rescale data (between lower limits and upper limits)
lower_limit             = -1
lower_upper             = 1
minmaxscaler            = MinMaxScaler(feature_range=(lower_limit, lower_upper))
nparr_scaled_values     = minmaxscaler.fit_transform(nparr_bonus)
print('scaled values \n',nparr_scaled_values)

# plotting re-scaled values
plt.plot(nparr_scaled_values)
plt.xticks(np.arange(0, nparr_scaled_values.size, 1.0))
plt.ylabel('re-scaled values')
plt.show()



#===============================================================
# standard scaler
nparr_scaled_values     = StandardScaler().fit_transform(nparr_bonus)
print('scaled values \n',nparr_scaled_values)
# plotting re-scaled values
plt.plot(nparr_scaled_values)
plt.xticks(np.arange(0, nparr_scaled_values.size, 1.0))
plt.ylabel('re-scaled values')
plt.show()



#===============================================================
# scaler to slace values in binary fashion with a threshold
nparr_scaled_values     = Binarizer(threshold=24000.0).fit_transform(nparr_bonus)
print('scaled values \n',nparr_scaled_values)
# plotting re-scaled values
plt.plot(nparr_scaled_values)
plt.xticks(np.arange(0, nparr_scaled_values.size, 1.0))
plt.ylabel('re-scaled values')
plt.show()




