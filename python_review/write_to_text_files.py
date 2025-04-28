# WRITING TO TEXT FILES

# File will be created or overwritten
with open('plne/myfile.txt', 'w') as f:
    f.write('Just a line.##############\n')
    f.write('Just a second line.\n')

# Append to the end of the file
with open('plne/myfile.txt', 'a') as f:
    f.write('Just a third line.\n')

# Open for r + w; file must exist
with open('plne/myfile.txt', 'r+') as f:
    f.write('This line added by mode r+\n')
# Starts at the top of the file and replaces characters, not lines.
# file is one long string
