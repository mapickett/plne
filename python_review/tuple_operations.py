# TUPLE OPERATIONS

my_tuple = (1.4, 10, 'abc', True, (20, 40), 'x')
t1 = my_tuple + tuple('yz')
print(t1)

t2 = (1, 2, 'a') * 3
print(t2)

# Slicing works the same as lists
print(my_tuple[0:2])

# Iteration
movies = ('The Wizrd of Oz', 'The Legend', 'Casablanca')
for movie in movies:
    print(f'We are watching {movie}')

print('The Legend' in movies)
print('The Legend' not in movies)