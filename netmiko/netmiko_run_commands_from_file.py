from netmiko import ConnectHandler
cisco_device = {
    'device_type': 'cisco_ios',
    'host': '172.16.0.1',
    'username': 'admin',
    'password': 'admin',
    'verbose': True
    }
connection = ConnectHandler(**cisco_device)

print('Entering the enable mode')
connection.enable()

print('Sending commands from file')
output = connection.send_config_from_file('ospf.txt')
print(output)

print('Saving configuration')
connection.save_config()

print('Closing connection')
connection.disconnect()
