# THE RETURN STATEMENT

n = len([1, 2, 4, 5]) # len returned value
print(n)

def add1(a, b):
    print(f'Sum: {a + b}')
    
def add2(a, b):
    return a + b # exits function
    print('Never executes')

add1(10,20)
my_sum = add2(5, 2)
print(my_sum)

def func1():
    pass
    # implicit return None

x = func1()
print(x)

def my_func(x):
    return x, x**2, x**3, x**4

print(my_func(3))

# unpack tuple

a, b, c, d = my_func(3)
print(a, b, c, d)

x, *y = my_func(3)
print(x, y)

