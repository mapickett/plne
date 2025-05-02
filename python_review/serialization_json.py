# DATA SERIALIZATION WITH JSON

import json
friends = {"Dan": [20, "London", 3234567890], "Maria": [25, "Madrid", 1234567890]}

# write object
with open('plne/python_review/friends.json', 'w') as f:
    json.dump(friends, f, indent=4) 

# write string
json_string = json.dumps(friends, indent=4) # dump string
# print(json_string)

# read object
with open('plne/python_review/friends.json', 'rt') as f:
    obj = json.load(f)
    # print(type(obj))
    # print(obj)

json_string2 = """{
    "Dan": [
        20,
        "London",
        3234567890
    ],
    "Maria": [
        25,
        "Madrid",
        1234567890
    ]
}"""
print(json_string2)

# read string
obj2 = json.loads(json_string2)
print(type(obj2))
print(obj2)

friends_t = {"Dan": (20, "London", 3234567890), "Maria": (25, "Madrid", 1234567890)}
# tuple converted to json type "array"
# cannot serialize a set