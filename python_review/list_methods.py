# LIST METHODS

# l1 = list()
# print(dir(l1))

# __ or dunder methods

# help(l1.append)

# Adding to the list: append(), extend(), insert()

l1 = [1, 2.2, 'abc']
l1.append(5)
print(f'l1: {l1}')

l1.extend(['x', 'y'])
l1.extend('xy')
print(f'l1: {l1}')

years = [2020, 2022, 2023]
years.insert(1, 2021)
years.insert(len(years), 2024)
years.insert(-1, 2025) # inserts in second the last position
print(years)

years.clear()
print(years)

l2 = [10, 20, 30, 40]
x = l2.pop()
print(x)
print(l2)
y = l2.pop(1)
print(y)
print(l2)

years = [2020, 2022, 2023]
years.insert(1, 2021)
years.insert(len(years), 2024)
years.insert(-1, 2025)
print(years)
years.remove(2025) # Remove does not return value removed
print(years)
years.extend([2020, 2022, 2023])
print(years)

while 2020 in years:
    years.remove(2020)
print(years)

names = ['john', 'dan', 'tom', 'john', 'bill']
i = names.index('dan', 1, 3) # 1, 3 start/stop index
print(i)
i = names.index('john') # returns first occurence
print(i)
n = names.count('john')
print(n)

names.reverse() # modifies the list in place
print(names)

# list.sort() sorted(list)
ages = [10, 40, 25, 80, 13, 100]
la = sorted(ages) # returns sorted list, original unchanged.
print(la, ages)

n = ages.sort() 
print(n) # returns none, list sorted in place
print(ages)

# max() and min() sum() - builtin functions, not list methods
print(max(ages))
print(min(ages))
print(sum(ages))

