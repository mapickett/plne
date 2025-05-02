# Using the myparamiko module

import myparamiko

client = myparamiko.connect('172.20.20.6', '22', 'admin', 'admin')
shell = myparamiko.get_shell(client)

myparamiko.send_command(shell, 'ifconfig -a')

output = myparamiko.show(shell) # show flushes the buffer
print(output)

myparamiko.close(client)
