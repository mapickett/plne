# SET AND DICT COMPREHENSIONS

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

# zip() - takes one or more iterables and combines into list or dict of tuples

years = [2017, 2018, 2019]
revenue = [30000, 40000, 50000]
z = zip(years, revenue)
sales = list(z)
print(sales)

# my_sales = dict(z) # emtpy result. "keys in z have been consumed"
my_sales = dict(zip(years, revenue))
print(my_sales)

profit = {k:v*0.15 for k,v in my_sales.items()}
print(profit)
