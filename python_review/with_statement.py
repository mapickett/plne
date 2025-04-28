# WITH STATEMENT - Closes file at end of block

with open('plne/configuration.txt') as file:
    content = file.read()
    print(content)

print(file.closed)