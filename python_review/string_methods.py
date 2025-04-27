# String Methods
# Strings are immutable

# print(), len(), type() are all builtin functions

# Print all methods
print(dir(str))

# help(str.replace)

s = 'Python'
# S = s.upper()
# print(s)
# print(S)

# print('prOgrAmming'.lower())

my_str = 'I learn Python Programming, python is cool!'

# str.upper()
print(my_str.upper())

# str.lower()
print(my_str.lower())

# str.strip()
ip = '  192.168.0.1    '
ip = ip.strip()
print(ip)
print(ip.strip('1'))

# str.replace
print(ip.replace('168', '192'))

# str.count
print(ip.count('192'))

print(my_str.lower().count('python'))

# str.split
print(my_str.split())
print(ip.split('.'))

# str.join
ip_list = ip.split('.')
print(ip_list)
ip_str = '.'.join(ip_list)
print(ip_str)

# str.find
print(my_str.find('Python')) # use only to find location in string

# in - used to test for substring
print('Python' in my_str) 
print('Golang' not in my_str) 