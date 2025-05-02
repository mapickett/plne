# Configure OSPF on Routers

import paramiko
import time
import getpass

# Create the ssh client
ssh_client = paramiko.SSHClient()
# print(type(ssh_client))

# Disable host key checking
ssh_client.set_missing_host_key_policy(paramiko.MissingHostKeyPolicy())

# Connection credentials
password = getpass.getpass('Enter device password:')
router1 = {'hostname': '172.20.20.5',
          'username': 'admin',
          'password': password
}
router2 = {'hostname': '172.20.20.3',
          'username': 'admin',
          'password': password
}
router3 = {'hostname': '172.20.20.2',
          'username': 'admin',
          'password': password
}

routers = [router1, router2, router3]

# Loop over routers and deploy configurations
for router in routers:

    # Connect to host
    print(f'Connecting to {router['hostname']}...')
    # ** kwarg of type dictionary, unpacks the dictionary
    ssh_client.connect(**router, look_for_keys=False, allow_agent=False)

    # Open interactive shell
    shell = ssh_client.invoke_shell()
    shell.send('terminal length 0\n') # disable paging

    # Send commands
    shell.send('enable\n')
    shell.send(f'{password}\n')
    shell.send('configure terminal\n')
    shell.send('router ospf 1\n')
    shell.send('network 0.0.0.0 0.0.0.0 area 0\n')
    shell.send('end\n')
    shell.send('show ip protocols\n')

    # Give the router time to respond
    time.sleep(2)

    # decode binary output to a string
    output = shell.recv(10000).decode() # max bytes received then decode

    print(output)

    # Close the ssh client
    if ssh_client.get_transport().is_active():
        print('Closing the session.')
        ssh_client.close()
