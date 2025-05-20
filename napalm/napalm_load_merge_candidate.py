from napalm import get_network_driver
import json

driver = get_network_driver('ios')
optional_args = {'secret': 'admin'}
ios = driver('172.16.0.1', 'admin', 'admin', optional_args=optional_args)
ios.open()

ios.load_merge_candidate('acl.txt')

diff = ios.compare_config()

if len(diff):
    print(diff)
    answer = input('Commit changes?,yes|no> ')
    if answer == 'yes':
        print('Committing changes...', end='')
        ios.commit_config()
        print('Done')
    else:
        print('No changes applied')
        ios.discard_config()

ios.close()