# SCOPES AND NAMESCAPES

# Builtin namespace
# Global namespace (nested inside Builtin)
# Local namespace (nested inside Global)

# t1 = tuple(range(20)) # t1 global ns, tuple,range builtin ns
# print(t1)

# x = 10

# def my_func():
#     x = 5
#     print(f'x inside the function: {x}')

# my_func()
# print(f'x outside the function: {x}')

# def my_func2():
#     global x # accezs global namespace
#     x += 1
#     print(f'x inside the function: {x}')

# my_func2()
# print(f'x outside the function: {x}')

# def my_func3():
#     print(f'x inside the function: {x}') # error cannot access local variable
#     x = 8 # masks global variable
# my_func3()

print(len('abc'))
def len(x):
    print(x)

len('abcdefg')  # masks Builtin namespace and uses global function

del len # removes len from global namespace
print(len('abcdefg'))

numbers = [1, 2, 3]
x = 10

def my_function(numbers, x):
    numbers.append(5)
    x = 66
    print(f'x inside the function {x}')
my_function(numbers, x)

print(f'After calling the function, number is {numbers} and x is {x}')
# list is modified by the function
# assignment is done to a new local scoped variable
# no assignment statement done with numbers, so no local copy created
# numbers = [8,9] would create a new locally scoped variable
