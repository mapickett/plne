# PYTHON LIST GOTCHAS

l1 = [1, 2, 3]
l2 = l1

# 1 The asignment operate creates a new name (pointer) to the same memory address
l2[0] = 'XX'
l2.append(10)

print(f'l2: {l2}')
print(f'l1: {l1}')

l1.remove(2)
print(f'l2: {l2}')

# The copy method creates a new list
l3 = l1.copy()
l3.append('abc')
print(f'l3: {l3}', id(l3))
print(f'l2: {l2}', id(l2))
print(f'l1: {l1}', id(l1))

# 2
nums = [1, 2, 3, 4, 5 ,6 ,7 ,0, 1, 2]

# WRONG WAY - Don't modify a list while iterating.
for n in nums:
    if n < 5:
        nums.remove(n)

print(f'nums: {nums}')

# Use secondary list
new_list = list()
for n in nums:
    if n >=5:
        new_list.append(n)

print(f'new_list: {new_list}')

# Use list comprehension
my_list = [n for n in nums if n>= 5]
print(f'my_list: {my_list}')