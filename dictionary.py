#collection data type which is unordered and mutable
#key value pairs

mydict = {"name":"Max", "age":28, "city":"New York"}
print(mydict)

#using dict function to create the dictionary

mydict2 = dict(name="Mary",age =27, city="Boston")
print(mydict2)

value = mydict["name"]
print(value)

#giving keys and values to the previously created dictionary

mydict["email"]= "maxxyz@mail.com"
print(mydict)

#deleting the keys from the dictionary
'''
del mydict["name"]
print(mydict)
 
mydict.pop("name")
print(mydict)
'''
#checking the keys inside the dictionary
if "age" in mydict:
    print(mydict["age"])

 #using loop in a dictionary
for key in mydict:
    print(key)

for value in mydict.values():
    print(value)

print ("---------------------------------------")

for key,value in mydict.items():
    print (key , value)

print("------------------------------------------")

#copying a dictionary

mydict_cpy = mydict.copy()

mydict_cpy["country"] = "USA"

print(mydict)
print(mydict_cpy)

print("--------------------------------------------")
#update() method in dictionary

my_dict3 = {"name":"max", "age":28,"email":"max@xyz.com"}
my_dict4 = {"name":"mary", "age":27,"city":"Boston"}

#updating  my_dict3 with mydict_4

my_dict3.update(my_dict4)
print(my_dict3)

my_dict5 = {3:9, 6:36, 9:81}
print(my_dict5)

value = my_dict5[3]
print(value)

#creating the dictionary with the tuples

mytuple = (8,7)
mydict6 = {mytuple : 15}

print(mydict6)

# we cannot create dictionary from the list