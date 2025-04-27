# PYTHON LISTS

l1 = [1, 2.5, 'python', True, ['abc', 'def'], (10, 20, 30)]
print(len(l1))
l2 = [] # emtpy list
l3 = list() # empty list

# Lists support indexing and slicing

print(l1[0])
print(l1[-1])

# Lists are mutable
s1 = 'Go Python Go'
l4 = list(s1)
print(l4)
l4[4] = 'Y'
print(l4)