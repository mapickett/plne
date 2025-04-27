# LAMBDA EXPRESSIONS

# lambda parameter_list: expression

def add(a, b, c):
    return a + b +c

# no name, single line of code
result = (lambda a, b, c: a + b + c)(3, 4, 5)

print(result)

square = lambda x=10: x ** 2
print(square(4))

# use case is as an argument for another function

friends = [('Diana', 30), ('Ana', 25), ('Tudor', 22)]
friends.sort() # sort by first value in tuple
print(friends)

friends.sort(key=lambda x: x[1]) # sort by the second element in the tuple
print(friends)

friends.sort(key=lambda x: len(x[0])) # sort by length of name
print(friends)
