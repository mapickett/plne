from netmiko import ConnectHandler
cisco_device = {
    'device_type': 'cisco_ios',
    'host': '172.16.0.1',
    'username': 'admin',
    'password': 'admin',
    }
connection = ConnectHandler(**cisco_device)

# Check if we need to enable
if not connection.check_enable_mode():
    connection.enable()     # Enter enable mode using secret

# Check if we are in configuration mode
if not connection.check_config_mode():
    connection.config_mode()

connection.send_command('username user1 secret cisco')

connection.exit_config_mode()

print('Closing connection')
connection.disconnect()
