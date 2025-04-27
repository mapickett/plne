# FROZEN SETS

# immutable sets
# Can be used as keys iun dictionaries or members of other sets
# because immutable

fs1 = frozenset({1, 2, 3, 'a', 'b'})
print(fs1, type(fs1))

s1 = 'Python is cool!!'
fs2 = frozenset(s1) # can use any iterable
print(fs2, type(fs2))

# All non-modifiable methods are available to frozen sets

fs1 = frozenset({1, 2, 3})
fs2 = frozenset({3, 4, 5})

fs3 = fs1.intersection(fs2)
print(fs3)

# When mixing sets and frozen sets the result will have the type 
# of the object that calls the method

s1 = {4, 10, 20}
result1 = s1.intersection(fs2)
result2 = fs2 - s1
print(f'Result1 type: {type(result1)}')
print(f'Result2 type: {type(result2)}')
