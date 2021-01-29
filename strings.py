"""
my_string = "I am a programmer "
print (my_string)

my_string1 = "Hello world"
char = my_string1[1]
print (char)


my_string2 = "Hi world"
my_string3 = "I am asim"
substring = my_string2[1:5]
substring1 = my_string2[::-1] # reversing the string

sentence = my_string2 + " " + my_string3
print(sentence)

# print (substring)
# print (substring1)

# for i in sentence:
    # print(i)
    
if 'i' in sentence:
    print("yes")
else:
    print ("no")


name = "Asim Mahat"
print (name.upper())
print (name.replace('Mahat', 'Singh Mahat'))

#string conactation

my_string = "How are you doing"
my_list = my_string.split(" ")
print(my_list)
new_string = "".join(my_list)
print(new_string)


from timeit import default_timer as timer
my_list = ['a'] * 10000000
# print(my_list)

start1 = timer()
my_string = ''
for i in my_list:
    my_string += i
# print(my_string)
stop1 = timer()
print (stop1-start1)

start = timer()
my_string1 =''.join(my_list)
# print(my_string)
stop = timer()
print(stop - start)

"""
#String formatting
# '%', .format(), f-Strings

var ="tom"
my_string = "the variable is %s" %var
print (my_string)


dec = 4
my_string1 = "the variable size is %d" % dec
print(my_string1)

dec = 12.222332
my_string2 = "the variable size in floating point is %.3f" % dec
print(my_string2)

#using .format() method
var1 = 23.45
var2 = 45.67
my_string3 = " The variables are {:.1f} and {:.1f}".format(var1, var2)
print(my_string3)

#using f-strings
var3 = 21.45
var4 = 51.67
my_string4 = f"The variables are {var3:.1f} and {var4:.1f}"
print(my_string4)
