# PYTHON FUNCTIONS

def my_function():
    print('Hello Python World!')
    x = 10
    print(x ** x)

my_function()

# positional arguments

def difference(a, b):
    result = a - b
    print(result)

difference(5,8)

# parameters vs arguments
def func1(x, y): # parameters
    print(f'1st parameter x is {x}')
    print(f'2nd parameter y is {y}')

func1('Python', 55) # arguments

# kewyword, named arguments
def func2(x, y, z): # parameters
    print(f'1st parameter x is {x}')
    print(f'2nd parameter y is {y}')
    print(f'3rd parameter y is {z}')

func2(y=7, x=3, z=9)
func2(3, 7, 9)
# You can mix positional and keyword arguements, but positionals must all be first
func2(3, z=9, y=7)

# default arguments
def add(x, y=10, z=20):
    print(f'x is {x}, y is {y} ans z is {z}')
    print(f'{x} + {y} + {z} = {x + y + z}')

add(2, 3, 4)
add(2, 3)
add(2)
add(x=2, z=3)
