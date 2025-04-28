# PROJECT: FILE PROCESSING

with open('plne/devices.txt') as f:
    content = f.readlines()
    devices = list()
    for line in content[1:]:    # slicing list to drop first line
        devices.append(line.split(':'))
    print(devices)

for device in devices:
    print(f'Pinging {device[1]}')
