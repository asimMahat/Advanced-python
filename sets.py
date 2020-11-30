#sets : unordered , mutable and no duplicates

myset = {1,2,3,1,2} # set doesnot allow the duplicates
print(myset)
myset.add(4)
myset.add(5)
myset.add(6)

myset.remove(3)
print(myset)

print (myset.pop())

print (myset)

myset1 = set("hello")
print(myset1)

for i in myset:
    print (i)

if 2 in myset:
    print ("yes")
else:
    print ("no")

print ("---------------------------")
#printing out the union and intersection in sets

odds = {1,3,5,7,9}
evens = {0,2,4,6,8}
primes = {2,3,5,7}

u = odds.union(evens)
print(u)

i = odds.intersection(primes)
print(i)

#difference of the two sets

setA = {1,2,3,4,5,6,7,8,9}
setB = {1,2,3,10,11,12}

diff = setA.difference(setB)
print (diff)

sy_diff = setA.symmetric_difference(setB)
print (sy_diff)

print ("--------------------------------------")
#updating the sets
setA = {1,2,3,4,5,6,7,8,9}
setB = {1,2,3,10,11,12}

setA.update(setB)
print(setA)

print ("--------------------------------------")

setA = {1,2,3,4,5,6,7,8,9}
setB = {1,2,3}

print (setA.issubset(setB))
print (setB.issubset(setA))


print("----------------------------------------")
#copying two sets

setA = {1,2,3,4,5,6}
setB = setA.copy()
print (setB)

#frozen set - collection datatype and immutable

a = frozenset([1,2,3,4])
print(a)
