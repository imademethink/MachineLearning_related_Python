#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np

# arrange array increments by 1.0
arr = np.arange(2.1, 10.1, dtype = np.float)
print ("---simple float array --- using np.arange(2.1, 10, dtype = np.float) ---\n",arr)
print ("---array data type ---- :",arr.dtype)
print ("\n")

arr_linespace = np.linspace(0.4, 10.09, 6)
print ("---float array with linspace --- using np.linspace(0.4, 10.09, 6) ---\n",arr_linespace)
print ("---array data type ---- :",arr_linespace.dtype)
print ("\n")

mtrx_simple = np.matrix(np.linspace(0.4, 80.44, 16).reshape(4,4))
print ("---simple float matrix --- using np.matrix(np.linspace(0.4, 80.44, 16)).reshape(4,4) ---\n",mtrx_simple)
print ("---conjugate transpose ---\n",mtrx_simple.H)
print ("---transpose of self ---\n",mtrx_simple.T)




print ("\n")