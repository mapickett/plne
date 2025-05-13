from netmiko import ConnectHandler

cisco_device = {
    'device_type': 'cisco_ios',
    'host': '172.16.0.1',
    'username': 'admin',
    'password': 'admin',
    'verbose': True
    }

connection = ConnectHandler(**cisco_device)

interface = input('Enter the interface to enable: ')

# Check if we need to enable
if not connection.check_enable_mode:
    print('Entering enable mode')
    connection.enable()

output = connection.send_command(f'show interface {interface}')
if 'Invalid input detected' in output:
    print('You entered an invalid interface name')
else:
    intf_state = output.splitlines()[0].split(',')[0]
    intf_name = intf_state.split()[0]
    print(f'The current interface state is: {intf_state}')
    if 'is administratively down' in intf_state:
        print('Enabling the interface...')
        commands = [f'interface {intf_name}', 'no shutdown']
        connection.send_config_set(commands)
        print('Saving config...')
        connection.save_config()
    else:
        print(f'{intf_name} is enabled. No action taken.')

print('Closing connection')
connection.disconnect()