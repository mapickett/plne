# Loops and Ranges
s = 0

for n in range(101): # range(0, 101, 1)
    s += n

print(f'Sum: {s}')

# the underscore _ in a for loop is used as a convention
# to indicate that the loop variable is intentionally unused
for _ in range(10): 
    print('Do Something')

import random
names = ['a','b','c','d','e']

for _ in range(3):
    print(f'Choosing winner. Round {_} ...')
    winner = random.choice(names)
    names.remove(winner)
    print(winner)
    print('#' * 10)