# PROJECT: TEST NETWORK CONNECTIONS

import subprocess
# command = 'ping -c 1 8.8.8.8'
# output = subprocess.check_output(command.split()) #takes list, not string
# print(output.decode())

with open('project_hosts.txt') as f:
    ip_addresses = f.read().splitlines()
    for ip in ip_addresses:
        try:
            command = f'ping -c 1 {ip}'
            output = subprocess.check_output(command.split())
            print(output.decode())
        except Exception as e:
            print(f'Host {ip} is down => {e}')
    print('#' * 25)
