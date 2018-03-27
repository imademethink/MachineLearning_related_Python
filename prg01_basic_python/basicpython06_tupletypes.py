#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# tuple
tuple_a = (0xddd,'var 2','dd' * 2,'',-4.5,'fifth element')
print("tuple_a=        ",   tuple_a)
print("tuple_a[5]=     ",   tuple_a[5])
print("negative index tuple_a[-4]= ",tuple_a[-4])	# count from right
print("\n")

print("tuple_a[:2]=     " , 	tuple_a[:2])
print("tuple_a[2:]=     " , 	tuple_a[2:])
print("tuple_a[0:3]=    " , 	tuple_a[0:3])
print("\n")

tuple_in  = (3,5,'%%')
tuple_out = (tuple_in,tuple_in)
tuple_add = tuple_in + tuple_in
print("tuple_in =		" , 	tuple_in)
print("tuple inside another tuple")
print("tuple_out=		" , 	tuple_out)
print("tuple addition")
print("tuple_add=		" , 	tuple_add)
print("\n")

tuple_b = tuple_a
print("tuple_b=		" , 	tuple_b)
# both pointing to same tuple
print("tuple_a[5]=	" , 	tuple_a[5])
print("tuple_b[5]=	" , 	tuple_b[5])
print("\n")

print("len(tuple_a)=" , 	len(tuple_a))
print("\n")

for lst_element in tuple_a:
    print("lst_element= ",lst_element)
print("\n")

tuple_c = (9, 8, 7, 6, 5)
print("tuple_c=       ",tuple_c)
tuple_c = set(tuple_c)
print("set(tuple_c)=  ",tuple_c)
print("\n")

tuple_d = (90, 80, 70, 60, 58)
print("max(tuple_d)=	" , 	max(tuple_d))
print("\n")

tuple_1 = [15,1,'two',3.3]
tuple_2 = [1,'two',3.3]
tuple_3 = ['dummy',1,'two',3.3]
tuple_4 = ['dummy',1,'three',3.3]
print("tuple_1                    =	" , 	tuple_1)
print("tuple_2                    =	" , 	tuple_2)
print("tuple_3                    =	" , 	tuple_3)
print("tuple_4                    =	" , 	tuple_4)
print("set(tuple_1)               =	" , 	set(tuple_1))
print("set(tuple_1) & set(tuple_2) =	" , 	set(tuple_1) & set(tuple_2))
print("set(tuple_1) | set(tuple_3) =	" , 	set(tuple_1) | set(tuple_3))
print("set(tuple_1) < set(tuple_4) =	" , 	set(tuple_1) < set(tuple_4))
print("set(tuple_4) < set(tuple_1) =	" , 	set(tuple_4) < set(tuple_1))
print("set(tuple_1) - set(tuple_4) =	" , 	set(tuple_1) - set(tuple_4))
print("set(tuple_4) - set(tuple_1) =	" , 	set(tuple_4) - set(tuple_1))
print("\n")

tuple_math=[0,3,7,8,2,0.01,0xABCD]
print("tuple_math                        =	" , 	tuple_math)
print("min(tuple_math)                   =	" , 	min(tuple_math))
print("max(tuple_math)                   =	" , 	max(tuple_math))
print("\n")

print("sorted(tuple_math)                =	" , 	sorted(tuple_math))
print("tuple_math                        =	" , 	tuple_math)
print("sorted(tuple_math,reverse=True)   =	" , 	sorted(tuple_math,reverse=True))
print("tuple_math                        =	" , 	tuple_math)
print("\n")

print("tuple_math                        =	" , 	tuple_math)
tuple_math.sort()
print("tuple_math.sort()                 =	" , 	tuple_math)
tuple_math.sort(reverse=True)
print("tuple_math.sort(reverse=True)     =	" , 	tuple_math)
print("\n")

tuple_methods=('dummy',9999.0,'three',3.3,3.3,(1,2,77,3.3))
# count occurance of particular element
print("tuple_methods.count(9999.0)          =	" , 	tuple_methods.count(9999.0))
print("tuple_methods.index([1,2,77,3.3])    =	" , 	tuple_methods.index((1,2,77,3.3)))
print("\n")

# list to touple
lst = ['milk','powder','bread']
print("lst original                         =	" , 	lst)
print("lst original to tpl                 =	" , 	tuple(lst))
print("\n")

# dictionary to list
d_dict={"tc1":"pass","tc_title":"regression test","tested at":25101981} 
print("d_dict                               =   " , 	d_dict)
tuple_keys   = tuple([ v for v in d_dict.keys() ])
print("tuple_keys                           =   " , 	tuple_keys)
tuple_values = tuple([ v for v in d_dict.values() ])
print("tuple_values                         =   " , 	tuple_values)
tuple_items   = tuple([ v for v in d_dict.items() ])
print("tuple_items                          =   " , 	tuple_items)
print("\n")








