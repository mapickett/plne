s1 = 'abc'

b1 = s1.encode('utf-8') # UTF-8 by default

print(type(b1))

for b in b1:
    print(b)

print(b1)   # will auto translate ascii

s2 = 'アップル'
b2 = s2.encode()

print(b2)   # \x means base 16 = hex

s3 = b2.decode()
print(s3)