# Add user script for Alpine linux

import myparamiko
import getpass

server_ip = '172.02.20.6'
ssh_port = '22'
username = 'admin'
password = 'admin'

ssh_client = myparamiko.connect(server_ip, ssh_port, username, password)
shell = myparamiko.get_shell(ssh_client)

new_user = input('Enter the new username:')
new_password = getpass.getpass('Enter the new user password:')
command = f'adduser -h /home/{new_user} -s /bin/ash {new_user}'
myparamiko.send_command(shell, command)
myparamiko.send_command(shell, new_password)
myparamiko.send_command(shell, new_password)

