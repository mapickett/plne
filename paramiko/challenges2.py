# Challenge Exercises - Multithreading

import paramiko
import time
import threading

def execute_command(device, command):

    # Create the SSH Client
    ssh_client = paramiko.SSHClient()
    # Disable host key checking
    ssh_client.set_missing_host_key_policy(paramiko.MissingHostKeyPolicy())

    print(f'Connecting to {device["hostname"]}')
    ssh_client.connect(**device)

    shell = ssh_client.invoke_shell()
    print(f'Sending command "{command}" to "{device["hostname"]}"')
    shell.send('term length 0\n')
    shell.send(f'{command}\n')
    time.sleep(1)

    output = shell.recv(100000).decode()
    print(output)

    if ssh_client.get_transport().is_active():
        ssh_client.close()

if __name__ == '__main__':

    router1 = {'hostname': '172.20.20.5',
            'port': '22',
            'username': 'admin',
            'password': 'admin',
            'look_for_keys': False, 'allow_agent': False }
    router2 = {'hostname': '172.20.20.3',
            'port': '22',
            'username': 'admin',
            'password': 'admin',
            'look_for_keys': False, 'allow_agent': False }
    router3 = {'hostname': '172.20.20.2',
            'port': '22',
            'username': 'admin',
            'password': 'admin',
            'look_for_keys': False, 'allow_agent': False }

    routers= [router1, router2, router3]

    threads = list()
    for router in routers:
        th = threading.Thread(target=execute_command, 
                              args=(router, 'show ip interface brief'))
        threads.append(th)
    
    for th in threads:
        th.start()

    for th in threads:
        th.join()
 