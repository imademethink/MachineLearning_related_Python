#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np

def print_this_matrix(given_matrix):
  for i in range(len(given_matrix)):
   for j in range(len(given_matrix[i])):
    print (given_matrix[i][j]," ",end="")
   print()
  print("\n")


# reshape an array to 4 x 4 matrix
# note -- input array should be multiple of 4*4 = 16
arr_now = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
print("arr_now =             ",arr_now)
arr_reshaped_to_2d = np.reshape(arr_now,(4,4))
print("arr_reshaped_to_2d -- after reshape = \n",arr_reshaped_to_2d)
print("\n")

matrix_student = np.array([['Roy',11,12,13,14,15],
                        ['John',21,22,23,24,25],
                        ['Dave',31,32,33,34,35],
                        ['Deidra',41,42,43,44,45],
                        ['April',51,52,53,54,55]])

# append a row at the last
matrix_student = np.append(matrix_student,[['Lee',61,62,63,64,65]],0)
print("matrix_student after append =             ")
print_this_matrix(matrix_student)
print("\n")

# insert a row at a given index
matrix_student = np.insert(matrix_student,3,[['Ted',71,72,73,74,75]],axis=0)
print("matrix_student after insert =             ")
print_this_matrix(matrix_student)
print("\n")

# insert a col at a given index
matrix_student = np.insert(matrix_student,1,[["col1","col1","col1","col1","col1","col1","col1"]],axis=1)
print("matrix_student after inserting column =             ")
print_this_matrix(matrix_student)
print("\n")

# delete a row at given index
matrix_student = np.delete(matrix_student,[2],0)
print("matrix_student after deleting row at given index =             ")
print_this_matrix(matrix_student)
print("\n")

# delete multiple rows starting at given start and end index
matrix_student = np.delete(matrix_student,slice(0,2),axis=0)
print("matrix_student after deleting row at given index =             ")
print_this_matrix(matrix_student)
print("\n")

matrix_student = np.array([['Roy',11,12,13,14,15],
                        ['John',21,22,23,24,25],
                        ['Dave',31,32,33,34,35],
                        ['Deidra',41,42,43,44,45],
                        ['April',51,52,53,54,55]])
# delete a col at given index
matrix_student = np.delete(matrix_student,[2],1)
print("matrix_student after deleting column at given index =             ")
print_this_matrix(matrix_student)
print("\n")

# delete multiple columns starting at given start and end index
matrix_student = np.delete(matrix_student,slice(3,10),1)
print("matrix_student after deleting columns starting at given start and end index =             ")
print_this_matrix(matrix_student)
print("\n")

matrix_student = np.array([['Roy',11,12,13,14,15],
                        ['John',21,22,23,24,25],
                        ['Deidra',41,42,43,44,45],
                        ['April',51,52,53,54,55]])
print("matrix_student =             ",matrix_student)
# shape give row x col
print("matrix_student.shape() is tuple =             ",matrix_student.shape)
print("\n")

arr_zeros           = np.zeros((2,2))   # Create an array of 2 x 2 filled with all zeros
arr_ones            = np.ones((3,2))   # Create an array of 3 x 2 filled with all ones
arr_random          = np.random.random((3,2)) # Create an array of 3 x 2 filled with all random float values
arr_random2         = np.random.rand(18,5) # 18 row x 5 col
arr_custom_int      = np.full((5,6), 22) # Create an array of n x m filled all with customr value
arr_custom_float    = np.full((5,6), 2.2222) # Create an array of n x m filled all with customr value
arr_identity_matrix = np.eye(6) # Create an identity matrix of n x n
print("arr_random =             \n",arr_random)
arr_empty_like = np.empty_like(arr_custom_int) # Create a matrix copying given matrix but empty
print("arr_empty_like =             \n",arr_empty_like)
print("\n")

arr35 = np.array([[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15]])
print("arr35 =             \n")
print_this_matrix(arr35)

arr52 = np.array([[11,16],[12,17],[13,18],[14,19],[15,20]])
print("arr52 =             \n")
print_this_matrix(arr52)







arr_final_32 = arr35.dot(arr52)
print("arr_final_32 = dot product of 2 arrays =             \n")
print_this_matrix(arr_final_32)

arr351 = np.array([[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15]])
arr352 = np.array([[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15]])
arr_vector_product = np.vdot(arr351, arr352)
print("arr_vector_product = vector product of 2 arrays =             \n",arr_vector_product)
print("\n")




arr3n5 = np.array([[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15]])
print("arr3n5 =             \n")
print_this_matrix(arr3n5)
print("sum(arr3n5) == ",sum(arr3n5))
print("sum(arr3n5, axis=0) == ",sum(arr3n5, axis=0))
print("sum(arr3n5, axis=1) == ",sum(arr3n5, axis=1))
print("\n")

arr3n5 = arr3n5.T # transpose of matrix
print("arr3n5 transpose of matrix =             \n")
print_this_matrix(arr3n5)
print("\n")




''' add child array in each parent array : row wise'''
arr2n5 = np.array([[1,2],[3,4],[5,6],[7,8],[9,10]])
print("arr2n5 =             \n")
print_this_matrix(arr2n5)
arr2n5new = np.empty_like(arr2n5)
print("arr2n5new =             \n", arr2n5new)
eachrowadd = np.array([5,8])
print("eachrowadd =             \n", eachrowadd)
for i in range(arr2n5new.shape[0]):
    arr2n5new[i, :] = arr2n5[i, :] + eachrowadd
print("arr2n5new =             \n", arr2n5new)
print("\n")


# 'complex': [numpy.complex64, numpy.complex128, numpy.complex192],
# 'float': [numpy.float16, numpy.float32, numpy.float64, numpy.float96],
# 'int': [numpy.int8, numpy.int16, numpy.int32, numpy.int32, numpy.int64],
# 'others': [bool, object, str, unicode, numpy.void],
# 'uint': [numpy.uint8, numpy.uint16, numpy.uint32, numpy.uint32, numpy.uint64]

''' declaring array as intended dtype '''
arr_dype_unsigned_int  = np.array([[1,2],[3,4],[5,6],[7,8],[9,10]],dtype=np.uint)
print("arr_dype_unsigned_int  = \n", arr_dype_unsigned_int)
arr_dype_int  = np.array([[1,2],[3,4],[5,6],[7,8],[9,10]],dtype=np.int)
print("arr_dype_int  = \n", arr_dype_int)
arr_dype_int8 = np.array([[1,2],[3,4],[5,6],[7,8],[9,10]],dtype=np.int8)
print("arr_dype_int8 = \n", arr_dype_int8)
arr_dype_int16 = np.array([[1,2],[3,4],[5,6],[7,8],[9,10]],dtype=np.int16)
print("arr_dype_int16= \n", arr_dype_int16)
arr_dype_int32 = np.array([[1,2],[3,4],[5,6],[7,8],[9,10]],dtype=np.int32)
print("arr_dype_int32= \n", arr_dype_int32)
print("\n")





matrix_student = np.array([['Roy',11,12,13,14,15],
                        ['John',21,22,23,24,25],
                        ['Deidra',41,42,43,44,45],
                        ['April',51,52,53,54,55]])
print("matrix_student original = \n", matrix_student)
print("matrix_student.shape  = \n", matrix_student.shape)
print_this_matrix(matrix_student)
print("matrix_student.ravel() i.e. flattened 1d array = \n", matrix_student.ravel())
print("reshape will not change orignal array")
print("matrix_student.reshape(8,3)  = \n", matrix_student.reshape(8,3))
print("resize will change orignal array permenantly")
matrix_student.resize(8,3)
print("matrix_student.resize(8,3)  = \n", matrix_student)
print("\n")




print("stacking of different types of array")
matrix_student1= np.array([['Roy',11,12,13,14,15],
                        ['John',21,22,23,24,25],
                        ['Deidra',41,42,43,44,45],
                        ['April',51,52,53,54,55]])
matrix_student2= np.array([['Roy',11,12,13,14,15],
                        ['John',21,22,23,24,25],
                        ['Deidra',41,42,43,44,45],
                        ['April',51,52,53,54,55]])
print("matrix_student1 original = \n", matrix_student1)
print("matrix_student2 original = \n", matrix_student2)






arr_first_4n3 = np.array([['zero',  1,  True,  3],
                       ['twelve', 13, False, 15]])
arr_second_4n3 = np.array([['four',  5,  False,  7],
                        ['eight',  9, True, 11]])
print("arr_first_4n3   = \n", arr_first_4n3)
print("arr_second_4n3  = \n", arr_second_4n3)
print("verticle stacking   col count should match --> arr_first_4n3 and arr_second_4n3  = \n", 
      np.vstack((arr_first_4n3,arr_second_4n3)))
print("horizontal stacking row count should match --> arr_first_4n3 and arr_second_4n3  = \n", 
      np.hstack((arr_first_4n3,arr_second_4n3)))
print("concatenate vertically \n",   np.concatenate((arr_first_4n3,arr_second_4n3), axis=0))
print("concatenate horizontally \n", np.concatenate((arr_first_4n3,arr_second_4n3), axis=1))
print("\n")






print("place arrays as column in another array")
arr_c1 = np.array([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])
arr_c2 = np.array([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])
newaxis = 1
print("arr_c1   = \n", arr_c1)
print("arr_c2   = \n", arr_c2)
print("c1 and c2 side by side   = \n", np.column_stack((arr_c1,arr_c2)))
print("\n")



''' add array element using + symbol  '''
arr_reshaped_to_2d = [[ 0,  1,  2,  3],
                      [ 4,  5,  6,  7],
                      [ 8,  9, 10, 11],
                      [12, 13, 14, 15]]
arr_reshaped_to_2d = arr_reshaped_to_2d  + [[10,10,10,10]]
arr_reshaped_to_2d = arr_reshaped_to_2d  + [[20,20,20,20]]
print("arr_reshaped_to_2d -- after addition using + symbol       = \n",arr_reshaped_to_2d)
print("\n")






matrix_student = np.array([['Roy',11,12,13,14,15],
                        ['John',21,22,23,24,25],
                        ['Dave',31,32,33,34,35],
                        ['Deidra',41,42,43,44,45],
                        ['April',51,52,53,54,55]])
print("matrix_student =             ")
print_this_matrix(matrix_student)






# get selected slice of matrix elements
print("get selected slice of matrix elements")
print("---> from row 1 to row 3 and from col 2 to col 3")
print("matrix_student[1:3,[2,3]] ==\n", matrix_student[1:3,[2,3]])
print("---> from row 0 to row 3 and from col 2 to col 3")
print("matrix_student[:3,[2,3]]  ==\n", matrix_student[:3,[2,3]])
print("---> from row 1 to row last and from col 2 to col 3")
print("matrix_student[1:,[2,3]]  ==\n", matrix_student[1:,[2,3]])
print("---> from row 1 to row 4 and from col 0 to col 0")
print("matrix_student[1:4,0]     ==\n", matrix_student[1:4,0])
print("---> from row 1 to row 4 and from col 0 to col last")
print("matrix_student[1:4]     ==\n", matrix_student[1:4])
print("\n")







matrix_student = np.array([['Roy',11,12,13,14,15],
                        ['John',21,22,23,24,25],
                        ['Dave',31,32,33,34,35],
                        ['Deidra',41,42,43,44,45],
                        ['April',51,52,53,54,55],
                        ['Harry',61,62,63,64,65]])
print("matrix_student =             ")
print_this_matrix(matrix_student)

# split matrix elements
print("split matrix elements")
print("---> split matrix horizontally into equal columns")
print("hsplit(matrix_student,2)[0])     ==\n", np.hsplit(matrix_student,2)[0])
print("hsplit(matrix_student,2)[1])     ==\n", np.hsplit(matrix_student,2)[1])
print("hsplit(matrix_student,3)[0])     ==\n", np.hsplit(matrix_student,3)[0])
print("---> split matrix vertically into equal rows")
print("vsplit(matrix_student,2)[0])     ==\n", np.vsplit(matrix_student,2)[0])
print("vsplit(matrix_student,2)[1])     ==\n", np.vsplit(matrix_student,2)[1])
print("vsplit(matrix_student,3)[0])     ==\n", np.vsplit(matrix_student,3)[0])
print("\n")






# also simple array_split for 1d normal array
arr_normal = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
print("arr_normal =          ",arr_normal)
print("simple 1d array split -- array_split(arr_normal,4)[3] ",np.array_split(arr_normal,4)[3])
print("simple 1d array split -- array_split(arr_normal,2)[1] ",np.array_split(arr_normal,2)[1])
print("\n")




# same array with multiple names etc
arr_1 = np.array([['Roy',11,12,13,14,15],
               ['John',21,22,23,24,25],
               ['Dave',31,32,33,34,35],
               ['Deidra',41,42,43,44,45],
               ['April',51,52,53,54,55],
               ['Harry',61,62,63,64,65]])
arr_2 = arr_1
print("id(arr_1) =          ",id(arr_1))
print("id(arr_2) =          ",id(arr_2))
print("arr_1 is arr_2 =     ",arr_1 is arr_2)




# using view() method, which creates just another name of the object
# shape view doesn't change even shape of original changed
print("arr_1.shape =        ",arr_1.shape)
arr_3 = arr_1.view()
arr_1.resize(12,3)
print("arr_1.shape =        ",arr_1.shape)
print("arr_3.shape =        ",arr_3.shape)

arr_1 = np.array([['Roy',11,12,13,14,15],
               ['John',21,22,23,24,25],
               ['Dave',31,32,33,34,35],
               ['Deidra',41,42,43,44,45],
               ['April',51,52,53,54,55],
               ['Harry',61,62,63,64,65]])


# using copy() method, which creates fresh copy of the object
arr_4 = arr_1.copy()
print("arr_4 after copying arr_1 =        \n",arr_4)
print("id(arr_1) =          ",id(arr_1))
print("id(arr_4) =          ",id(arr_4))
print("arr_1 is arr_4 =     ",arr_1 is arr_4)

