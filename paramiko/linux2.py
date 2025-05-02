# Using paramiko to connect to linux systems

import paramiko
import getpass
import time

# create ssh client
ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.MissingHostKeyPolicy())

# set device parameters and credentials
password = getpass.getpass('Enter device password:')
node1 = {'hostname': '172.20.20.6', 'username': 'admin', 'password': password}

# connect to the device
print(f'Connecting to {node1['hostname']}...')
ssh_client.connect(**node1, look_for_keys=False, allow_agent=False)

# send commands using exec_commmand
# returns tuple of bytes
# https://docs.paramiko.org/en/stable/api/client.html

stdin, stdout, stderr = ssh_client.exec_command('ifconfig\n') 
print(stdout.read().decode())
time.sleep(1)

stdin, stdout, stderr = ssh_client.exec_command('ip route\n') 
print(stdout.read().decode())
time.sleep(1)

# add get_pty=True when using sudo
stdin, stdout, stderr = ssh_client.exec_command('sudo cat /etc/shadow\n', get_pty=True) 
print(stdout.read().decode())
time.sleep(1)

if ssh_client.get_transport().is_active():
    print('Closing session')
    ssh_client.close()
