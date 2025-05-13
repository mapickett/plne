from netmiko import ConnectHandler

import time
start= time.time()

with open('devices.txt', 'rt') as f:
    devices = f.readlines()

for ip in devices:

    cisco_device = {
        'device_type': 'cisco_ios',
        'host': ip,
        'username': 'admin',
        'password': 'admin',
        'verbose': True
        }

    connection = ConnectHandler(**cisco_device)

    print('Entering enable mode')
    if not connection.check_enable_mode():
        connection.enable()

    hostname = connection.find_prompt()[0:-1]

    output = connection.send_command('show run')

    print('Closing connection')
    connection.disconnect()

    from datetime import date
    now = date.today().isoformat()

    filename = f'{hostname}-backup_{now}.txt'
    with open(filename, 'wt') as f:
        f.write(output)
        print(f'Backup of {hostname} written to {filename}')
        print('\n','#' * 30,'\n', sep='')

end = time.time()
print(f'Total execution time:{end - start}')
