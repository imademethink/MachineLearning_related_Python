#!/usr/bin/env python3
# -*- coding: utf-8 -*-

d_dict={"tc1":"pass","tc_title":"regression test","tested at":25101981} 
print("d_dict=                      ",d_dict)
print("d_dict[\"tc_title\"]=        ",d_dict["tc_title"])
print("d_dict.get(\"tc_title\")=    ",d_dict.get("tc_title"))
print("d_dict.keys()=               ",d_dict.keys())
print("d_dict.values()=             ",d_dict.values())
print("\n")

d_dict_tuple={"tc1":"pass",(1,2,3):25101981} 
print("d_dict_tuple=            ",   d_dict_tuple)
print("d_dict_tuple[(1,2,3)]=   ",   d_dict_tuple[(1,2,3)])
print("\n")

d_dict_previous={"song":"oldies","dance":"traditional"}
d_dict={"tc1":"pass","tc_title":"regression test","tested at":25101981} 
d_dict_new={"pass":"more than 60%","fail": d_dict_previous}
print("d_dict=                ",   d_dict)
print("d_dict_new=            ",   d_dict_new)
print("d_dict_previous=       ",   d_dict_previous)
print("d_dict_new[[d_dict[\"tc1\"]]]=  ",   d_dict_new[d_dict["tc1"]])
print("d_dict_new[\"fail\"]=  ",   d_dict_new["fail"])
print("d_dict_new[\"fail\"][\"dance\"]=  ",   d_dict_new["fail"]["dance"])
print("\n")

d_dict_new={"pass":"more than 60%","fail": d_dict_previous}
print("before delete - len(d_dict_new)=       ",   len(d_dict_new))
del(d_dict_new["fail"])
print("after delete  - len(d_dict_new)=       ",   len(d_dict_new))
print("\n")

d_dict_search={
	"make":"a wish",
	"keep kalm":"and code python",
	"usa":"HIMYM",
	"uk":"bond",
	"empty":"",
	"awesome":"me"}
if "awesome" in d_dict_search:
	print("if true =                                ", d_dict_search["awesome"])
if "no awesome" not in d_dict_search:
	print("if false=                                ", d_dict_search["awesome"])
print("\n")

d_dict_copied = d_dict_search.copy()
print("d_dict_search=            ",   d_dict_search)
print("d_dict_copied=            ",   d_dict_copied)
print("\n")

print("len(d_dict_copied) =            ",   len(d_dict_copied))
d_dict_copied.clear()
print("d_dict_copied after clear =     ",   d_dict_copied)
print("len(d_dict_copied) =            ",   len(d_dict_copied))
print("\n")

# iterating through dictionary
dd={
	"make":"a wish",
	"keep kalm":"and code python",
	"usa":"HIMYM",
	"uk":"bond",
	"empty":"",
	"awesome":"me"}

print("justkeys===")
for justkey in dd.keys():
	print (justkey)
print("\n")

print("justvalues===")
for justvalue in dd.values():
	print (justvalue)
print("\n")

print("key and values===")
for keyone in dd:
	print("key=  ",keyone," ",end="")
	print("value=",dd[keyone])
print("\n")

print("key and values===")
for keyone, valueone in dd.items():
	print("key=  ",keyone," ",end="")
	print("value=",valueone)
print("\n")

print("make dictionary with 2 lists")
countries = ["Italy", "Germany", "Spain", "USA"]	
dishes = ["pizza", "sauerkraut", "paella", "Hamburger"]
print("countries=                    ",countries)
print("dishes=                       ",dishes)
coockeddictionary = dict(zip(countries,dishes))
print("dict(zip(countries,dishes))=  ", coockeddictionary)
print("\n")


use_keys = {'red', 'green', 'blue', 'white', 'black'}
use_value = 'colour'
combine = dict.fromkeys(use_keys, use_value)
print("keys----",use_keys)
print("values--",use_value)
print("combine-",combine)
print("\n")


# searching and sorting
import operator
#x = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
x = {"k1":"v2", "k3":"v4", "k4":"v3", "k2":"v1", "k0":"v0"}
print("x original",x)

sorted_x = sorted(x.items(), key=operator.itemgetter(1),reverse=False)
print("sorting on key ascending   ---",sorted_x)
sorted_x = sorted(x.items(), key=operator.itemgetter(0),reverse=False)
print("sorting on value ascending     ---",sorted_x)

