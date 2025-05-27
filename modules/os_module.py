# os — Miscellaneous operating system interfaces
# https://docs.python.org/3.12/library/os.html

import os

output = os.popen('ip neighbor').read()
print(output)

output = os.popen('ls -al /etc').read()
print(output)

# Can also use os.system() but is not recommended
