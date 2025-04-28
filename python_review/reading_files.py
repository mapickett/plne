# READING FILES

f = open('plne/configuration.txt')
content = f.read(5)
print(content)

content = f.read(3)
print(content)

# cursor - position at which you are in the file
print(f.tell()) # 8

f.seek(2)
content = f.read(3)
print(content)

f.seek(0)
content = f.read(3)
print(content)

