# Converting Types

# # 1 mile = 1.609 km
# miles = float(input('Enter distance in miles:'))
# # miles = float(miles)
# km = miles * 1.609
# print('Distance in km:', km)

a = 10
b = 2.5
c = '8.2'

# int => float

a_float = float(a)

# float => int
b_int = int(b)

# float => str
b_str = str(b)

# str => float
c_float = float(c)

# str => int
c_int = int(float(c))

c = int(float(c))
print ('c:', type(c))
