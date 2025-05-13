from netmiko import ConnectHandler

import logging
logging.basicConfig(filename='test.log', level=logging.DEBUG)
logger = logging.getLogger('netmiko')

linux = {
        'device_type': 'linux',
        'host': '172.20.20.2',
        'username': 'admin',
        'password': 'admin',
        'port': 22,
        'secret': 'admin',  # sudo passwd
        'verbose': True
        }

connection = ConnectHandler(**linux)

#connection.enable() # su

output = connection.send_command('apk list')

print(output)

print('Closing connection')
connection.disconnect()
