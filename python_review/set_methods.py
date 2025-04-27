# SET METHODS

# # add()

# s1 = {1, 2, 3}
# s1.add('a')
# s1.add(4.5)
# s1.add(1) # does nothing - dup
# print(s1)

# # remove() discard() pop()

# s1.remove('a') # key error if element does not exist
# print(s1)

# # discard()
# s1.discard('a') # removes
# s1.discard('foobar') # does nothing, no error
# print(s1)

# # pop() - removes and returns random element
# x1 = s1.pop()
# print(x1, s1)

# # clear() - wipes out everything
# s2 = set('abc')
# s3 = s2
# s3.clear()
# print(s2, s3)

# # copy()

# s4 = s1.copy()
# s4.add('z')
# print(s1, s4)

# ALL THE FOLLOWING RETURN NEW SETS

set1 = {1, 3, 5}
set2 = {5, 7, 9}

# intersection() / &

set3 = set1.intersection(set2)
# set3 = set1 & set2 -same thing
print(set3)

# difference() / -
set4 = set1.difference(set2) # works with any iterable
set4 = set1 - set2 # only works with two sets
print(set4)

# symmetric_difference() / ^ 
# excludes common elements
set5 = set1.symmetric_difference(set2)
set5 = set1 ^ set2
print(set5)

# union() / |
set6 = set1.union(set2)
set6 = set1 | set2
print(set6)

# isdisjoint()
# no common elements
print(set1.isdisjoint(set2))
print(set3.isdisjoint(set4))

# <, <=, >, >=, 
# < is included

# There are many more set methods
