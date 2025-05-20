from napalm import get_network_driver
import json

driver = get_network_driver('ios')
optional_args = {'secret': 'admin'}
ios = driver('172.16.0.1', 'admin', 'admin', optional_args=optional_args)
ios.open()

# NAPALM uses SCP
# ip scp server enable
# NAPALM requires configuration archive
# archive
#  path unix:
# show archive

ios.load_replace_candidate(filename='r1-config.log')

diff = ios.compare_config()

if len(diff):
    print(diff)
    print('Commiting changes... ', end='')
    ios.commit_config()
    print('Done')
else:
    print('No changes required')
    ios.discard_config()

ios.close()