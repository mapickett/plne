# sys — System-specific parameters and functions
# https://docs.python.org/3.12/library/sys.html

import sys

print(f'Specific settings for {sys.platform}')
print(sys.version)
print(sys.implementation)
print(sys.path)

my_list = list(range(1_000_000))
my_tuple = tuple(my_list)
my_set = set(my_list)
print(sys.getsizeof(my_list), sys.getsizeof(my_tuple), sys.getsizeof(my_set))

stdout = sys.stdout

with open('modules/output.log', 'a') as sys.stdout:
    print('Output redirection...')
    help('sys')

sys.stdout = stdout

with open('modules/output.log', 'r') as f:
    print(f.read())

# pip install ansible
# sys.argv[0] == pip
# sys.argv[1] == install
# sys.argv[2] == ansible

if len(sys.argv) > 1:
    for a in sys.argv[1:]:
        with open(a, 'r') as f:
            print(f.read())
else:
    print('Wrong number of arguments')