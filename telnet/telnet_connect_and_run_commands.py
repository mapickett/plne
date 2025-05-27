# Telnet provided by telnetlib standard library
# telnetlib USES BYTES
# 'telnetlib' is deprecated and slated for removal in Python 3.13

import telnetlib
import time

host = '172.16.0.1'
port = '23'
user = 'admin'
password = 'admin'

tn = telnetlib.Telnet(host=host, port=port)

tn.read_until(b'Username: ') #telnetlib uses bytes
tn.write(user.encode() + b'\n')
tn.read_until('Password: '.encode())    # another option
tn.write(password.encode() + b'\n')

# Call write command once for each command
tn.write(b'terminal length 0\n')

tn.write(b'show ip interface brief\n')
tn.write(b'exit\n')
time.sleep(1)

output = tn.read_all().decode()
print(output)