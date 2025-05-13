from netmiko import ConnectHandler

with open('devices.txt', 'rt') as f:
    devices = f.readlines()

device_list = list()

for ip in devices:
    cisco_device = {
        'device_type': 'cisco_ios',
        'host': ip,
        'username': 'admin',
        'password': 'admin',
        'verbose': True
    }
    device_list.append(cisco_device)

for device in device_list:
    connection = ConnectHandler(**device)

    print('Entering the enable mode')
    connection.enable()

    print('Sending commands from file')
    output = connection.send_config_from_file('ospf.txt')
    print(output)

    print('Saving configuration')
    connection.save_config()

    print('Closing connection')
    connection.disconnect()
