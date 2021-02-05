import json

# person = {"name":"John", "age":30,"city":"New York",
        # "hasChildren ": False,"titles": ["engineer",
        # "programmer"]}

 
#covert into json
# person_json=json.dumps(person, indent=4 , sort_keys=True)
# print(person_json)

'''
#use different formatting style
person_json2=json.dumps(person, indent=4, separators=(";",
"="), sort_keys=True)

#the result is json string

print(person_json)
print("-----------------------------------")
print(person_json2)


# with open('person.json','w') as file:
#     json.dump(person, file)

 
with open('person.json', 'r') as f:
        person=json.load(f)
        print(person)

'''

class User:
    def __init__(self,name,age):
        self.name=name
        self.age=age

user=User("MAx",27)

def encode_user(o):

    if isinstance(o,User):
        return{'name':o.name,'age':o.age,o.__class__.__name__:True}
    else:
        raise TypeError("Object of type User is not Serializable")




from json import JSONEncoder
class UserEncoder(JSONEncoder):
    def default(self,o):
            if isinstance(o,User):
                return{'name':o.name,'age':o.age,o.__class__.__name__:True}
            return JSONEncoder.default(self,o)

                
userJSON=UserEncoder().encode(user)
# userJSON = json.dumps(user, cls=UserEncoder)
# userJSON = json.dumps(user, default=encode_user)
print(userJSON)

def decode_user(dct):
    if User.__name__ in dct:
        return User(name=dct['name'], age=dct['age'])
    return dct

user = json.loads(userJSON, object_hook=decode_user)
print(type(user))
print(user.name)

