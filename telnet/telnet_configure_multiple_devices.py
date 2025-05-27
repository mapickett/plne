import telnetlib
import time
import getpass

routers= [
         {'host': '172.16.0.1', 'user': 'admin'},
         {'host': '172.16.0.2', 'user': 'admin'},
         {'host': '172.16.0.3', 'user': 'admin'}
         ]

for router in routers:
    print(f'Connecting to {router["host"]}')
    tn = telnetlib.Telnet(host=router['host'])

    # Login
    input = getpass.getpass('Enter user password: ')
    tn.read_until(b'Username: ')
    tn.write(router['user'].encode() + b'\n')
    tn.read_until('Password: '.encode())    # another way to encode
    tn.write(input.encode() + b'\n')
   
    # Apply Configuration
    tn.write(b'configure terminal\n')
    tn.write(b'ip route 0.0.0.0 0.0.0.0 1.1.1.1\n')
    tn.write(b'end\n')
    
    # Run show commands
    tn.write(b'terminal length 0\n')
    tn.write(b'show ip route\n')

    # Close session and capture output
    tn.write(b'exit\n')
    time.sleep(1)
    output = tn.read_all().decode()
    print(output)