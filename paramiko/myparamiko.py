# Refactoring paramiko to a more accessible module

import paramiko
import time

def connect(server_ip, server_port, user, passwd):
    # Create ssh client
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.MissingHostKeyPolicy())
    # connect to the device
    print(f'Connecting to {server_ip}...')
    ssh_client.connect(hostname=server_ip, port=server_port, 
                       username=user, password=passwd,  
                       look_for_keys=False, allow_agent=False)
    return ssh_client

def get_shell(ssh_client):
    shell = ssh_client.invoke_shell()
    return shell

def send_command(shell, command, timeout=1):
    print(f'Sending command: {command}')
    shell.send(command + '\n')
    time.sleep(timeout)

def send_from_list(shell, commands):
    for command in commands:
        send_command(shell, command)

def send_from_file(shell, file_name):
    with open(file_name) as f:
        commands = f.readlines()
    send_from_list(shell, commands)

def show(shell, n=10000):
    output = shell.recv(n)
    return output.decode()

def close(ssh_client):
    if ssh_client.get_transport().is_active():
        print('Closing session')
        ssh_client.close()

if __name__ == '__main__':
    router1 = {'server_ip': '172.20.20.5', 'server_port': '22',
            'user': 'admin', 'passwd': 'admin'}

    client = connect(**router1)
    shell = get_shell(client)
    send_command(shell, 'terminal length 0')
    send_command(shell, 'show version')
    send_command(shell, 'show ip protocols')

    output = show(shell)
    print(output)
