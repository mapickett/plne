# Introduction to Dictionaries

# An ordered (since 3.7) collection of key:value pairs

# person = {'name': 'John', 'age': 30}
# print(type(person))

# d1 = dict()
# d2 = {}     # avoided due to confusion with sets

# # keys must be immutable and unique
# # values can be any value

# # len()
# print(len(person))

# # Assignment
# person['name'] = 'Dan'
# print(person)

# # Adding new k,v pair
# person['location'] = 'Berlin'
# print(person)

# # Accessing values
# a = person['age'] # error if key does not exist
# print(a)

# # get ()
# value = person.get('city', 'Key does not exist')
# print(value)

# # pop() retrievesd and removes k,v pair
# name = person.pop('name')
# print(name, person)
# person['name'] = 'Dan'

# # popitem() pops last item in dict
# print(person.popitem())

# # del - delete a k,v pair
# del person['location']
# print(person)

germany = {
    'cities': ['Hamburg', 'Berlin', 'Munich'],
    'info': {'population': 83_000_000, 'people': ['Einstein', 'Bach', 'Gauss']}
}
print(germany['cities'][1])
print(germany['info']['people'][0])
print(germany['info']['people'][1])
print(germany['info']['people'][-1])

countries = [
    {
        'cities': ['Hamburg', 'Berlin', 'Munich'],
        'info': {'population': 83_000_000, 'people': ['Einstein', 'Bach', 'Gauss']}
    },
    {
        'cities': ['Paris', 'Lyon', 'Bordeau'],
        'info': {'population': 67_000_000, 'people': ['Monet', 'Curie', 'Napoleon']}
    }
]

print(countries[0]['cities'][1])
print(countries[0]['info']['people'][-1])
print(countries[1]['cities'][1])
print(countries[1]['info']['people'][-1])
