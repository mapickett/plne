# Data Serialization in Python

# Can only write strings to files

# friends = {"Dan": [20, "london", 3234567890], "Maria": [25, "Madrid", 1234567890]}

# with open('friends.txt', 'w') as f:
#     f.write(friends) # TypeError: write() argument must be str, not dict

# Native data serialization module for python is pickle. Python proprietary.
# Binary encoding protocol; considered insecure, unpickle can execute malicious code

import pickle
friends1 = {"Dan": [20, "London", 3234567890], "Maria": [25, "Madrid", 1234567890]}
friends2 = {"Bob": [24, "New York", 2124567890], "Nina": [27, "Barcelone", 3214567890]}
friends = (friends1, friends2)

# write
with open('plne/python_review/friends.dat', 'wb') as f:
    pickle.dump(friends, f)

# read
with open('plne/python_review/friends.dat', 'rb') as f:
    obj = pickle.load(f)
    print(type(obj))
    print(obj)

# cPickle is a faster version, not in python standard library