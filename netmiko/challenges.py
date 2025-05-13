# Challenge
# Create a Python script that connects to a Cisco Router using SSH and Netmiko.
# The script should execute the show arp command in order to display the ARP table.
# Print out the output of the command.
# Read inventory from file, save results to file
# use multithreading

from netmiko import ConnectHandler
from datetime import date
import threading

def cmd_runner(device, commands):
    print('#' * 40)
    print(f'Connecting to {device['host']}')
    connection = ConnectHandler(**device)

    output_list = list()

    # Send command and capture output
    print('Sending commands')
    for cmd in commands:
        output = connection.send_command(cmd)
        output_list.append({'cmd': cmd, 'output': output})
   
    hostname = connection.find_prompt()[0:-1]
    now = date.today().isoformat()
    filename = f'{hostname}-cmd-output_{now}.txt'
    print(f'Writing output to: {filename}')
    with open(filename, 'wt') as f:
        for item in output_list:
            f.write('#' * 10 + f' BEGIN: {item['cmd'].rstrip()} ' + '#' * 10 + '\n')
            f.write(item['output'] + '\n')
            f.write('#' * 10 + f' END: {item['cmd'].rstrip()} ' + '#' * 10 + '\n')
    
    print(f'Disconnecting from {device['host']}')
    connection.disconnect()
    print('#' * 40)

# Read inventory from file
with open('inventory.txt', 'rt') as f:
    inventory_list = f.read().split('\n')

# Read commands from file
with open('commands.txt', 'rt') as f:
    commands = f.read().split('\n')

# Create list of dictionaries for ConnectHandler
device_list = list()
for device in inventory_list:
    # Ignore commented lines
    if not device[0] == '#':
        _ = device.split(':')
        dev = {'device_type': 'cisco_ios',
            'host': _[0],
            'port': _[1],
            'username': _[2],
            'password': _[3],
            'secret': _[4],
            'verbose': True  
        }
        device_list.append(dev)

print('Found devices:')
for device in device_list:
    print(device['host'])

print('Found commands:')
for command in commands:
    print(command)

# Single threaded
for device in device_list:
    try:
        cmd_runner(device, commands)
    except Exception as e:
        print(f'{e}\n')
        print(f'{device['host']} failed.')

# Multithreading
# threads = list()
# for device in device_list:
#     th = threading.Thread(target=cmd_runner, args=(device, commands))
#     threads.append(th)

# for th in threads:
#     th.start()

# for th in threads:
#     th.join()
