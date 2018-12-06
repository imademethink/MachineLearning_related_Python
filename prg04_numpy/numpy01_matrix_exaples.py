#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np 
import numpy.matlib as npmatlib


def print_this_matrix(given_matrix):
  for i in range(len(given_matrix)):
   for j in range(len(given_matrix[i])):
    print (given_matrix[i][j]," ",end="")
   print()
  print("\n")

def print_this_string_matrix(given_matrix):
  for i in range(len(given_matrix)):
   for j in range(len(given_matrix[i])):
    print (given_matrix[i][j],end="")
   print()
  print("\n")



print("generatng matrix for given n x m - with given default values")
print(npmatlib.ones((5,6)))
print("generatng matrix for given n x m - with given default values")
print(npmatlib.zeros((4,3)))

# returns a matrix with 1 along the diagonal elements and the zeros elsewhere.
# K =  start index to start first 1
print(np.matlib.eye(n = 5, M = 8, k = 6, dtype = float))
print(np.matlib.eye(n = 5, M = 5, k = 3, dtype = float))

print("generatng identity matrix for given n x n - with given default values")
print(np.matlib.identity(5, dtype = float))

print("generatng identity matrix for given n x n - with given default values")
print(np.matlib.rand(3,3))

print("generatng matrix for given n x m - with random values")
print(np.matlib.rand(3,3))

print("generatng matrix from given array")
arr_now = np.array([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])
print(np.matrix(arr_now))
arr_now = np.array([[0,1,2,3],[4,5,6,7],[8,9,10,11],[12,13,14,15]])
print(np.matrix(arr_now))

arr_now = np.array([[0,1,2,3],[4,5,6,7],[8,9,10,11],[12,13,14,15]])
print("as matrix from given array -- \n", np.asmatrix(arr_now))

matrx_now = np.matlib.ones((5,6))
print("as array from given matrix -- \n", np.asarray(matrx_now))


# inner product
arr_normal = np.array([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])
print("arr_normal =   \n",arr_normal)
print("inner product  \n",np.inner(arr_normal,arr_normal))


arr_2d_1 = [[ 0,  1,  2,  3],
            [ 4,  5,  6,  7],
            [ 8,  9, 10, 11],
            [12, 13, 14, 15]]
arr_2d_2 = [[ 0,  1,  2,  3],
            [ 4,  5,  6,  7],
            [ 8,  9, 10, 11],
            [12, 13, 14, 15]]
print("arr_2d_1 =   \n",arr_2d_1)
print("arr_2d_2 =   \n",arr_2d_2)
print("np.matmul(arr_2d_1,arr_2d_2) =   \n",np.matmul(arr_2d_1,arr_2d_2))




# solving linear equation
aaa=   2.0
bbb= - 9.0
ccc=  55.0
print(( 9 * aaa) + (    bbb) - (10 * ccc)) # -541
print((-8 * aaa) - (5 * bbb) - ( 0 * ccc)) #  029
print(( 9 * aaa) + (3 * bbb) + ( 1 * ccc)) #  046

eq1      = np.array([[9,1,-10],[-8,-5,0],[9,3,1]])
eq_total = np.array([-541,29,46])
print("np.linalg.solve(eq1, eq_total) =   \n",np.linalg.solve(eq1, eq_total))

arr_extreme = np.array([[ 4,   5,  6,   7],
                        [ 3,  -1, -2,  -3],
                        [ 8,   9,  10,  11],
                        [12,   13, 14,  15]])
print("np.amax(arr_extreme)                    --->",np.amax(arr_extreme))
print("np.amax(arr_extreme, axis=0)--vertical  --->",np.amax(arr_extreme, axis=0))
print("np.amax(arr_extreme, axis=1)--horizontal--->",np.amax(arr_extreme, axis=1))
print("np.amax(arr_extreme, axis=1)--horizontal--->",np.amax(arr_extreme, axis=1))

# flatten : return a copy of the array collapsed into one dimension
arr_extreme.flatten()
print("just index of sorted element")
print("np.argmax(arr_extreme, axis=1)--horizontal--->",np.argmax(arr_extreme, axis=1))


print("numbers sorting using numpy--->")
arr_tosort = np.array([[ 4.,   5.,  6,  -7],
                       [ 3.,  -1., -2,  -3],
                       [ 8.,   9.,  10, -11],
                       [12.,   13.,-14,  15]],dtype='float64')
print_this_matrix(arr_tosort)

print("np.sort() does not change original array --->\n")
print("np.sort(arr_tosort)                          --->\n",np.sort(arr_tosort))
print("np.sort(arr_tosort,axis = 0)   vertically    --->\n",np.sort(arr_tosort,axis = 0))
print("np.sort(arr_tosort,axis = 1)   horizontally  --->\n",np.sort(arr_tosort,axis = 1))
print("sort on a row --->\n",arr_tosort[arr_tosort[:,1].argsort()])

print_this_matrix(arr_tosort)
print("array_name.sort() changes original array --->")
arr_tosort.sort()
print("after arr_tosort.sort() --->")
print_this_matrix(arr_tosort)
print("\n")


print("string sorting using numpy--->")
input_string_array = np.array(["year","month","eye","i","stream","key","house"])
print("input string array")
print_this_string_matrix(input_string_array)
input_string_array_sorted_index = list(map(lambda x: len(x), input_string_array))
output_string_array = input_string_array[np.argsort(input_string_array_sorted_index)]
print("output string array sorted ---> ")
print_this_string_matrix(output_string_array)
print("\n")



arr_where = np.array([[ 4.,   5.,  6,  -7],
                      [ 3.,  -1., -2,  -3],
                      [ 8.,   9.,  10, -11],
                      [12.,   13.,-14,  15]],dtype='float64')
print_this_matrix(arr_where)
arr_idx_greater_than = np.where(arr_where > 5.5)
print("indices of elements greater than 5.5     --->",arr_idx_greater_than)
print("all actual elements greater than 5.5     --->",arr_where[arr_idx_greater_than])
print("shape of resultant array is always 1d    --->",arr_where[arr_idx_greater_than].shape)
print("\n")


print("numpy extract elements out of an array with a condition")
arr_extract = np.array([[ 4.,   5.,  6,  -7],
                        [ 3.,  -1., -2,  -3],
                        [ 8.,   9.,  10, -11],
                        [12.,   13.,-14,  15]],dtype='float64')
print_this_matrix(arr_where)
condition = np.mod(arr_extract,2.0) == 0
print("condition = np.mod(arr_extract,2.0) == 0  ----> ",np.mod(arr_extract,2.0) == 0)
print("np.extract(condition, arr_extract)        ----> ",np.extract(condition, arr_extract))
print("\n")

print("save array output to a .npy file")
arr_saveme = np.array([[ 4.,   5.,  6,  -7],
                       [ 3.,  -1., -2,  -3],
                       [ 8.,   9.,  10, -11],
                       [12.,   13.,-14,  15]],dtype='float64')
np.save('__arr_saveme',arr_saveme)
print("load array output from a .npy file \n",np.load('__arr_saveme.npy'))
print("\n")
