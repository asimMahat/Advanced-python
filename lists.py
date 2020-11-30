
mylist = ['banana', 'apple','orange']
# print(mylist)

mylist2 = [5,'apple',True]
# print (mylist2)

item = mylist[-1]
# print (item)

for i in mylist:
    print(i)
'''
if 'orange' in mylist:
    print("yes")
else:
    print("no")
'''
# print(len(mylist))

mylist.append("lemon")
print(mylist)

mylist.insert(1,'berry')
print(mylist)

#removing the data from the list
item=mylist.pop()
print (item) # gives which item is removed
print(mylist)

#removing the specific element from the list

item = mylist.remove("berry")
print(mylist)

#inserting specific item into the list
item = mylist.insert(2,"berry")
print(mylist)

#sorting the list in ascending order

mylist3 = [-1,-2,7,9,3,2,1]
items = sorted(mylist3)
print(items)
print("-----------------------------------------------")

#adding the two lists
first_list = [0] *5
print (first_list)

second_list = [2,3,1,7,9]
print (second_list)

third_list = first_list + second_list
print(third_list)
print("-----------------------------------------------")

#slicing 
my_list =[1,2,3,4,5,6,7,8,9]

a = my_list[1:5]
print(a)

#lists, ordered , mutable , allows duplicate elements
lists_org = ["banana","cherry","apple"]

list_cpy = lists_org
list_cpy.append("lemon")

print(list_cpy)

print("----------------------------------------------")

#list comprehension
b = [1,2,3,4,5,6]
c = [i*i for i in b]
print(b)
print(c)