# LISTS VS TUPLES

# tuples are fast and more efficient
# use whenever lists will not change (days, gps coords, us states)

# if tuples contains mutable objects (lists, dict, sets) then 
# they are not more efficient

# tuples protect data integrity (won't change by accident)

# tuples can be used as dict keys, lists cannot

# tuples more memory efficient
l1 = [1, 2, 3, 4, 5, 6]
t1 = (1, 2, 3, 4, 5 ,6)

import sys

print(f'List memory size: {sys.getsizeof(l1)}')
print(f'Tuple memory size: {sys.getsizeof(t1)}')
