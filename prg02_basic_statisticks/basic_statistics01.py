#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://www.mathportal.org/calculators/statistics-calculator/standard-deviation-calculator.php

import numpy as np 

def print_this_matrix(given_matrix):
  for i in range(len(given_matrix)):
   for j in range(len(given_matrix[i])):
    print (given_matrix[i][j]," ",end="")
   print()
  print("\n")

arr_extreme = np.array([[ 4,   5,  6,   7],
                        [ 3,  -1, -2,  -3],
                        [ 8,   9,  10,  11],
                        [12,   13, 14,  15]])
print("np.ptp() -- difference between max and min")
print("np.ptp(arr_extreme)                     --->",np.ptp(arr_extreme))
print("np.ptp(arr_extreme, axis=0)--vertical   --->",np.ptp(arr_extreme, axis=0))
print("np.ptp(arr_extreme, axis=1)--horizontal --->",np.ptp(arr_extreme, axis=1))

print("np.percentile() -- percentitle of sum of given range of values")
print("np.percentile(arr_extreme)                     --->",np.percentile(arr_extreme,10))        # 10% of the total values 
print("np.percentile(arr_extreme, axis=0)--vertical   --->",np.percentile(arr_extreme,10,axis=0)) # 10% of the total values
print("np.percentile(arr_extreme, axis=1)--horizontal --->",np.percentile(arr_extreme,10,axis=1)) # 10% of the total values

print("np.mean() -- mean = 50% percentile")
print("np.mean(arr_extreme)                     --->",np.mean(arr_extreme))
print("np.mean(arr_extreme, axis=0)--vertical   --->",np.mean(arr_extreme, axis=0))
print("np.mean(arr_extreme, axis=1)--horizontal --->",np.mean(arr_extreme, axis=1))

print("np.median() -- middle number or avg of the middle 2 numbers")
print("np.median(arr_extreme)                     --->",np.median(arr_extreme))
print("np.median(arr_extreme, axis=0)--vertical   --->",np.median(arr_extreme, axis=0))
print("np.median(arr_extreme, axis=1)--horizontal --->",np.median(arr_extreme, axis=1))

print("np.average(arr_extreme)                     --->",np.average(arr_extreme))
print("np.std(arr_extreme)    standard deviation   --->",np.std(arr_extreme))
print("np.var(arr_extreme)    variance             --->",np.var(arr_extreme))
print("\n")

arr_extreme = np.array([[ 4,   5,  6,   7],
                        [ 3,  -1, -2,  -3],
                        [ 8,   9,  10,  11],
                        [12,   13, 14,  15]])
print_this_matrix(arr_extreme)
print("np.amin(arr_extreme)                    --->",np.amin(arr_extreme))
print("np.amin(arr_extreme, axis=0)--vertical  --->",np.amin(arr_extreme, axis=0))
print("np.amin(arr_extreme, axis=1)--horizontal--->",np.amin(arr_extreme, axis=1))
print("just index of sorted element")
arr_extreme.flatten()
print("np.argmin(arr_extreme, axis=1)--horizontal--->",np.argmin(arr_extreme, axis=1))


from scipy import stats

arr_extreme = np.array([[ 4,   5,  6,   7],
                        [ 3,  -1, -2,  -3],
                        [ 8,   9,  10,  11],
                        [12,   13, 14,  15]])

stats.describe(arr_extreme)
