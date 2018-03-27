#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
#from pylab import show as sh_show
from scipy.cluster.vq import vq
from scipy.cluster.vq import kmeans
import numpy as np
import pandas as pd
np.set_printoptions(precision=3)

base_path               = '/home/imademethink/prg05_scipy/'
file_raw_data           = base_path + 'temperature_data.csv'
temperature_date_df     = pd.read_csv(file_raw_data,
                                  header='infer',sep=',',index_col=False,
                                  dtype = 'object')
temperature_date_values = temperature_date_df.values

# get the temperature and day number of the year
temperature_date_values = np.append(
                                temperature_date_values[:,:-1], 
                                np.arange(1,366).reshape(365,1),
                                axis=1)

# plotting raw values
plt.plot(temperature_date_values[:,-2])
plt.xticks(np.arange(0, temperature_date_values.size, 1.0))
plt.ylabel('original values')
plt.show()

# get columnwise data
c1               = pd.Series(temperature_date_values[:,2:3].ravel())
only_day_count   = pd.to_numeric(c1, errors='ignore')
c2               = pd.Series(temperature_date_values[:,1:2].ravel())
only_temperature = pd.to_numeric(c2, errors='ignore')

# merge column wise data
data = np.hstack((
        only_day_count.values.reshape(365,1),
        only_temperature.values.reshape(365,1)))
centroid_count      = 2
iterations_kmeans   = 1000
threshold_kmeans    = 0.01
# computing K-Means with K = 2 (2 clusters)
for x in range(0, 1):
    centroids,distortion = kmeans(
            data,
            centroid_count,
            iterations_kmeans,
            threshold_kmeans)
    print("centroids  =\n",centroids)
    print("distortion =\n",distortion)
# assign each sample to a cluster
idx,_ = vq(data,centroids)
print("idx  =\n",idx)

# some plotting using numpy's logical indexing
plt.plot(data[idx==0,0],data[idx==0,1],'ob',
         data[idx==1,0],data[idx==1,1],'or')
plt.plot(centroids[:,0],
         centroids[:,1],'sg',markersize=8)
plt.show()




# use this for 3 centroids when data= data6
plt.plot(data[idx==0,0],data[idx==0,1],'ob',
     data[idx==1,0],data[idx==1,1],'or',
     data[idx==2,0],data[idx==2,1],'og') # third cluster points
plt.plot(centroids[:,0],centroids[:,1],'sm',markersize=8)
plt.show()


