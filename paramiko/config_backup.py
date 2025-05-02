# Backup a device configuration

import myparamiko
from datetime import datetime


router = {'server_ip': '172.20.20.5', 'server_port': '22',
        'user': 'admin', 'passwd': 'admin'}

client = myparamiko.connect(**router)
shell = myparamiko.get_shell(client)

myparamiko.send_command(shell, 'terminal length 0')
myparamiko.send_command(shell, 'show running-config')

output = myparamiko.show(shell)
# remove leading and trailing lines
output_list = output.splitlines()
output_list = output_list[11:-2]

output = '\n'.join(output_list)

now = datetime.now()
year = now.year
month = now.month
day = now.day

file_name = f'{router['server_ip']}_{year}-{month}-{day}.txt'

with open(f'paramiko/{file_name}', 'w') as f:
    f.write(output)

myparamiko.close(client)
