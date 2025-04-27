# DICTIONARY OPERATIONS AND METHODS

person = {'name': 'John', 'age': 30, 'location': 'USA'}

friend = person # creates a new name to the same memory address

person['name'] = 'Peter'
print(friend)

# copy()
neighbor = person.copy()
person['location'] = 'Europe'
print(neighbor, person)

# update()
countries = {'ro': 'Romania', 'us': 'United States', 'de': 'Germany'}
countries.update({'hu': 'Hungary', 'fr': 'France'})
print(countries)

# clear()
person.clear()
print(person, friend)

# keys()
person = {'name': 'John', 'age': 30, 'location': 'USA'}
k = person.keys()
print(k)
k_list = list(k)

# values()
v = person.values()
print(v)

# items()
print(person.items())

print('name' in person)     # checks keys, not values
print(10 in person.keys())
print('USA' in person)
print('USA' in person.values())
print(('age', 30) in person.items())

d1 = {10: 'a', 20: 'b', 30:'c'}
v = d1.values()
d1[10] = 'z'  # changes v also
print(v)

# keys are uniqgue, so set methods are available also
d1 = {10: 'a', 20: 'b'}
d2 = {20: 'c', 30: 'c'}
k1 = d1.keys()
k2 = d2.keys()
print(k1 & k2) # con only use symbol operations, not names 
print(k1 | k2)

# iteration
for k in person:
# for k in person.keys():   # no difference
    print(f'key is {k}')

for v in person.values():
    print(f'value is {v}')

for k in person.keys():
    print(f'Key is {k}, value is {person[k]}')

for k,v in person.items():
    print(f'Key is {k}, value is {v}')
