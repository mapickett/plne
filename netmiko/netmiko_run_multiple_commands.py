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

commands = ['int loopback0', 'ip address 1.1.1.1 255.255.255.255']
# cmd = 'ip version 2;access-list 1 permit any;ip domain name lab.local'
cmd2 = '''ip version 2
access-list 1 permit any
ip domain name lab.local
'''

connection.send_config_set(commands) # enters/exits enable mode on its own
# connection.send_config_set(cmd.split(';'))
# connection.send_config_set(cmd2.split('\n'))

print('Saving configuration')
connection.save_config()

print('Closing connection')
connection.disconnect()
