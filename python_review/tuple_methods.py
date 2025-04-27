# TUPLE METHODS

t1 = (1, 2, 3, 4, 5, 2)

# index()
i = t1.index(2)
print(f'2 is at position {i}')

# count()
i = t1.count(2)
print(f'2 is at present {i} times')

# builtin methods len(), max(), min(), sum(), sorted()
# work but do not change the tuple
t2 = sorted(t1, reverse=True)
print(t2)