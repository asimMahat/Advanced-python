
# lambda arguments : expressions
'''
add10 = lambda x : x+10
print(add10(5))

# multiple arguments lambda functions

mult = lambda x,y : x*y
print (mult(2,7))

points2d = [(1,2),(2,3),(15,2),(10,4),(5,-1)]
#list sorted according to the y index 
points2d_sorted = sorted(points2d, key=lambda x: x[1]) 

print(points2d)
print(points2d_sorted)

# map(function ,sequence)
a=[1,2,3,4,5]
b=map(lambda x : x*2, a)
print(list(b))

#simple list comphrehension

c=[x*2 for x in a]
print(c)

# filter(function ,sequence)
a=[1,2,3,4,5,6]
b=filter(lambda x : x%2==0, a)
print(list(b))

c=[x for x in a if x%2==0]
print(list(c))


# reduce(function,sequence)
# reduce function always has two arguments
from functools import reduce
a=[1,2,3,4,5,6]
prod = reduce(lambda x,y: x*y, a) #finding the product of 'x' and 'y'
print(prod)

'''
