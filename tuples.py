#in tuples the paranthesis are optional
mytuples = "Max",28,"Boston"
print (type(mytuples))
print(mytuples)

item = mytuples[2]
print (item)

#tuples are immutable

for i in mytuples:
    print(i)

if "Max" in mytuples:
    print ("yes")
else:
    print ("no")

print("---------------------------------------")

my_tuple = ('a','p','p','l','e')
print(len(my_tuple))
print (my_tuple.count('p'))
#finding the index of item inside the tuples

print(my_tuple.index('p'))

#creating list out of tuples
my_list = list(my_tuple)
print(my_list)

print("----------------------------------------")
#creating tuples from list
my_tuple2 = tuple(my_list)
print(my_tuple2)

print ("-----------------------------------------")

#slicing with the tuples

d = 1,2,3,4,5,6,7,8,9,10
print(d)
e = d[2:6]
print (e)

#tuples unpacking
my_tuple3 = "Mike", 21, "NewYork"

name,age,city = my_tuple3
print(name)
print(age)
print(city)

#if there are too many values to unpack

my_tuple4 = 1,2,3,4,5,6
i1, *i2, i3 = 1,2,3,4,5,6
print(i1)
print(i2)
print(i3)

print("-----------------------------------------")
#comparing the size of lists and tuples
import sys
MY_list = [0,1,2,"hello",True]
MY_tuple = {0,1,2,"hello",True}
print(sys.getsizeof(MY_list),"bytes")
print(sys.getsizeof(MY_tuple),"bytes")

import timeit
print(timeit.timeit(stmt="[0,1,2,3,4,5]",number=1000000))
print(timeit.timeit(stmt="{0,1,2,3,4,5}",number=1000000))
