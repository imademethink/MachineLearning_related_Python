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
file_raw_data           = base_path + 'employee_data.csv'
emp_data_df             = pd.read_csv(file_raw_data,
                                  header='infer',
                                  sep=',',
                                  #delimiter='\s+',
                                  index_col=False,
                                  dtype = 'object')
emp_data_values         = emp_data_df.values
print(emp_data_values.size)
nparr_bonus_ratings     = emp_data_values[:,1:3].astype(float)
print('original values \n',nparr_bonus_ratings)
# plotting raw values
plt.plot(nparr_bonus_ratings)
plt.xticks(np.arange(0, nparr_bonus_ratings.size/2, 1.0))
plt.xlabel('samples')
plt.ylabel('bonus')
plt.title('plotting sample vs bonus')
plt.show()

# Clustering basics - diagram
# K-means clustering - eucleadian distance, root of squares formulae
# centroid and distortions
# kmeans method and parameter (mandatory, optional) explaination
# simple to complex examples
#       different data points
#       centroid moves towards dense area
#       iteration count (default=10) and centroid co-ordinate value consistency
#       centroid count
# vector quantisation
# plotting
# kmeans2 example

# data points



data                = nparr_bonus_ratings
#data               = whiten(data1)
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
plt.xlabel('bonus')
plt.ylabel('rating')
plt.title('plotting bonus vs rating - clustered')
plt.show()

# use this for 3 centroids when data= data6
#plt.plot(data[idx==0,0],data[idx==0,1],'ob',
#     data[idx==1,0],data[idx==1,1],'or',
#     data[idx==2,0],data[idx==2,1],'og') # third cluster points
#plt.plot(centroids[:,0],centroids[:,1],'sm',markersize=8)
#plt.show()



#import time

#t = (2009, 2, 17, 17, 3, 38, 1, 48, 0)
#t = (1981, 1, 5, 10, 0, 0, 0, 0, 0)
#t = time.mktime(t)
#print (type(int(time.strftime("%j", time.gmtime(t)))))

