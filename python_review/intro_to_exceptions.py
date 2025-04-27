# PYTHON ERRORS AND EXCEPTION HANDLING

# Syntax (parsing) errors
# Exceptions (runtime errors)

# with open('a.txt') as f:
#     print(f.read())

# exception FileNotFoundError
# https://docs.python.org/3.12/library/exceptions.html

a, b = 10, 0
# print(a/b)

d1 = {'a': 4}
# print(d1['b']) # KeyError

# try except else finally structure
try:
    a = int(input('Enter a: '))
    b = int(input('Enter b: '))
    c = a / b
    print(c)
# except:
except ZeroDivisionError as e:
    print('An exception has occured.')
    print(f'Division by zero is not permitted: {e.args}')
except TypeError as e:
    print(f'Operations of different types are not permitted: {e.args}')
except Exception as e:
    print(f'An generic exception has occured: {e}')
else: # Runs if no exceptions
    print('No errors.')
    print(f'c={c}')
finally: # Always runs
    print('This code is always executed')

x = 10
print(x**x)
print('some other code')

# Best practice - don't user general exceptions, use multiple specific

while True:
    try:
        a = int(input('Enter a: '))
        b = int(input('Enter b: '))
        c = a / b
        print(c)
    except Exception as e:
        print(f'An generic exception has occured: {e}')
    else: # Runs if no exceptions
        print('No errors.')
        break

# Can raise your own exception
age = -1
if age < 0:
    raise Exception('Age below zero is not permitted!')
