#Errors and exceptions
'''
a = [1,2,3]
a.remove(1)
print(a)

my_dict = {'name': 'Max'}
print(my_dict['name'])

#raising an exception
x=-5
if x<0:
    raise Exception('x should be positive')

x =-5
assert (x>=0), "x is not positive"


#exception handling  
try:
    a = 5/0
except Exception as e:
    print(e)
    #actual message of exception is passed

try:
    a=5/0
    b= a + "10"
except ZeroDivisionError as e:
    print (e)
except TypeError as t:
    print(t)
else:
    print("Everything is fine")
finally:
    print ("Run always if threre was exception or not")

'''
#define our own exceptions 

class ValueTooHighError(Exception):
    pass

class ValueTooSmallError(Exception):
    def __init__(self, message, value):
        self.message = message
        self.value=value
    
def test_value(a):
    if a >100:
        raise ValueTooHighError('Value is too High')
    elif a<10:
        raise ValueTooSmallError('Value is too Small', a)
    else:
        print("The value is in limit")

try:
    test_value(2)

except ValueTooHighError as e:
    print(e)

except ValueTooSmallError as s:
    print(s.message, s.value)



