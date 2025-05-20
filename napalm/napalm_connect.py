from napalm import get_network_driver

driver = get_network_driver('ios')

optional_args = {'secret': 'admin'}
ios = driver('172.16.0.1', 'admin', 'admin', optional_args=optional_args)
ios.open()

print(dir(ios))

ios.close()