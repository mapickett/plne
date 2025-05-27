#  subprocess — Subprocess management
#  https://docs.python.org/3.12/library/subprocess.html

# Preferred over the os module

import subprocess

cmd = ['ip', 'neighbor', 'show']
# run a command and display output to stdout
subprocess.check_call(cmd)

# run a command and return its output
output = subprocess.check_output(cmd)

cmd = ['ping', '-c', '1', '8.8.8.8']
subprocess.check_call(cmd)