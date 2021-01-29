
#itertools : product, permutation, combination, accumulate
# groupby, and infinite iterators
'''
from itertools import product
a = [1,2]
b = [3,4]
prod = product(a,b)

print (list(prod))


from itertools import permutations
a=[1,2,3]
perm = permutations(a)

print(list(perm))



from itertools import combinations, combinations_with_replacement
a =[1,2,3, 4]
comb = combinations(a, 2)
print (list(comb))

comb_wr = combinations_with_replacement(a,2)
print (list(comb_wr))


from itertools import accumulate
import operator
a= [1,2,3,4]

acc = accumulate(a, func=operator.mul)
print(a)
print(list(acc))



from itertools import groupby

def smaller_than_3(x):
    return x<3

a =[1,2,3,4]

groupby_obj = groupby(a, key = smaller_than_3)

for key,value in groupby_obj:
    print(key, list(value))

 
#using the lambda function

from itertools import groupby

a =[1,2,3,4]
groupby_obj = groupby(a, key = lambda x : x < 3) 
for key,value in groupby_obj:
    print(key, list(value))

 
from itertools import groupby
persons = [{"name": "lisa", "age":20},{"name": "mina", "age":19},{"name":"jen","age":19},{"name":"tina","age":20}]

groupby_obj = groupby(persons, key=lambda x: x["age"])

for key,value in groupby_obj:
    print(key,list(value))
'''

from itertools import count,cycle ,repeat

for i in count(10):
    print(i)

    if i==15:
        break

# a =[1,2,3]
# for i in cycle(a):
    # print (i)
    

for i in repeat(1,4):
    print(i)


