# CODING CHALLANGE - SERIALIZATION

import json
import pickle

# 1 Create a function called serialize() that takes 3 arguments: 
# 1) the Python object you want to serialize, 
# 2) the file to which it serializes the object and 
# 3) the serialization protocol which is pickle or json.

# The function will create the file (the 2nd argument) 
# and will write the Python object to that file according to its 3rd argument.
# If the 3rd argument is pickle, It will use pickle to serialize the object and
# if the argument is json it will use json for serialization.

def serialize(object, file, protocol='json'):
    if protocol == 'pickle':
        import pickle
        with open(file, 'wb') as f:
            pickle.dump(object, f)
    else:
        import json
        with open(file, 'wt') as f:
            json.dump(object, f) 


# 2 Create a function called deserialize() that takes 2 arguments:
# 1) the file which contains serialized data and
# 2) the type of deserialization which is pickle or json.

# The function will deserialize from the file into a Python object
# and will return that object.

def deserialize(file, protocol='json'):
    if protocol == 'pickle':
        import pickle
        with open(file, 'rb') as f:
            object = pickle.load(f)
        return object
    else:
        import json
        with open(file, 'rt') as f:
            object = json.load(f) 
        return object

# tests
friends = {"Dan": [20, "London", 3234567890], "Maria": [25, "Madrid", 1234567890]}

serialize(object=friends, file='python_review/friends.json', protocol='json')
test1 = deserialize(file='python_review/friends.json', protocol='json')
print(test1)

serialize(object=friends, file='python_review/friends.dat', protocol='pickle')
test2 = deserialize(file='python_review/friends.dat', protocol='pickle')
print(test2)