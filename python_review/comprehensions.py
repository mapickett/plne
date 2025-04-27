# COMPREHENSIONS

# { expression loop conditional }

# list comprehension
nums = [1, 2, 3, 4, 5 ,6 ,7 ,0, 1, 2]
my_list = [n for n in nums if n>= 5]
print(f'my_list: {my_list}')

# set comprehension
names = {'tom', 'ANNE', 'John', 'dAn'}
names = {n.capitalize() for n in names}
print(names)

# dict comprehensions
d1 = {'a': 1, 'b': 2, 'c': 3}
d2 = {k*2: v*2 for k,v in d1.items()}
print(d2)

d3 = {k.upper(): v*2 for k,v in d1.items() if v % 3 == 0}
print(d3)