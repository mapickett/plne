from netmiko import ConnectHandler
from datetime import date
import time
import threading
start= time.time()

def backup(device):
    connection = ConnectHandler(**device)
    print('Entering enable mode')
    if not connection.check_enable_mode():
        connection.enable()

    hostname = connection.find_prompt()[0:-1]
    now = date.today().isoformat()
    filename = f'{hostname}-backup_{now}.txt'

    output = connection.send_command('show run')

    with open(filename, 'wt') as f:
        f.write(output)
        print(f'Backup of {hostname} written to {filename}')
        print('\n','#' * 30,'\n', sep='')

    print('Closing connection')
    connection.disconnect()

with open('devices.txt', 'rt') as f:
    devices = f.readlines()

threads = list()
for ip in devices:
    device = {
        'device_type': 'cisco_ios',
        'host': ip,
        'username': 'admin',
        'password': 'admin',
        'verbose': True
        }
    th = threading.Thread(target=backup, args=(device,)) # args is tuple
    threads.append(th)

for th in threads:
    th.start()

for th in threads:
    th.join()

end = time.time()
print(f'Total execution time:{end - start:.2f} seconds') # round to two places
