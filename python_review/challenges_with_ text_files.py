# Challenges with text files

# Consider macs.txt that contains multiple duplicate MAC addresses.
# Create a new file that contains only unique MAC addresses. 
# Each MAC should be on its own line.

with open('plne/macs.txt', 'r') as f:
    content = f.read().split()

macs = list(set(content))

with open('plne/mac_list.txt', 'w') as f:
    for mac in macs:
        f.write(f'{mac}\n')

# Create a Python script that reads sample_file.txt into a list 
# and then converts the list into a string that has the entire file content.

with open('plne/sample_file.txt', 'r') as f:
    content = f.read().splitlines()
    # file_str = str()
    # for line in content: # doesn't insert newlines
    #     file_str += line
    my_str = '/n'.join(content)

print(my_str)
