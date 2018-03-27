#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# list
list_a = [0xddd,'var 2','dd' * 2,'',-4.5,'fifth element']
print("list_a=		" , 	list_a)
print("list_a[5]=	" , 	list_a[5])
print("negative index list_a[-4]=	" , 	list_a[-4])	# count from right
list_a[5]=5
print("list_a[5]=	" , 	list_a[5])
list_a.insert(6,6.6)				#insert
print("list_a[6]=	" , 	list_a[6])
list_a.append(7.7 * 2)				#append
print("list_a[7]=	" , 	list_a[7])
print("list_a[:2]   =	" , 	list_a[:2])
print("list_a[2:]   =	" , 	list_a[2:])
print("list_a[0:3]   =	" , 	list_a[0:3])
print("list_a+[1,2,3,4]=" , 	list_a + [1,2,3,4])
list_in  = [3,5,'%%']
list_out = [list_in,list_in]
print("list_in =		" , 	list_in)
print("list inside another list")
print("list_out=		" , 	list_out)
print("\n")


list_b = list_a
print("list_b=		" , 	list_b)
list_b[5]=55					# both pointing to same list
print("list_a[5]=	" , 	list_a[5])
print("\n")


del (list_a[5])
print("delete(list_a[5])=" , 	list_a[5])
print("\n")


print("len(list_a)=	" , 	len(list_a))
print("\n")


for lst_element in list_a:
    print("lst_element=		" , 	lst_element)
print("\n")


list_c = [9, 8, 7, 6, 5]
print("list_c=		" , 	list_c)
list_c = set(list_c)
print("set(list_c)=	" , 	list_c)
print("\n")


list_d = [90, 80, 70, 60, 58]
print("max(list_d)=	" , 	max(list_d))
print("\n")


list_1 = [15,1,'two',3.3]
list_2 = [1,'two',3.3]
list_3 = ['dummy',1,'two',3.3]
list_4 = ['dummy',1,'three',3.3]
print("list_1                    =	" , 	list_1)
print("list_2                    =	" , 	list_2)
print("list_3                    =	" , 	list_3)
print("list_4                    =	" , 	list_4)
print("set(list_1)               =	" , 	set(list_1))
print("set(list_1) & set(list_2) =	" , 	set(list_1) & set(list_2))
print("set(list_1) | set(list_3) =	" , 	set(list_1) | set(list_3))
print("set(list_1) < set(list_4) =	" , 	set(list_1) < set(list_4))
print("set(list_4) < set(list_1) =	" , 	set(list_4) < set(list_1))
print("set(list_1) - set(list_4) =	" , 	set(list_1) - set(list_4))
print("set(list_4) - set(list_1) =	" , 	set(list_4) - set(list_1))
print("\n")

list_math=[0,3,7,8,2,0.01,0xABCD]
print("list_math                        =	" , 	list_math)
print("min(list_math)                   =	" , 	min(list_math))
print("max(list_math)                   =	" , 	max(list_math))
print("\n")

print("sorted(list_math)                =	" , 	sorted(list_math))
print("list_math                        =	" , 	list_math)
print("sorted(list_math,reverse=True)   =	" , 	sorted(list_math,reverse=True))
print("list_math                        =	" , 	list_math)
print("\n")

list_math.sort()
print("list_math.sort()                 =	" , 	list_math)
list_math.sort(reverse=True)
print("list_math.sort(reverse=True)     =	" , 	list_math)
print("\n")

list_temp   =['milk','powder']
list_methods=['dummy',9999.0,'three',3.3,3.3,[1,2,77,3.3]]
print("list_methods                        =	" , 	list_methods)
list_methods.append(555)
print("list_methods after append           =	" , 	list_methods)
print("list_methods.count(3.3)             =	" , 	list_methods.count(3.3))
list_methods.extend(list_temp)
print("list_methods after extend           =	" , 	list_methods)
print("list_methods.index([1,2,77,3.3])    =	" , 	list_methods.index([1,2,77,3.3]))
print("list_methods.index(9999.0)          =	" , 	list_methods.index(9999.0))
list_methods.insert(1,'inserted_1')
print("list_methods.insert(1,'inserted_1') =	" , 	list_methods)
list_methods.reverse()
print("list_methods.reverse()              =	" , 	list_methods)
print("\n")

# touple to list
tpl = ('milk','powder','bread')
print("tpl original                         =	" , 	tpl)
print("tpl original to list                 =	" , 	list(tpl))
print("\n")

# dictionary to list
d_dict={"tc1":"pass","tc_title":"regression test","tested at":25101981} 
print("d_dict                               =   " , 	d_dict)
list_keys   = [ v for v in d_dict.keys() ]
print("list_keys                            =   " , 	list_keys)
list_values = [ v for v in d_dict.values() ]
print("list_values                          =   " , 	list_values)
list_items   = [ v for v in d_dict.items() ]
print("list_items                           =   " , 	list_items)
print("\n")


