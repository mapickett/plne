# from netmiko import Netmiko

# connection = Netmiko(host='172.16.0.1', port='22', 
#                      username='admin', password='admin',
#                      device_type='cisco_ios'
#                      )

from netmiko import ConnectHandler

cisco_device = {
    'device_type': 'cisco_ios',
    'host': '172.16.0.1',
    'username': 'admin',
    'password': 'admin',
    'port': '22',           # optional, default 22
    'secret': 'cisco',      # optional, default ''
    'verbose': True         # optional, default False
    }

connection = ConnectHandler(**cisco_device)

output = connection.send_command('show ip int brief')
print(output)

print('Closing connection')
connection.disconnect()

