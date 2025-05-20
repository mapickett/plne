from napalm import get_network_driver
import json

driver = get_network_driver('ios')

optional_args = {'secret': 'admin'}
ios = driver('172.16.0.1', 'admin', 'admin', optional_args=optional_args)
ios.open()

output = ios.get_facts()
dump = json.dumps(output, sort_keys=True, indent=4)
print(dump)

output = ios.get_interfaces()
dump = json.dumps(output, sort_keys=True, indent=4)
print(dump)

output = ios.get_interfaces_counters()
dump = json.dumps(output, sort_keys=True, indent=4)
print(dump)

output = ios.get_interfaces_ip()
dump = json.dumps(output, sort_keys=True, indent=4)
print(dump)

ios.close()