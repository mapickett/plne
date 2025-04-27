# PYTHON SETS

s1 = {1, 2, 3, 'a', 'b', 4}

# Sets are unordered; so you can't use indexes
print(s1)

# Duplicates are not allowed
# There will not be an error, but only one instance will exist.

# Sets are mutable; all elements must be immutable
# Cannot add a list element (mutable)

# Ses user more memory, but have the fastest lookup time

# Immutable data types:
# Numbers
# Boolean
# Strings
# Bytes
# Tuples
# Frozen Sets

# Mutable data types:
# Lists
# dictionaries
# Sets
# Byte Arrays

s1.add((10,20))
# s1.add([10,20]) - gives unhashable error
print(s1)
s1.remove('a')
print(s1)

s2 = set()
# s2 = {} - Dictionary, not set

# str to set
s4 = set('hellooooo!!!!')
print(s4)

# tuple to set
s5 = set((10,20))
print(s5)

# list to set
s6 = set([10, 20, 30, 20])
print(s6)

for _ in s4:
    print(_)

set1 = {1,2,3}
set2 = {2,1,3}
print(set1 == set2) # True, same elements
print(set1 is set2) # False, false different memory address

