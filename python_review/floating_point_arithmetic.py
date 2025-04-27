# Floating Point Arithmetic: Issues and Limitations

print(0.125 == 1/10 + 2/100 + 5/1000)

print(format(1/3, '.20f')) # 0.33333333333333331483

print(format(1/10, '.20f')) # 0.10000000000000000555

print(format(0.1, '.20f')) # 0.10000000000000000555

print(format(0.125, '.50f')) # has an exact binary representation

a = 0.1 * 3
b = 0.3
print(a == b) # False

print(format(a, '.20f')) # 0.30000000000000004441

# Don't use == with floats
# use isclose()

from math import isclose
x = 0.00000001
y = 0.00000002

print(x == y)
print(isclose(x, y, abs_tol=0.01))

a = 999999999.01
b = 999999999.02
print(a == b)
print(isclose(a, b, rel_tol=0.01))

a = 3.4
b = 2.3

print(a + b) # False

print(format(a, '.20f'))
print(format(b, '.20f'))
