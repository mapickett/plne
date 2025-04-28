# READING FILES INTO A LIST

# # 1. f.read().splitlines() - EOL's not included
# with open('plne/configuration.txt', 'rt') as f:
#     content = f.read().splitlines()
#     print(content)

# print('#' * 50)

# # 2. f.readlines()
# with open('plne/configuration.txt', 'rt') as f2:
#     content2 = f2.readlines()
#     print(content2)

# print('#' * 50)

# # 3. list() - files are iterable
# with open('plne/configuration.txt') as f3:
#     content3 = list(f3)
#     print(content3)

# iterate over a file
with open('plne/configuration.txt') as f:
    for line in f:
        print(line, end='') # do not add \n to the end of each line 