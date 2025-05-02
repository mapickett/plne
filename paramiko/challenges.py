# Challenge Exercises

# 1. Create a Python script that connects to a Cisco Router using SSH and Paramiko.
# The script should execute the show users command in order to display 
# the logged-in users.
# Print out the output of the command.

import paramiko
import time
import getpass

# List of commands to run
# commands = ['enable', 'cisco', 'conf t', 
#             'username admin1 secret cisco', 
#             'access-list 1 permit any', 'end', 
#             'terminal length 0', 'sh run | i user']
# with open('paramiko/commands.txt', 'r') as f:
#    commands = f.readlines()

# Create the SSH Client
ssh_client = paramiko.SSHClient()

# Disable host key checking
ssh_client.set_missing_host_key_policy(paramiko.MissingHostKeyPolicy())

# Connection Credentials
password = getpass.getpass('Enter device password:')
router1 = {'hostname': '172.20.20.5',
          'port': '22',
          'username': 'admin',
          'password': password,
           'config': 'paramiko/ospf.txt' }
router2 = {'hostname': '172.20.20.3',
          'port': '22',
          'username': 'admin',
          'password': password,
           'config': 'paramiko/eigrp.txt' }
router3 = {'hostname': '172.20.20.2',
          'port': '22',
          'username': 'admin',
          'password': password,
           'config': 'paramiko/router3.txt' }
routers= [router1, router2, router3]

for router in routers:
   
    # Create SSH Connection
    ssh_client.connect(hostname=router['hostname'],
                       port=router['port'],
                       username=router['username'],
                       password=router['password'], 
                       look_for_keys=False, allow_agent=False)

    # Invoke Shell
    shell = ssh_client.invoke_shell()

    shell.send('terminal length 0\n')

    with open(router['config'], 'r') as f:
        commands = f.readlines()
        for cmd in commands:
            shell.send(cmd + '\n')
            time.sleep(0.5)

        output = shell.recv(10000).decode()

    # with open('paramiko/challenge_output.txt', 'a') as f:
    #     f.write(output)
    print(output)

    if ssh_client.get_transport().is_active():
        ssh_client.close()

