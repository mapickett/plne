from napalm import get_network_driver
import json

driver = get_network_driver('ios')

optional_args = {'secret': 'admin'}
ios = driver('172.16.0.1', 'admin', 'admin', optional_args=optional_args)
ios.open()

output = ios.get_arp_table(vrf='clab-mgmt')
dump = json.dumps(output, sort_keys=True, indent=4)
with open('arp.log', 'w') as f:
    f.write(dump)

ios.close()