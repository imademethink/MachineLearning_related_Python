#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from pylab import plot,show
from numpy import array
#from numpy.random import *
from scipy.cluster.vq import vq
from scipy.cluster.vq import kmeans
import numpy as np


# data points
data11                     = array([[1.,1.],[2.,2.],[3.,3.],[4.,4.],[5. ,5.],[2.,1.],[3.,2.],[4.,3.],[5.,4.],[6. ,5.]],dtype='float64')
data                       = data11
centroid_count       = 2
iterations_kmeans  = 1000
threshold_kmeans  = 0.01
# computing K-Means with K = 2 (2 clusters)
centroids,distortion = kmeans(data,centroid_count)
# assign each sample to a cluster
idx,_ = vq(data,centroids)
print("data.          =\n",data)
print("centroids.  =\n",centroids)
print("distortion. =\n",distortion)
print("idx.            =\n",idx) # idx represent an index of applicable centroid to each data member
                                            # in this case total centroid are 2 so index range is 0 to 1

# some plotting using numpy's logical indexing
plot(data[idx==0,0],data[idx==0,1],'ob',   data[idx==1,0],data[idx==1,1],'or')
plot(centroids[:,0],centroids[:,1],'sg',markersize=8)
show()





data22  = np.array([[0.5,2.]],dtype='float64')
data      = data22
# assign each sample to another cluster
idx,_      = vq(data,centroids)
print("idx  =\n",idx)

# some plotting using numpy's logical indexing
plot(data[idx==0,0],data[idx==0,1],'ob',   data[idx==1,0],data[idx==1,1],'or')
plot(centroids[:,0],centroids[:,1],'sg',markersize=8)
show()

