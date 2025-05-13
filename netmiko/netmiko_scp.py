from netmiko import ConnectHandler
from netmiko import file_transfer

cisco_device = {
    'device_type': 'cisco_ios',
    'host': '172.16.0.1',
    'username': 'admin',
    'password': 'admin',
    'verbose': True
    }

connection = ConnectHandler(**cisco_device)

transfer_output = file_transfer(connection, 
                                source_file='ospf.txt', 
                                dest_file='ospf.txt',
                                file_system='unix:',
                                direction='put',
                                overwrite_file=True
                                )

print(transfer_output)

connection.disconnect()
