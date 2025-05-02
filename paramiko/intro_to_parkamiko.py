# INTRO TO PARAMIKO
# Docs- https://www.paramiko.org/

# Install pip install paramiko

import paramiko
import time
import getpass

# Create the ssh client
ssh_client = paramiko.SSHClient()
# print(type(ssh_client))

# Disable host key checking
ssh_client.set_missing_host_key_policy(paramiko.MissingHostKeyPolicy())

# Use  AutoAddPolicy for host keys
# ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# Connection credentials
password = getpass.getpass('Enter device password:')
router = {'hostname': '172.20.20.4',
          'username': 'admin',
          'password': password
}

# Connect to host
print(f'Connecting to {router['hostname']}...')
# ** kwarg of type dictionary, unpacks the dictionary
ssh_client.connect(**router, look_for_keys=False, allow_agent=False)

# Check ssh session
# print(ssh_client.get_transport().is_active())

# Open interactive shell
shell = ssh_client.invoke_shell()
shell.send('terminal length 0\n') # disable paging
shell.send('show version\n')
shell.send('show ip interface brief')

# Give the router time to respond
time.sleep(1)

# decode binary output to a string
output = shell.recv(10000) # max bytes received
output = output.decode('utf-8') #convert to string

print(output)

# Close the ssh client
if ssh_client.get_transport().is_active():
    print('Closing the session.')
    ssh_client.close()
