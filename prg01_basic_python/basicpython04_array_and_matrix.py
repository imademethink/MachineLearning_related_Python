#!/usr/bin/env python3
# -*- coding: utf-8 -*-

array_1_d = ["emp_01","sales",30000, 0.4]
array_2_d = [array_1_d, ["emp_02","prod",40000, 0.45], ["emp_03","procurement",350000, 0.5]]

print ("array_1_d                     == ",array_1_d)
print ("array_1_d.index(\"sales\")    == ",array_1_d.index("sales"))
array_1_d.remove(0.4)
print ("array_1_d after remove(0.4)   == ",array_1_d)
array_1_d.insert(len(array_1_d),0.4)
print ("array_1_d after insert(len(array_1_d),0.4)        == ",array_1_d)
array_1_d.pop(2)
print ("array_1_d after pop(2)        == ",array_1_d)
print ("array_1_d                     == ",array_1_d)
print ("array_2_d[1]                  == ",array_2_d[1])
print ("array_2_d                     == ",array_2_d)
print ("array_2_d.index([\"emp_03\",\"procurement\",350000, 0.5])    == ",array_2_d.index(["emp_03","procurement",350000, 0.5]))

print("access array elements using simple for loop")
for i in range(len(array_2_d)):
 for j in range(len(array_2_d[i])):
  print (array_2_d[i][j]," ",end="")
 print()
print("\n")

print("access array elements using simple for loop part 2")
for row in array_2_d:
 for e in row:
  print (e," ",end="")
 print()
print("\n")

myarr=[
  [0,1,2,3],
  [4,5,6,7],
  [8,9,10,11],
  [12,13,14,15]]
print("myarr =             ",myarr)
print("myarr[3] =          ",myarr[3])
print("myarr[3][0]=        ",myarr[3][0])
print("myarr[1:3]=         ",myarr[1:3])    # only row 1 to row 3
print("\n")

