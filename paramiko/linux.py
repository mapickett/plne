# Using paramiko to connect to linux systems

import paramiko
import time
import getpass

# create ssh client
ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.MissingHostKeyPolicy())

# set device parameters and credentials
password = getpass.getpass('Enter device password:')
node1 = {'hostname': '172.20.20.6', 'username': 'admin', 'password': password}

# connect to the device
print(f'Connecting to {node1['hostname']}...')
ssh_client.connect(**node1, look_for_keys=False, allow_agent=False)
# open interactive shell
shell = ssh_client.invoke_shell()

# send commands
shell.send('ifconfig\n')

# wait for response
time.sleep(1)

# save output and decode to string
output = shell.recv(10000).decode()

print(output)

if ssh_client.get_transport().is_active():
    print('Closing session')
    ssh_client.close()
