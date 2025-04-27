# VARIABLE LENGTH ARGUMENTS

#  *args - variable number of positional arguments
# convention is to use name args; but any name could be used

def average(a, b, *args):
    print(f'args is {args}')
    return (a + b + sum(args)) / (2 + len(args))

print(average(4, 5))
print(average(4, 5, 6, 7, 8))

def concatenate(*args):
    result = ''
    for tmp in args:
        result = result + tmp
    return result

r = concatenate('Python', ' 3', '!')
print(r)

# **kwargs - variable number of keyword arguments
# kwargs is naming convention, can be any name

def my_function(**kwargs):
    print(kwargs)
    for k,v in kwargs.items():
        print(f'k is {k} and v is {v}')

my_function(name='John', age=40, location='London')
person = {'name': 'John', 'age': 30, 'location': 'USA'}
my_function(**person)

def connect(ip, port, username, password):
    print(ip, port, username, password)

linux_server = {'ip': '192.168.0.1', 'port': 22, 'username': 'admin', 'password': 'secret'}

connect(**linux_server)
