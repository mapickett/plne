# OPENING AND READING FILES

# open('filename', 'mode')

# Text files - each line is a sequence of characters (UTF-8) followed by EOL
# Binary file - any type of file that is not a text file
f = open('configuration.txt', 'rt')

# read() returns entire content as a string

content = f.read()

print(content)

f.close()
