# ASBSOLUTE AND RELATIVE PATHS

# f = open('plne/configuration.txt')

# f.open('C:\Users\mapic\.ssh\config') # backslash causes error

# Windows path names
# f1 = open('C:\\Users\\mapic\\.ssh\\config') # must escape or
# f2 = open(r'C:\Users\mapic\.ssh\config') # use raw string

f = open('/mnt/c/Users/mapic/.ssh/config', 'rt')